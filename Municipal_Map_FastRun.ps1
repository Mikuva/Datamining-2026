param(
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

# ====================================================================
# VYNÚTENIE UTF-8 KÓDOVANIA (Oprava pádov na diakritike)
# ====================================================================
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
# ====================================================================

$global:CollectedIssues = @()

function Write-StepHeader {
    param([string]$Name)

    Write-Host ""
    Write-Host "============================================================"
    Write-Host $Name
    Write-Host "============================================================"
}

function Wait-AnyKey {
    param([string]$Message)

    Write-Host ""
    Write-Host $Message
    [void][System.Console]::ReadKey($true)
    Write-Host ""
}

function Add-CollectedIssue {
    param([string]$Message)

    $global:CollectedIssues += $Message
}

function Format-OutputSnippet {
    param(
        [string[]]$Lines,
        [int]$MaxLines = 8
    )

    $cleanLines = @($Lines | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })

    if ($cleanLines.Count -eq 0) {
        return $null
    }

    $snippet = ($cleanLines | Select-Object -First $MaxLines) -join " | "

    if ($cleanLines.Count -gt $MaxLines) {
        $snippet = "$snippet | ..."
    }

    return $snippet
}

function Resolve-ProjectPaths {
    $scriptDir = Split-Path -Parent $MyInvocation.ScriptName

    if ([string]::IsNullOrWhiteSpace($scriptDir)) {
        $scriptDir = (Get-Location).Path
    }

    if ((Test-Path (Join-Path $scriptDir "src")) -and (Test-Path (Join-Path $scriptDir "README.md"))) {
        $projectDir = $scriptDir
        $repoRoot = Split-Path -Parent $projectDir
    }
    elseif (Test-Path (Join-Path $scriptDir "municipal_map_mvp\src")) {
        $repoRoot = $scriptDir
        $projectDir = Join-Path $repoRoot "municipal_map_mvp"
    }
    else {
        throw "Cannot find municipal_map_mvp project folder from: $scriptDir"
    }

    return [pscustomobject]@{
        RepoRoot = (Resolve-Path $repoRoot).Path
        ProjectDir = (Resolve-Path $projectDir).Path
        ProjectName = Split-Path -Leaf $projectDir
    }
}

function Resolve-PythonCommand {
    param(
        [string]$RepoRoot,
        [string]$ProjectDir
    )

    $repoVenvPython = Join-Path $RepoRoot ".venv\Scripts\python.exe"
    if (Test-Path $repoVenvPython) {
        return [pscustomobject]@{
            Exe = $repoVenvPython
            Prefix = @()
            Display = $repoVenvPython
        }
    }

    $projectVenvPython = Join-Path $ProjectDir ".venv\Scripts\python.exe"
    if (Test-Path $projectVenvPython) {
        return [pscustomobject]@{
            Exe = $projectVenvPython
            Prefix = @()
            Display = $projectVenvPython
        }
    }

    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) {
        return [pscustomobject]@{
            Exe = $python.Source
            Prefix = @()
            Display = $python.Source
        }
    }

    $py = Get-Command py -ErrorAction SilentlyContinue
    if ($py) {
        return [pscustomobject]@{
            Exe = $py.Source
            Prefix = @("-3")
            Display = "$($py.Source) -3"
        }
    }

    throw "Cannot find Python. Create .venv first or install Python 3.10+."
}

function Invoke-PythonCommand {
    param(
        [string]$Name,
        [object]$PythonCommand,
        [string[]]$Arguments
    )

    $allArgs = @($PythonCommand.Prefix) + $Arguments
    $stdoutPath = [System.IO.Path]::GetTempFileName()
    $stderrPath = [System.IO.Path]::GetTempFileName()
    $exitCode = 0
    $invokeError = $null

    try {
        $previousErrorActionPreference = $ErrorActionPreference
        $ErrorActionPreference = "Continue"

        & $PythonCommand.Exe @allArgs 1> $stdoutPath 2> $stderrPath
        $exitCode = $LASTEXITCODE
    }
    catch {
        $exitCode = 1
        $invokeError = $_.Exception.Message
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }

    $stdout = @()
    $stderr = @()

    if (Test-Path $stdoutPath) {
        $stdout = @(Get-Content -Path $stdoutPath -ErrorAction SilentlyContinue)
        Remove-Item -Path $stdoutPath -Force -ErrorAction SilentlyContinue
    }

    if (Test-Path $stderrPath) {
        $stderr = @(Get-Content -Path $stderrPath -ErrorAction SilentlyContinue)
        Remove-Item -Path $stderrPath -Force -ErrorAction SilentlyContinue
    }

    $stdout | ForEach-Object { Write-Host $_ }
    $stderr | ForEach-Object { Write-Host $_ -ForegroundColor DarkYellow }

    return [pscustomobject]@{
        Name = $Name
        ExitCode = $exitCode
        StdOut = $stdout
        StdErr = $stderr
        InvocationError = $invokeError
    }
}

function Add-PythonResultIssue {
    param(
        [object]$Result,
        [string]$MessagePrefix = "Step"
    )

    $message = "$MessagePrefix '$($Result.Name)' reported an issue (Exit Code: $($Result.ExitCode))."

    if ($Result.InvocationError) {
        $message = "$message Invocation error: $($Result.InvocationError)"
    }

    $stderrSnippet = Format-OutputSnippet -Lines $Result.StdErr
    if ($stderrSnippet) {
        $message = "$message stderr: $stderrSnippet"
    }

    Add-CollectedIssue $message
}

function Invoke-PythonStep {
    param(
        [string]$Name,
        [object]$PythonCommand,
        [string[]]$Arguments
    )

    Write-StepHeader $Name

    $allArgs = @($PythonCommand.Prefix) + $Arguments
    Write-Host "> $($PythonCommand.Display) $($Arguments -join ' ')"

    if ($DryRun) {
        return
    }

    $result = Invoke-PythonCommand -Name $Name -PythonCommand $PythonCommand -Arguments $Arguments

    if ($result.ExitCode -ne 0 -or $result.InvocationError) {
        Add-PythonResultIssue -Result $result
    }
}

function Invoke-DependencyInstall {
    param(
        [object]$PythonCommand,
        [string]$ProjectDir
    )

    Write-StepHeader "00/13 Install Python dependencies"

    $requirementsPath = Join-Path $ProjectDir "requirements.txt"
    if (-not (Test-Path $requirementsPath)) {
        Add-CollectedIssue "Dependency installation skipped because requirements.txt was not found: $requirementsPath"
        return
    }

    $commands = @(
        @("-m", "pip", "install", "--upgrade", "pip"),
        @("-m", "pip", "install", "-r", $requirementsPath)
    )

    foreach ($arguments in $commands) {
        $allArgs = @($PythonCommand.Prefix) + $arguments
        Write-Host "> $($PythonCommand.Display) $($arguments -join ' ')"

        if ($DryRun) {
            continue
        }

        $result = Invoke-PythonCommand -Name "Install Python dependencies" -PythonCommand $PythonCommand -Arguments $arguments

        if ($result.ExitCode -ne 0 -or $result.InvocationError) {
            Add-PythonResultIssue -Result $result -MessagePrefix "Dependency command"
        }
    }
}

function Show-Visoh2Instructions {
    param([string]$VisohDir)

    Write-Host ""
    Write-Host "VISOH2 input is missing."
    Write-Host ""
    Write-Host "What you need to do:"
    Write-Host "1) Download/export VISOH2 waste data as XLSX or CSV."
    Write-Host "2) Save the file here:"
    Write-Host "   $VisohDir"
    Write-Host "3) If there are multiple files, the newest XLSX/XLS/CSV file will be used."
    Write-Host "4) After saving the file, come back here and press any key."
}

function Invoke-Visoh2Step {
    param(
        [object]$PythonCommand,
        [string]$ScriptPath,
        [string]$VisohDir
    )

    Write-StepHeader "10/13 VISOH2 waste data"

    $arguments = @($ScriptPath)
    $allArgs = @($PythonCommand.Prefix) + $arguments
    Write-Host "> $($PythonCommand.Display) $($arguments -join ' ')"

    if ($DryRun) {
        return
    }

    $result = Invoke-PythonCommand -Name "VISOH2 waste data" -PythonCommand $PythonCommand -Arguments $arguments

    if ($result.ExitCode -eq 0 -and -not $result.InvocationError) {
        return
    }

    $text = @($result.StdOut + $result.StdErr) -join "`n"
    $looksLikeMissingInput =
        ($text -match "VISOH2 export") -or
        ($text -match "Soubor neexistuje") -or
        ($text -match "Nenasel") -or
        ($text -match "Nena")

    if (-not $looksLikeMissingInput) {
        Add-PythonResultIssue -Result $result
        return
    }

    Show-Visoh2Instructions -VisohDir $VisohDir
    Wait-AnyKey "Press any key to continue"

    Write-Host "> retry: $($PythonCommand.Display) $($arguments -join ' ')"

    $retryResult = Invoke-PythonCommand -Name "VISOH2 waste data after retry" -PythonCommand $PythonCommand -Arguments $arguments

    if ($retryResult.ExitCode -ne 0 -or $retryResult.InvocationError) {
        Add-PythonResultIssue -Result $retryResult
    }
}

try {
    $paths = Resolve-ProjectPaths
    Set-Location $paths.RepoRoot

    $project = $paths.ProjectName
    $src = Join-Path $project "src"
    $python = Resolve-PythonCommand -RepoRoot $paths.RepoRoot -ProjectDir $paths.ProjectDir

    Write-Host "Working directory set to: $($paths.RepoRoot)"
    Write-Host "Project folder: $($paths.ProjectDir)"
    Write-Host "Python: $($python.Display)"

    Invoke-DependencyInstall $python $paths.ProjectDir

    Invoke-PythonStep "01/13 Download CSU MOS data" $python @((Join-Path $src "01_download_data.py"))
    Invoke-PythonStep "02/13 Download municipality geometries" $python @((Join-Path $src "00_download_municipality_geometries.py"))

    Invoke-PythonStep "03/13 Pipeline config" $python @((Join-Path $src "pipeline_core_scripts_02_06.py"), "config")
    Invoke-PythonStep "04/13 Pipeline geo" $python @((Join-Path $src "pipeline_core_scripts_02_06.py"), "geo")
    Invoke-PythonStep "05/13 Pipeline indicators" $python @((Join-Path $src "pipeline_core_scripts_02_06.py"), "indicators")
    Invoke-PythonStep "06/13 Pipeline score" $python @((Join-Path $src "pipeline_core_scripts_02_06.py"), "score")

    Invoke-PythonStep "07/13 Build indicator trends" $python @((Join-Path $src "13_build_indicator_trends.py"))

    Invoke-PythonStep "08/13 Download age structure" $python @((Join-Path $src "download_age_structure_oby02e.py"))
    Invoke-PythonStep "09/13 Add age structure" $python @((Join-Path $src "15_add_age_structure.py"))

    $visohDir = Join-Path $paths.ProjectDir "data\raw\visoh2"
    Invoke-Visoh2Step $python (Join-Path $src "19_download_visoh2_waste.py") $visohDir

    Invoke-PythonStep "11/13 Add land use and environment" $python @((Join-Path $src "20_add_land_use_environment.py"))
    Invoke-PythonStep "12/13 Apply methodology updates" $python @((Join-Path $src "17_apply_methodology_updates.py"))
    Invoke-PythonStep "13/13 Generate interactive map" $python @((Join-Path $src "14_generate_interactive_map_business_dashboard_Kuba.py"))

    $mapPath = Join-Path $paths.ProjectDir "outputs\interactive_map_business_dashboard_Kuba.html"

    if ($DryRun) {
        Write-Host ""
        Write-Host "Dry run finished."
        exit 0
    }

    Write-Host ""
    if ($global:CollectedIssues.Count -gt 0) {
        Write-Host "============================================================" -ForegroundColor Yellow
        Write-Host "Potential issues:" -ForegroundColor Yellow
        $global:CollectedIssues | ForEach-Object { Write-Host "- $_" -ForegroundColor Yellow }
        Write-Host "============================================================" -ForegroundColor Yellow
        Write-Host ""
    }

    $answer = Read-Host "all finished, pres Y to open the interactive map"

    if ($answer -eq "Y" -or $answer -eq "y") {
        if (Test-Path $mapPath) {
            if ($IsMacOS) {
                # Pro Mac pouzije nativni prikaz 'open'
                Invoke-Expression "open `"$mapPath`""
            }
            elseif ($IsLinux) {
                # Pro Linux pouzije 'xdg-open'
                Invoke-Expression "xdg-open `"$mapPath`""
            }
            else {
                # Pro Windows zustane puvodni Start-Process
                Start-Process $mapPath
            }
        }
        else {
            Write-Host "Map file was not found: $mapPath"
        }
    }

    exit 0
}
catch {
    Write-Host ""
    Write-Host "Sorry, Its fucked up :("
    Write-Host $_.Exception.Message
    exit 1
}
