# CZSO IKZ – territorially sorted output

Vygenerováno: 2026-04-20 01:35:49

## Souhrn podle územní úrovně

territorial_scope_label category  dataset_count
                   kraj        A             13
                   kraj        B              1
                   kraj        C             29
                   kraj        D             14
               neurčeno        D             34
                   obec        A              1
                   obec        C             84
                   obec        D              1
                  okres        A              1
                  okres        B              8
                  okres        C              2
                  okres        D             15
       podobecní úroveň        C              2
     region soudržnosti        A              1
      správní obvod ORP        C              5
  více úrovní / smíšené        D              3
              ČR / stát        A              3
              ČR / stát        B              9
              ČR / stát        D             47

# Územní úroveň: neurčeno

## Kategorie A

### 001. [A] Dokončené byty v obcích

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  tb_cis  tb_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do             stapro_txt  tb_txt  vuzemi_txt
1457433181        2        3103     NaN     NaN          43      539783 2024 2024-01-01 2024-12-31 Počet dokončených bytů     NaN       Oplot
1457432328        2        3103     NaN     NaN          43      532479 2024 2024-01-01 2024-12-31 Počet dokončených bytů     NaN  Kmetiněves
1457433488        1        3103     NaN     NaN          43      551821 2024 2024-01-01 2024-12-31 Počet dokončených bytů     NaN     Tvrdkov
1457431105        0        3103     NaN     NaN          43      559806 2024 2024-01-01 2024-12-31 Počet dokončených bytů     NaN   Hlohovice
1457433090        3        3103     NaN     NaN          43      574911 2024 2024-01-01 2024-12-31 Počet dokončených bytů     NaN Dolní Roveň
```

#### TAIL

```
     idhod  hodnota  stapro_kod  tb_cis  tb_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do             stapro_txt     tb_txt      vuzemi_txt
1290507562        0        3103  5711.0    10.0          43      506753 2023 2023-01-01 2023-12-31 Počet dokončených bytů Bytový dům  Háj ve Slezsku
1290510176        0        3103  5711.0    10.0          43      549169 2023 2023-01-01 2023-12-31 Počet dokončených bytů Bytový dům        Kbelnice
1290507434        0        3103  5711.0    10.0          43      500062 2023 2023-01-01 2023-12-31 Počet dokončených bytů Bytový dům          Krhová
1290507436        0        3103  5711.0    10.0          43      500071 2023 2023-01-01 2023-12-31 Počet dokončených bytů Bytový dům         Poličná
1290507438        0        3103  5711.0    10.0          43      500194 2023 2023-01-01 2023-12-31 Počet dokončených bytů Bytový dům Polná na Šumavě
```

## Kategorie C

### 002. [C] Zařízení sociálních služeb podle obcí

                       hodnota
polozka                       
target_years_present      2024
has_primary_key           True
primary_key_column    obec_kod

#### HEAD

```
     idhod  hodnota  stapro_kod  dsz_cis  dsz_kod  rok  obec_kod obec_txt  okres_kod okres_txt                                 dsz_txt
1493415753        1        6098     2910      130 2024    529303  Benešov      40169   Benešov                      Domovy pro seniory
1493415756        1        6098     2910      131 2024    529303  Benešov      40169   Benešov                            Azylové domy
1493415757        1        6098     2910      132 2024    529303  Benešov      40169   Benešov                       Domy na půl cesty
1493415759        1        6098     2910      114 2024    529303  Benešov      40169   Benešov               Nízkoprahová denní centra
1493415760        1        6098     2910      115 2024    529303  Benešov      40169   Benešov Nízkoprahová zařízení pro děti a mládež
```

#### TAIL

```
     idhod  hodnota  stapro_kod  dsz_cis  dsz_kod  rok  obec_kod obec_txt  okres_kod okres_txt                                   dsz_txt
1493459157        8        6098     2910      125 2024    554782    Praha      40924     Praha                      Služby následné péče
1493459097        7        6098     2910      121 2024    554782    Praha      40924     Praha                     Centra denních služeb
1493459098       27        6098     2910      128 2024    554782    Praha      40924     Praha                          Stacionáře denní
1493459099        4        6098     2910      156 2024    554782    Praha      40924     Praha                        Stacionáře týdenní
1493459100       11        6098     2910      129 2024    554782    Praha      40924     Praha Domovy pro osoby se zdravotním postižením
```

### 003. [C] Pohyb obyvatel - rok 2022

                         hodnota
polozka                         
target_years_present        None
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota     vuk vuk_text  stapro_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do            vuzemi_txt
1119737864        6 DEM0008  Zemřelí        5393          43      577341 2022 2022-01-01 2022-12-31 Nová Ves nad Popelkou
1119730479        2 DEM0008  Zemřelí        5393          43      549525 2022 2022-01-01 2022-12-31         Králova Lhota
1119733489       17 DEM0008  Zemřelí        5393          43      558656 2022 2022-01-01 2022-12-31              Bezvěrov
1119731485        5 DEM0008  Zemřelí        5393          43      551775 2022 2022-01-01 2022-12-31              Strašice
1119730022        1 DEM0008  Zemřelí        5393          43      562319 2022 2022-01-01 2022-12-31         Horní Slatina
```

#### TAIL

```
     idhod  hodnota      vuk              vuk_text  stapro_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do  vuzemi_txt
1092295882    13037 DEM0026A Počet obyvatel k 1.1.        2406          65        5210 2022 2022-01-01 2022-01-01   Nová Paka
1092295872    32082 DEM0026A Počet obyvatel k 1.1.        2406          65        5314 2022 2022-01-01 2022-01-01 Vysoké Mýto
1092295877    16761 DEM0026A Počet obyvatel k 1.1.        2406          65        3213 2022 2022-01-01 2022-01-01     Stříbro
1092295881    48118 DEM0026A Počet obyvatel k 1.1.        2406          65        8115 2022 2022-01-01 2022-01-01  Nový Jičín
1092295883    49967 DEM0026A Počet obyvatel k 1.1.        2406          65        2112 2022 2022-01-01 2022-01-01  Kutná Hora
```

### 004. [C] Pohyb obyvatel - rok 2023

                         hodnota
polozka                         
target_years_present        2023
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota     vuk vuk_text  stapro_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do vuzemi_txt
1286495326        5 DEM0008  Zemřelí        5393          43      552674 2023 2023-01-01 2023-12-31    Střítež
1286494798        2 DEM0008  Zemřelí        5393          43      555835 2023 2023-01-01 2023-12-31   Bolešiny
1286494804        0 DEM0008  Zemřelí        5393          43      558010 2023 2023-01-01 2023-12-31    Louňová
1286494806        5 DEM0008  Zemřelí        5393          43      550922 2023 2023-01-01 2023-12-31   Čejetice
1286495335        3 DEM0008  Zemřelí        5393          43      589128 2023 2023-01-01 2023-12-31      Věžky
```

#### TAIL

```
     idhod  hodnota      vuk              vuk_text  stapro_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do        vuzemi_txt
1284791049     3094 DEM0026A Počet obyvatel k 1.1.        2406          43      529516 2023 2023-01-01 2023-01-01           Čerčany
1284791050      359 DEM0026A Počet obyvatel k 1.1.        2406          43      529605 2023 2023-01-01 2023-01-01            Rokytá
1284791051     1609 DEM0026A Počet obyvatel k 1.1.        2406          43      506737 2023 2023-01-01 2023-01-01          Chvalčov
1284791052      307 DEM0026A Počet obyvatel k 1.1.        2406          43      550680 2023 2023-01-01 2023-01-01           Záblatí
1284791053     1718 DEM0026A Počet obyvatel k 1.1.        2406          43      553441 2023 2023-01-01 2023-01-01 Bělá nad Radbuzou
```

### 005. [C] Pohyb obyvatel - rok 2024

                         hodnota
polozka                         
target_years_present        2024
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota     vuk vuk_text  stapro_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do       vuzemi_txt
1446607887        8 DEM0008  Zemřelí        5393          43      578231 2024 2024-01-01 2024-12-31         Koclířov
1446607050        7 DEM0008  Zemřelí        5393          43      575534 2024 2024-01-01 2024-12-31             Ráby
1446607855        2 DEM0008  Zemřelí        5393          43      597473 2024 2024-01-01 2024-12-31 Karlova Studánka
1446607865        3 DEM0008  Zemřelí        5393          43      557374 2024 2024-01-01 2024-12-31    Velké Hydčice
1446607870        3 DEM0008  Zemřelí        5393          43      594831 2024 2024-01-01 2024-12-31         Střelice
```

#### TAIL

```
     idhod  hodnota      vuk                vuk_text  stapro_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do vuzemi_txt
1446314214      952 DEM0026A   Počet obyvatel k 1.1.        2406          43      534803 2024 2024-01-01 2024-01-01      Hořín
1446314215      369 DEM0026B Počet obyvatel k 31.12.        2406          43      564443 2024 2024-12-31 2024-12-31    Svijany
1446314218      272 DEM0026A   Počet obyvatel k 1.1.        2406          43      500135 2024 2024-01-01 2024-01-01     Kozlov
1446314222      407 DEM0026A   Počet obyvatel k 1.1.        2406          43      550531 2024 2024-01-01 2024-01-01    Strážný
1446315041      256 DEM0026A   Počet obyvatel k 1.1.        2406          43      535591 2024 2024-01-01 2024-01-01     Zvíkov
```

### 006. [C] Počty ekonomických subjektů podle odvětví převažující činnosti za správní obvody Prahy, obcí s rozšířenou působností, obce a městské obvody a části - 2022

                         hodnota
polozka                         
target_years_present        None
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  odvetvi_cis  odvetvi_kod  vuzemi_cis  vuzemi_kod     casref  aktivita_txt  odvetvi_txt  vuzemi_txt
1059155094       74        4958           NaN           NaN          NaN          NaN          43      539783 2022-12-31           NaN          NaN       Oplot
1058829431       78        4958           NaN           NaN          NaN          NaN          43      532479 2022-12-31           NaN          NaN  Kmetiněves
1059372157       57        4958           NaN           NaN          NaN          NaN          43      551821 2022-12-31           NaN          NaN     Tvrdkov
1059372316       91        4958           NaN           NaN          NaN          NaN          43      559806 2022-12-31           NaN          NaN   Hlohovice
1058358308      478        4958           NaN           NaN          NaN          NaN          43      574911 2022-12-31           NaN          NaN Dolní Roveň
```

#### TAIL

```
    idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  odvetvi_cis odvetvi_kod  vuzemi_cis  vuzemi_kod     casref      aktivita_txt          odvetvi_txt vuzemi_txt
963082969        6        4958         571.0           1.0       5103.0           H          44      554324 2022-03-31 Zjištěná aktivita Doprava a skladování     Lhotka
963568816       28        4958         571.0           1.0       5103.0           H          44      554669 2022-03-31 Zjištěná aktivita Doprava a skladování    Hrabová
962963606       18        4958         571.0           1.0       5103.0           H          43      500062 2022-03-31 Zjištěná aktivita Doprava a skladování     Krhová
963214186        6        4958         571.0           1.0       5103.0           H          43      500071 2022-03-31 Zjištěná aktivita Doprava a skladování    Poličná
962482441        2        4958         571.0           1.0       5103.0           H          43      500135 2022-03-31 Zjištěná aktivita Doprava a skladování     Kozlov
```

### 007. [C] Počty ekonomických subjektů podle odvětví převažující činnosti za správní obvody Prahy, obcí s rozšířenou působností, obce a městské obvody a části - 2023

                         hodnota
polozka                         
target_years_present        2023
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  odvetvi_cis  odvetvi_kod  vuzemi_cis  vuzemi_kod     casref  aktivita_txt  odvetvi_txt  vuzemi_txt
1225403364       65        4958           NaN           NaN          NaN          NaN          43      539783 2023-12-31           NaN          NaN       Oplot
1225557557       71        4958           NaN           NaN          NaN          NaN          43      532479 2023-12-31           NaN          NaN  Kmetiněves
1225949426       51        4958           NaN           NaN          NaN          NaN          43      551821 2023-12-31           NaN          NaN     Tvrdkov
1225720374       83        4958           NaN           NaN          NaN          NaN          43      559806 2023-12-31           NaN          NaN   Hlohovice
1224744792      437        4958           NaN           NaN          NaN          NaN          43      574911 2023-12-31           NaN          NaN Dolní Roveň
```

#### TAIL

```
     idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  odvetvi_cis odvetvi_kod  vuzemi_cis  vuzemi_kod     casref      aktivita_txt          odvetvi_txt vuzemi_txt
1102192762        6        4958         571.0           1.0       5103.0           H          44      554324 2023-03-31 Zjištěná aktivita Doprava a skladování     Lhotka
1103342770       29        4958         571.0           1.0       5103.0           H          44      554669 2023-03-31 Zjištěná aktivita Doprava a skladování    Hrabová
1103091898       19        4958         571.0           1.0       5103.0           H          43      500062 2023-03-31 Zjištěná aktivita Doprava a skladování     Krhová
1102978232        7        4958         571.0           1.0       5103.0           H          43      500071 2023-03-31 Zjištěná aktivita Doprava a skladování    Poličná
1102930638        2        4958         571.0           1.0       5103.0           H          43      500135 2023-03-31 Zjištěná aktivita Doprava a skladování     Kozlov
```

### 008. [C] Počty ekonomických subjektů podle odvětví převažující činnosti za správní obvody Prahy, obcí s rozšířenou působností, obce a městské obvody a části - 2024

                         hodnota
polozka                         
target_years_present        2024
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  odvetvi_cis  odvetvi_kod  vuzemi_cis  vuzemi_kod     casref  aktivita_txt  odvetvi_txt  vuzemi_txt
1297578230       62        4958           NaN           NaN          NaN          NaN          43      539783 2024-06-30           NaN          NaN       Oplot
1296792131       74        4958           NaN           NaN          NaN          NaN          43      532479 2024-06-30           NaN          NaN  Kmetiněves
1297342262       51        4958           NaN           NaN          NaN          NaN          43      551821 2024-06-30           NaN          NaN     Tvrdkov
1297179880       80        4958           NaN           NaN          NaN          NaN          43      559806 2024-06-30           NaN          NaN   Hlohovice
1296854657      440        4958           NaN           NaN          NaN          NaN          43      574911 2024-06-30           NaN          NaN Dolní Roveň
```

#### TAIL

```
     idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  odvetvi_cis odvetvi_kod  vuzemi_cis  vuzemi_kod     casref      aktivita_txt          odvetvi_txt      vuzemi_txt
1270694326       31        4958         571.0           1.0       5103.0           H          44      554669 2024-03-31 Zjištěná aktivita Doprava a skladování         Hrabová
1270257972       19        4958         571.0           1.0       5103.0           H          43      500062 2024-03-31 Zjištěná aktivita Doprava a skladování          Krhová
1271150894        7        4958         571.0           1.0       5103.0           H          43      500071 2024-03-31 Zjištěná aktivita Doprava a skladování         Poličná
1270826200        2        4958         571.0           1.0       5103.0           H          43      500135 2024-03-31 Zjištěná aktivita Doprava a skladování          Kozlov
1271150980        1        4958         571.0           1.0       5103.0           H          43      500194 2024-03-31 Zjištěná aktivita Doprava a skladování Polná na Šumavě
```

### 009. [C] Počty ekonomických subjektů podle vybraných právních forem za správní obvody Prahy, obcí s rozšířenou působností, obce a městské obvody a části - 2022

                         hodnota
polozka                         
target_years_present        None
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  forma_cis  forma_kod  vuzemi_cis  vuzemi_kod     casref  aktivita_txt  forma_txt  vuzemi_txt
1059155094       74        4958           NaN           NaN        NaN        NaN          43      539783 2022-12-31           NaN        NaN       Oplot
1058829431       78        4958           NaN           NaN        NaN        NaN          43      532479 2022-12-31           NaN        NaN  Kmetiněves
1059372157       57        4958           NaN           NaN        NaN        NaN          43      551821 2022-12-31           NaN        NaN     Tvrdkov
1059372316       91        4958           NaN           NaN        NaN        NaN          43      559806 2022-12-31           NaN        NaN   Hlohovice
1058358308      478        4958           NaN           NaN        NaN        NaN          43      574911 2022-12-31           NaN        NaN Dolní Roveň
```

#### TAIL

```
    idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  forma_cis  forma_kod  vuzemi_cis  vuzemi_kod     casref      aktivita_txt  forma_txt           vuzemi_txt
963406813        8        4958         571.0           1.0        NaN        NaN          43      500101 2022-03-31 Zjištěná aktivita        NaN               Bražec
963246178       38        4958         571.0           1.0        NaN        NaN          43      500160 2022-03-31 Zjištěná aktivita        NaN         Město Libavá
962758387       12        4958         571.0           1.0        NaN        NaN          43      500127 2022-03-31 Zjištěná aktivita        NaN   Doupovské Hradiště
963406815        8        4958         571.0           1.0        NaN        NaN          43      500194 2022-03-31 Zjištěná aktivita        NaN      Polná na Šumavě
962921539        6        4958         571.0           1.0        NaN        NaN          43      500151 2022-03-31 Zjištěná aktivita        NaN Luboměř pod Strážnou
```

### 010. [C] Počty ekonomických subjektů podle vybraných právních forem za správní obvody Prahy, obcí s rozšířenou působností, obce a městské obvody a části - 2023

                         hodnota
polozka                         
target_years_present        2023
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  forma_cis  forma_kod  vuzemi_cis  vuzemi_kod     casref  aktivita_txt  forma_txt  vuzemi_txt
1225403364       65        4958           NaN           NaN        NaN        NaN          43      539783 2023-12-31           NaN        NaN       Oplot
1225557557       71        4958           NaN           NaN        NaN        NaN          43      532479 2023-12-31           NaN        NaN  Kmetiněves
1225949426       51        4958           NaN           NaN        NaN        NaN          43      551821 2023-12-31           NaN        NaN     Tvrdkov
1225720374       83        4958           NaN           NaN        NaN        NaN          43      559806 2023-12-31           NaN        NaN   Hlohovice
1224744792      437        4958           NaN           NaN        NaN        NaN          43      574911 2023-12-31           NaN        NaN Dolní Roveň
```

#### TAIL

```
     idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  forma_cis  forma_kod  vuzemi_cis  vuzemi_kod     casref      aktivita_txt  forma_txt           vuzemi_txt
1103181551        3        4958         571.0           1.0        NaN        NaN          43      500101 2023-03-31 Zjištěná aktivita        NaN               Bražec
1103027749       42        4958         571.0           1.0        NaN        NaN          43      500160 2023-03-31 Zjištěná aktivita        NaN         Město Libavá
1102866719       10        4958         571.0           1.0        NaN        NaN          43      500127 2023-03-31 Zjištěná aktivita        NaN   Doupovské Hradiště
1103164049        5        4958         571.0           1.0        NaN        NaN          43      500194 2023-03-31 Zjištěná aktivita        NaN      Polná na Šumavě
1102704986        5        4958         571.0           1.0        NaN        NaN          43      500151 2023-03-31 Zjištěná aktivita        NaN Luboměř pod Strážnou
```

### 011. [C] Počty ekonomických subjektů podle vybraných právních forem za správní obvody Prahy, obcí s rozšířenou působností, obce a městské obvody a části - 2024

                         hodnota
polozka                         
target_years_present        2024
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  forma_cis  forma_kod  vuzemi_cis  vuzemi_kod     casref  aktivita_txt  forma_txt  vuzemi_txt
1297578230       62        4958           NaN           NaN        NaN        NaN          43      539783 2024-06-30           NaN        NaN       Oplot
1296792131       74        4958           NaN           NaN        NaN        NaN          43      532479 2024-06-30           NaN        NaN  Kmetiněves
1297342262       51        4958           NaN           NaN        NaN        NaN          43      551821 2024-06-30           NaN        NaN     Tvrdkov
1297179880       80        4958           NaN           NaN        NaN        NaN          43      559806 2024-06-30           NaN        NaN   Hlohovice
1296854657      440        4958           NaN           NaN        NaN        NaN          43      574911 2024-06-30           NaN        NaN Dolní Roveň
```

#### TAIL

```
     idhod  hodnota  stapro_kod  aktivita_cis  aktivita_kod  forma_cis  forma_kod  vuzemi_cis  vuzemi_kod     casref      aktivita_txt  forma_txt           vuzemi_txt
1271022714       12        4958         571.0           1.0        NaN        NaN          43      500101 2024-03-31 Zjištěná aktivita        NaN               Bražec
1270291784       44        4958         571.0           1.0        NaN        NaN          43      500160 2024-03-31 Zjištěná aktivita        NaN         Město Libavá
1270693146       17        4958         571.0           1.0        NaN        NaN          43      500127 2024-03-31 Zjištěná aktivita        NaN   Doupovské Hradiště
1271022715       12        4958         571.0           1.0        NaN        NaN          43      500194 2024-03-31 Zjištěná aktivita        NaN      Polná na Šumavě
1270860050        6        4958         571.0           1.0        NaN        NaN          43      500151 2024-03-31 Zjištěná aktivita        NaN Luboměř pod Strážnou
```

### 012. [C] Statistická data pro územně analytické podklady - rok 2020

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  vuk_id  rok  uzemi_cis  uzemi_kod                uzemi_txt  prislorp_kod prislorp_txt                 vuk_txt
878797427     38.0 DEM0008 2020         43     500011 Želechovice nad Dřevnicí          7213         Zlín                 Zemřelí
878902331    -20.0 DEM0011 2020         43     500011 Želechovice nad Dřevnicí          7213         Zlín     Přirozený přírůstek
878800648    -18.0 DEM0012 2020         43     500011 Želechovice nad Dřevnicí          7213         Zlín       Celkový přírůstek
886097260  24995.0 FIN0004 2020         43     500011 Želechovice nad Dřevnicí          7213         Zlín            Běžné výdaje
866054672    252.0 UZE0004 2020         43     500011 Želechovice nad Dřevnicí          7213         Zlín Orná půda (v hektarech)
```

#### TAIL

```
    idhod  hodnota  vuk_id  rok  uzemi_cis  uzemi_kod     uzemi_txt  prislorp_kod     prislorp_txt                         vuk_txt
866090467     1.64 UZE0001 2020         43     566161          Úboč        3202.0        Domažlice Koeficient ekologické stability
866094290     2.04 UZE0001 2020         43     577120  Horní Branná        5104.0        Jilemnice Koeficient ekologické stability
866091890     1.02 UZE0001 2020         43     557862    Kasejovice        3207.0          Nepomuk Koeficient ekologické stability
866098251     1.08 UZE0001 2020         43     578720         Sádek        5310.0          Polička Koeficient ekologické stability
866098471     1.61 UZE0001 2020         43     577987 Dlouhá Loučka        5308.0 Moravská Třebová Koeficient ekologické stability
```

### 013. [C] Statistická data pro územně analytické podklady - rok 2021

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  vuk_id  rok  uzemi_cis  uzemi_kod                uzemi_txt  prislorp_kod prislorp_txt                 vuk_txt
967546151     34.0 DEM0008 2021         43     500011 Želechovice nad Dřevnicí          7213         Zlín                 Zemřelí
967524876    -18.0 DEM0011 2021         43     500011 Želechovice nad Dřevnicí          7213         Zlín     Přirozený přírůstek
967417913    -14.0 DEM0012 2021         43     500011 Želechovice nad Dřevnicí          7213         Zlín       Celkový přírůstek
982086649  31783.0 FIN0004 2021         43     500011 Želechovice nad Dřevnicí          7213         Zlín            Běžné výdaje
927206497    252.0 UZE0004 2021         43     500011 Želechovice nad Dřevnicí          7213         Zlín Orná půda (v hektarech)
```

#### TAIL

```
    idhod  hodnota  vuk_id  rok  uzemi_cis  uzemi_kod       uzemi_txt  prislorp_kod   prislorp_txt                         vuk_txt
927096577     0.74 UZE0001 2021         43     568538      Dlouhá Ves        6102.0 Havlíčkův Brod Koeficient ekologické stability
927094272     0.57 UZE0001 2021         43     571385 Heřmanův Městec        5304.0        Chrudim Koeficient ekologické stability
927099694     0.55 UZE0001 2021         43     583502        Nová Ves        6208.0       Ivančice Koeficient ekologické stability
927099528     0.12 UZE0001 2021         43     584011       Trboušany        6208.0       Ivančice Koeficient ekologické stability
927104091     0.76 UZE0001 2021         43     592200      Hradčovice        7208.0   Uherský Brod Koeficient ekologické stability
```

### 014. [C] Statistická data pro územně analytické podklady - rok 2022

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  vuk_id  rok  uzemi_cis  uzemi_kod                uzemi_txt  prislorp_kod prislorp_txt                             vuk_txt
1119624482     28.0 DEM0008 2022         43     500011 Želechovice nad Dřevnicí          7213         Zlín                             Zemřelí
1119816430     -5.0 DEM0011 2022         43     500011 Želechovice nad Dřevnicí          7213         Zlín                 Přirozený přírůstek
1119816431     27.0 DEM0012 2022         43     500011 Želechovice nad Dřevnicí          7213         Zlín                   Celkový přírůstek
1070384166    251.0 UZE0004 2022         43     500011 Želechovice nad Dřevnicí          7213         Zlín             Orná půda (v hektarech)
1070307838    235.0 UZE0009 2022         43     500011 Želechovice nad Dřevnicí          7213         Zlín Trvalé travní porosty (v hektarech)
```

#### TAIL

```
     idhod  hodnota  vuk_id  rok  uzemi_cis  uzemi_kod uzemi_txt  prislorp_kod prislorp_txt                    vuk_txt
1070446423     39.0 UZE0012 2022         43     560898    Hošťka        3215.0       Tachov Vodní plochy (v hektarech)
1070452743      3.0 UZE0012 2022         43     569224   Oudoleň        6104.0     Chotěboř Vodní plochy (v hektarech)
1070455607     13.0 UZE0012 2022         43     584363 Brumovice        6207.0    Hustopeče Vodní plochy (v hektarech)
1070452813      4.0 UZE0012 2022         43     587362   Kamenná        6105.0      Jihlava Vodní plochy (v hektarech)
1070460474      3.0 UZE0012 2022         43     585661  Provodov        7213.0         Zlín Vodní plochy (v hektarech)
```

### 015. [C] Statistická data pro územně analytické podklady - rok 2023

                        hodnota
polozka                        
target_years_present       2023
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  vuk_id  rok  uzemi_cis  uzemi_kod                uzemi_txt  prislorp_kod prislorp_txt             vuk_txt
1286549899     15.0 DEM0008 2023         43     500011 Želechovice nad Dřevnicí          7213         Zlín             Zemřelí
1286499958     65.0 DEM0009 2023         43     500011 Želechovice nad Dřevnicí          7213         Zlín        Přistěhovalí
1286524284     54.0 DEM0010 2023         43     500011 Želechovice nad Dřevnicí          7213         Zlín         Vystěhovalí
1286515410     -5.0 DEM0011 2023         43     500011 Želechovice nad Dřevnicí          7213         Zlín Přirozený přírůstek
1286495957      6.0 DEM0012 2023         43     500011 Želechovice nad Dřevnicí          7213         Zlín   Celkový přírůstek
```

#### TAIL

```
     idhod    hodnota  vuk_id  rok  uzemi_cis  uzemi_kod            uzemi_txt  prislorp_kod  prislorp_txt                             vuk_txt
1223859100       5.23 NEZ0004 2023        100       3140 Moravskoslezský kraj           NaN           NaN       Podíl nezaměstnaných osob (%)
1286408854 1189204.00 DEM0026 2023        100       3140 Moravskoslezský kraj           NaN           NaN                      Počet obyvatel
1284304183  179058.00 DEM0027 2023        100       3140 Moravskoslezský kraj           NaN           NaN    Počet obyvatel ve věku do 15 let
1284312367  757202.00 DEM0028 2023        100       3140 Moravskoslezský kraj           NaN           NaN Počet obyvatel ve věku 15 až 64 let
1284339745  252944.00 DEM0029 2023        100       3140 Moravskoslezský kraj           NaN           NaN           Počet obyvatel nad 65 let
```

### 016. [C] Statistická data pro územně analytické podklady - rok 2024

                        hodnota
polozka                        
target_years_present       2024
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  vuk_id  rok  uzemi_cis  uzemi_kod                uzemi_txt  prislorp_kod prislorp_txt             vuk_txt
1446565628     14.0 DEM0008 2024         43     500011 Želechovice nad Dřevnicí          7213         Zlín             Zemřelí
1446592380     56.0 DEM0009 2024         43     500011 Želechovice nad Dřevnicí          7213         Zlín        Přistěhovalí
1446584407     74.0 DEM0010 2024         43     500011 Želechovice nad Dřevnicí          7213         Zlín         Vystěhovalí
1446574143      4.0 DEM0011 2024         43     500011 Želechovice nad Dřevnicí          7213         Zlín Přirozený přírůstek
1446579244    -14.0 DEM0012 2024         43     500011 Želechovice nad Dřevnicí          7213         Zlín   Celkový přírůstek
```

#### TAIL

```
     idhod    hodnota  vuk_id  rok  uzemi_cis  uzemi_kod            uzemi_txt  prislorp_kod  prislorp_txt                             vuk_txt
1375187152       5.82 NEZ0004 2024        100       3140 Moravskoslezský kraj           NaN           NaN       Podíl nezaměstnaných osob (%)
1446323663 1182613.00 DEM0026 2024        100       3140 Moravskoslezský kraj           NaN           NaN                      Počet obyvatel
1446106728  174283.00 DEM0027 2024        100       3140 Moravskoslezský kraj           NaN           NaN    Počet obyvatel ve věku do 15 let
1446117064  753248.00 DEM0028 2024        100       3140 Moravskoslezský kraj           NaN           NaN Počet obyvatel ve věku 15 až 64 let
1446059025  255082.00 DEM0029 2024        100       3140 Moravskoslezský kraj           NaN           NaN           Počet obyvatel nad 65 let
```

### 017. [C] Uchazeči o zaměstnání dosažitelní a podíl nezaměstnaných osob podle obcí - rok 2020

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota     vuk                          vuk_text   obdobi  rok  mesic  uzemi_cis  uzemi_kod uzemi_txt
826725487        3 NEZ0001 Uchazeči o zaměstnání dosažitelní 20200131 2020      1         43     568970    Kynice
826725594        1 NEZ0001 Uchazeči o zaměstnání dosažitelní 20200131 2020      1         43     560391  Kuřimany
826728993      155 NEZ0001 Uchazeči o zaměstnání dosažitelní 20200131 2020      1         43     586412  Mutěnice
826728966        3 NEZ0001 Uchazeči o zaměstnání dosažitelní 20200131 2020      1         43     558095 Nekvasovy
826726066       18 NEZ0001 Uchazeči o zaměstnání dosažitelní 20200131 2020      1         43     559148     Ledce
```

#### TAIL

```
    idhod  hodnota     vuk              vuk_text   obdobi  rok  mesic  uzemi_cis  uzemi_kod uzemi_txt
844823662      7.0 NEZ0007 Uchazeči o zaměstnání 20201130 2020     11         43     533475  Libenice
844823687     26.0 NEZ0007 Uchazeči o zaměstnání 20201130 2020     11         43     566349  Libčeves
844824959     34.0 NEZ0007 Uchazeči o zaměstnání 20201130 2020     11         43     531456     Liteň
844828556     13.0 NEZ0007 Uchazeči o zaměstnání 20201130 2020     11         43     596302      Olší
844828559     16.0 NEZ0007 Uchazeči o zaměstnání 20201130 2020     11         43     567761     Ohníč
```

### 018. [C] Uchazeči o zaměstnání dosažitelní a podíl nezaměstnaných osob podle obcí - rok 2021

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota     vuk              vuk_text   obdobi  rok  mesic  uzemi_cis  uzemi_kod                uzemi_txt
864659649     32.0 NEZ0007 Uchazeči o zaměstnání 20210131 2021      1         43     500011 Želechovice nad Dřevnicí
868087328     34.0 NEZ0007 Uchazeči o zaměstnání 20210228 2021      2         43     500011 Želechovice nad Dřevnicí
899900953     34.0 NEZ0007 Uchazeči o zaměstnání 20210630 2021      6         43     500011 Želechovice nad Dřevnicí
884443233     33.0 NEZ0007 Uchazeči o zaměstnání 20210430 2021      4         43     500011 Želechovice nad Dřevnicí
888703764     35.0 NEZ0007 Uchazeči o zaměstnání 20210531 2021      5         43     500011 Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota     vuk                              vuk_text   obdobi  rok  mesic  uzemi_cis  uzemi_kod   uzemi_txt
906433334    1.741 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20210831 2021      8         43     599999 Trojanovice
914193319    1.866 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20211031 2021     10         43     599999 Trojanovice
909385973    2.114 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20210930 2021      9         43     599999 Trojanovice
917352090    1.493 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20211130 2021     11         43     599999 Trojanovice
921004701    1.617 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20211231 2021     12         43     599999 Trojanovice
```

### 019. [C] Uchazeči o zaměstnání dosažitelní a podíl nezaměstnaných osob podle obcí

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota     vuk              vuk_text   obdobi  rok  mesic  uzemi_cis  uzemi_kod                uzemi_txt
 963806612     27.0 NEZ0007 Uchazeči o zaměstnání 20220331 2022      3         43     500011 Želechovice nad Dřevnicí
 971575908     32.0 NEZ0007 Uchazeči o zaměstnání 20220430 2022      4         43     500011 Želechovice nad Dřevnicí
 982185473     29.0 NEZ0007 Uchazeči o zaměstnání 20220531 2022      5         43     500011 Želechovice nad Dřevnicí
 932018613     28.0 NEZ0007 Uchazeči o zaměstnání 20220228 2022      2         43     500011 Želechovice nad Dřevnicí
1009517366     32.0 NEZ0007 Uchazeči o zaměstnání 20220831 2022      8         43     500011 Želechovice nad Dřevnicí
```

#### TAIL

```
     idhod  hodnota     vuk                              vuk_text   obdobi  rok  mesic  uzemi_cis  uzemi_kod     uzemi_txt
1061229316    3.226 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20221231 2022     12         43     531987   Dolní Zimoř
1061229847    3.704 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20221231 2022     12         43     585203       Držková
1061227062    3.800 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20221231 2022     12         43     533262 Červené Pečky
1061226961   14.286 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20221231 2022     12         43     540463        Bolkov
1061180794    1.900 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20221231 2022     12         43     583286    Lelekovice
```

### 020. [C] Uchazeči o zaměstnání dosažitelní a podíl nezaměstnaných osob podle obcí

                        hodnota
polozka                        
target_years_present       2023
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota     vuk              vuk_text   obdobi  rok  mesic  uzemi_cis  uzemi_kod                uzemi_txt
1067703135     34.0 NEZ0007 Uchazeči o zaměstnání 20230131 2023      1         43     500011 Želechovice nad Dřevnicí
1134596392     20.0 NEZ0007 Uchazeči o zaměstnání 20230731 2023      7         43     500011 Želechovice nad Dřevnicí
1175844147     19.0 NEZ0007 Uchazeči o zaměstnání 20230930 2023      9         43     500011 Želechovice nad Dřevnicí
1210153651     23.0 NEZ0007 Uchazeči o zaměstnání 20231130 2023     11         43     500011 Želechovice nad Dřevnicí
1195558594     18.0 NEZ0007 Uchazeči o zaměstnání 20231031 2023     10         43     500011 Želechovice nad Dřevnicí
```

#### TAIL

```
     idhod  hodnota     vuk                              vuk_text   obdobi  rok  mesic  uzemi_cis  uzemi_kod             uzemi_txt
1223708159    0.000 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20231231 2023     12         43     575917              Urbanice
1223711622    0.000 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20231231 2023     12         43     560430         Zhoř u Tábora
1223715802    6.276 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20231231 2023     12         43     598933           Český Těšín
1223720851    5.512 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20231231 2023     12         43     574155             Jetřichov
1223719509    2.604 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20231231 2023     12         43     554065 Jakubčovice nad Odrou
```

### 021. [C] Uchazeči o zaměstnání dosažitelní a podíl nezaměstnaných osob podle obcí

                        hodnota
polozka                        
target_years_present       2024
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota     vuk              vuk_text   obdobi  rok  mesic  uzemi_cis  uzemi_kod                uzemi_txt
1285998842     29.0 NEZ0007 Uchazeči o zaměstnání 20240430 2024      4         43     500011 Želechovice nad Dřevnicí
1354646498     26.0 NEZ0007 Uchazeči o zaměstnání 20241130 2024     11         43     500011 Želechovice nad Dřevnicí
1307690694     25.0 NEZ0007 Uchazeči o zaměstnání 20240731 2024      7         43     500011 Želechovice nad Dřevnicí
1335857939     26.0 NEZ0007 Uchazeči o zaměstnání 20240930 2024      9         43     500011 Želechovice nad Dřevnicí
1270041170     24.0 NEZ0007 Uchazeči o zaměstnání 20240331 2024      3         43     500011 Želechovice nad Dřevnicí
```

#### TAIL

```
     idhod  hodnota     vuk                              vuk_text   obdobi  rok  mesic  uzemi_cis  uzemi_kod   uzemi_txt
1330852734    1.738 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20240831 2024      8         43     599999 Trojanovice
1290447813    1.970 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20240531 2024      5         43     599999 Trojanovice
1301383520    1.854 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20240630 2024      6         43     599999 Trojanovice
1249670750    1.718 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20240131 2024      1         43     599999 Trojanovice
1374939350    2.317 NEZ0006 Podíl nezaměstnaných osob  - ženy (%) 20241231 2024     12         43     599999 Trojanovice
```

### 022. [C] Pohyb obyvatel za ČR, kraje, okresy, SO ORP a obce - rok 2020

                         hodnota
polozka                         
target_years_present        None
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
    idhod  hodnota     vuk vuk_text  stapro_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do        vuzemi_txt
878636192     6383 DEM0008  Zemřelí        5393         100        3093 2020 2020-01-01 2020-12-31   Pardubický kraj
878636233    14015 DEM0008  Zemřelí        5393         100        3115 2020 2020-01-01 2020-12-31 Jihomoravský kraj
878636297     7794 DEM0008  Zemřelí        5393         100        3131 2020 2020-01-01 2020-12-31      Zlínský kraj
878657310    15302 DEM0008  Zemřelí        5393         100        3026 2020 2020-01-01 2020-12-31  Středočeský kraj
878657442    10793 DEM0008  Zemřelí        5393         100        3069 2020 2020-01-01 2020-12-31      Ústecký kraj
```

#### TAIL

```
    idhod  hodnota     vuk              vuk_text  stapro_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do                vuzemi_txt
878924573      326 DEM0004 Střední stav obyvatel        2406          43      595578 2020 2020-07-01 2020-07-01 Fryšava pod Žákovou horou
878924578     1613 DEM0004 Střední stav obyvatel        2406          43      595586 2020 2020-07-01 2020-07-01         Hamry nad Sázavou
878917290      318 DEM0004 Střední stav obyvatel        2406          43      572560 2020 2020-07-01 2020-07-01                     Banín
878920267      110 DEM0004 Střední stav obyvatel        2406          43      582344 2020 2020-07-01 2020-07-01                   Skrchov
878920291      122 DEM0004 Střední stav obyvatel        2406          43      582450 2020 2020-07-01 2020-07-01                   Synalov
```

### 023. [C] Pohyb obyvatel za ČR, kraje, okresy, SO ORP a obce - rok 2021

                         hodnota
polozka                         
target_years_present        None
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
    idhod  hodnota     vuk vuk_text  stapro_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do   vuzemi_txt
967561553        0 DEM0008  Zemřelí        5393          43      581526 2021 2021-01-01 2021-12-31 Dlouhá Lhota
967558929        1 DEM0008  Zemřelí        5393          43      571814 2021 2021-01-01 2021-12-31       Zdětín
967558946        5 DEM0008  Zemřelí        5393          43      571881 2021 2021-01-01 2021-12-31    Strážiště
967559924        8 DEM0008  Zemřelí        5393          43      575089 2021 2021-01-01 2021-12-31    Chvojenec
967561518      170 DEM0008  Zemřelí        5393          43      581372 2021 2021-01-01 2021-12-31    Boskovice
```

#### TAIL

```
    idhod  hodnota     vuk              vuk_text  stapro_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do       vuzemi_txt
967423467     1084 DEM0004 Střední stav obyvatel        9379          43      545431 2021 2021-01-01 2021-12-31            Brloh
967423471      792 DEM0004 Střední stav obyvatel        9379          43      545457 2021 2021-01-01 2021-12-31 Černá v Pošumaví
967553715     1014 DEM0004 Střední stav obyvatel        9379          43      552020 2021 2021-01-01 2021-12-31        Hlušovice
967550132     3773 DEM0004 Střední stav obyvatel        9379          43      538540 2021 2021-01-01 2021-12-31         Nehvizdy
967550135     1403 DEM0004 Střední stav obyvatel        9379          43      538558 2021 2021-01-01 2021-12-31         Nová Ves
```

### 024. [C] Sčítání 2021 - Byty podle obydlenosti

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  obydlenost_cis  obydlenost_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt    obydlenost_txt                uzemi_txt
988459561      859      2607             NaN             NaN         43     500011      2021 2021-03-26 Počet bytů               NaN Želechovice nad Dřevnicí
988445854      669      2607          3316.0             1.0         43     500011      2021 2021-03-26 Počet bytů   obvykle obydlen Želechovice nad Dřevnicí
988445855      190      2607          3244.0            52.0         43     500011      2021 2021-03-26 Počet bytů obvykle neobydlen Želechovice nad Dřevnicí
988456154      552      2607             NaN             NaN         43     500020      2021 2021-03-26 Počet bytů               NaN        Petrov nad Desnou
988445856      469      2607          3316.0             1.0         43     500020      2021 2021-03-26 Počet bytů   obvykle obydlen        Petrov nad Desnou
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  obydlenost_cis  obydlenost_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt    obydlenost_txt     uzemi_txt
988441577   146498      2607          3316.0             1.0        101      40916      2021 2021-03-26 Počet bytů   obvykle obydlen Ostrava-město
988441578    13707      2607          3244.0            52.0        101      40916      2021 2021-03-26 Počet bytů obvykle neobydlen Ostrava-město
988456799   721332      2607             NaN             NaN        101      40924      2021 2021-03-26 Počet bytů               NaN         Praha
988450315   627705      2607          3316.0             1.0        101      40924      2021 2021-03-26 Počet bytů   obvykle obydlen         Praha
988450316    93627      2607          3244.0            52.0        101      40924      2021 2021-03-26 Počet bytů obvykle neobydlen         Praha
```

### 025. [C] Sčítání 2021 - Hospodařící domácnosti podle velikosti a typu domácnosti

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  clenu_cis  clenu_kod  typ_cis  typ_kod typ_struktura  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                       ukaz_txt  clenu_txt                                             typ_txt                uzemi_txt uzemi_typ
1061994271      759      2423        NaN        NaN      NaN      NaN           NaN         43     500011      2021 2021-03-26 Počet hospodařících domácností        NaN                                                 NaN Želechovice nad Dřevnicí      obec
1062015492      528      2423        NaN        NaN   3303.0     12.0             1         43     500011      2021 2021-03-26 Počet hospodařících domácností        NaN                                  Rodinné domácnosti Želechovice nad Dřevnicí      obec
1061948848      505      2423        NaN        NaN   3303.0     13.0           1.1         43     500011      2021 2021-03-26 Počet hospodařících domácností        NaN                                Domácnost - 1 rodina Želechovice nad Dřevnicí      obec
1062520654      429      2423        NaN        NaN   3303.0     14.0        1.1.1.         43     500011      2021 2021-03-26 Počet hospodařících domácností        NaN                          Domácnost - 1 úplná rodina Želechovice nad Dřevnicí      obec
1062466884      356      2423        NaN        NaN   3303.0      4.0       1.1.1.1         43     500011      2021 2021-03-26 Počet hospodařících domácností        NaN Domácnost - 1 rodina - úplná rodina - manželský pár Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  clenu_cis  clenu_kod  typ_cis  typ_kod typ_struktura  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                       ukaz_txt clenu_txt                                               typ_txt uzemi_txt uzemi_typ
1062425399       15      2423     7601.0    79999.0   3303.0      9.0       1.1.2.2        101      40924      2021 2021-03-26 Počet hospodařících domácností  7 a více Domácnost - 1 rodina - neúplná rodina - osamělá matka     Praha     okres
1061854974      593      2423     7601.0    79999.0   3303.0     10.0           1.2        101      40924      2021 2021-03-26 Počet hospodařících domácností  7 a více                            Domácnost - 2 a více rodin     Praha     okres
1061940637       18      2423     7601.0    79999.0   3303.0     11.0             2        101      40924      2021 2021-03-26 Počet hospodařících domácností  7 a více                                  Nerodinné domácnosti     Praha     okres
1061968613        0      2423     7601.0    79999.0   3301.0   1100.0           2.1        101      40924      2021 2021-03-26 Počet hospodařících domácností  7 a více                                 Domácnost jednotlivce     Praha     okres
1061826678       18      2423     7601.0    79999.0   3303.0     20.0           2.2        101      40924      2021 2021-03-26 Počet hospodařících domácností  7 a více                        Vícečlenná nerodinná domácnost     Praha     okres
```

### 026. [C] Sčítání 2021 - Obydlené byty podle celkové plochy bytu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  plocha_cis   plocha_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt   plocha_txt                uzemi_txt
988445854      669      2607         NaN          NaN         43     500011      2021 2021-03-26 Počet obydlených bytů          NaN Želechovice nad Dřevnicí
988552787       35      2607      5768.0 9.000000e+00         43     500011      2021 2021-03-26 Počet obydlených bytů   nezjištěno Želechovice nad Dřevnicí
988758513       21      2607      7700.0 3.999996e+14         43     500011      2021 2021-03-26 Počet obydlených bytů   do 39,9 m2 Želechovice nad Dřevnicí
988905538       38      2607      7700.0 4.100406e+14         43     500011      2021 2021-03-26 Počet obydlených bytů 40,0-59,9 m2 Želechovice nad Dřevnicí
988905640      115      2607      7700.0 4.100606e+14         43     500011      2021 2021-03-26 Počet obydlených bytů 60,0-79,9 m2 Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  plocha_cis   plocha_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt      plocha_txt uzemi_txt
988627403   184551      2607      7700.0 4.100606e+14        101      40924      2021 2021-03-26 Počet obydlených bytů    60,0-79,9 m2     Praha
988987371    80072      2607      7700.0 4.100806e+14        101      40924      2021 2021-03-26 Počet obydlených bytů    80,0-99,9 m2     Praha
989060858    33186      2607      7700.0 4.201006e+14        101      40924      2021 2021-03-26 Počet obydlených bytů  100,0-119,9 m2     Praha
988914826    22108      2607      7700.0 4.201206e+14        101      40924      2021 2021-03-26 Počet obydlených bytů  120,0-149,9 m2     Praha
988694301    24354      2607      7700.0 4.201508e+14        101      40924      2021 2021-03-26 Počet obydlených bytů 150,0 a více m2     Praha
```

### 027. [C] Sčítání 2021 - Obydlené byty podle hlavního zdroje energie používaného k vytápění

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  energie_cis  energie_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                energie_txt                uzemi_txt uzemi_typ
 988445854      669      2607          NaN          NaN         43     500011      2021 2021-03-26 Počet obydlených bytů                        NaN Želechovice nad Dřevnicí      obec
1025234117        2      2607       3063.0          1.0         43     500011      2021 2021-03-26 Počet obydlených bytů         Z kotelny mimo dům Želechovice nad Dřevnicí      obec
1025246019       54      2607       3063.0          2.0         43     500011      2021 2021-03-26 Počet obydlených bytů Uhlí, koks, uhelné brikety Želechovice nad Dřevnicí      obec
1025200775      139      2607       3063.0          3.0         43     500011      2021 2021-03-26 Počet obydlených bytů     Dřevo, dřevěné brikety Želechovice nad Dřevnicí      obec
1025200780        1      2607       3063.0          4.0         43     500011      2021 2021-03-26 Počet obydlených bytů         Topné oleje, nafta Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  energie_cis  energie_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                              energie_txt uzemi_txt uzemi_typ
1025183742      942      2607       3063.0         10.0        101      40924      2021 2021-03-26 Počet obydlených bytů Jiné druhy plynu (LPG, CNG, bioplyn aj.)     Praha     okres
1025242520      190      2607       3063.0         11.0        101      40924      2021 2021-03-26 Počet obydlených bytů                           Dřevěné pelety     Praha     okres
1025230689      160      2607       3063.0         12.0        101      40924      2021 2021-03-26 Počet obydlených bytů                        Solární kolektory     Praha     okres
1025183743     1796      2607       3063.0          8.0        101      40924      2021 2021-03-26 Počet obydlených bytů                                     Jiný     Praha     okres
1025242519    57201      2607       3063.0         99.0        101      40924      2021 2021-03-26 Počet obydlených bytů                               Nezjištěno     Praha     okres
```

### 028. [C] Sčítání 2021 - Obydlené byty podle materiálu nosných zdí a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  material_cis  material_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt           material_txt                                   druhdomu_txt                uzemi_txt uzemi_typ
1056378243        9      2607          3043             6           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů                  Dřevo                                            NaN Želechovice nad Dřevnicí      obec
1056306090        0      2607          3043             6        3041.0           4.0         43     500011      2021 2021-03-26 Počet obydlených bytů                  Dřevo                                    Bytové domy Želechovice nad Dřevnicí      obec
1056208834        9      2607          3043             6        3240.0          51.0         43     500011      2021 2021-03-26 Počet obydlených bytů                  Dřevo                                   Rodinné domy Želechovice nad Dřevnicí      obec
1055992104        0      2607          3043             6        3240.0          55.0         43     500011      2021 2021-03-26 Počet obydlených bytů                  Dřevo Ostatní budovy (bez rodinných a bytových domů) Želechovice nad Dřevnicí      obec
1056022162      566      2607          3337            10           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů Kámen, cihly, tvárnice                                            NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  material_cis  material_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                  material_txt                                   druhdomu_txt uzemi_txt uzemi_typ
1055912079      626      2607          3337            27        3240.0          55.0        101      40924      2021 2021-03-26 Počet obydlených bytů Ostatní materiály a kombinace Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
1056001833   217086      2607          3043             4           NaN           NaN        101      40924      2021 2021-03-26 Počet obydlených bytů                Stěnové panely                                            NaN     Praha     okres
1056181046   214383      2607          3043             4        3041.0           4.0        101      40924      2021 2021-03-26 Počet obydlených bytů                Stěnové panely                                    Bytové domy     Praha     okres
1056537352     1475      2607          3043             4        3240.0          51.0        101      40924      2021 2021-03-26 Počet obydlených bytů                Stěnové panely                                   Rodinné domy     Praha     okres
1056003220     1228      2607          3043             4        3240.0          55.0        101      40924      2021 2021-03-26 Počet obydlených bytů                Stěnové panely Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
```

### 029. [C] Sčítání 2021 - Obydlené byty podle polohy bytu v domě a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  poloha_cis  poloha_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt     poloha_txt                                   druhdomu_txt                uzemi_txt uzemi_typ
1056838985        5      2607        3058           1           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů Suterén, sklep                                            NaN Želechovice nad Dřevnicí      obec
1056662139        0      2607        3058           1        3041.0           4.0         43     500011      2021 2021-03-26 Počet obydlených bytů Suterén, sklep                                    Bytové domy Želechovice nad Dřevnicí      obec
1056738670        5      2607        3058           1        3240.0          51.0         43     500011      2021 2021-03-26 Počet obydlených bytů Suterén, sklep                                   Rodinné domy Želechovice nad Dřevnicí      obec
1056738671        0      2607        3058           1        3240.0          55.0         43     500011      2021 2021-03-26 Počet obydlených bytů Suterén, sklep Ostatní budovy (bez rodinných a bytových domů) Želechovice nad Dřevnicí      obec
1056877256      426      2607        3058           2           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů        Přízemí                                            NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  poloha_cis  poloha_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt          poloha_txt                                   druhdomu_txt uzemi_txt uzemi_typ
1056890008      216      2607        3341          52        3240.0          55.0        101      40924      2021 2021-03-26 Počet obydlených bytů 8. a vyšší poschodí Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
1056622150    56937      2607        3058          99           NaN           NaN        101      40924      2021 2021-03-26 Počet obydlených bytů          Nezjištěno                                            NaN     Praha     okres
1056660157    52127      2607        3058          99        3041.0           4.0        101      40924      2021 2021-03-26 Počet obydlených bytů          Nezjištěno                                    Bytové domy     Praha     okres
1056736689     4023      2607        3058          99        3240.0          51.0        101      40924      2021 2021-03-26 Počet obydlených bytů          Nezjištěno                                   Rodinné domy     Praha     okres
1056851812      787      2607        3058          99        3240.0          55.0        101      40924      2021 2021-03-26 Počet obydlených bytů          Nezjištěno Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
```

### 030. [C] Sčítání 2021 - Obydlené byty podle počtu obytných místností

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  mistnosti_cis  mistnosti_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                   ukaz_txt  mistnosti_txt                uzemi_txt
988481225     3.99      2416            NaN            NaN         43     500011      2021 2021-03-26 Průměrný počet obytných místností na 1 byt            NaN Želechovice nad Dřevnicí
988481226     3.54      2416            NaN            NaN         43     500020      2021 2021-03-26 Průměrný počet obytných místností na 1 byt            NaN        Petrov nad Desnou
988492658     3.95      2416            NaN            NaN         43     500046      2021 2021-03-26 Průměrný počet obytných místností na 1 byt            NaN                  Libhošť
988503734     3.79      2416            NaN            NaN         43     500062      2021 2021-03-26 Průměrný počet obytných místností na 1 byt            NaN                   Krhová
988481227     3.75      2416            NaN            NaN         43     500071      2021 2021-03-26 Průměrný počet obytných místností na 1 byt            NaN                  Poličná
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  mistnosti_cis  mistnosti_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt mistnosti_txt uzemi_txt
988767519  69381.0      2607         7600.0            1.0        101      40924      2021 2021-03-26 Počet obydlených bytů             1     Praha
988767518 195199.0      2607         7600.0            2.0        101      40924      2021 2021-03-26 Počet obydlených bytů             2     Praha
988914591 205274.0      2607         7600.0            3.0        101      40924      2021 2021-03-26 Počet obydlených bytů             3     Praha
988694060  66622.0      2607         7600.0            4.0        101      40924      2021 2021-03-26 Počet obydlených bytů             4     Praha
988914590  36824.0      2607         7601.0        59999.0        101      40924      2021 2021-03-26 Počet obydlených bytů      5 a více     Praha
```

### 031. [C] Sčítání 2021 - Obydlené byty podle počtu obytných místností včetně kuchyně

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  mistnosti_cis  mistnosti_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt  mistnosti_txt                uzemi_txt
988445854      669      2607            NaN            NaN         43     500011      2021 2021-03-26 Počet obydlených bytů            NaN Želechovice nad Dřevnicí
988445856      469      2607            NaN            NaN         43     500020      2021 2021-03-26 Počet obydlených bytů            NaN        Petrov nad Desnou
988445858      627      2607            NaN            NaN         43     500046      2021 2021-03-26 Počet obydlených bytů            NaN                  Libhošť
988445860      782      2607            NaN            NaN         43     500062      2021 2021-03-26 Počet obydlených bytů            NaN                   Krhová
988445862      652      2607            NaN            NaN         43     500071      2021 2021-03-26 Počet obydlených bytů            NaN                  Poličná
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  mistnosti_cis  mistnosti_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                                        ukaz_txt  mistnosti_txt     uzemi_txt
999992230 3.787444      9621            NaN            NaN        101      40886      2021 2021-03-26 Průměrný počet obytných místností (s kuchyní) na 1 obydlený byt            NaN       Karviná
999989158 4.124827      9621            NaN            NaN        101      40894      2021 2021-03-26 Průměrný počet obytných místností (s kuchyní) na 1 obydlený byt            NaN    Nový Jičín
999989170 4.321796      9621            NaN            NaN        101      40908      2021 2021-03-26 Průměrný počet obytných místností (s kuchyní) na 1 obydlený byt            NaN         Opava
999989162 3.640287      9621            NaN            NaN        101      40916      2021 2021-03-26 Průměrný počet obytných místností (s kuchyní) na 1 obydlený byt            NaN Ostrava-město
999992232 3.204358      9621            NaN            NaN        101      40924      2021 2021-03-26 Průměrný počet obytných místností (s kuchyní) na 1 obydlený byt            NaN         Praha
```

### 032. [C] Sčítání 2021 - Obydlené byty podle počtu osob v bytě

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  osob_cis  osob_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                              ukaz_txt  osob_txt                uzemi_txt
987843452     2.65      2419       NaN       NaN         43     500011      2021 2021-03-26 Průměrný počet osob na 1 obydlený byt       NaN Želechovice nad Dřevnicí
987848944     2.47      2419       NaN       NaN         43     500020      2021 2021-03-26 Průměrný počet osob na 1 obydlený byt       NaN        Petrov nad Desnou
987844341     2.68      2419       NaN       NaN         43     500046      2021 2021-03-26 Průměrný počet osob na 1 obydlený byt       NaN                  Libhošť
987848529     2.57      2419       NaN       NaN         43     500062      2021 2021-03-26 Průměrný počet osob na 1 obydlený byt       NaN                   Krhová
987843555     2.61      2419       NaN       NaN         43     500071      2021 2021-03-26 Průměrný počet osob na 1 obydlený byt       NaN                  Poličná
```

#### TAIL

```
    idhod   hodnota  ukaz_kod  osob_cis  osob_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                    ukaz_txt  osob_txt     uzemi_txt
987841818  227997.0      4152       NaN       NaN        101      40886      2021 2021-03-26 Počet bydlících osob v bytě       NaN       Karviná
987841831  141778.0      4152       NaN       NaN        101      40894      2021 2021-03-26 Počet bydlících osob v bytě       NaN    Nový Jičín
987841828  166501.0      4152       NaN       NaN        101      40908      2021 2021-03-26 Počet bydlících osob v bytě       NaN         Opava
987841394  301098.0      4152       NaN       NaN        101      40916      2021 2021-03-26 Počet bydlících osob v bytě       NaN Ostrava-město
987840966 1261930.0      4152       NaN       NaN        101      40924      2021 2021-03-26 Počet bydlících osob v bytě       NaN         Praha
```

### 033. [C] Sčítání 2021 - Obydlené byty podle právního důvodu užívání bytu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  uzivani_cis  uzivani_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt            uzivani_txt                uzemi_txt
988445854      669      2607          NaN          NaN         43     500011      2021 2021-03-26 Počet obydlených bytů                    NaN Želechovice nad Dřevnicí
988991446      493      2607       3055.0          1.0         43     500011      2021 2021-03-26 Počet obydlených bytů       ve vlastním domě Želechovice nad Dřevnicí
988697662       47      2607       3055.0          2.0         43     500011      2021 2021-03-26 Počet obydlených bytů  v osobním vlastnictví Želechovice nad Dřevnicí
988918189       50      2607       3055.0          3.0         43     500011      2021 2021-03-26 Počet obydlených bytů jiné bezplatné užívání Želechovice nad Dřevnicí
988844224       30      2607       3055.0          4.0         43     500011      2021 2021-03-26 Počet obydlených bytů      nájemní/pronajatý Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  uzivani_cis  uzivani_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt            uzivani_txt uzemi_txt
988562018    36630      2607       3055.0          3.0        101      40924      2021 2021-03-26 Počet obydlených bytů jiné bezplatné užívání     Praha
989061420   200753      2607       3055.0          4.0        101      40924      2021 2021-03-26 Počet obydlených bytů      nájemní/pronajatý     Praha
988628077    16766      2607       3055.0          8.0        101      40924      2021 2021-03-26 Počet obydlených bytů             jiný důvod     Praha
988987930    35107      2607       3055.0          9.0        101      40924      2021 2021-03-26 Počet obydlených bytů             družstevní     Praha
989061422    56267      2607       3055.0         99.0        101      40924      2021 2021-03-26 Počet obydlených bytů             nezjištěno     Praha
```

### 034. [C] Sčítání 2021 - Obydlené byty podle převažujícího způsobu vytápění

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  vytapeni_cis  vytapeni_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                         vytapeni_txt                uzemi_txt uzemi_typ
 988445854      669      2607           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů                                  NaN Želechovice nad Dřevnicí      obec
1025149181        2      2607        3062.0           1.0         43     500011      2021 2021-03-26 Počet obydlených bytů                     Ústřední dálkové Želechovice nad Dřevnicí      obec
1025149180      250      2607        3261.0          54.0         43     500011      2021 2021-03-26 Počet obydlených bytů                     Ústřední domovní Želechovice nad Dřevnicí      obec
1025149182      321      2607        3062.0           3.0         43     500011      2021 2021-03-26 Počet obydlených bytů Ústřední s vlastním zdrojem (v bytě) Želechovice nad Dřevnicí      obec
1025149183       52      2607        3062.0           4.0         43     500011      2021 2021-03-26 Počet obydlených bytů              Lokální topidla (kamna) Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  vytapeni_cis  vytapeni_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                         vytapeni_txt uzemi_txt uzemi_typ
1025152832   112037      2607        3261.0          54.0        101      40924      2021 2021-03-26 Počet obydlených bytů                     Ústřední domovní     Praha     okres
1025152834   115272      2607        3062.0           3.0        101      40924      2021 2021-03-26 Počet obydlených bytů Ústřední s vlastním zdrojem (v bytě)     Praha     okres
1025152835    59359      2607        3062.0           4.0        101      40924      2021 2021-03-26 Počet obydlených bytů              Lokální topidla (kamna)     Praha     okres
1025153843     5986      2607        3062.0           5.0        101      40924      2021 2021-03-26 Počet obydlených bytů                                 Jiný     Praha     okres
1025153844    31646      2607        3062.0           9.0        101      40924      2021 2021-03-26 Počet obydlených bytů                           Nezjištěno     Praha     okres
```

### 035. [C] Sčítání 2021 - Obydlené byty podle připojení na plyn

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  plyn_cis  plyn_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                          plyn_txt                uzemi_txt uzemi_typ
 988445854      669      2607       NaN       NaN         43     500011      2021 2021-03-26 Počet obydlených bytů                               NaN Želechovice nad Dřevnicí      obec
1025272432      429      2607    3056.0       3.0         43     500011      2021 2021-03-26 Počet obydlených bytů                    Z veřejné sítě Želechovice nad Dřevnicí      obec
1025272436        1      2607    3056.0       4.0         43     500011      2021 2021-03-26 Počet obydlených bytů Z domovního (lokálního) zásobníku Želechovice nad Dřevnicí      obec
1025272435       10      2607    3056.0       5.0         43     500011      2021 2021-03-26 Počet obydlených bytů       Pouze plynové tlakové lahve Želechovice nad Dřevnicí      obec
1025272433      225      2607    3056.0       2.0         43     500011      2021 2021-03-26 Počet obydlených bytů                         Bez plynu Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  plyn_cis  plyn_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                          plyn_txt uzemi_txt uzemi_typ
1025267959   453589      2607    3056.0       3.0        101      40924      2021 2021-03-26 Počet obydlených bytů                    Z veřejné sítě     Praha     okres
1025267963     3273      2607    3056.0       4.0        101      40924      2021 2021-03-26 Počet obydlených bytů Z domovního (lokálního) zásobníku     Praha     okres
1025267962      811      2607    3056.0       5.0        101      40924      2021 2021-03-26 Počet obydlených bytů       Pouze plynové tlakové lahve     Praha     okres
1025267960   163121      2607    3056.0       2.0        101      40924      2021 2021-03-26 Počet obydlených bytů                         Bez plynu     Praha     okres
1025267961     6911      2607    3056.0       9.0        101      40924      2021 2021-03-26 Počet obydlených bytů                        Nezjištěno     Praha     okres
```

### 036. [C] Sčítání 2021 - Obydlené byty podle připojení na vodovod

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  vodovod_cis  vodovod_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                                    vodovod_txt                uzemi_txt uzemi_typ
 988445854      669      2607          NaN          NaN         43     500011      2021 2021-03-26 Počet obydlených bytů                                            NaN Želechovice nad Dřevnicí      obec
1025125229      300      2607       3061.0          4.0         43     500011      2021 2021-03-26 Počet obydlených bytů                  V bytě - pouze z veřejné sítě Želechovice nad Dřevnicí      obec
1025113300      241      2607       3061.0          5.0         43     500011      2021 2021-03-26 Počet obydlených bytů            V bytě - pouze ze soukromého zdroje Želechovice nad Dřevnicí      obec
1025125020       95      2607       3061.0          6.0         43     500011      2021 2021-03-26 Počet obydlených bytů V bytě - z veřejné sítě i ze soukromého zdroje Želechovice nad Dřevnicí      obec
1025090470        2      2607       3061.0          2.0         43     500011      2021 2021-03-26 Počet obydlených bytů                                Mimo byt v domě Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  vodovod_cis  vodovod_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                                    vodovod_txt uzemi_txt uzemi_typ
1025125982     1555      2607       3061.0          5.0        101      40924      2021 2021-03-26 Počet obydlených bytů            V bytě - pouze ze soukromého zdroje     Praha     okres
1025094367     3048      2607       3061.0          6.0        101      40924      2021 2021-03-26 Počet obydlených bytů V bytě - z veřejné sítě i ze soukromého zdroje     Praha     okres
1025114272      533      2607       3061.0          2.0        101      40924      2021 2021-03-26 Počet obydlených bytů                                Mimo byt v domě     Praha     okres
1025114271      119      2607       3061.0          3.0        101      40924      2021 2021-03-26 Počet obydlených bytů                                   Bez vodovodu     Praha     okres
1025125983    54111      2607       3061.0          9.0        101      40924      2021 2021-03-26 Počet obydlených bytů                                     Nezjištěno     Praha     okres
```

### 037. [C] Sčítání 2021 - Obydlené byty podle vlastníka a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  vlastnik_cis  vlastnik_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt    vlastnik_txt                                   druhdomu_txt                uzemi_txt uzemi_typ
1056455826      590      2607          3049             1           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů   Fyzická osoba                                            NaN Želechovice nad Dřevnicí      obec
1056047151        5      2607          3049             1        3041.0           4.0         43     500011      2021 2021-03-26 Počet obydlených bytů   Fyzická osoba                                    Bytové domy Želechovice nad Dřevnicí      obec
1056241247      584      2607          3049             1        3240.0          51.0         43     500011      2021 2021-03-26 Počet obydlených bytů   Fyzická osoba                                   Rodinné domy Želechovice nad Dřevnicí      obec
1056565629        1      2607          3049             1        3240.0          55.0         43     500011      2021 2021-03-26 Počet obydlených bytů   Fyzická osoba Ostatní budovy (bez rodinných a bytových domů) Želechovice nad Dřevnicí      obec
1055921627        1      2607          3049            10           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů Bytové družstvo                                            NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  vlastnik_cis  vlastnik_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt        vlastnik_txt                                   druhdomu_txt uzemi_txt uzemi_typ
1056269498      108      2607          3049             7        3240.0          55.0        101      40924      2021 2021-03-26 Počet obydlených bytů Kombinace vlastníků Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
1056445785      907      2607          3049             9           NaN           NaN        101      40924      2021 2021-03-26 Počet obydlených bytů          Nezjištěno                                            NaN     Praha     okres
1056448071      387      2607          3049             9        3041.0           4.0        101      40924      2021 2021-03-26 Počet obydlených bytů          Nezjištěno                                    Bytové domy     Praha     okres
1056536797      461      2607          3049             9        3240.0          51.0        101      40924      2021 2021-03-26 Počet obydlených bytů          Nezjištěno                                   Rodinné domy     Praha     okres
1056180640       59      2607          3049             9        3240.0          55.0        101      40924      2021 2021-03-26 Počet obydlených bytů          Nezjištěno Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
```

### 038. [C] Sčítání 2021 - Obydlené byty podle vybavení domu výtahem a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  vytah_cis  vytah_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt  vytah_txt                                   druhdomu_txt                uzemi_txt uzemi_typ
1055714597        0      2607       3206          1           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů  S výtahem                                            NaN Želechovice nad Dřevnicí      obec
1055754312        0      2607       3206          1        3041.0           4.0         43     500011      2021 2021-03-26 Počet obydlených bytů  S výtahem                                    Bytové domy Želechovice nad Dřevnicí      obec
1055754189        0      2607       3206          1        3240.0          51.0         43     500011      2021 2021-03-26 Počet obydlených bytů  S výtahem                                   Rodinné domy Želechovice nad Dřevnicí      obec
1055810234        0      2607       3206          1        3240.0          55.0         43     500011      2021 2021-03-26 Počet obydlených bytů  S výtahem Ostatní budovy (bez rodinných a bytových domů) Želechovice nad Dřevnicí      obec
1055686827      666      2607       3206          2           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů Bez výtahu                                            NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  vytah_cis  vytah_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt  vytah_txt                                   druhdomu_txt uzemi_txt uzemi_typ
1055828735     3500      2607       3206          2        3240.0          55.0        101      40924      2021 2021-03-26 Počet obydlených bytů Bez výtahu Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
1055772686      983      2607       5768          9           NaN           NaN        101      40924      2021 2021-03-26 Počet obydlených bytů Nezjištěno                                            NaN     Praha     okres
1055772970      569      2607       5768          9        3041.0           4.0        101      40924      2021 2021-03-26 Počet obydlených bytů Nezjištěno                                    Bytové domy     Praha     okres
1055800850      280      2607       5768          9        3240.0          51.0        101      40924      2021 2021-03-26 Počet obydlených bytů Nezjištěno                                   Rodinné domy     Praha     okres
1055745113      134      2607       5768          9        3240.0          55.0        101      40924      2021 2021-03-26 Počet obydlených bytů Nezjištěno Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
```

### 039. [C] Sčítání 2021 - Obydlené byty podle vybavení kuchyní

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  kuchyne_cis  kuchyne_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                         kuchyne_txt                uzemi_txt
988445854      669      2607          NaN          NaN         43     500011      2021 2021-03-26 Počet obydlených bytů                                 NaN Želechovice nad Dřevnicí
999576287      523      2607       3223.0         10.0         43     500011      2021 2021-03-26 Počet obydlených bytů                              Kuchyň Želechovice nad Dřevnicí
999576286      119      2607       3223.0         11.0         43     500011      2021 2021-03-26 Počet obydlených bytů                      Kuchyňský kout Želechovice nad Dřevnicí
999576289        3      2607       3223.0         12.0         43     500011      2021 2021-03-26 Počet obydlených bytů Bez kuchyně a bez kuchyňského koutu Želechovice nad Dřevnicí
999576288       24      2607       3223.0          9.0         43     500011      2021 2021-03-26 Počet obydlených bytů                          Nezjištěno Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  kuchyne_cis  kuchyne_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                         kuchyne_txt uzemi_txt
988450315   627705      2607          NaN          NaN        101      40924      2021 2021-03-26 Počet obydlených bytů                                 NaN     Praha
999564105   284612      2607       3223.0         10.0        101      40924      2021 2021-03-26 Počet obydlených bytů                              Kuchyň     Praha
999564104   283728      2607       3223.0         11.0        101      40924      2021 2021-03-26 Počet obydlených bytů                      Kuchyňský kout     Praha
999564107     4822      2607       3223.0         12.0        101      40924      2021 2021-03-26 Počet obydlených bytů Bez kuchyně a bez kuchyňského koutu     Praha
999564106    54543      2607       3223.0          9.0        101      40924      2021 2021-03-26 Počet obydlených bytů                          Nezjištěno     Praha
```

### 040. [C] Sčítání 2021 - Obydlené byty podle způsobu odvádění odpadních vod a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  odpad_cis  odpad_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt       odpad_txt                                   druhdomu_txt                uzemi_txt uzemi_typ
1055879666      239      2607       2335         10           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů Kanalizační síť                                            NaN Želechovice nad Dřevnicí      obec
1055791123       27      2607       2335         10        3041.0           4.0         43     500011      2021 2021-03-26 Počet obydlených bytů Kanalizační síť                                    Bytové domy Želechovice nad Dřevnicí      obec
1055763204      208      2607       2335         10        3240.0          51.0         43     500011      2021 2021-03-26 Počet obydlených bytů Kanalizační síť                                   Rodinné domy Želechovice nad Dřevnicí      obec
1055902781        4      2607       2335         10        3240.0          55.0         43     500011      2021 2021-03-26 Počet obydlených bytů Kanalizační síť Ostatní budovy (bez rodinných a bytových domů) Želechovice nad Dřevnicí      obec
1055879665      350      2607       2335         20           NaN           NaN         43     500011      2021 2021-03-26 Počet obydlených bytů           Žumpa                                            NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  odpad_cis  odpad_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt     odpad_txt                                   druhdomu_txt uzemi_txt uzemi_typ
1055828738        8      2607       2335         40        3240.0          55.0        101      40924      2021 2021-03-26 Počet obydlených bytů Bez připojení Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
1055828348     9925      2607       5768          9           NaN           NaN        101      40924      2021 2021-03-26 Počet obydlených bytů    Nezjištěno                                            NaN     Praha     okres
1055717263     7369      2607       5768          9        3041.0           4.0        101      40924      2021 2021-03-26 Počet obydlených bytů    Nezjištěno                                    Bytové domy     Praha     okres
1055800862     1718      2607       5768          9        3240.0          51.0        101      40924      2021 2021-03-26 Počet obydlených bytů    Nezjištěno                                   Rodinné domy     Praha     okres
1055800957      838      2607       5768          9        3240.0          55.0        101      40924      2021 2021-03-26 Počet obydlených bytů    Nezjištěno Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
```

### 041. [C] Sčítání 2021 - Obydlené domy podle materiálu nosných zdí a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  zdi_cis  zdi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt  druh_txt                               zdi_txt                uzemi_txt uzemi_typ
1046559733        7      2409       NaN       NaN     3043        6         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                                 Dřevo Želechovice nad Dřevnicí      obec
1048068757       37      2409       NaN       NaN     3043        7         43     500011      2021 2021-03-26 Počet obydlených domů       NaN            Jiné materiály a kombinace Želechovice nad Dřevnicí      obec
1042786910       29      2409       NaN       NaN     5768        9         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                            Nezjištěno Želechovice nad Dřevnicí      obec
1045051804      433      2409       NaN       NaN     3337       10         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                Kámen, cihly, tvárnice Želechovice nad Dřevnicí      obec
1042786912        0      2409       NaN       NaN     3043       20         43     500011      2021 2021-03-26 Počet obydlených domů       NaN Monolit (monolitická betonová tyčová) Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  zdi_cis  zdi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                                       druh_txt                               zdi_txt uzemi_txt uzemi_typ
1045014606        8      2409    3240.0      55.0     3043        6        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                                 Dřevo     Praha     okres
1045769734      224      2409    3240.0      55.0     3043        7        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)            Jiné materiály a kombinace     Praha     okres
1046524436      694      2409    3240.0      55.0     5768        9        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                            Nezjištěno     Praha     okres
1048033453     1394      2409    3240.0      55.0     3337       10        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                Kámen, cihly, tvárnice     Praha     okres
1048033454       16      2409    3240.0      55.0     3043       20        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů) Monolit (monolitická betonová tyčová)     Praha     okres
```

### 042. [C] Sčítání 2021 - Obydlené domy podle napojení na kanalizaci a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  odpad_cis  odpad_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt  druh_txt                      odpad_txt                uzemi_txt uzemi_typ
1046553698      181      2409       NaN       NaN       2335         10         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                Kanalizační síť Želechovice nad Dřevnicí      obec
1046553699      274      2409       NaN       NaN       2335         20         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                          Žumpa Želechovice nad Dřevnicí      obec
1043533247       51      2409       NaN       NaN       2335         30         43     500011      2021 2021-03-26 Počet obydlených domů       NaN Vlastní čistírna odpadních vod Želechovice nad Dřevnicí      obec
1042779133        6      2409       NaN       NaN       2335         40         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                  bez připojení Želechovice nad Dřevnicí      obec
1043534988       18      2409       NaN       NaN       5768          9         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                     Nezjištěno Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  odpad_cis  odpad_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                                       druh_txt                      odpad_txt uzemi_txt uzemi_typ
1043505672     1935      2409    3240.0      55.0       2335         10        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                Kanalizační síť     Praha     okres
1047278927       89      2409    3240.0      55.0       2335         20        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                          Žumpa     Praha     okres
1043505673        9      2409    3240.0      55.0       2335         30        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů) Vlastní čistírna odpadních vod     Praha     okres
1045769477        7      2409    3240.0      55.0       2335         40        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                  bez připojení     Praha     okres
1045014315      600      2409    3240.0      55.0       5768          9        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                     Nezjištěno     Praha     okres
```

### 043. [C] Sčítání 2021 - Obydlené domy podle napojení na plyn a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  plyn_cis  plyn_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt  druh_txt                                     plyn_txt                uzemi_txt uzemi_typ
1048700824        5      2409       NaN       NaN      2663        20         43     500011      2021 2021-03-26 Počet obydlených domů       NaN Lokální zásobník plynu pro dokončenou stavbu Želechovice nad Dřevnicí      obec
1048415233      181      2409       NaN       NaN      2663        40         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                            Bez přívodu plynu Želechovice nad Dřevnicí      obec
1048944668      345      2409       NaN       NaN      3247        51         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                                  Plyn v domě Želechovice nad Dřevnicí      obec
1048700823      340      2409       NaN       NaN      2663        52         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                          Plyn z veřejné sítě Želechovice nad Dřevnicí      obec
1049272398        4      2409       NaN       NaN      5768         9         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                                   Nezjištěno Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  plyn_cis  plyn_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                                       druh_txt                                     plyn_txt uzemi_txt uzemi_typ
1049120152       30      2409    3240.0      55.0      2663        20        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů) Lokální zásobník plynu pro dokončenou stavbu     Praha     okres
1049120151      521      2409    3240.0      55.0      2663        40        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                            Bez přívodu plynu     Praha     okres
1048549561     1867      2409    3240.0      55.0      3247        51        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                                  Plyn v domě     Praha     okres
1049120150     1837      2409    3240.0      55.0      2663        52        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                          Plyn z veřejné sítě     Praha     okres
1048833590      252      2409    3240.0      55.0      5768         9        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                                   Nezjištěno     Praha     okres
```

### 044. [C] Sčítání 2021 - Obydlené domy podle napojení na vodovod a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  vodovod_cis  vodovod_kod  vodovod_cleneni  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt  druh_txt                     vodovod_txt                uzemi_txt uzemi_typ
1048271171        5      2409       NaN       NaN         3050            4                1         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                    Bez vodovodu Želechovice nad Dřevnicí      obec
1048786530      516      2409       NaN       NaN         3248           51                1         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                  Vodovod v domě Želechovice nad Dřevnicí      obec
1049129361        9      2409       NaN       NaN         3050            9                1         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                      Nezjištěno Želechovice nad Dřevnicí      obec
1048557732      229      2409       NaN       NaN         3050            1                2         43     500011      2021 2021-03-26 Počet obydlených domů       NaN Vodovod v domě - z veřejné sítě Želechovice nad Dřevnicí      obec
1049272001      196      2409       NaN       NaN         3050            2                2         43     500011      2021 2021-03-26 Počet obydlených domů       NaN         Vodovod v domě - domácí Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  vodovod_cis  vodovod_kod  vodovod_cleneni  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                                       druh_txt                              vodovod_txt uzemi_txt uzemi_typ
1049121967     2292      2409    3240.0      55.0         3248           51                1        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                           Vodovod v domě     Praha     okres
1048263017      344      2409    3240.0      55.0         3050            9                1        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                               Nezjištěno     Praha     okres
1048690775     2207      2409    3240.0      55.0         3050            1                2        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)          Vodovod v domě - z veřejné sítě     Praha     okres
1048833199       26      2409    3240.0      55.0         3050            2                2        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                  Vodovod v domě - domácí     Praha     okres
1048405217       59      2409    3240.0      55.0         3050            5                2        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů) Vodovod v domě - z veřejné sítě i domácí     Praha     okres
```

### 045. [C] Sčítání 2021 - Obydlené domy podle počtu bytů v domě a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  byty_cis  byty_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt    druh_txt  byty_txt                uzemi_txt uzemi_typ
1029484583       11      2409      3041         4       NaN       NaN         43     500011      2021 2021-03-26 Počet obydlených domů Bytové domy       NaN Želechovice nad Dřevnicí      obec
1029316250        0      2409      3041         4    7600.0       1.0         43     500011      2021 2021-03-26 Počet obydlených domů Bytové domy       1.0 Želechovice nad Dřevnicí      obec
1029595244        0      2409      3041         4    7600.0       2.0         43     500011      2021 2021-03-26 Počet obydlených domů Bytové domy       2.0 Želechovice nad Dřevnicí      obec
1029651080        0      2409      3041         4    7600.0       3.0         43     500011      2021 2021-03-26 Počet obydlených domů Bytové domy       3.0 Želechovice nad Dřevnicí      obec
1029483725        2      2409      3041         4    7600.0       4.0         43     500011      2021 2021-03-26 Počet obydlených domů Bytové domy       4.0 Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  byty_cis  byty_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                                       druh_txt  byty_txt uzemi_txt uzemi_typ
1029622086       80      2409      3240        55    7600.0       4.0        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)         4     Praha     okres
1029566107      126      2409      3240        55    7601.0   50009.0        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)       5-9     Praha     okres
1029454418       46      2409      3240        55    7601.0  100019.0        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)     10-19     Praha     okres
1029231213       33      2409      3240        55    7601.0  200049.0        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)     20-49     Praha     okres
1029510405        6      2409      3240        55    7601.0  509999.0        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů) 50 a více     Praha     okres
```

### 046. [C] Sčítání 2021 - Obydlené domy podle počtu nadzemních podlaží a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  podlazi_cis  podlazi_kod  druh_cis  druh_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt  podlazi_txt                                       druh_txt                uzemi_txt uzemi_typ
1054075472      157      2409         7600            1       NaN       NaN         43     500011      2021 2021-03-26 Počet obydlených domů            1                                            NaN Želechovice nad Dřevnicí      obec
1054127702        0      2409         7600            1    3041.0       4.0         43     500011      2021 2021-03-26 Počet obydlených domů            1                                    Bytové domy Želechovice nad Dřevnicí      obec
1054057891      156      2409         7600            1    3240.0      51.0         43     500011      2021 2021-03-26 Počet obydlených domů            1                                   Rodinné domy Želechovice nad Dřevnicí      obec
1054127703        1      2409         7600            1    3240.0      55.0         43     500011      2021 2021-03-26 Počet obydlených domů            1 Ostatní budovy (bez rodinných a bytových domů) Želechovice nad Dřevnicí      obec
1054075355      323      2409         7600            2       NaN       NaN         43     500011      2021 2021-03-26 Počet obydlených domů            2                                            NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  podlazi_cis  podlazi_kod  druh_cis  druh_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt podlazi_txt                                       druh_txt uzemi_txt uzemi_typ
1054190070       56      2409         7601        99999    3240.0      55.0        101      40924      2021 2021-03-26 Počet obydlených domů    9 a více Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
1054086160     2442      2409         5768            9       NaN       NaN        101      40924      2021 2021-03-26 Počet obydlených domů  Nezjištěno                                            NaN     Praha     okres
1054085477       91      2409         5768            9    3041.0       4.0        101      40924      2021 2021-03-26 Počet obydlených domů  Nezjištěno                                    Bytové domy     Praha     okres
1054050734     1783      2409         5768            9    3240.0      51.0        101      40924      2021 2021-03-26 Počet obydlených domů  Nezjištěno                                   Rodinné domy     Praha     okres
1054189981      568      2409         5768            9    3240.0      55.0        101      40924      2021 2021-03-26 Počet obydlených domů  Nezjištěno Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
```

### 047. [C] Sčítání 2021 - Obydlené domy podle vlastnictví a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  vlastnik_cis  vlastnik_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt  druh_txt                               vlastnik_txt                uzemi_txt uzemi_typ
1034547151      505      2409       NaN       NaN          3049             1         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                              Fyzická osoba Želechovice nad Dřevnicí      obec
1033847536        1      2409       NaN       NaN          3049            10         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                            Bytové družstvo Želechovice nad Dřevnicí      obec
1034896246       13      2409       NaN       NaN          3049            11         43     500011      2021 2021-03-26 Počet obydlených domů       NaN Spoluvlastnictví vlastníků bytů (jednotek) Želechovice nad Dřevnicí      obec
1033497194        3      2409       NaN       NaN          3049             2         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                                 Obec, stát Želechovice nad Dřevnicí      obec
1034197187        3      2409       NaN       NaN          3049             6         43     500011      2021 2021-03-26 Počet obydlených domů       NaN                       Jiná právnická osoba Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  vlastnik_cis  vlastnik_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                                       druh_txt                               vlastnik_txt uzemi_txt uzemi_typ
1034848427       58      2409    3240.0      55.0          3049            11        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů) Spoluvlastnictví vlastníků bytů (jednotek)     Praha     okres
1034150029      369      2409    3240.0      55.0          3049             2        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                                 Obec, stát     Praha     okres
1034500223     1326      2409    3240.0      55.0          3049             6        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                       Jiná právnická osoba     Praha     okres
1035898604       34      2409    3240.0      55.0          3049             7        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                        Kombinace vlastníků     Praha     okres
1035198965       40      2409    3240.0      55.0          3049             9        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)                                 Nezjištěno     Praha     okres
```

### 048. [C] Sčítání 2021 - Obydlené domy podle vybavení výtahem a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  vytah_cis  vytah_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt    druh_txt  vytah_txt                uzemi_txt uzemi_typ
1048066184        0      2409       NaN       NaN       3206          1         43     500011      2021 2021-03-26 Počet obydlených domů         NaN  s výtahem Želechovice nad Dřevnicí      obec
1048066183      527      2409       NaN       NaN       3206          2         43     500011      2021 2021-03-26 Počet obydlených domů         NaN bez výtahu Želechovice nad Dřevnicí      obec
1042784327        3      2409       NaN       NaN       5768          9         43     500011      2021 2021-03-26 Počet obydlených domů         NaN Nezjištěno Želechovice nad Dřevnicí      obec
1042967618        0      2409    3041.0       4.0       3206          1         43     500011      2021 2021-03-26 Počet obydlených domů Bytové domy  s výtahem Želechovice nad Dřevnicí      obec
1046741299       11      2409    3041.0       4.0       3206          2         43     500011      2021 2021-03-26 Počet obydlených domů Bytové domy bez výtahu Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  vytah_cis  vytah_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                                       druh_txt  vytah_txt uzemi_txt uzemi_typ
1048032195    60701      2409    3240.0      51.0       3206          2        101      40924      2021 2021-03-26 Počet obydlených domů                                   Rodinné domy bez výtahu     Praha     okres
1045013303      247      2409    3240.0      51.0       5768          9        101      40924      2021 2021-03-26 Počet obydlených domů                                   Rodinné domy Nezjištěno     Praha     okres
1044258091      441      2409    3240.0      55.0       3206          1        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)  s výtahem     Praha     okres
1047277860     2109      2409    3240.0      55.0       3206          2        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů) bez výtahu     Praha     okres
1048032196       90      2409    3240.0      55.0       5768          9        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů) Nezjištěno     Praha     okres
```

### 049. [C] Sčítání 2021 - Obydlené domy způsobu vytápění a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  vytapeni_cis  vytapeni_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt    druh_txt          vytapeni_txt                uzemi_txt uzemi_typ
1049501186      409      2409       NaN       NaN          3242            52         43     500011      2021 2021-03-26 Počet obydlených domů         NaN        Kotelna v domě Želechovice nad Dřevnicí      obec
1049416753      116      2409       NaN       NaN          3048             8         43     500011      2021 2021-03-26 Počet obydlených domů         NaN Bez ústředního topení Želechovice nad Dřevnicí      obec
1049416754        2      2409       NaN       NaN          3048             9         43     500011      2021 2021-03-26 Počet obydlených domů         NaN      Kotelna mimo dům Želechovice nad Dřevnicí      obec
1049416755        3      2409       NaN       NaN          3048            99         43     500011      2021 2021-03-26 Počet obydlených domů         NaN            Nezjištěno Želechovice nad Dřevnicí      obec
1049443022        9      2409    3041.0       4.0          3242            52         43     500011      2021 2021-03-26 Počet obydlených domů Bytové domy        Kotelna v domě Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  druh_cis  druh_kod  vytapeni_cis  vytapeni_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum              ukaz_txt                                       druh_txt          vytapeni_txt uzemi_txt uzemi_typ
1049455481      385      2409    3240.0      51.0          3048            99        101      40924      2021 2021-03-26 Počet obydlených domů                                   Rodinné domy            Nezjištěno     Praha     okres
1049400586     1484      2409    3240.0      55.0          3242            52        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)        Kotelna v domě     Praha     okres
1049400585      481      2409    3240.0      55.0          3048             8        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů) Bez ústředního topení     Praha     okres
1049469427      547      2409    3240.0      55.0          3048             9        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)      Kotelna mimo dům     Praha     okres
1049401035      128      2409    3240.0      55.0          3048            99        101      40924      2021 2021-03-26 Počet obydlených domů Ostatní budovy (bez rodinných a bytových domů)            Nezjištěno     Praha     okres
```

### 050. [C] Sčítání 2021 - Obyvatelstvo podle bydliště matky v době narození a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  bydl_narozeni_cis  bydl_narozeni_kod  bydl_cleneni_typ  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                     bydl_narozeni_txt bydl_cleneni_txt  pohlavi_txt                uzemi_txt
1009668978      872      3162               3239                  1                 1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem               V obci obvyklého pobytu         základní          NaN Želechovice nad Dřevnicí
1009668979      631      3162               3239                  2                 1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   V jiné obci okresu obvyklého pobytu         základní          NaN Želechovice nad Dřevnicí
1009651437       88      3162               3239                  3                 1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem V jiném okrese kraje obvyklého pobytu         základní          NaN Želechovice nad Dřevnicí
1009668977      130      3162               3334                 51                 1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                         V jiném kraji         základní          NaN Želechovice nad Dřevnicí
1009651436       50      3162               3239                  7                 1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                V ČR, místo nezjištěno         základní          NaN Želechovice nad Dřevnicí
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  bydl_narozeni_cis  bydl_narozeni_kod  bydl_cleneni_typ  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                                   bydl_narozeni_txt bydl_cleneni_txt pohlavi_txt uzemi_txt
1009771919    27164      3162                 86                804                 3        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                            Ukrajina             země         muž     Praha
1009831028    25856      3162                 86                804                 3        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                            Ukrajina             země        žena     Praha
1009771063     3030      3162                 86                826                 3          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Spojené království Velké Británie a Severního Irska             země         NaN     Praha
1009771920     2209      3162                 86                826                 3        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Spojené království Velké Británie a Severního Irska             země         muž     Praha
1009919531      821      3162                 86                826                 3        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Spojené království Velké Británie a Severního Irska             země        žena     Praha
```

### 051. [C] Sčítání 2021 - Obyvatelstvo podle bydliště rok před sčítáním a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  bydl_1rok_cis  bydl_1rok_kod  bydl_cleneni_typ  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                         bydl_1rok_txt bydl_cleneni_txt  pohlavi_txt                uzemi_txt
1010088181     1713      3162           3239              1                 1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem               V obci obvyklého pobytu         základní          NaN Želechovice nad Dřevnicí
1010043149       51      3162           3239              2                 1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   V jiné obci okresu obvyklého pobytu         základní          NaN Želechovice nad Dřevnicí
1010043150        7      3162           3239              3                 1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem V jiném okrese kraje obvyklého pobytu         základní          NaN Želechovice nad Dřevnicí
1010088182       15      3162           3334             51                 1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                         V jiném kraji         základní          NaN Želechovice nad Dřevnicí
1010043151        0      3162           3239              7                 1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                V ČR, místo nezjištěno         základní          NaN Želechovice nad Dřevnicí
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  bydl_1rok_cis  bydl_1rok_kod  bydl_cleneni_typ  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                                       bydl_1rok_txt bydl_cleneni_txt pohlavi_txt uzemi_txt
1010289441     1281      3162             86            804                 3        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                            Ukrajina             země         muž     Praha
1010141777     1083      3162             86            804                 3        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                            Ukrajina             země        žena     Praha
1010241910     1216      3162             86            826                 3          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Spojené království Velké Británie a Severního Irska             země         NaN     Praha
1010289442      572      3162             86            826                 3        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Spojené království Velké Británie a Severního Irska             země         muž     Praha
1010318874      644      3162             86            826                 3        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Spojené království Velké Británie a Severního Irska             země        žena     Praha
```

### 052. [C] Sčítání 2021 - Obyvatelstvo podle desetiletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vek_cis      vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt   vek_txt pohlavi_txt                uzemi_txt
947108883     1817      3162      NaN          NaN          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem       NaN         NaN Želechovice nad Dřevnicí
947084833      909      3162      NaN          NaN        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem       NaN         muž Želechovice nad Dřevnicí
947119976      908      3162      NaN          NaN        102.0          2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem       NaN        žena Želechovice nad Dřevnicí
964971449      162      3162   1035.0 1100000009.0          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 0 - 9 let         NaN Želechovice nad Dřevnicí
964954808       94      3162   1035.0 1100000009.0        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 0 - 9 let         muž Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vek_cis      vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt        vek_txt pohlavi_txt uzemi_txt
964702861     2612      3162   1035.0 1300900099.0        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    90 - 99 let         muž     Praha
964645732     6557      3162   1035.0 1300900099.0        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    90 - 99 let        žena     Praha
964631895      118      3162   1035.0 1201009999.0          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 100 a více let         NaN     Praha
964669271       22      3162   1035.0 1201009999.0        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 100 a více let         muž     Praha
964683740       96      3162   1035.0 1201009999.0        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 100 a více let        žena     Praha
```

### 053. [C] Sčítání 2021 - Obyvatelstvo podle druhu registrovaného pobytu a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  druh_regpobytu_cis  druh_regpobytu_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                         ukaz_txt                         druh_regpobytu_txt  pohlavi_txt                uzemi_txt uzemi_typ
1016844711     1794      3162                3260                  59          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obyklým pobytem                     Trvalý pobyt občana ČR          NaN Želechovice nad Dřevnicí      obec
1016862576       11      3162                3260                  60          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obyklým pobytem Trvalý pobyt cizince (bez rozlišení státu)          NaN Želechovice nad Dřevnicí      obec
1016844712        8      3162                3260                  61          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obyklým pobytem                   Dlouhodobý pobyt cizince          NaN Želechovice nad Dřevnicí      obec
1016844713        4      3162                5616                  88          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obyklým pobytem                  Bez registrovaného pobytu          NaN Želechovice nad Dřevnicí      obec
1016857945        0      3162                5768                   9          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obyklým pobytem                                 Nezjištěno          NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  druh_regpobytu_cis  druh_regpobytu_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                         ukaz_txt        druh_regpobytu_txt pohlavi_txt uzemi_txt uzemi_typ
1016848655     7252      3162                5616                  88        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obyklým pobytem Bez registrovaného pobytu         muž     Praha     okres
1016848656     6401      3162                5616                  88        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obyklým pobytem Bez registrovaného pobytu        žena     Praha     okres
1016852355      539      3162                5768                   9          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obyklým pobytem                Nezjištěno         NaN     Praha     okres
1016848657      276      3162                5768                   9        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obyklým pobytem                Nezjištěno         muž     Praha     okres
1016848658      263      3162                5768                   9        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obyklým pobytem                Nezjištěno        žena     Praha     okres
```

### 054. [C] Sčítání 2021 - Obyvatelstvo podle ekonomické aktivity a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  aktivita_struktura  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt ekonaktiv_txt pohlavi_txt                uzemi_txt uzemi_typ
1059667763      997      3162          3249            53                 1.0          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla         NaN Želechovice nad Dřevnicí      obec
1059748058      555      3162          3249            53                 1.0        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla         muž Želechovice nad Dřevnicí      obec
1059669618      442      3162          3249            53                 1.0        102.0          2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla        žena Želechovice nad Dřevnicí      obec
1059743292      973      3162          3249            51                 1.1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Zaměstnaní         NaN Želechovice nad Dřevnicí      obec
1059711624      542      3162          3249            51                 1.1        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Zaměstnaní         muž Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  aktivita_struktura  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                     ekonaktiv_txt pohlavi_txt uzemi_txt uzemi_typ
1059675493     2049      3162          3072             7                 2.5        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Ostatní s vlastním zdrojem obživy         muž     Praha     okres
1059675492     1684      3162          3072             7                 2.5        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Ostatní s vlastním zdrojem obživy        žena     Praha     okres
1059714550    22219      3162          3072            99                 3.0          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                        Nezjištěno         NaN     Praha     okres
1059753478    12557      3162          3072            99                 3.0        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                        Nezjištěno         muž     Praha     okres
1059636015     9662      3162          3072            99                 3.0        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                        Nezjištěno        žena     Praha     okres
```

### 055. [C] Sčítání 2021 - Obyvatelstvo podle ekonomické aktivity, desetiletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  aktivita_struktura  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt  aktivita_txt     vek_txt  pohlavi_txt                uzemi_txt uzemi_typ
1079815117        0      3162          3249            53                   1     1035 1100000009          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla   0 - 9 let          NaN Želechovice nad Dřevnicí      obec
1080061250       11      3162          3249            53                   1     1035 1300100019          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla 10 - 19 let          NaN Želechovice nad Dřevnicí      obec
1081030199      120      3162          3249            53                   1     1035 1300200029          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla 20 - 29 let          NaN Želechovice nad Dřevnicí      obec
1080804300      210      3162          3249            53                   1     1035 1300300039          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla 30 - 39 let          NaN Želechovice nad Dřevnicí      obec
1081030200      265      3162          3249            53                   1     1035 1300400049          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla 40 - 49 let          NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  aktivita_struktura  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt aktivita_txt        vek_txt pohlavi_txt uzemi_txt uzemi_typ
1080083573        8      3162          3072            99                   3     1035 1300900099        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno    90 - 99 let         muž     Praha     okres
1079872606        8      3162          3072            99                   3     1035 1300900099        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno    90 - 99 let        žena     Praha     okres
1080181127        2      3162          3072            99                   3     1035 1201009999          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 100 a více let         NaN     Praha     okres
1081301958        0      3162          3072            99                   3     1035 1201009999        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 100 a více let         muž     Praha     okres
1079872607        2      3162          3072            99                   3     1035 1201009999        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 100 a více let        žena     Praha     okres
```

### 056. [C] Sčítání 2021 - Obyvatelstvo podle ekonomické aktivity, základních věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  aktivita_struktura  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt  aktivita_txt     vek_txt pohlavi_txt                uzemi_txt uzemi_typ
1064711789        0      3162          3249            53                   1     1035 1100000014          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla  0 - 14 let         NaN Želechovice nad Dřevnicí      obec
1064699480        0      3162          3249            53                   1     1035 1100000014        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla  0 - 14 let         muž Želechovice nad Dřevnicí      obec
1064196364        0      3162          3249            53                   1     1035 1100000014        102.0          2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla  0 - 14 let        žena Želechovice nad Dřevnicí      obec
1064825248      941      3162          3249            53                   1     1035 1300150064          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla 15 - 64 let         NaN Želechovice nad Dřevnicí      obec
1064585697      519      3162          3249            53                   1     1035 1300150064        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla 15 - 64 let         muž Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  aktivita_struktura  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt aktivita_txt       vek_txt pohlavi_txt uzemi_txt uzemi_typ
1064788463    11927      3162          3072            99                   3     1035 1300150064        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno   15 - 64 let         muž     Praha     okres
1064124569     9155      3162          3072            99                   3     1035 1300150064        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno   15 - 64 let        žena     Praha     okres
1064800298      709      3162          3072            99                   3     1035 1200659999          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 65 a více let         NaN     Praha     okres
1064788464      434      3162          3072            99                   3     1035 1200659999        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 65 a více let         muž     Praha     okres
1064902353      275      3162          3072            99                   3     1035 1200659999        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 65 a více let        žena     Praha     okres
```

### 057. [C] Sčítání 2021 - Obyvatelstvo podle jednotek věku a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vek_cis      vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt vek_txt pohlavi_txt                uzemi_txt
947108883     1817      3162      NaN          NaN          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     NaN         NaN Želechovice nad Dřevnicí
947084833      909      3162      NaN          NaN        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     NaN         muž Želechovice nad Dřevnicí
947119976      908      3162      NaN          NaN        102.0          2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     NaN        žena Želechovice nad Dřevnicí
971997841       18      3162   1035.0 1000000000.0          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   0 let         NaN Želechovice nad Dřevnicí
971969567       11      3162   1035.0 1000000000.0        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   0 let         muž Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vek_cis      vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt        vek_txt pohlavi_txt uzemi_txt
964697887       15      3162   1035.0 1000990099.0        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         99 let         muž     Praha
964669617      101      3162   1035.0 1000990099.0        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         99 let        žena     Praha
964631895      118      3162   1035.0 1201009999.0          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 100 a více let         NaN     Praha
964669271       22      3162   1035.0 1201009999.0        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 100 a více let         muž     Praha
964683740       96      3162   1035.0 1201009999.0        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 100 a více let        žena     Praha
```

### 058. [C] Sčítání 2021 - Obyvatelstvo podle mateřského jazyka (1 mateřský jazyk)

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt       jazyk_txt                uzemi_txt
947108883     1817      3162        NaN        NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem             NaN Želechovice nad Dřevnicí
967371033     1662      3162     5750.0        1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český jazyk Želechovice nad Dřevnicí
967371034       16      3162     5750.0        2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slovenský jazyk Želechovice nad Dřevnicí
967415048        2      3162     5750.0        3.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem  Anglický jazyk Želechovice nad Dřevnicí
967371735        0      3162     5750.0        5.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Německý jazyk Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt      jazyk_txt uzemi_txt
967380094     3358      3162     5750.0       14.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Čínský jazyk     Praha
967393108      356      3162     5750.0       25.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Romský jazyk     Praha
967380086      139      3162     5750.0       26.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Moravský jazyk     Praha
967404966       23      3162     5750.0      301.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem  Slezský jazyk     Praha
967416708   100661      3162     5750.0       99.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Nezjištěno     Praha
```

### 059. [C] Sčítání 2021 - Obyvatelstvo podle mateřského jazyka (1 nebo 2 mateřské jazyky)

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt        jazyk_txt                uzemi_txt
947108883     1817      3162        NaN        NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem              NaN Želechovice nad Dřevnicí
968161229     1696      3162     3295.0      201.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český celkem Želechovice nad Dřevnicí
968169634       34      3162     3295.0      202.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slovenský celkem Želechovice nad Dřevnicí
968214176        0      3162     3295.0      203.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Romský celkem Želechovice nad Dřevnicí
968158867        0      3162     3295.0      204.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Polský celkem Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt         jazyk_txt uzemi_txt
968166894    43403      3162     3295.0      225.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Ukrajinský celkem     Praha
968164851    14674      3162     3295.0      226.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Vietnamský celkem     Praha
968197293      387      3162     3295.0      228.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Moravský celkem     Praha
968197931       73      3162     3295.0      229.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Slezský celkem     Praha
967416708   100661      3162     5750.0       99.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        Nezjištěno     Praha
```

### 060. [C] Sčítání 2021 - Obyvatelstvo podle místa registrovaného pobytu a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  misto_regpobytu_cis  misto_regpobytu_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                         ukaz_txt                    misto_regpobytu_txt  pohlavi_txt                uzemi_txt uzemi_typ
1016806271     1670      3162                 3320                    2          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obyklým pobytem                         Ve stejné obci          NaN Želechovice nad Dřevnicí      obec
1016806272      113      3162                 3320                    3          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obyklým pobytem            V jiné obci stejného okresu          NaN Želechovice nad Dřevnicí      obec
1016806273       18      3162                 3320                    4          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obyklým pobytem                   V jiném okrese kraje          NaN Želechovice nad Dřevnicí      obec
1016825361       12      3162                 3342                   50          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obyklým pobytem V jiném kraji oblasti a v jiné oblasti          NaN Želechovice nad Dřevnicí      obec
1016806274        4      3162                 5616                   88          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obyklým pobytem              Bez registrovaného pobytu          NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  misto_regpobytu_cis  misto_regpobytu_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                         ukaz_txt                    misto_regpobytu_txt pohlavi_txt uzemi_txt uzemi_typ
1016796045    55288      3162                 3342                   50        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obyklým pobytem V jiném kraji oblasti a v jiné oblasti         muž     Praha     okres
1016796046    51098      3162                 3342                   50        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obyklým pobytem V jiném kraji oblasti a v jiné oblasti        žena     Praha     okres
1016796640    13653      3162                 5616                   88          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obyklým pobytem              Bez registrovaného pobytu         NaN     Praha     okres
1016796049     7252      3162                 5616                   88        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obyklým pobytem              Bez registrovaného pobytu         muž     Praha     okres
1016818623     6401      3162                 5616                   88        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obyklým pobytem              Bez registrovaného pobytu        žena     Praha     okres
```

### 061. [C] Sčítání 2021 - Obyvatelstvo podle náboženské víry

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vira_cis  vira_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                      vira_txt                uzemi_txt
947108883     1817      3162       NaN       NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                           NaN Želechovice nad Dřevnicí
946276585      567      3162    3078.0       1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem           Bez náboženské víry Želechovice nad Dřevnicí
946276732        0      3162    3078.0       2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem             Apoštolská církev Želechovice nad Dřevnicí
946746866        1      3162    3078.0       3.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Bratrská jednota baptistů Želechovice nad Dřevnicí
946545251        0      3162    3078.0       4.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Církev adventistů sedmého dne Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vira_cis  vira_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                                      vira_txt uzemi_txt
946477264       23      3162    3078.0      75.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                 zoroastrismus     Praha
946746427       49      3162    3078.0      76.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                    druidismus     Praha
946276070       38      3162    3078.0      77.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                               rastafariánství     Praha
946275766     7630      3162    3078.0      78.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem věřící - hlásící se k církvi - název neuveden     Praha
946389512   368384      3162    3078.0      99.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                     Neuvedeno     Praha
```

### 062. [C] Sčítání 2021 - Obyvatelstvo podle národnosti

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  narodnost_cis  narodnost_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt         narodnost_txt                uzemi_txt
947108883     1817      3162            NaN            NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                   NaN Želechovice nad Dřevnicí
959308279        0      3162         3267.0          201.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem      Afghánská celkem Želechovice nad Dřevnicí
959201672        0      3162         3267.0          202.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem       Albánská celkem Želechovice nad Dřevnicí
959307772        0      3162         3267.0          203.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Americká (USA) celkem Želechovice nad Dřevnicí
959455676        0      3162         3267.0          204.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem       Anglická celkem Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  narodnost_cis  narodnost_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt     narodnost_txt uzemi_txt
959315607        1      3162         3267.0          275.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Valonská celkem     Praha
959183234       21      3162         3267.0          276.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Velšská celkem     Praha
959250234    10185      3162         3267.0          277.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Vietnamská celkem     Praha
959183762        5      3162         3267.0          278.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Vlámská celkem     Praha
959051628     1299      3162         3267.0          279.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Židovská celkem     Praha
```

### 063. [C] Sčítání 2021 - Obyvatelstvo podle pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt pohlavi_txt                uzemi_txt
947108883     1817      3162          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         NaN Želechovice nad Dřevnicí
947084833      909      3162        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         muž Želechovice nad Dřevnicí
947119976      908      3162        102.0          2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena Želechovice nad Dřevnicí
947108884     1195      3162          NaN          NaN         43     500020      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         NaN        Petrov nad Desnou
947108254      592      3162        102.0          1.0         43     500020      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         muž        Petrov nad Desnou
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt pohlavi_txt     uzemi_txt
947104848   153118      3162        102.0          1.0        101      40916      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         muž Ostrava-město
947128355   160739      3162        102.0          2.0        101      40916      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena Ostrava-město
947093125  1301432      3162          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         NaN         Praha
947116836   633449      3162        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         muž         Praha
947140309   667983      3162        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena         Praha
```

### 064. [C] Sčítání 2021 - Obyvatelstvo podle pětiletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vek_cis      vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt    vek_txt pohlavi_txt                uzemi_txt
947108883     1817      3162      NaN          NaN          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        NaN         NaN Želechovice nad Dřevnicí
947084833      909      3162      NaN          NaN        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        NaN         muž Želechovice nad Dřevnicí
947119976      908      3162      NaN          NaN        102.0          2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        NaN        žena Želechovice nad Dřevnicí
964961283       93      3162   1035.0 1100000004.0          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 0 - 4 roky         NaN Želechovice nad Dřevnicí
964734134       60      3162   1035.0 1100000004.0        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 0 - 4 roky         muž Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vek_cis      vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt        vek_txt pohlavi_txt uzemi_txt
964612411      340      3162   1035.0 1300950099.0        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    95 - 99 let         muž     Praha
964683828     1251      3162   1035.0 1300950099.0        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    95 - 99 let        žena     Praha
964631895      118      3162   1035.0 1201009999.0          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 100 a více let         NaN     Praha
964669271       22      3162   1035.0 1201009999.0        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 100 a více let         muž     Praha
964683740       96      3162   1035.0 1201009999.0        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 100 a více let        žena     Praha
```

### 065. [C] Sčítání 2021 - Obyvatelstvo podle rodinného stavu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt            stav_txt                uzemi_txt
947108883     1817      3162       NaN       NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                 NaN Želechovice nad Dřevnicí
947122957      671      3162    5788.0       1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Svobodný/svobodná Želechovice nad Dřevnicí
947076021      823      3162    5788.0       2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        Ženatý/vdaná Želechovice nad Dřevnicí
947111359      171      3162    5788.0       3.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Rozvedený/rozvedená Želechovice nad Dřevnicí
947076022      142      3162    5788.0       4.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        Vdovec/vdova Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                                                   stav_txt uzemi_txt
947068838    70478      3162    5788.0       4.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                               Vdovec/vdova     Praha
947151849     1519      3162    5788.0       5.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                          Registrované partnerství trvající     Praha
947116619      351      3162    5788.0       7.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         Registrované partnerství zaniklé rozhodnutím soudu     Praha
947104901       44      3162    5788.0       8.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Registrované partnerství zaniklé úmrtím partnera/partnerky     Praha
947128453    14688      3162    5788.0      99.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                                 Nezjištěno     Praha
```

### 066. [C] Sčítání 2021 - Obyvatelstvo podle státního občanství

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  obcanstvi_cis  obcanstvi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                          obcanstvi_txt                uzemi_txt
947108883     1817      3162            NaN            NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                    NaN Želechovice nad Dřevnicí
957683227        7      3162         3181.0            5.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                        Dvojí občanství Želechovice nad Dřevnicí
955058555        0      3162         3228.0            4.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         Islámská republika Afghánistán Želechovice nad Dřevnicí
955057028        0      3162         3228.0            8.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                     Albánská republika Želechovice nad Dřevnicí
955422517        0      3162         3228.0           12.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Alžírská lidová demokratická republika Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  obcanstvi_cis  obcanstvi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt          obcanstvi_txt uzemi_txt
955569831        0      3162         3228.0          882.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezávislý stát Samoa     Praha
955023439       50      3162         3228.0          887.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Jemenská republika     Praha
955164914       25      3162         3228.0          894.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Zambijská republika     Praha
955871804       84      3162         3228.0          900.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem bez státního občanství     Praha
955871508    11395      3162         3228.0         9999.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem             Nezjištěno     Praha
```

### 067. [C] Sčítání 2021 - Obyvatelstvo podle vzdělání

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                                ukaz_txt                                                   vzdelani_txt                uzemi_txt
944997548     1577      3162           NaN           NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let                                                            NaN Želechovice nad Dřevnicí
945010849        9      3162        1294.0           1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let                                                   Bez vzdělání Želechovice nad Dřevnicí
944984326       59      3162        1294.0         900.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let                                                     Nezjištěno Želechovice nad Dřevnicí
944984325      489      3162        5181.0    35450001.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Úplné  střední (s maturitou), vč. nástavbového a pomaturitního Želechovice nad Dřevnicí
944984323      540      3162        5784.0         105.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let                             Střední vč. vyučení (bez maturity) Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                                ukaz_txt                                                   vzdelani_txt uzemi_txt
944985791   361420      3162        5181.0    35450001.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Úplné  střední (s maturitou), vč. nástavbového a pomaturitního     Praha
945031627   187884      3162        5784.0         105.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let                             Střední vč. vyučení (bez maturity)     Praha
945024983   371351      3162        5784.0         109.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let                                                  Vysokoškolské     Praha
944998234    85743      3162        5784.0         117.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let                                      Základní vč. neukončeného     Praha
945018230    24906      3162        5784.0         130.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let                                     Vyšší odborné, konzervatoř     Praha
```

### 068. [C] Sčítání 2021 - Obyvatelstvo podle vzdělání, základních věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                                ukaz_txt vzdelani_txt       vek_txt pohlavi_txt                uzemi_txt uzemi_typ
1065348324        6      3162          1294             1     1035 1300150064          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Bez vzdělání   15 - 64 let         NaN Želechovice nad Dřevnicí      obec
1065987611        4      3162          1294             1     1035 1300150064        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Bez vzdělání   15 - 64 let         muž Želechovice nad Dřevnicí      obec
1065439653        2      3162          1294             1     1035 1300150064        102.0          2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Bez vzdělání   15 - 64 let        žena Želechovice nad Dřevnicí      obec
1066034432        3      3162          1294             1     1035 1200659999          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Bez vzdělání 65 a více let         NaN Želechovice nad Dřevnicí      obec
1065233243        2      3162          1294             1     1035 1200659999        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Bez vzdělání 65 a více let         muž Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                                ukaz_txt vzdelani_txt       vek_txt pohlavi_txt uzemi_txt uzemi_typ
1065204964    34735      3162          1294           900     1035 1300150064        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let   Nezjištěno   15 - 64 let         muž     Praha     okres
1065623054    20965      3162          1294           900     1035 1300150064        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let   Nezjištěno   15 - 64 let        žena     Praha     okres
1065206631    11143      3162          1294           900     1035 1200659999          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let   Nezjištěno 65 a více let         NaN     Praha     okres
1065923183     4890      3162          1294           900     1035 1200659999        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let   Nezjištěno 65 a více let         muž     Praha     okres
1065500709     6253      3162          1294           900     1035 1200659999        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let   Nezjištěno 65 a více let        žena     Praha     okres
```

### 069. [C] Sčítání 2021 - Obyvatelstvo podle věkových skupin

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vek_cis      vek_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt       vek_txt                uzemi_txt
947108883     1817      3162      NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem           NaN Želechovice nad Dřevnicí
947149795      240      3162   1035.0 1100000014.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    0 - 14 let Želechovice nad Dřevnicí
947091150     1158      3162   1035.0 1300150064.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   15 - 64 let Želechovice nad Dřevnicí
947138048      419      3162   1035.0 1200659999.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 65 a více let Želechovice nad Dřevnicí
947108884     1195      3162      NaN          NaN         43     500020      2021 2021-03-26 Počet obyvatel s obvyklým pobytem           NaN        Petrov nad Desnou
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vek_cis      vek_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt       vek_txt     uzemi_txt
947081520    64689      3162   1035.0 1200659999.0        101      40916      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 65 a více let Ostrava-město
947093125  1301432      3162      NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem           NaN         Praha
947069184   199369      3162   1035.0 1100000014.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    0 - 14 let         Praha
947140509   863086      3162   1035.0 1300150064.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   15 - 64 let         Praha
947140508   238977      3162   1035.0 1200659999.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 65 a více let         Praha
```

### 070. [C] Sčítání 2021 - Obyvatelstvo podle způsobu bydlení a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  bydleni_cis  bydleni_kod  bydleni_cleneni  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                                                  bydleni_txt pohlavi_txt                uzemi_txt
989167155     1817      3162         3335           56                1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)         NaN Želechovice nad Dřevnicí
989187098      909      3162         3335           56                1        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)         muž Želechovice nad Dřevnicí
989169784      908      3162         3335           56                1        102.0          2.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)        žena Želechovice nad Dřevnicí
989148017        0      3162         3321            7                1          NaN          NaN         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                                   Bezdomovci         NaN Želechovice nad Dřevnicí
989247974        0      3162         3321            7                1        102.0          1.0         43     500011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                                   Bezdomovci         muž Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  bydleni_cis  bydleni_kod  bydleni_cleneni  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                        bydleni_txt pohlavi_txt uzemi_txt
989186465    13477      3162         3335           53                2        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v ubytovacím zařízení         muž     Praha
989134457    10147      3162         3335           53                2        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v ubytovacím zařízení        žena     Praha
989180744    15267      3162         3335           55                2          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Osoby žijící v jiných obydlích         NaN     Praha
989238751    10883      3162         3335           55                2        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Osoby žijící v jiných obydlích         muž     Praha
989151814     4384      3162         3335           55                2        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Osoby žijící v jiných obydlích        žena     Praha
```

### 071. [C] Sčítání 2021 - Plodnost žen

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  pocetdeti_cis  pocetdeti_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                        ukaz_txt  pocetdeti_txt                uzemi_txt
975026246      795      3162            NaN            NaN         43     500011      2021 2021-03-26 Počet žen ve věku 15 a více let            NaN Želechovice nad Dřevnicí
971890990      155      3162         7600.0            0.0         43     500011      2021 2021-03-26 Počet žen ve věku 15 a více let            0.0 Želechovice nad Dřevnicí
971890991      114      3162         7600.0            1.0         43     500011      2021 2021-03-26 Počet žen ve věku 15 a více let            1.0 Želechovice nad Dřevnicí
971890989      388      3162         7600.0            2.0         43     500011      2021 2021-03-26 Počet žen ve věku 15 a více let            2.0 Želechovice nad Dřevnicí
971893829      109      3162         7600.0            3.0         43     500011      2021 2021-03-26 Počet žen ve věku 15 a více let            3.0 Želechovice nad Dřevnicí
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  pocetdeti_cis  pocetdeti_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                        ukaz_txt pocetdeti_txt uzemi_txt
971889629   195387      3162         7600.0            2.0        101      40924      2021 2021-03-26 Počet žen ve věku 15 a více let             2     Praha
971916631    37675      3162         7600.0            3.0        101      40924      2021 2021-03-26 Počet žen ve věku 15 a více let             3     Praha
971889631     6117      3162         7600.0            4.0        101      40924      2021 2021-03-26 Počet žen ve věku 15 a více let             4     Praha
971910649     1869      3162         7601.0        59999.0        101      40924      2021 2021-03-26 Počet žen ve věku 15 a více let      5 a více     Praha
971898985    19219      3162         5768.0            9.0        101      40924      2021 2021-03-26 Počet žen ve věku 15 a více let    Nezjištěno     Praha
```

### 072. [C] Sčítání 2021 - Počet členů hospodařících domácností podle velikosti a typu domácnosti

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  clenu_cis  clenu_kod  typ_cis  typ_kod typ_struktura  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                           ukaz_txt  clenu_txt                                             typ_txt                uzemi_txt uzemi_typ
1061894925     1817      3337        NaN        NaN      NaN      NaN           NaN         43     500011      2021 2021-03-26 Počet členů hospodařící domácnosti        NaN                                                 NaN Želechovice nad Dřevnicí      obec
1062027264     1578      3337        NaN        NaN   3303.0     12.0             1         43     500011      2021 2021-03-26 Počet členů hospodařící domácnosti        NaN                                  Rodinné domácnosti Želechovice nad Dřevnicí      obec
1061861681     1457      3337        NaN        NaN   3303.0     13.0           1.1         43     500011      2021 2021-03-26 Počet členů hospodařící domácnosti        NaN                                Domácnost - 1 rodina Želechovice nad Dřevnicí      obec
1062471958     1272      3337        NaN        NaN   3303.0     14.0        1.1.1.         43     500011      2021 2021-03-26 Počet členů hospodařící domácnosti        NaN                          Domácnost - 1 úplná rodina Želechovice nad Dřevnicí      obec
1062463710     1052      3337        NaN        NaN   3303.0      4.0       1.1.1.1         43     500011      2021 2021-03-26 Počet členů hospodařící domácnosti        NaN Domácnost - 1 rodina - úplná rodina - manželský pár Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  clenu_cis  clenu_kod  typ_cis  typ_kod typ_struktura  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                    ukaz_txt  clenu_txt                                               typ_txt uzemi_txt uzemi_typ
1062312664     2.42      2426        NaN        NaN   3303.0      9.0       1.1.2.2        101      40924      2021 2021-03-26 Průměrný počet členů hospodařící domácnosti        NaN Domácnost - 1 rodina - neúplná rodina - osamělá matka     Praha     okres
1062358964     5.19      2426        NaN        NaN   3303.0     10.0           1.2        101      40924      2021 2021-03-26 Průměrný počet členů hospodařící domácnosti        NaN                            Domácnost - 2 a více rodin     Praha     okres
1062316923     1.07      2426        NaN        NaN   3303.0     11.0             2        101      40924      2021 2021-03-26 Průměrný počet členů hospodařící domácnosti        NaN                                  Nerodinné domácnosti     Praha     okres
1062370130     1.00      2426        NaN        NaN   3301.0   1100.0           2.1        101      40924      2021 2021-03-26 Průměrný počet členů hospodařící domácnosti        NaN                                 Domácnost jednotlivce     Praha     okres
1062311053     2.13      2426        NaN        NaN   3303.0     20.0           2.2        101      40924      2021 2021-03-26 Průměrný počet členů hospodařící domácnosti        NaN                        Vícečlenná nerodinná domácnost     Praha     okres
```

### 073. [C] Sčítání 2021 - Průměrný věk obyvatel podle pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                     ukaz_txt pohlavi_txt                uzemi_txt
957097509     45.4      2407          NaN          NaN         43     500011      2021 2021-03-26 Průměrný věk obyvatel (roky)         NaN Želechovice nad Dřevnicí
957094144     43.4      2407        102.0          1.0         43     500011      2021 2021-03-26 Průměrný věk obyvatel (roky)         muž Želechovice nad Dřevnicí
957082718     47.4      2407        102.0          2.0         43     500011      2021 2021-03-26 Průměrný věk obyvatel (roky)        žena Želechovice nad Dřevnicí
957097510     44.7      2407          NaN          NaN         43     500020      2021 2021-03-26 Průměrný věk obyvatel (roky)         NaN        Petrov nad Desnou
957089067     43.7      2407        102.0          1.0         43     500020      2021 2021-03-26 Průměrný věk obyvatel (roky)         muž        Petrov nad Desnou
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                     ukaz_txt pohlavi_txt     uzemi_txt
957096497     41.3      2407        102.0          1.0        101      40916      2021 2021-03-26 Průměrný věk obyvatel (roky)         muž Ostrava-město
957088826     44.9      2407        102.0          2.0        101      40916      2021 2021-03-26 Průměrný věk obyvatel (roky)        žena Ostrava-město
957084460     41.4      2407          NaN          NaN        101      40924      2021 2021-03-26 Průměrný věk obyvatel (roky)         NaN         Praha
957092656     39.9      2407        102.0          1.0        101      40924      2021 2021-03-26 Průměrný věk obyvatel (roky)         muž         Praha
957090137     42.8      2407        102.0          2.0        101      40924      2021 2021-03-26 Průměrný věk obyvatel (roky)        žena         Praha
```

### 074. [C] Sčítání 2021 - Vyjíždějící do zaměstnání a školy podle frekvence vyjížďky

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  frekvence_cis  frekvence_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt                aktivita_txt                           frekvence_txt  pohlavi_txt                uzemi_txt uzemi_typ
1099813543      659      2623          3249            58         3073.0           20.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti                      5x týdně a častěji          NaN Želechovice nad Dřevnicí      obec
1100116197      101      2623          3249            58         3073.0           21.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti                           1x - 4x týdně          NaN Želechovice nad Dřevnicí      obec
1099987893        4      2623          3249            58         3073.0           22.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti       pravidelně, ale méně než 1x týdně          NaN Želechovice nad Dřevnicí      obec
1099726240       36      2623          3249            58         3073.0           23.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti                            nepravidelně          NaN Želechovice nad Dřevnicí      obec
1100116198        5      2623          3249            58         3073.0           24.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti z jiného místa než z obvyklého bydliště          NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  frekvence_cis  frekvence_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt                aktivita_txt                           frekvence_txt pohlavi_txt uzemi_txt uzemi_typ
1099793592     1575      2623          3249            58         3073.0           24.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti z jiného místa než z obvyklého bydliště        žena     Praha     okres
1099712229    95879      2623          3249            58         5768.0            9.0          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti                              Nezjištěno         NaN     Praha     okres
1099974688    50743      2623          3249            58         5768.0            9.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti                              Nezjištěno         muž     Praha     okres
1099793591    45136      2623          3249            58         5768.0            9.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti                              Nezjištěno        žena     Praha     okres
1099262547   660139      2623          3249            58            NaN            NaN          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti                                     NaN         NaN     Praha     okres
```

### 075. [C] Sčítání 2021 - Vyjíždějící do zaměstnání a školy podle hlavního dopravního prostředku

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  prostredek_cis  prostredek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt                aktivita_txt           prostredek_txt  pohlavi_txt                uzemi_txt uzemi_typ
1099335760      903      2623          3249            58             NaN             NaN          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti                      NaN          NaN Želechovice nad Dřevnicí      obec
1099718094      101      2623          3249            58          3090.0             1.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti      Autobus (kromě MHD)          NaN Želechovice nad Dřevnicí      obec
1099805321       44      2623          3249            58          3090.0             2.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti                     Vlak          NaN Želechovice nad Dřevnicí      obec
1099805320       78      2623          3249            58          3090.0             3.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti Městská hromadná doprava          NaN Želechovice nad Dřevnicí      obec
1099932766      409      2623          3249            58          3090.0             4.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Automobil - řidič          NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  prostredek_cis  prostredek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt                aktivita_txt      prostredek_txt pohlavi_txt uzemi_txt uzemi_typ
1099886703    32026      2623          3249            58          3090.0             9.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti Žádný (pouze pěšky)         muž     Praha     okres
1099712071    38340      2623          3249            58          3090.0             9.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti Žádný (pouze pěšky)        žena     Praha     okres
1099974769    95167      2623          3249            58          3090.0           999.0          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti          Nezjištěno         NaN     Praha     okres
1099537865    50366      2623          3249            58          3090.0           999.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti          Nezjištěno         muž     Praha     okres
1099537776    44801      2623          3249            58          3090.0           999.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti          Nezjištěno        žena     Praha     okres
```

### 076. [C] Sčítání 2021 - Vyjíždějící do zaměstnání podle frekvence vyjížďky

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  frekvence_cis  frekvence_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt aktivita_txt                           frekvence_txt  pohlavi_txt                uzemi_txt uzemi_typ
1100095272      542      2623          3249            51         3073.0           20.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní                      5x týdně a častěji          NaN Želechovice nad Dřevnicí      obec
1099658728       82      2623          3249            51         3073.0           21.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní                           1x - 4x týdně          NaN Želechovice nad Dřevnicí      obec
1099658627        3      2623          3249            51         3073.0           22.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní       pravidelně, ale méně než 1x týdně          NaN Želechovice nad Dřevnicí      obec
1099858559       31      2623          3249            51         3073.0           23.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní                            nepravidelně          NaN Želechovice nad Dřevnicí      obec
1099858560        4      2623          3249            51         3073.0           24.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní z jiného místa než z obvyklého bydliště          NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  frekvence_cis  frekvence_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt aktivita_txt                           frekvence_txt pohlavi_txt uzemi_txt uzemi_typ
1099969893      837      2623          3249            51         3073.0           24.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní z jiného místa než z obvyklého bydliště        žena     Praha     okres
1100058237    41030      2623          3249            51         5768.0            9.0          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní                              Nezjištěno         NaN     Praha     okres
1099823937    23036      2623          3249            51         5768.0            9.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní                              Nezjištěno         muž     Praha     okres
1100057309    17994      2623          3249            51         5768.0            9.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní                              Nezjištěno        žena     Praha     okres
1099039447   496421      2623          3249            51            NaN            NaN          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní                                     NaN         NaN     Praha     okres
```

### 077. [C] Sčítání 2021 - Vyjíždějící do zaměstnání podle hlavního dopravního prostředku

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  prostredek_cis  prostredek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt aktivita_txt           prostredek_txt  pohlavi_txt                uzemi_txt uzemi_typ
1098784826      699      2623          3249            51             NaN             NaN          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní                      NaN          NaN Želechovice nad Dřevnicí      obec
1099850415       53      2623          3249            51          3090.0             1.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní      Autobus (kromě MHD)          NaN Želechovice nad Dřevnicí      obec
1099850307       24      2623          3249            51          3090.0             2.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní                     Vlak          NaN Želechovice nad Dřevnicí      obec
1099756573       51      2623          3249            51          3090.0             3.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní Městská hromadná doprava          NaN Želechovice nad Dřevnicí      obec
1099756574      408      2623          3249            51          3090.0             4.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Automobil - řidič          NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  prostredek_cis  prostredek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt aktivita_txt      prostredek_txt pohlavi_txt uzemi_txt uzemi_typ
1099621415    13640      2623          3249            51          3090.0             9.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní Žádný (pouze pěšky)         muž     Praha     okres
1099534270    20871      2623          3249            51          3090.0             9.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní Žádný (pouze pěšky)        žena     Praha     okres
1099706289    40515      2623          3249            51          3090.0           999.0          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní          Nezjištěno         NaN     Praha     okres
1100145560    22746      2623          3249            51          3090.0           999.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní          Nezjištěno         muž     Praha     okres
1099824415    17769      2623          3249            51          3090.0           999.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní          Nezjištěno        žena     Praha     okres
```

### 078. [C] Sčítání 2021 - Vyjíždějící do školy podle frekvence vyjížďky

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  frekvence_cis  frekvence_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt   aktivita_txt                           frekvence_txt  pohlavi_txt                uzemi_txt uzemi_typ
1099796904      117      2623          3072             8         3073.0           20.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti                      5x týdně a častěji          NaN Želechovice nad Dřevnicí      obec
1099924377       19      2623          3072             8         3073.0           21.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti                           1x - 4x týdně          NaN Želechovice nad Dřevnicí      obec
1099924378        1      2623          3072             8         3073.0           22.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti       pravidelně, ale méně než 1x týdně          NaN Želechovice nad Dřevnicí      obec
1099769128        5      2623          3072             8         3073.0           23.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti                            nepravidelně          NaN Želechovice nad Dřevnicí      obec
1099769127        1      2623          3072             8         3073.0           24.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti z jiného místa než z obvyklého bydliště          NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  frekvence_cis  frekvence_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt   aktivita_txt                           frekvence_txt pohlavi_txt uzemi_txt uzemi_typ
1099792523      738      2623          3072             8         3073.0           24.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti z jiného místa než z obvyklého bydliště        žena     Praha     okres
1100148543    54849      2623          3072             8         5768.0            9.0          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti                              Nezjištěno         NaN     Praha     okres
1100061143    27707      2623          3072             8         5768.0            9.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti                              Nezjištěno         muž     Praha     okres
1099792524    27142      2623          3072             8         5768.0            9.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti                              Nezjištěno        žena     Praha     okres
1098817712   163718      2623          3072             8            NaN            NaN          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti                                     NaN         NaN     Praha     okres
```

### 079. [C] Sčítání 2021 - Vyjíždějící do školy podle hlavního dopravního prostředku

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  prostredek_cis  prostredek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt   aktivita_txt           prostredek_txt  pohlavi_txt                uzemi_txt uzemi_typ
1098535036      204      2623          3072             8             NaN             NaN          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti                      NaN          NaN Želechovice nad Dřevnicí      obec
1100091199       48      2623          3072             8          3090.0             1.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti      Autobus (kromě MHD)          NaN Želechovice nad Dřevnicí      obec
1099654563       20      2623          3072             8          3090.0             2.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti                     Vlak          NaN Želechovice nad Dřevnicí      obec
1100016129       27      2623          3072             8          3090.0             3.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti Městská hromadná doprava          NaN Želechovice nad Dřevnicí      obec
1100016238        1      2623          3072             8          3090.0             4.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Automobil - řidič          NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  prostredek_cis  prostredek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt   aktivita_txt      prostredek_txt pohlavi_txt uzemi_txt uzemi_typ
1099791803    18386      2623          3072             8          3090.0             9.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti Žádný (pouze pěšky)         muž     Praha     okres
1100060239    17469      2623          3072             8          3090.0             9.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti Žádný (pouze pěšky)        žena     Praha     okres
1100147287    54652      2623          3072             8          3090.0           999.0          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti          Nezjištěno         NaN     Praha     okres
1099710890    27620      2623          3072             8          3090.0           999.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti          Nezjištěno         muž     Praha     okres
1099710818    27032      2623          3072             8          3090.0           999.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti          Nezjištěno        žena     Praha     okres
```

### 080. [C] Sčítání 2021 - Zaměstnaní podle hlavních tříd zaměstnání a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  klasif_cis  klasif_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt                       klasif_txt pohlavi_txt                uzemi_txt uzemi_typ
1060662276        1      3162        5705           0          NaN          NaN         43     500011      2021 2021-03-26 Zaměstnaní Zaměstnanci v ozbrojených silách         NaN Želechovice nad Dřevnicí      obec
1060551490        1      3162        5705           0        102.0          1.0         43     500011      2021 2021-03-26 Zaměstnaní Zaměstnanci v ozbrojených silách         muž Želechovice nad Dřevnicí      obec
1060580214        0      3162        5705           0        102.0          2.0         43     500011      2021 2021-03-26 Zaměstnaní Zaměstnanci v ozbrojených silách        žena Želechovice nad Dřevnicí      obec
1060690932       50      3162        5705           1          NaN          NaN         43     500011      2021 2021-03-26 Zaměstnaní  Zákonodárci a řídící pracovníci         NaN Želechovice nad Dřevnicí      obec
1060666332       35      3162        5705           1        102.0          1.0         43     500011      2021 2021-03-26 Zaměstnaní  Zákonodárci a řídící pracovníci         muž Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  klasif_cis  klasif_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt                           klasif_txt pohlavi_txt uzemi_txt uzemi_typ
1060712307     8851      3162        5705           9        102.0          1.0        101      40924      2021 2021-03-26 Zaměstnaní Pomocní a nekvalifikovaní pracovníci         muž     Praha     okres
1060539974    12006      3162        5705           9        102.0          2.0        101      40924      2021 2021-03-26 Zaměstnaní Pomocní a nekvalifikovaní pracovníci        žena     Praha     okres
1060567100    84280      3162        5705        9999          NaN          NaN        101      40924      2021 2021-03-26 Zaměstnaní                           nezjištěno         NaN     Praha     okres
1060740872    48152      3162        5705        9999        102.0          1.0        101      40924      2021 2021-03-26 Zaměstnaní                           nezjištěno         muž     Praha     okres
1060625969    36128      3162        5705        9999        102.0          2.0        101      40924      2021 2021-03-26 Zaměstnaní                           nezjištěno        žena     Praha     okres
```

### 081. [C] Sčítání 2021 - Zaměstnaní podle odvětví ekonomické činnosti a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  odvetvi_cis odvetvi_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt                       odvetvi_txt pohlavi_txt                uzemi_txt uzemi_typ
1060289087       35      3162         5103           A          NaN          NaN         43     500011      2021 2021-03-26 Zaměstnaní Zemědělství, lesnictví, rybářství         NaN Želechovice nad Dřevnicí      obec
1059840196       24      3162         5103           A        102.0          1.0         43     500011      2021 2021-03-26 Zaměstnaní Zemědělství, lesnictví, rybářství         muž Želechovice nad Dřevnicí      obec
1059930458       11      3162         5103           A        102.0          2.0         43     500011      2021 2021-03-26 Zaměstnaní Zemědělství, lesnictví, rybářství        žena Želechovice nad Dřevnicí      obec
1060236677        2      3162         5103           B          NaN          NaN         43     500011      2021 2021-03-26 Zaměstnaní                  Těžba a dobývání         NaN Želechovice nad Dřevnicí      obec
1060381104        2      3162         5103           B        102.0          1.0         43     500011      2021 2021-03-26 Zaměstnaní                  Těžba a dobývání         muž Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  odvetvi_cis odvetvi_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt                                   odvetvi_txt pohlavi_txt uzemi_txt uzemi_typ
1060117788      282      3162         5103           U        102.0          1.0        101      40924      2021 2021-03-26 Zaměstnaní Činnosti exteritoriálních organizací a orgánů         muž     Praha     okres
1059858596      373      3162         5103           U        102.0          2.0        101      40924      2021 2021-03-26 Zaměstnaní Činnosti exteritoriálních organizací a orgánů        žena     Praha     okres
1060452235     7866      3162         5103           X          NaN          NaN        101      40924      2021 2021-03-26 Zaměstnaní                                    Nezjištěno         NaN     Praha     okres
1060270911     4999      3162         5103           X        102.0          1.0        101      40924      2021 2021-03-26 Zaměstnaní                                    Nezjištěno         muž     Praha     okres
1060361779     2867      3162         5103           X        102.0          2.0        101      40924      2021 2021-03-26 Zaměstnaní                                    Nezjištěno        žena     Praha     okres
```

### 082. [C] Sčítání 2021 - Zaměstnaní podle postavení v zaměstnání a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  postaveni_cis  postaveni_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt  postaveni_txt pohlavi_txt                uzemi_txt uzemi_typ
1060504297      732      3162           5661              1          NaN          NaN         43     500011      2021 2021-03-26 Zaměstnaní    Zaměstnanci         NaN Želechovice nad Dřevnicí      obec
1059916947      372      3162           5661              1        102.0          1.0         43     500011      2021 2021-03-26 Zaměstnaní    Zaměstnanci         muž Želechovice nad Dřevnicí      obec
1060403404      360      3162           5661              1        102.0          2.0         43     500011      2021 2021-03-26 Zaměstnaní    Zaměstnanci        žena Želechovice nad Dřevnicí      obec
1060143758       21      3162           5661              2          NaN          NaN         43     500011      2021 2021-03-26 Zaměstnaní Zaměstnavatelé         NaN Želechovice nad Dřevnicí      obec
1060044764       17      3162           5661              2        102.0          1.0         43     500011      2021 2021-03-26 Zaměstnaní Zaměstnavatelé         muž Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  postaveni_cis  postaveni_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt                   postaveni_txt pohlavi_txt uzemi_txt uzemi_typ
1059912744    87149      3162           5661              3        102.0          1.0        101      40924      2021 2021-03-26 Zaměstnaní Osoby pracující na vlastní účet         muž     Praha     okres
1060273181    48769      3162           5661              3        102.0          2.0        101      40924      2021 2021-03-26 Zaměstnaní Osoby pracující na vlastní účet        žena     Praha     okres
1060363128    76612      3162           5661              9          NaN          NaN        101      40924      2021 2021-03-26 Zaměstnaní                      nezjištěno         NaN     Praha     okres
1059822038    42489      3162           5661              9        102.0          1.0        101      40924      2021 2021-03-26 Zaměstnaní                      nezjištěno         muž     Praha     okres
1060040045    34123      3162           5661              9        102.0          2.0        101      40924      2021 2021-03-26 Zaměstnaní                      nezjištěno        žena     Praha     okres
```

### 083. [C] Sčítání 2021 - Vyjíždějící do zaměstnání a školy podle kraje místa pracoviště/školy

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  kraj_dojizdky_cis  kraj_dojizdky_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt                aktivita_txt  kraj_dojizdky_txt pohlavi_txt                uzemi_txt uzemi_typ
1099335760      903      2623          3249            58                NaN                NaN          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti                NaN         NaN Želechovice nad Dřevnicí      obec
1099004757        9      2623          3249            58              100.0             3018.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti Hlavní město Praha         NaN Želechovice nad Dřevnicí      obec
1098777122        3      2623          3249            58              100.0             3018.0        102.0          1.0         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti Hlavní město Praha         muž Želechovice nad Dřevnicí      obec
1098778331        6      2623          3249            58              100.0             3018.0        102.0          2.0         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti Hlavní město Praha        žena Želechovice nad Dřevnicí      obec
1098671307        2      2623          3249            58              100.0             3026.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti   Středočeský kraj         NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  kraj_dojizdky_cis  kraj_dojizdky_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt                aktivita_txt    kraj_dojizdky_txt pohlavi_txt uzemi_txt uzemi_typ
1099262081      218      2623          3249            58              100.0             3131.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti         Zlínský kraj         muž     Praha     okres
1098928464      129      2623          3249            58              100.0             3131.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti         Zlínský kraj        žena     Praha     okres
1099192550      348      2623          3249            58              100.0             3140.0          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti Moravskoslezský kraj         NaN     Praha     okres
1099191640      236      2623          3249            58              100.0             3140.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti Moravskoslezský kraj         muž     Praha     okres
1098928463      112      2623          3249            58              100.0             3140.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti Moravskoslezský kraj        žena     Praha     okres
```

### 084. [C] Sčítání 2021 - Vyjíždějící do zaměstnání podle kraje místa pracoviště

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  kraj_dojizdky_cis  kraj_dojizdky_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt aktivita_txt  kraj_dojizdky_txt pohlavi_txt                uzemi_txt uzemi_typ
1098784826      699      2623          3249            51                NaN                NaN          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní                NaN         NaN Želechovice nad Dřevnicí      obec
1099050715        8      2623          3249            51              100.0             3018.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní Hlavní město Praha         NaN Želechovice nad Dřevnicí      obec
1098846461        2      2623          3249            51              100.0             3018.0        102.0          1.0         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní Hlavní město Praha         muž Želechovice nad Dřevnicí      obec
1098624340        6      2623          3249            51              100.0             3018.0        102.0          2.0         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní Hlavní město Praha        žena Želechovice nad Dřevnicí      obec
1099273104        2      2623          3249            51              100.0             3026.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní   Středočeský kraj         NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  kraj_dojizdky_cis  kraj_dojizdky_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt aktivita_txt    kraj_dojizdky_txt pohlavi_txt uzemi_txt uzemi_typ
1098744278      129      2623          3249            51              100.0             3131.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní         Zlínský kraj         muž     Praha     okres
1099260840       52      2623          3249            51              100.0             3131.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní         Zlínský kraj        žena     Praha     okres
1098743662      286      2623          3249            51              100.0             3140.0          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní Moravskoslezský kraj         NaN     Praha     okres
1099261716      207      2623          3249            51              100.0             3140.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní Moravskoslezský kraj         muž     Praha     okres
1099180977       79      2623          3249            51              100.0             3140.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní Moravskoslezský kraj        žena     Praha     okres
```

### 085. [C] Sčítání 2021 - Vyjíždějící do školy podle kraje místa školy

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  kraj_dojizdky_cis  kraj_dojizdky_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt   aktivita_txt  kraj_dojizdky_txt pohlavi_txt                uzemi_txt uzemi_typ
1098535036      204      2623          3072             8                NaN                NaN          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti                NaN         NaN Želechovice nad Dřevnicí      obec
1098637799        1      2623          3072             8              100.0             3018.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti Hlavní město Praha         NaN Želechovice nad Dřevnicí      obec
1098649744        1      2623          3072             8              100.0             3018.0        102.0          1.0         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti Hlavní město Praha         muž Želechovice nad Dřevnicí      obec
1098739594        0      2623          3072             8              100.0             3018.0        102.0          2.0         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti Hlavní město Praha        žena Želechovice nad Dřevnicí      obec
1098538143        0      2623          3072             8              100.0             3026.0          NaN          NaN         43     500011      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti   Středočeský kraj         NaN Želechovice nad Dřevnicí      obec
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  kraj_dojizdky_cis  kraj_dojizdky_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                 ukaz_txt   aktivita_txt    kraj_dojizdky_txt pohlavi_txt uzemi_txt uzemi_typ
1098780654       89      2623          3072             8              100.0             3131.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti         Zlínský kraj         muž     Praha     okres
1098929034       77      2623          3072             8              100.0             3131.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti         Zlínský kraj        žena     Praha     okres
1099181761       62      2623          3072             8              100.0             3140.0          NaN          NaN        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti Moravskoslezský kraj         NaN     Praha     okres
1098929035       29      2623          3072             8              100.0             3140.0        102.0          1.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti Moravskoslezský kraj         muž     Praha     okres
1098927823       33      2623          3072             8              100.0             3140.0        102.0          2.0        101      40924      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti Moravskoslezský kraj        žena     Praha     okres
```

## Kategorie D

### 086. [D] Sčítání 2021 - Dojížďka mezi obcemi, včetně denní dojížďky

                          hodnota
polozka                          
target_years_present         None
has_primary_key              True
primary_key_column    op_obec_kod

#### HEAD

```
    lokalizace op_lau1_kod op_okres  op_orp_kod op_orp  op_obec_kod op_obec doj_lau1_kod  doj_okres  doj_orp_kod   doj_orp  doj_obec_kod        doj_obec  dojizdka_prace  dojizdka_skola  dojizdka_celkova  dojizdka_celkova_denni
0_na_adrese_OP      CZ0100    PRAHA        1000  PRAHA       554782   PRAHA       CZ0100      PRAHA         1000     PRAHA        554782           PRAHA          141946              96            142042                       0
  1_meziobecni      CZ0100    PRAHA        1000  PRAHA       554782   PRAHA       CZ0641    BLANSKO         6202 BOSKOVICE        582018          LYSICE               0               1                 1                       0
  1_meziobecni      CZ0100    PRAHA        1000  PRAHA       554782   PRAHA       CZ0641    BLANSKO         6202 BOSKOVICE        582409           SUCHÝ               1               0                 1                       0
  1_meziobecni      CZ0100    PRAHA        1000  PRAHA       554782   PRAHA       CZ0641    BLANSKO         6202 BOSKOVICE        582646 VELKÉ OPATOVICE               1               0                 1                       0
  1_meziobecni      CZ0100    PRAHA        1000  PRAHA       554782   PRAHA       CZ0642 BRNO-MĚSTO         6203      BRNO        582786            BRNO             482             338               820                       0
```

#### TAIL

```
  lokalizace op_lau1_kod      op_okres  op_orp_kod  op_orp  op_obec_kod    op_obec doj_lau1_kod        doj_okres  doj_orp_kod          doj_orp  doj_obec_kod         doj_obec  dojizdka_prace  dojizdka_skola  dojizdka_celkova  dojizdka_celkova_denni
1_meziobecni      CZ0806 OSTRAVA-MĚSTO        8119 OSTRAVA       568449 ZBYSLAVICE       CZ0806    OSTRAVA-MĚSTO       8119.0          OSTRAVA        554821          OSTRAVA             159              38               197                     162
1_meziobecni      CZ0806 OSTRAVA-MĚSTO        8119 OSTRAVA       568449 ZBYSLAVICE       CZ0100            PRAHA       1000.0            PRAHA        554782            PRAHA               3               2                 5                       0
1_meziobecni      CZ0806 OSTRAVA-MĚSTO        8119 OSTRAVA       568449 ZBYSLAVICE       CZ0806    OSTRAVA-MĚSTO       8119.0          OSTRAVA        554049        OLBRAMICE               5               4                 9                       7
1_meziobecni      CZ0806 OSTRAVA-MĚSTO        8119 OSTRAVA       568449 ZBYSLAVICE       CZ0311 ČESKÉ BUDĚJOVICE       3102.0 ČESKÉ BUDĚJOVICE        544256 ČESKÉ BUDĚJOVICE               1               0                 1                       0
1_meziobecni      CZ0806 OSTRAVA-MĚSTO        8119 OSTRAVA       568449 ZBYSLAVICE       CZ0714           PŘEROV       7101.0          HRANICE        513750          HRANICE               1               0                 1                       1
```

## Kategorie C

### 087. [C] Obyvatelstvo podle jednotek věku a pohlaví ve správních obvodech obcí s rozšířenou působností - rok 2020

                         hodnota
polozka                         
target_years_present        None
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
    idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis         vek_kod  vuzemi_cis  vuzemi_kod  casref_do pohlavi_txt                                     vek_txt vuzemi_txt
879093847      135        2406          102            2     7700 410034610035000          65        3114 2020-12-31        žena 34 až 35 (více nebo rovno 34 a méně než 35)     Třeboň
879137782      216        2406          102            2     7700 410034610035000          65        8102 2020-12-31        žena 34 až 35 (více nebo rovno 34 a méně než 35)    Bohumín
879107785     1001        2406          102            2     7700 410034610035000          65        5105 2020-12-31        žena 34 až 35 (více nebo rovno 34 a méně než 35)    Liberec
879127177      190        2406          102            2     7700 410034610035000          65        6214 2020-12-31        žena 34 až 35 (více nebo rovno 34 a méně než 35)     Rosice
879105967       99        2406          102            2     7700 410034610035000          65        4215 2020-12-31        žena 34 až 35 (více nebo rovno 34 a méně než 35)  Varnsdorf
```

#### TAIL

```
    idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis         vek_kod  vuzemi_cis  vuzemi_kod  casref_do pohlavi_txt                                     vek_txt    vuzemi_txt
879105186      109        2406          102            1     7700 410077610078000          65        4212 2020-12-31         muž 77 až 78 (více nebo rovno 77 a méně než 78)       Rumburk
879100641       43        2406          102            1     7700 410077610078000          65        4104 2020-12-31         muž 77 až 78 (více nebo rovno 77 a méně než 78)      Kraslice
879141546      107        2406          102            1     7700 410077610078000          65        8114 2020-12-31         muž 77 až 78 (více nebo rovno 77 a méně než 78)         Krnov
879114276       67        2406          102            1     7700 410077610078000          65        5301 2020-12-31         muž 77 až 78 (více nebo rovno 77 a méně než 78) Česká Třebová
879081855     4687        2406          102            1     7700 410077610078000          65        1000 2020-12-31         muž 77 až 78 (více nebo rovno 77 a méně než 78)         Praha
```

### 088. [C] Obyvatelstvo podle jednotek věku a pohlaví ve správních obvodech obcí s rozšířenou působností - rok 2021

                         hodnota
polozka                         
target_years_present        None
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
    idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis         vek_kod  vuzemi_cis  vuzemi_kod  casref_do pohlavi_txt                                     vek_txt vuzemi_txt
975483566      125        2406          102            2     7700 410034610035000          65        3114 2021-12-31        žena 34 až 35 (více nebo rovno 34 a méně než 35)     Třeboň
975535800      209        2406          102            2     7700 410034610035000          65        8102 2021-12-31        žena 34 až 35 (více nebo rovno 34 a méně než 35)    Bohumín
975477457      948        2406          102            2     7700 410034610035000          65        5105 2021-12-31        žena 34 až 35 (více nebo rovno 34 a méně než 35)    Liberec
975518625      184        2406          102            2     7700 410034610035000          65        6214 2021-12-31        žena 34 až 35 (více nebo rovno 34 a méně než 35)     Rosice
975500537       95        2406          102            2     7700 410034610035000          65        4215 2021-12-31        žena 34 až 35 (více nebo rovno 34 a méně než 35)  Varnsdorf
```

#### TAIL

```
    idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis         vek_kod  vuzemi_cis  vuzemi_kod  casref_do pohlavi_txt                                     vek_txt    vuzemi_txt
975500433       90        2406          102            1     7700 410077610078000          65        4212 2021-12-31         muž 77 až 78 (více nebo rovno 77 a méně než 78)       Rumburk
975507520       39        2406          102            1     7700 410077610078000          65        4104 2021-12-31         muž 77 až 78 (více nebo rovno 77 a méně než 78)      Kraslice
975512707      152        2406          102            1     7700 410077610078000          65        8114 2021-12-31         muž 77 až 78 (více nebo rovno 77 a méně než 78)         Krnov
975532801       59        2406          102            1     7700 410077610078000          65        5301 2021-12-31         muž 77 až 78 (více nebo rovno 77 a méně než 78) Česká Třebová
975474191     4782        2406          102            1     7700 410077610078000          65        1000 2021-12-31         muž 77 až 78 (více nebo rovno 77 a méně než 78)         Praha
```

### 089. [C] Sčítání 2021 - Obyvatelstvo podle ekonomické aktivity, pětiletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  aktivita_struktura  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt  aktivita_txt    vek_txt pohlavi_txt uzemi_txt                                  uzemi_typ
1081591850        0      3162          3249            53                   1     1035 1100000004          NaN          NaN         65       1000      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla 0 - 4 roky         NaN     Praha správní obvod obce s rozšířenou působností
1079844191        0      3162          3249            53                   1     1035 1100000004        102.0          1.0         65       1000      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla 0 - 4 roky         muž     Praha správní obvod obce s rozšířenou působností
1081358900        0      3162          3249            53                   1     1035 1100000004        102.0          2.0         65       1000      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla 0 - 4 roky        žena     Praha správní obvod obce s rozšířenou působností
1080627018        0      3162          3249            53                   1     1035 1300050009          NaN          NaN         65       1000      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla  5 - 9 let         NaN     Praha správní obvod obce s rozšířenou působností
1080394665        0      3162          3249            53                   1     1035 1300050009        102.0          1.0         65       1000      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla  5 - 9 let         muž     Praha správní obvod obce s rozšířenou působností
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  aktivita_struktura  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt aktivita_txt        vek_txt pohlavi_txt uzemi_txt uzemi_typ
1081304293        2      3162          3072            99                   3     1035 1300950099        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno    95 - 99 let         muž     Praha     okres
1081304294        3      3162          3072            99                   3     1035 1300950099        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno    95 - 99 let        žena     Praha     okres
1080181127        2      3162          3072            99                   3     1035 1201009999          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 100 a více let         NaN     Praha     okres
1081301958        0      3162          3072            99                   3     1035 1201009999        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 100 a více let         muž     Praha     okres
1079872607        2      3162          3072            99                   3     1035 1201009999        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 100 a více let        žena     Praha     okres
```

### 090. [C] Sčítání 2021 - Zaměstnaní podle odvětví ekonomické činnosti, desetiletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  odvetvi_cis odvetvi_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum           ukaz_txt                       odvetvi_txt       vek_txt pohlavi_txt uzemi_txt                                  uzemi_typ
1093928886     5098      3162         5103           A     1035 1200159999          NaN          NaN         65       1000      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství 15 a více let         NaN     Praha správní obvod obce s rozšířenou působností
1094378013     3482      3162         5103           A     1035 1200159999        102.0          1.0         65       1000      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství 15 a více let         muž     Praha správní obvod obce s rozšířenou působností
1093972562     1616      3162         5103           A     1035 1200159999        102.0          2.0         65       1000      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství 15 a více let        žena     Praha správní obvod obce s rozšířenou působností
1094324702       70      3162         5103           A     1035 1300100019          NaN          NaN         65       1000      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství   10 - 19 let         NaN     Praha správní obvod obce s rozšířenou působností
1094474740       48      3162         5103           A     1035 1300100019        102.0          1.0         65       1000      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství   10 - 19 let         muž     Praha správní obvod obce s rozšířenou působností
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  odvetvi_cis odvetvi_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum           ukaz_txt odvetvi_txt        vek_txt pohlavi_txt uzemi_txt uzemi_typ
1093626009       12      3162         5103           X     1035 1300900099        102.0          1.0        101      40924      2021 2021-03-26 Počet zaměstnaných  Nezjištěno    90 - 99 let         muž     Praha     okres
1093863087        8      3162         5103           X     1035 1300900099        102.0          2.0        101      40924      2021 2021-03-26 Počet zaměstnaných  Nezjištěno    90 - 99 let        žena     Praha     okres
1094412302        0      3162         5103           X     1035 1201009999          NaN          NaN        101      40924      2021 2021-03-26 Počet zaměstnaných  Nezjištěno 100 a více let         NaN     Praha     okres
1094057968        0      3162         5103           X     1035 1201009999        102.0          1.0        101      40924      2021 2021-03-26 Počet zaměstnaných  Nezjištěno 100 a více let         muž     Praha     okres
1093768484        0      3162         5103           X     1035 1201009999        102.0          2.0        101      40924      2021 2021-03-26 Počet zaměstnaných  Nezjištěno 100 a více let        žena     Praha     okres
```

### 091. [C] Sčítání 2021 - Zaměstnaní podle odvětví ekonomické činnosti, pětiletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  odvetvi_cis odvetvi_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum           ukaz_txt                       odvetvi_txt       vek_txt pohlavi_txt uzemi_txt                                  uzemi_typ
1093928886     5098      3162         5103           A     1035 1200159999          NaN          NaN         65       1000      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství 15 a více let         NaN     Praha správní obvod obce s rozšířenou působností
1094378013     3482      3162         5103           A     1035 1200159999        102.0          1.0         65       1000      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství 15 a více let         muž     Praha správní obvod obce s rozšířenou působností
1093972562     1616      3162         5103           A     1035 1200159999        102.0          2.0         65       1000      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství 15 a více let        žena     Praha správní obvod obce s rozšířenou působností
1093870940       70      3162         5103           A     1035 1300150019          NaN          NaN         65       1000      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství   15 - 19 let         NaN     Praha správní obvod obce s rozšířenou působností
1094463156       48      3162         5103           A     1035 1300150019        102.0          1.0         65       1000      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství   15 - 19 let         muž     Praha správní obvod obce s rozšířenou působností
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  odvetvi_cis odvetvi_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum           ukaz_txt odvetvi_txt        vek_txt pohlavi_txt uzemi_txt uzemi_typ
1093814981        2      3162         5103           X     1035 1300950099        102.0          1.0        101      40924      2021 2021-03-26 Počet zaměstnaných  Nezjištěno    95 - 99 let         muž     Praha     okres
1094178535        2      3162         5103           X     1035 1300950099        102.0          2.0        101      40924      2021 2021-03-26 Počet zaměstnaných  Nezjištěno    95 - 99 let        žena     Praha     okres
1094412302        0      3162         5103           X     1035 1201009999          NaN          NaN        101      40924      2021 2021-03-26 Počet zaměstnaných  Nezjištěno 100 a více let         NaN     Praha     okres
1094057968        0      3162         5103           X     1035 1201009999        102.0          1.0        101      40924      2021 2021-03-26 Počet zaměstnaných  Nezjištěno 100 a více let         muž     Praha     okres
1093768484        0      3162         5103           X     1035 1201009999        102.0          2.0        101      40924      2021 2021-03-26 Počet zaměstnaných  Nezjištěno 100 a více let        žena     Praha     okres
```

## Kategorie A

### 092. [A] Zemřelí podle příčin smrti a pohlaví v ČR, krajích a okresech

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  ps_cis ps_kod  ps0_cis ps0_kod  vuzemi_cis  vuzemi_kod  rok pohlavi_txt                   ps_txt                                         ps0_txt      vuzemi_txt
1481729926        1        5393        102.0          1.0    5121    A01     5120       I          97          19 2024         muž Břišní tyfus a paratyfus Některé infekční a parazitární nemoci (A00–B99) Česká republika
1481726838        1        5393        102.0          1.0    5121    A01     5120       I         100        3093 2024         muž Břišní tyfus a paratyfus Některé infekční a parazitární nemoci (A00–B99) Pardubický kraj
1481751852        1        5393        102.0          1.0    5121    A01     5120       I         101       40622 2024         muž Břišní tyfus a paratyfus Některé infekční a parazitární nemoci (A00–B99)       Pardubice
1481723918        1        5393          NaN          NaN    5121    A01     5120       I          97          19 2024         NaN Břišní tyfus a paratyfus Některé infekční a parazitární nemoci (A00–B99) Česká republika
1481739990        1        5393          NaN          NaN    5121    A01     5120       I         100        3093 2024         NaN Břišní tyfus a paratyfus Některé infekční a parazitární nemoci (A00–B99) Pardubický kraj
```

#### TAIL

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  ps_cis  ps_kod  ps0_cis  ps0_kod  vuzemi_cis  vuzemi_kod  rok  pohlavi_txt  ps_txt  ps0_txt       vuzemi_txt
1347495990     2366        5393          NaN          NaN     NaN     NaN      NaN      NaN         101       40878 2023          NaN     NaN      NaN    Frýdek-Místek
1347462172     1183        5393          NaN          NaN     NaN     NaN      NaN      NaN         101       40223 2023          NaN     NaN      NaN   Mladá Boleslav
1347460897     1130        5393          NaN          NaN     NaN     NaN      NaN      NaN         101       40525 2023          NaN     NaN      NaN       Česká Lípa
1347436347     1227        5393          NaN          NaN     NaN     NaN      NaN      NaN         101       40690 2023          NaN     NaN      NaN Žďár nad Sázavou
1347486154      649        5393          NaN          NaN     NaN     NaN      NaN      NaN         101       40274 2023          NaN     NaN      NaN         Rakovník
```

## Kategorie B

### 093. [B] Volby do zastupitelstev obcí 2022 - registr kandidátů

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
 DATUMVOLEB  OKRES  KODZASTUP  COBVODU  POR_STR_HL  OSTRANA  PORCISLO    JMENO             PRIJMENI TITULPRED TITULZA  VEK      POVOLANI BYDLISTEN  PSTRANA  NSTRANA PLATNOST  POCHLASU PRESKOCENI  POCPROCVSE MANDAT  PORADIMAND  PORADINAHR
   20230107   7104     514802        1           1      901         1  Dalibor              Krbílek       NaN     NaN 60.0          OSVČ     Líšná     99.0     80.0        A        94          A       14.57      A           2           0
   20230107   7104     514802        1           1      901         2    Petra           Maksantová       Bc.     NaN 41.0            RD     Líšná     99.0     80.0        A        80          N       12.40      A           5           0
   20230107   7104     514802        1           1      901         3     Hana     Petrášová Mrvová Ing. Mgr.    DiS. 37.0   učitelka SŠ     Líšná     99.0     80.0        A        93          A       14.41      A           3           0
   20230107   7104     514802        1           1      901         4  Markéta Poláchová Kropáčková       Bc.    DiS. 52.0 ředitelka MAS     Líšná     99.0     80.0        A        96          A       14.88      A           1           0
   20230107   7104     514802        1           1      901         5 Ladislav               Tomčík       NaN     NaN 38.0          OSVČ     Líšná     99.0     80.0        A        83          N       12.86      A           6           0
```

#### TAIL

```
 DATUMVOLEB  OKRES  KODZASTUP  COBVODU  POR_STR_HL  OSTRANA  PORCISLO   JMENO   PRIJMENI TITULPRED  TITULZA  VEK                        POVOLANI       BYDLISTEN  PSTRANA  NSTRANA PLATNOST  POCHLASU PRESKOCENI  POCPROCVSE MANDAT  PORADIMAND  PORADINAHR
   20241207   3202     578321        1           1      901         2 Vendula   Faistová       NaN      NaN 50.0                            OSVČ Újezd u Plánice     99.0     80.0        A        44          A       19.13      A           4           0
   20241207   3202     578321        1           1      901         3  Libuše Fremundová       NaN      NaN 40.0 pracovník v sociálních službách Újezd u Plánice     99.0     80.0        A        45          A       19.56      A           3           0
   20241207   3202     578321        1           1      901         4  Helena  Bergerová      Mgr.      NaN 54.0                            OSVČ Újezd u Plánice     99.0     80.0        A        41          N       17.82      A           5           0
   20241207   3202     578321        1           1      901         5 Martina    Toušová       NaN      NaN 49.0             pojišťovací poradce Újezd u Plánice     99.0     80.0        A        46          A       20.00      A           1           0
   20241207   3202     578321        1           1      901         6   Jitka  Dvořáková      Ing.      NaN 34.0                          geodet Újezd u Plánice     99.0     80.0        A         9          N        3.91      N           0           1
```

### 094. [B] Volby do zastupitelstev obcí 2022 - registr kandidátů

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
 DATUMVOLEB  OKRES  KODZASTUP  COBVODU  POR_STR_HL  OSTRANA  PORCISLO    JMENO             PRIJMENI TITULPRED TITULZA  VEK      POVOLANI BYDLISTEN  PSTRANA  NSTRANA PLATNOST  POCHLASU PRESKOCENI  POCPROCVSE MANDAT  PORADIMAND  PORADINAHR
   20230107   7104     514802        1           1      901         1  Dalibor              Krbílek       NaN     NaN 60.0          OSVČ     Líšná     99.0     80.0        A        94          A       14.57      A           2           0
   20230107   7104     514802        1           1      901         2    Petra           Maksantová       Bc.     NaN 41.0            RD     Líšná     99.0     80.0        A        80          N       12.40      A           5           0
   20230107   7104     514802        1           1      901         3     Hana     Petrášová Mrvová Ing. Mgr.    DiS. 37.0   učitelka SŠ     Líšná     99.0     80.0        A        93          A       14.41      A           3           0
   20230107   7104     514802        1           1      901         4  Markéta Poláchová Kropáčková       Bc.    DiS. 52.0 ředitelka MAS     Líšná     99.0     80.0        A        96          A       14.88      A           1           0
   20230107   7104     514802        1           1      901         5 Ladislav               Tomčík       NaN     NaN 38.0          OSVČ     Líšná     99.0     80.0        A        83          N       12.86      A           6           0
```

#### TAIL

```
 DATUMVOLEB  OKRES  KODZASTUP  COBVODU  POR_STR_HL  OSTRANA  PORCISLO   JMENO   PRIJMENI TITULPRED  TITULZA  VEK                        POVOLANI       BYDLISTEN  PSTRANA  NSTRANA PLATNOST  POCHLASU PRESKOCENI  POCPROCVSE MANDAT  PORADIMAND  PORADINAHR
   20241207   3202     578321        1           1      901         2 Vendula   Faistová       NaN      NaN 50.0                            OSVČ Újezd u Plánice     99.0     80.0        A        44          A       19.13      A           4           0
   20241207   3202     578321        1           1      901         3  Libuše Fremundová       NaN      NaN 40.0 pracovník v sociálních službách Újezd u Plánice     99.0     80.0        A        45          A       19.56      A           3           0
   20241207   3202     578321        1           1      901         4  Helena  Bergerová      Mgr.      NaN 54.0                            OSVČ Újezd u Plánice     99.0     80.0        A        41          N       17.82      A           5           0
   20241207   3202     578321        1           1      901         5 Martina    Toušová       NaN      NaN 49.0             pojišťovací poradce Újezd u Plánice     99.0     80.0        A        46          A       20.00      A           1           0
   20241207   3202     578321        1           1      901         6   Jitka  Dvořáková      Ing.      NaN 34.0                          geodet Újezd u Plánice     99.0     80.0        A         9          N        3.91      N           0           1
```

### 095. [B] Volby do zastupitelstev obcí 2022 - registr volebních stran (ROS)

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
 DATUMVOLEB  OKRES  KODZASTUP NAZEVZAST  COBVODU  POR_STR_HL  OSTRANA  VSTRANA                NAZEVCELK               ZKRATKAO30 ZKRATKAO8  POCSTR_SLO  SLOZENI  HLASY_STR  PROCHLSTR  MAND_STR
   20230107   7104     514802     Líšná        1           1      901       90 Líšná spolu to zvládneme Líšná spolu to zvládneme       SNK           1       80      645.0     100.00       7.0
   20230107   2106     535397    Želízy        1           1      901       90          Za lepší Želízy          Za lepší Želízy       SNK           1       80      819.0      53.74       4.0
   20230107   2106     535397    Želízy        1           2      902       90         Želízy s rozumem         Želízy s rozumem       SNK           1       80      625.0      41.01       3.0
   20230107   2106     535397    Želízy        1           3      903       90           Ženy za Želízy           Ženy za Želízy       SNK           1       80       80.0      12.24       0.0
   20230107   2111     541451   Třebsko        1           1      807       80             Pavel Šedivý             Pavel Šedivý        NK           1       80       92.0      64.97       1.0
```

#### TAIL

```
 DATUMVOLEB  OKRES  KODZASTUP       NAZEVZAST  COBVODU  POR_STR_HL  OSTRANA  VSTRANA                      NAZEVCELK                     ZKRATKAO30 ZKRATKAO8  POCSTR_SLO  SLOZENI  HLASY_STR  PROCHLSTR  MAND_STR
   20241207   3107     563722     Černýšovice        1           3      801       80                Zdeněk Gottwald                Zdeněk Gottwald        NK           1       80       14.0      91.58       1.0
   20241207   3107     563722     Černýšovice        1           4      805       80                    Josef Karas                    Josef Karas        NK           1       80       21.0     137.38       1.0
   20241207   3107     563722     Černýšovice        1           5      804       80                   Josef Hruška                   Josef Hruška        NK           1       80       16.0     104.67       1.0
   20241207   3107     563722     Černýšovice        1           6      802       80                Zuzana Blažková                Zuzana Blažková        NK           1       80       17.0     111.21       1.0
   20241207   3202     578321 Újezd u Plánice        1           1      901       90 Sdružení nezávislých kandidátů Sdružení nezávislých kandidátů       SNK           1       80      230.0     100.00       5.0
```

### 096. [B] Volby do zastupitelstev obcí 2022 - registr volebních stran (ROS)

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
 DATUMVOLEB  OKRES  KODZASTUP NAZEVZAST  COBVODU  POR_STR_HL  OSTRANA  VSTRANA                NAZEVCELK               ZKRATKAO30 ZKRATKAO8  POCSTR_SLO  SLOZENI  HLASY_STR  PROCHLSTR  MAND_STR
   20230107   7104     514802     Líšná        1           1      901       90 Líšná spolu to zvládneme Líšná spolu to zvládneme       SNK           1       80      645.0     100.00       7.0
   20230107   2106     535397    Želízy        1           1      901       90          Za lepší Želízy          Za lepší Želízy       SNK           1       80      819.0      53.74       4.0
   20230107   2106     535397    Želízy        1           2      902       90         Želízy s rozumem         Želízy s rozumem       SNK           1       80      625.0      41.01       3.0
   20230107   2106     535397    Želízy        1           3      903       90           Ženy za Želízy           Ženy za Želízy       SNK           1       80       80.0      12.24       0.0
   20230107   2111     541451   Třebsko        1           1      807       80             Pavel Šedivý             Pavel Šedivý        NK           1       80       92.0      64.97       1.0
```

#### TAIL

```
 DATUMVOLEB  OKRES  KODZASTUP       NAZEVZAST  COBVODU  POR_STR_HL  OSTRANA  VSTRANA                      NAZEVCELK                     ZKRATKAO30 ZKRATKAO8  POCSTR_SLO  SLOZENI  HLASY_STR  PROCHLSTR  MAND_STR
   20241207   3107     563722     Černýšovice        1           3      801       80                Zdeněk Gottwald                Zdeněk Gottwald        NK           1       80       14.0      91.58       1.0
   20241207   3107     563722     Černýšovice        1           4      805       80                    Josef Karas                    Josef Karas        NK           1       80       21.0     137.38       1.0
   20241207   3107     563722     Černýšovice        1           5      804       80                   Josef Hruška                   Josef Hruška        NK           1       80       16.0     104.67       1.0
   20241207   3107     563722     Černýšovice        1           6      802       80                Zuzana Blažková                Zuzana Blažková        NK           1       80       17.0     111.21       1.0
   20241207   3202     578321 Újezd u Plánice        1           1      901       90 Sdružení nezávislých kandidátů Sdružení nezávislých kandidátů       SNK           1       80      230.0     100.00       5.0
```

### 097. [B] Volby do zastupitelstev obcí 2022 - registr volených zastupitelstev (RZCOCO)

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
 DATUMVOLEB  KRAJ  OKRES  TYPZASTUP  DRUHZASTUP  KODZASTUP NAZEVZAST   OBEC NAZEVOBCE  ORP  CPOU  REGURAD  OBVODY  COBVODU  MANDATY  POCOBYV  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  TYPDUVODU  POCET_VS  STAV_OBCE
   20230107  7100   7104          1           1     514802     Líšná 514802     Líšná 7109   851   511382       0        1        7      256           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          2         1          0
   20230107  2100   2106          1           1     535397    Želízy 535397    Želízy 2114   146   534676       0        1        7      522           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          1         3          0
   20230107  2100   2111          1           1     541451   Třebsko 541451   Třebsko 2120   197   539911       0        1        5      272           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          2         9          0
   20230107  3200   3204          1           1     546372    Buková 546372    Buková 3210   344   558249       0        1        7      237           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          2         2          0
   20230107  4200   4204          1           1     546895    Brodec 546895    Brodec 4207   441   565971       0        1        7       88           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          2         0          1
```

#### TAIL

```
 DATUMVOLEB  KRAJ  OKRES  TYPZASTUP  DRUHZASTUP  KODZASTUP       NAZEVZAST   OBEC       NAZEVOBCE  ORP  CPOU  REGURAD  OBVODY  COBVODU  MANDATY  POCOBYV  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  TYPDUVODU  POCET_VS  STAV_OBCE
   20241207  2100   2109          1           1     536130 Kostelní Hlavno 536130 Kostelní Hlavno 2103   175   538094       0        1        7      519           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          1         2          0
   20241207  4200   4204          1           1     546895          Brodec 546895          Brodec 4207   441   565971       0        1        7       85           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          2         0          1
   20241207  3100   3104          1           1     562254          Paseky 562254          Paseky 3108   259   549771       0        1        5      194           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          1         6          0
   20241207  3100   3107          1           1     563722     Černýšovice 563722     Černýšovice 3112   281   552054       0        1        7       85           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          1         6          0
   20241207  3200   3202          1           1     578321 Újezd u Plánice 578321 Újezd u Plánice 3205   325   556955       0        1        5      126           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          1         1          0
```

### 098. [B] Volby do zastupitelstev obcí 2022 - registr volených zastupitelstev (RZCOCO)

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
 DATUMVOLEB  KRAJ  OKRES  TYPZASTUP  DRUHZASTUP  KODZASTUP NAZEVZAST   OBEC NAZEVOBCE  ORP  CPOU  REGURAD  OBVODY  COBVODU  MANDATY  POCOBYV  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  TYPDUVODU  POCET_VS  STAV_OBCE
   20230107  7100   7104          1           1     514802     Líšná 514802     Líšná 7109   851   511382       0        1        7      256           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          2         1          0
   20230107  2100   2106          1           1     535397    Želízy 535397    Želízy 2114   146   534676       0        1        7      522           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          1         3          0
   20230107  2100   2111          1           1     541451   Třebsko 541451   Třebsko 2120   197   539911       0        1        5      272           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          2         9          0
   20230107  3200   3204          1           1     546372    Buková 546372    Buková 3210   344   558249       0        1        7      237           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          2         2          0
   20230107  4200   4204          1           1     546895    Brodec 546895    Brodec 4207   441   565971       0        1        7       88           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          2         0          1
```

#### TAIL

```
 DATUMVOLEB  KRAJ  OKRES  TYPZASTUP  DRUHZASTUP  KODZASTUP       NAZEVZAST   OBEC       NAZEVOBCE  ORP  CPOU  REGURAD  OBVODY  COBVODU  MANDATY  POCOBYV  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  TYPDUVODU  POCET_VS  STAV_OBCE
   20241207  2100   2109          1           1     536130 Kostelní Hlavno 536130 Kostelní Hlavno 2103   175   538094       0        1        7      519           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          1         2          0
   20241207  4200   4204          1           1     546895          Brodec 546895          Brodec 4207   441   565971       0        1        7       85           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          2         0          1
   20241207  3100   3104          1           1     562254          Paseky 562254          Paseky 3108   259   549771       0        1        5      194           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          1         6          0
   20241207  3100   3107          1           1     563722     Černýšovice 563722     Černýšovice 3112   281   552054       0        1        7       85           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          1         6          0
   20241207  3200   3202          1           1     578321 Újezd u Plánice 578321 Újezd u Plánice 3205   325   556955       0        1        5      126           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0          1         1          0
```

### 099. [B] Volby do zastupitelstev obcí 2022 - tiskopisy T3 za okrsky

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
 DATUMVOLEB  ID_OKRSKY  KRAJ  OKRES   OBEC  OKRSEK  TYPZASTUP  COBVODU  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  POCET_VS  POC_VS_HL  KODZASTUP
   20230107      33693  2100   2106 535397       1          1        1         413         248         248        1524         3          3     535397
   20230107      33694  2100   2107 571148       1          1        1         126          96          96         341         9          9     571148
   20230107      33695  2100   2111 541451       1          1        1         207         159         159         708         9          9     541451
   20230107      33696  3100   3104 549657       1          1        1         123          77          77         502         3          3     549657
   20230107      33697  3200   3204 546372       1          1        1         197         145         145         991         2          2     546372
```

#### TAIL

```
 DATUMVOLEB  ID_OKRSKY  KRAJ  OKRES   OBEC  OKRSEK  TYPZASTUP  COBVODU  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  POCET_VS  POC_VS_HL  KODZASTUP
   20241005      33794  8100   8105 553042       1          1        1         117          86          85         412         2          2     553042
   20241207      33795  2100   2109 536130       1          1        1         379         242         242        1572         2          2     536130
   20241207      33796  3100   3104 562254       1          1        1         143          87          87         326         6          6     562254
   20241207      33797  3100   3107 563722       1          1        1          73          31          31         107         6          6     563722
   20241207      33798  3200   3202 578321       1          1        1          97          61          61         230         1          1     578321
```

### 100. [B] Volby do zastupitelstev obcí 2022 - výsledky za okrsky

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
 DATUMVOLEB  ID_OKRSKY  KRAJ  OKRES   OBEC  OKRSEK  TYPZASTUP  POR_STR_HL  POC_HLASU  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  HLASY_23  HLASY_24  HLASY_25  HLASY_26  HLASY_27  HLASY_28  HLASY_29  HLASY_30  HLASY_31  HLASY_32  HLASY_33  HLASY_34  HLASY_35  HLASY_36  HLASY_37  HLASY_38  HLASY_39  HLASY_40  HLASY_41  HLASY_42  HLASY_43  HLASY_44  HLASY_45  HLASY_46  HLASY_47  HLASY_48  HLASY_49  HLASY_50  HLASY_51  HLASY_52  HLASY_53  HLASY_54  HLASY_55  HLASY_56  HLASY_57  HLASY_58  HLASY_59  HLASY_60  HLASY_61  HLASY_62  HLASY_63  HLASY_64  HLASY_65  HLASY_66  HLASY_67  HLASY_68  HLASY_69  HLASY_70
   20230107      33693  2100   2106 535397       1          1           1        819       110       129        72        69       119        85        94        62        79         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0
   20230107      33693  2100   2106 535397       1          1           2        625        92        71        92        68        55        90        77        60        20         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0
   20230107      33693  2100   2106 535397       1          1           3         80        31        35        14         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0
   20230107      33694  2100   2107 571148       1          1           1         68        68         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0
   20230107      33694  2100   2107 571148       1          1           2         37        37         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0
```

#### TAIL

```
 DATUMVOLEB  ID_OKRSKY  KRAJ  OKRES   OBEC  OKRSEK  TYPZASTUP  POR_STR_HL  POC_HLASU  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  HLASY_23  HLASY_24  HLASY_25  HLASY_26  HLASY_27  HLASY_28  HLASY_29  HLASY_30  HLASY_31  HLASY_32  HLASY_33  HLASY_34  HLASY_35  HLASY_36  HLASY_37  HLASY_38  HLASY_39  HLASY_40  HLASY_41  HLASY_42  HLASY_43  HLASY_44  HLASY_45  HLASY_46  HLASY_47  HLASY_48  HLASY_49  HLASY_50  HLASY_51  HLASY_52  HLASY_53  HLASY_54  HLASY_55  HLASY_56  HLASY_57  HLASY_58  HLASY_59  HLASY_60  HLASY_61  HLASY_62  HLASY_63  HLASY_64  HLASY_65  HLASY_66  HLASY_67  HLASY_68  HLASY_69  HLASY_70
   20241207      33797  3100   3107 563722       1          1           3         14        14         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0
   20241207      33797  3100   3107 563722       1          1           4         21        21         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0
   20241207      33797  3100   3107 563722       1          1           5         16        16         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0
   20241207      33797  3100   3107 563722       1          1           6         17        17         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0
   20241207      33798  3200   3202 578321       1          1           1        230        45        44        45        41        46         9         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0
```

## Kategorie C

### 101. [C] Sčítání 2021 - Byty podle obydlenosti a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  obydlenost_cis  obydlenost_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt obydlenost_txt                                   druhdomu_txt uzemi_txt uzemi_typ
1055289407      537      2607             NaN             NaN           NaN           NaN         42         19      2021 2021-03-26 Počet bytů            NaN                                            NaN  Abertamy část obce
1055535272      258      2607             NaN             NaN        3041.0           4.0         42         19      2021 2021-03-26 Počet bytů            NaN                                    Bytové domy  Abertamy část obce
1055395569      274      2607             NaN             NaN        3240.0          51.0         42         19      2021 2021-03-26 Počet bytů            NaN                                   Rodinné domy  Abertamy část obce
1054836674        5      2607             NaN             NaN        3240.0          55.0         42         19      2021 2021-03-26 Počet bytů            NaN Ostatní budovy (bez rodinných a bytových domů)  Abertamy část obce
1000356176      355      2607          3316.0             1.0           NaN           NaN         42         19      2021 2021-03-26 Počet bytů        Obydlen                                            NaN  Abertamy část obce
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  obydlenost_cis  obydlenost_kod  druhdomu_cis  druhdomu_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt obydlenost_txt                                   druhdomu_txt uzemi_txt uzemi_typ
1055189068     6601      2607             NaN             NaN        3240.0          55.0        101      40924      2021 2021-03-26 Počet bytů            NaN Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
 988450315   627705      2607          3316.0             1.0           NaN           NaN        101      40924      2021 2021-03-26 Počet bytů        Obydlen                                            NaN     Praha     okres
1055493492   542548      2607          3316.0             1.0        3041.0           4.0        101      40924      2021 2021-03-26 Počet bytů        Obydlen                                    Bytové domy     Praha     okres
1054815186    79161      2607          3316.0             1.0        3240.0          51.0        101      40924      2021 2021-03-26 Počet bytů        Obydlen                                   Rodinné domy     Praha     okres
1055068105     5996      2607          3316.0             1.0        3240.0          55.0        101      40924      2021 2021-03-26 Počet bytů        Obydlen Ostatní budovy (bez rodinných a bytových domů)     Praha     okres
```

### 102. [C] Sčítání 2021 - Obyvatelstvo s registrovaným pobytem podle pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                               ukaz_txt  pohlavi_txt      uzemi_txt uzemi_typ
1016738842      842      2406          NaN          NaN         42         19      2021 2021-03-26 Počet obyvatel s registrovaným pobytem          NaN       Abertamy část obce
1016795275       50      2406          NaN          NaN         42         27      2021 2021-03-26 Počet obyvatel s registrovaným pobytem          NaN       Hřebečná část obce
1016792454      984      2406          NaN          NaN         42         35      2021 2021-03-26 Počet obyvatel s registrovaným pobytem          NaN         Adamov část obce
1016741551      132      2406          NaN          NaN         42         51      2021 2021-03-26 Počet obyvatel s registrovaným pobytem          NaN Dolní Adršpach část obce
1016766939      353      2406          NaN          NaN         42         60      2021 2021-03-26 Počet obyvatel s registrovaným pobytem          NaN Horní Adršpach část obce
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                               ukaz_txt pohlavi_txt     uzemi_txt uzemi_typ
1016748668   152715      2406        102.0          1.0        101      40916      2021 2021-03-26 Počet obyvatel s registrovaným pobytem         muž Ostrava-město     okres
1016688005   160793      2406        102.0          2.0        101      40916      2021 2021-03-26 Počet obyvatel s registrovaným pobytem        žena Ostrava-město     okres
1016763061  1261304      2406          NaN          NaN        101      40924      2021 2021-03-26 Počet obyvatel s registrovaným pobytem         NaN         Praha     okres
1016762016   614531      2406        102.0          1.0        101      40924      2021 2021-03-26 Počet obyvatel s registrovaným pobytem         muž         Praha     okres
1016762015   646773      2406        102.0          2.0        101      40924      2021 2021-03-26 Počet obyvatel s registrovaným pobytem        žena         Praha     okres
```

## Kategorie D

### 103. [D] Volba prezidenta republiky 2023 - zápisy za všechny okrsky po 1. kole

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0   7204 500011       1     6     1         723         520         520         515  2279        34        37         0       165         2        75       175         8        19         0         0         0         0         0         0         0         0         0         0         0  2688  4967          9  509962
        1       0      0   7204 500011       2     0     1         417         295         295         292  1300        28        18         0        84         4        55        89         2        12         0         0         0         0         0         0         0         0         0         0         0  1497  2797          9  505617
        1       0      0   7204 500011       3     1     1         393         297         297         295  1283        25        12         0       115         2        40        88         3        10         0         0         0         0         0         0         0         0         0         0         0  1489  2772          9  505569
        1       0      0   7105 500020       1     2     1         262         151         151         151   716         7        12         0        32         0        29        68         0         3         0         0         0         0         0         0         0         0         0         0         0   836  1552          9  503137
        1       0      0   7105 500020       2     3     1         736         492         492         486  2207        32        18         0       120         4        89       199         8        16         0         0         0         0         0         0         0         0         0         0         0  2703  4910          9  509855
```

#### TAIL

```
 TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0   9999 999997     106     5     2          42          37          37          37   155         0         0         0        35         0         0         2         0         0         0         0         0         0         0         0         0         0         0         0         0   154   309          7 1000734
        1       0      0   9999 999997     107     6     2          32          18          18          18    88         0         0         0        15         0         0         3         0         0         0         0         0         0         0         0         0         0         0         0         0    81   169          7 1000456
        1       0      0   9999 999997     108     0     2           7           5           5           5    24         0         0         0         5         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    20    44          4 1000198
        1       0      0   9999 999997     109     1     2          88          46          46          46   228         0         0         0        41         0         0         5         0         0         0         0         0         0         0         0         0         0         0         0         0   199   427          7 1000969
        1       0      0   9999 999997     110     2     2         641         269         269         268  1449         0         0         0       239         0         0        29         0         0         0         0         0         0         0         0         0         0         0         0         0  1159  2608          7 1005333
```

### 104. [D] Volby do Evropského parlamentu 2024 - přílohy k zápisu s výsledky za okrsky

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  ESTRANA  POC_HLASU  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  HLASY_23  HLASY_24  HLASY_25  HLASY_26  HLASY_27  HLASY_28  KC_3  KC_4  POSL_KAND  KC_SUM
         1         2       0      0   7204 500011       1     6        1          1     2         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     2          0  507228
         1         2       0      0   7204 500011       1     6        3         26    29         4         5         7         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    35    64          3  507355
         1         2       0      0   7204 500011       1     6        4          1     5         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     5          0  507234
         1         2       0      0   7204 500011       1     6        6          3     9         1         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     3    12          2  507250
         1         2       0      0   7204 500011       1     6        9         26    35        15         1         0         2         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    25    60          4  507348
```

#### TAIL

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  ESTRANA  POC_HLASU  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  HLASY_23  HLASY_24  HLASY_25  HLASY_26  HLASY_27  HLASY_28  KC_3  KC_4  POSL_KAND  KC_SUM
     14714         2       0      0   8104 599999       2     0       23         45    68         2         4         2         4         1         1         1         0         2         0         0         5         0         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0   152   220         24  608571
     14714         2       0      0   8104 599999       2     0       24          1    25         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0    25          0  608157
     14714         2       0      0   8104 599999       2     0       26         52    78        21         4         0         0         0         1         0         1         1         0         0         0         0         0         0         0         0         0         0         0         4         0         0         0         0         0         0         0   136   214         21  608556
     14714         2       0      0   8104 599999       2     0       27          1    28         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0    28          0  608163
     14714         2       0      0   8104 599999       2     0       28          1    29         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0    29          0  608165
```

### 105. [D] Volby do Evropského parlamentu 2024 - zápisy s výsledky za okrsky

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KC_2                                                   ZAKRSTRANA  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK
         1         1       0      0   7204 500011       1     6  1552 101101001011111010111010011000000000000000000000000000000000         712         280         280         280
         2         1       0      0   7204 500011       2     0   905 011001001000011010111010011000000000000000000000000000000000         414         164         164         163
         3         1       0      0   7204 500011       3     1   877 101001001001011011111011010010000000000000000000000000000000         401         159         159         158
         4         1       0      0   7105 500020       1     2   499 001011001000010010111010010000000000000000000000000000000000         270          77          77          75
         5         1       0      0   7105 500020       2     3  1417 001011001001111110111110010000000000000000000000000000000000         739         228         228         222
```

#### TAIL

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KC_2                                                   ZAKRSTRANA  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK
     14710         1       0      0   8104 599948       4     6  1583 011011001011111010111010010001000000000000000000000000000000         708         292         292         291
     14711         1       0      0   8104 599956       1     1  3184 001111011111111111111011011000000000000000000000000000000000        1495         566         562         561
     14712         1       0      0   8104 599964       1     6  1675 111011001001111011111111011000000000000000000000000000000000         763         305         305         302
     14713         1       0      0   8104 599999       1     6  1042 001011001001110110111011011000000000000000000000000000000000         483         187         187         185
     14714         1       0      0   8104 599999       2     0  3451 011101011001011111111111011100000000000000000000000000000000        1601         618         618         614
```

### 106. [D] Volby do Evropského parlamentu 2024 - číselník obcí, městských částí, městských obvodů a volebních okrsků

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRAJ  OKRES  CPOU   OBEC  OBEC_PREZ                NAZEVOBCE  ORP  MINOKRSEK1  MAXOKRSEK1
 7200   7204   662 500011     500011 Želechovice nad Dřevnicí 7213           1           3
 7100   7105   860 500020     500020        Petrov nad Desnou 7111           1           2
 8100   8104   792 500046     500046                  Libhošť 8115           1           1
 1100   1100     1 500054     554782                  Praha 1 1000        1001        1021
 7200   7203   871 500062     500062                   Krhová 7210           1           1
```

#### TAIL

```
 KRAJ  OKRES  CPOU   OBEC  OBEC_PREZ         NAZEVOBCE  ORP  MINOKRSEK1  MAXOKRSEK1
 8100   8104   792 599930     599930 Suchdol nad Odrou 8115           1           2
 8100   8104   791 599948     599948         Štramberk 8112           1           4
 8100   8104   789 599956     599956             Tichá 8105           1           1
 8100   8104   788 599964     599964             Tísek 8101           1           1
 8100   8104   789 599999     599999       Trojanovice 8105           1           2
```

### 107. [D] Volby do Evropského parlamentu 2024 - číselník obcí, městských částí, městských obvodů a volebních okrsků

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRAJ  OKRES  CPOU   OBEC  OBEC_PREZ                NAZEVOBCE  ORP  MINOKRSEK1  MAXOKRSEK1
 7200   7204   662 500011     500011 Želechovice nad Dřevnicí 7213           1           3
 7100   7105   860 500020     500020        Petrov nad Desnou 7111           1           2
 8100   8104   792 500046     500046                  Libhošť 8115           1           1
 1100   1100     1 500054     554782                  Praha 1 1000        1001        1021
 7200   7203   871 500062     500062                   Krhová 7210           1           1
```

#### TAIL

```
 KRAJ  OKRES  CPOU   OBEC  OBEC_PREZ         NAZEVOBCE  ORP  MINOKRSEK1  MAXOKRSEK1
 8100   8104   792 599930     599930 Suchdol nad Odrou 8115           1           2
 8100   8104   791 599948     599948         Štramberk 8112           1           4
 8100   8104   789 599956     599956             Tichá 8105           1           1
 8100   8104   788 599964     599964             Tísek 8101           1           1
 8100   8104   789 599999     599999       Trojanovice 8105           1           2
```

### 108. [D] Volby do Evropského parlamentu 2024 - číselník okresů, krajů a regionů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NUMNUTS   NUTS          NAZEVNUTS  KODCIS CHODNOTA
       0     CZ    Česká republika     105       CZ
    1000   CZ01              Praha     107     CZ01
    1100  CZ010 Hlavní město Praha     108    CZ010
    1199 CZ0100              Praha     109   CZ0100
    2000   CZ02      Střední Čechy     107     CZ02
```

#### TAIL

```
 NUMNUTS   NUTS     NAZEVNUTS  KODCIS CHODNOTA
    8103 CZ0803       Karviná     109   CZ0803
    8104 CZ0804    Nový Jičín     109   CZ0804
    8105 CZ0805         Opava     109   CZ0805
    8106 CZ0806 Ostrava-město     109   CZ0806
    9999    NaN     Zahraničí     109   CZZZZZ
```

### 109. [D] Volby do Evropského parlamentu 2024 - číselník okresů, krajů a regionů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NUMNUTS   NUTS          NAZEVNUTS  KODCIS CHODNOTA
       0     CZ    Česká republika     105       CZ
    1000   CZ01              Praha     107     CZ01
    1100  CZ010 Hlavní město Praha     108    CZ010
    1199 CZ0100              Praha     109   CZ0100
    2000   CZ02      Střední Čechy     107     CZ02
```

#### TAIL

```
 NUMNUTS   NUTS     NAZEVNUTS  KODCIS CHODNOTA
    8103 CZ0803       Karviná     109   CZ0803
    8104 CZ0804    Nový Jičín     109   CZ0804
    8105 CZ0805         Opava     109   CZ0805
    8106 CZ0806 Ostrava-město     109   CZ0806
    9999    NaN     Zahraničí     109   CZZZZZ
```

### 110. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - číselník okresů, krajů a regionů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NUMNUTS   NUTS          NAZEVNUTS  KODCIS  CHODNOTA
       0    CZ0    Česká republika      97        19
    1000   CZ01              Praha      99       213
    1100  CZ010 Hlavní město Praha     100      3018
    1199 CZ0100              Praha     101     40924
    2000   CZ02      Střední Čechy      99       221
```

#### TAIL

```
 NUMNUTS   NUTS     NAZEVNUTS  KODCIS  CHODNOTA
    8103 CZ0803       Karviná     101     40886
    8104 CZ0804    Nový Jičín     101     40894
    8105 CZ0805         Opava     101     40908
    8106 CZ0806 Ostrava-město     101     40916
    9999 CZZZZZ     Zahraničí     101     40002
```

### 111. [D] Volby do Senátu Parlamentu ČR 2022 - číselník okresů, krajů a regionů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NUMNUTS   NUTS          NAZEVNUTS  KODCIS  CHODNOTA
       0     CZ    Česká republika      97        19
    1000   CZ01              Praha      99       213
    1100  CZ010 Hlavní město Praha     100      3018
    1199 CZ0100              Praha     101     40924
    2000   CZ02      Střední Čechy      99       221
```

#### TAIL

```
 NUMNUTS   NUTS     NAZEVNUTS  KODCIS  CHODNOTA
    8103 CZ0803       Karviná     101     40886
    8104 CZ0804    Nový Jičín     101     40894
    8105 CZ0805         Opava     101     40908
    8106 CZ0806 Ostrava-město     101     40916
    9999    NaN     Zahraničí     101     40002
```

### 112. [D] Volby do Senátu Parlamentu ČR 2022 - číselník okresů, krajů a regionů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NUMNUTS   NUTS          NAZEVNUTS  KODCIS  CHODNOTA
       0     CZ    Česká republika      97        19
    1000   CZ01              Praha      99       213
    1100  CZ010 Hlavní město Praha     100      3018
    1199 CZ0100              Praha     101     40924
    2000   CZ02      Střední Čechy      99       221
```

#### TAIL

```
 NUMNUTS   NUTS     NAZEVNUTS  KODCIS  CHODNOTA
    8103 CZ0803       Karviná     101     40886
    8104 CZ0804    Nový Jičín     101     40894
    8105 CZ0805         Opava     101     40908
    8106 CZ0806 Ostrava-město     101     40916
    9999    NaN     Zahraničí     101     40002
```

### 113. [D] Volby do Senátu Parlamentu ČR 2024 - číselník okresů, krajů a regionů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NUMNUTS   NUTS          NAZEVNUTS  KODCIS CHODNOTA
       0     CZ    Česká republika     105       CZ
    1000   CZ01              Praha     107     CZ01
    1100  CZ010 Hlavní město Praha     108    CZ010
    1199 CZ0100              Praha     109   CZ0100
    2000   CZ02      Střední Čechy     107     CZ02
```

#### TAIL

```
 NUMNUTS   NUTS     NAZEVNUTS  KODCIS CHODNOTA
    8103 CZ0803       Karviná     109   CZ0803
    8104 CZ0804    Nový Jičín     109   CZ0804
    8105 CZ0805         Opava     109   CZ0805
    8106 CZ0806 Ostrava-město     109   CZ0806
    9999    NaN     Zahraničí     109   CZZZZZ
```

### 114. [D] Volby do Senátu Parlamentu ČR 2024 - číselník okresů, krajů a regionů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NUMNUTS   NUTS          NAZEVNUTS  KODCIS CHODNOTA
       0     CZ    Česká republika     105       CZ
    1000   CZ01              Praha     107     CZ01
    1100  CZ010 Hlavní město Praha     108    CZ010
    1199 CZ0100              Praha     109   CZ0100
    2000   CZ02      Střední Čechy     107     CZ02
```

#### TAIL

```
 NUMNUTS   NUTS     NAZEVNUTS  KODCIS CHODNOTA
    8103 CZ0803       Karviná     109   CZ0803
    8104 CZ0804    Nový Jičín     109   CZ0804
    8105 CZ0805         Opava     109   CZ0805
    8106 CZ0806 Ostrava-město     109   CZ0806
    9999    NaN     Zahraničí     109   CZZZZZ
```

### 115. [D] Volby do zastupitelstev krajů 2024 - číselník okresů, krajů a regionů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NUMNUTS   NUTS          NAZEVNUTS  KODCIS CHODNOTA
       0     CZ    Česká republika     105       CZ
    1000   CZ01              Praha     107     CZ01
    1100  CZ010 Hlavní město Praha     108    CZ010
    1199 CZ0100              Praha     109   CZ0100
    2000   CZ02      Střední Čechy     107     CZ02
```

#### TAIL

```
 NUMNUTS   NUTS     NAZEVNUTS  KODCIS CHODNOTA
    8103 CZ0803       Karviná     109   CZ0803
    8104 CZ0804    Nový Jičín     109   CZ0804
    8105 CZ0805         Opava     109   CZ0805
    8106 CZ0806 Ostrava-město     109   CZ0806
    9999    NaN     Zahraničí     109   CZZZZZ
```

### 116. [D] Volby do zastupitelstev obcí 2022 - číselník okresů, krajů a regionů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NUMNUTS   NUTS          NAZEVNUTS  KODCIS  CHODNOTA
       0     CZ    Česká republika      97        19
    1000   CZ01              Praha      99       213
    1100  CZ010 Hlavní město Praha     100      3018
    1199 CZ0100              Praha     101     40924
    2000   CZ02      Střední Čechy      99       221
```

#### TAIL

```
 NUMNUTS   NUTS     NAZEVNUTS  KODCIS  CHODNOTA
    8103 CZ0803       Karviná     101     40886
    8104 CZ0804    Nový Jičín     101     40894
    8105 CZ0805         Opava     101     40908
    8106 CZ0806 Ostrava-město     101     40916
    9999    NaN     Zahraničí     101     40002
```

### 117. [D] Volby do zastupitelstev obcí 2022 - číselník okresů, krajů a regionů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NUMNUTS   NUTS          NAZEVNUTS  KODCIS  CHODNOTA
       0     CZ    Česká republika      97        19
    1000   CZ01              Praha      99       213
    1100  CZ010 Hlavní město Praha     100      3018
    1199 CZ0100              Praha     101     40924
    2000   CZ02      Střední Čechy      99       221
```

#### TAIL

```
 NUMNUTS   NUTS     NAZEVNUTS  KODCIS  CHODNOTA
    8103 CZ0803       Karviná     101     40886
    8104 CZ0804    Nový Jičín     101     40894
    8105 CZ0805         Opava     101     40908
    8106 CZ0806 Ostrava-město     101     40916
    9999    NaN     Zahraničí     101     40002
```

## Kategorie A

### 118. [A] Obyvatelstvo podle pohlaví a základních věkových skupin

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis      vek_kod  uzemi_cis  uzemi_kod     obdobi  pohlavi_txt  vek_txt          uzemi_txt uzemi_typ
1286408928  1384732        2406          NaN          NaN      NaN          NaN        100       3018 2023-12-31          NaN      NaN Hlavní město Praha      kraj
1446328288  1397880        2406          NaN          NaN      NaN          NaN        100       3018 2024-12-31          NaN      NaN Hlavní město Praha      kraj
1284353798   218647        2406          NaN          NaN   7700.0 4.000006e+14        100       3018 2023-12-31          NaN  0 až 14 Hlavní město Praha      kraj
1446176432   215285        2406          NaN          NaN   7700.0 4.000006e+14        100       3018 2024-12-31          NaN  0 až 14 Hlavní město Praha      kraj
1284201313   909437        2406          NaN          NaN   7700.0 4.100156e+14        100       3018 2023-12-31          NaN 15 až 64 Hlavní město Praha      kraj
```

#### TAIL

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis      vek_kod  uzemi_cis  uzemi_kod     obdobi pohlavi_txt   vek_txt       uzemi_txt uzemi_typ
1446113233   824554        2406        102.0          2.0   7700.0 4.000006e+14         97         19 2024-12-31        žena   0 až 14 Česká republika      stát
1284208372  3420347        2406        102.0          2.0   7700.0 4.100156e+14         97         19 2023-12-31        žena  15 až 64 Česká republika      stát
1446056827  3426641        2406        102.0          2.0   7700.0 4.100156e+14         97         19 2024-12-31        žena  15 až 64 Česká republika      stát
1284336948  1294312        2406        102.0          2.0   7700.0 4.100658e+14         97         19 2023-12-31        žena 65 a více Česká republika      stát
1446121230  1303726        2406        102.0          2.0   7700.0 4.100658e+14         97         19 2024-12-31        žena 65 a více Česká republika      stát
```

### 119. [A] Osevní plochy zemědělských plodin podle krajů

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  druhzplod_cis  druhzplod_kod  rok  uzemi_cis  uzemi_kod       uzemi_txt                  druhzplod_txt
1306615018   1890.0        5898      78   11104          208.0        20300.0 2023         97         19 Česká republika            Bob polní (na zrno)
1461161934   2135.0        5898      78   11104          208.0        20300.0 2024         97         19 Česká republika            Bob polní (na zrno)
1306614961  20947.0        5898      78   11104          209.0          306.0 2023         97         19 Česká republika                       Brambory
1461162245  22747.0        5898      78   11104          209.0          306.0 2024         97         19 Česká republika                       Brambory
1306613460  17334.0        5898      78   11104          209.0          301.0 2023         97         19 Česká republika Brambory (mimo rané a sadbové)
```

#### TAIL

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  druhzplod_cis  druhzplod_kod  rok  uzemi_cis  uzemi_kod            uzemi_txt druhzplod_txt
1306613672      NaN        5898      78   11104          208.0        60506.0 2024        100       3140 Moravskoslezský kraj        Špenát
1263383734    758.0        5898      78   11104          208.0        10200.0 2023        100       3140 Moravskoslezský kraj          Žito
1393172412    686.0        5898      78   11104          208.0        10200.0 2024        100       3140 Moravskoslezský kraj          Žito
1128582903 119438.0        5898      78   11104            NaN            NaN 2023        100       3140 Moravskoslezský kraj           NaN
1306613759 119336.0        5898      78   11104            NaN            NaN 2024        100       3140 Moravskoslezský kraj           NaN
```

### 120. [A] Stavební povolení

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota duvernost  stapro_kod  mj_cis  mj_kod  typstavby_cis  typstavby_kod  smer_cis  smer_kod  mesicod  mesicdo  rok  uzemi_cis  uzemi_kod       uzemi_txt                                    stapro_txt             mj_txt   typstavby_txt      smer_txt
1456743179  72066.0   verejny        3030      78   99998            NaN            NaN       NaN       NaN        1       12 2024         97         19 Česká republika Počet vydaných stavebních ohlášení a povolení četnostní jednotka             NaN           NaN
1456738537  11060.0   verejny        3030      78   99998         5632.0           11.0    2323.0      20.0        1       12 2024         97         19 Česká republika Počet vydaných stavebních ohlášení a povolení četnostní jednotka   Budovy bytové nová výstavba
1456736278   8263.0   verejny        3030      78   99998         5632.0           12.0    2323.0      20.0        1       12 2024         97         19 Česká republika Počet vydaných stavebních ohlášení a povolení četnostní jednotka Budovy nebytové nová výstavba
1456736275  42118.0   verejny        3030      78   99998         5631.0            1.0       NaN       NaN        1       12 2024         97         19 Česká republika Počet vydaných stavebních ohlášení a povolení četnostní jednotka          Budovy           NaN
1456741482  24260.0   verejny        3030      78   99998         5632.0           11.0       NaN       NaN        1       12 2024         97         19 Česká republika Počet vydaných stavebních ohlášení a povolení četnostní jednotka   Budovy bytové           NaN
```

#### TAIL

```
     idhod  hodnota duvernost  stapro_kod  mj_cis  mj_kod  typstavby_cis  typstavby_kod  smer_cis  smer_kod  mesicod  mesicdo  rok  uzemi_cis  uzemi_kod            uzemi_txt                                                      stapro_txt  mj_txt   typstavby_txt                                                         smer_txt
1456733739   8572.0   verejny        3037      78     206         5632.0           12.0    5747.0      20.0        1       11 2024        100       3140 Moravskoslezský kraj Orientační hodnota stavby se stavebním ohlášením nebo povolením mil. Kč Budovy nebytové Změny dokončených staveb (nástavby, přístavby a stavební úpravy)
1456739671  12878.0   verejny        3037      78     206         5632.0           11.0       NaN       NaN        1       11 2024        100       3140 Moravskoslezský kraj Orientační hodnota stavby se stavebním ohlášením nebo povolením mil. Kč   Budovy bytové                                                              NaN
1456740765  47455.0   verejny        3037      78     206            NaN            NaN       NaN       NaN        1       11 2024        100       3140 Moravskoslezský kraj Orientační hodnota stavby se stavebním ohlášením nebo povolením mil. Kč             NaN                                                              NaN
1456738984  21206.0   verejny        3037      78     206         5632.0           12.0       NaN       NaN        1       11 2024        100       3140 Moravskoslezský kraj Orientační hodnota stavby se stavebním ohlášením nebo povolením mil. Kč Budovy nebytové                                                              NaN
1456735185  13371.0   verejny        3037      78     206         5631.0            2.0       NaN       NaN        1       11 2024        100       3140 Moravskoslezský kraj Orientační hodnota stavby se stavebním ohlášením nebo povolením mil. Kč Inženýrská díla                                                              NaN
```

### 121. [A] Výroba masa na jatkách

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  druhzvire_cis  druhzvire_kod  mesic  rok  uzemi_cis  uzemi_kod                   stapro_txt                 mj_txt                             uzemi_txt      zviremaso_txt  status_kod  status_txt
1069202458   47.000        5660      78   80200            131             22      1 2023         97         19 Poražená hospodářská zvířata                    kus                       Česká republika        Skot - voli         NaN         NaN
1069202973   16.006        5660      78   93503            131             22      1 2023         97         19 Poražená hospodářská zvířata tuna jatečné hmotnosti                       Česká republika hovězí maso z volů         NaN         NaN
1069203015   78.000        5660      78   80200            131             50      1 2023         93          1 Poražená hospodářská zvířata                    kus Hlavní město Praha + Středočeský kraj            Jehňata         NaN         NaN
1069202501    1.373        5660      78   93503            131             50      1 2023         93          1 Poražená hospodářská zvířata tuna jatečné hmotnosti Hlavní město Praha + Středočeský kraj       jehněčí maso         NaN         NaN
1069202427  289.000        5660      78   80200            131             50      1 2023         97         19 Poražená hospodářská zvířata                    kus                       Česká republika            Jehňata         NaN         NaN
```

#### TAIL

```
     idhod   hodnota  stapro_kod  mj_cis  mj_kod  druhzvire_cis  druhzvire_kod  mesic  rok  uzemi_cis  uzemi_kod                   stapro_txt                 mj_txt            uzemi_txt                   zviremaso_txt status_kod      status_txt
1380991946       NaN        5660      78   80200            132              7     12 2024        100       3131 Poražená hospodářská zvířata                    kus         Zlínský kraj                    Skot - krávy          C Důvěrná hodnota
1380992298   188.000        5660      78   80200            132              7     12 2024        100       3140 Poražená hospodářská zvířata                    kus Moravskoslezský kraj                    Skot - krávy        NaN             NaN
1380992191     1.000        5660      78   80200            132             70     12 2024         97         19 Poražená hospodářská zvířata                    kus      Česká republika                            Koně        NaN             NaN
1380992025     0.307        5660      78   93503            132             70     12 2024         97         19 Poražená hospodářská zvířata tuna jatečné hmotnosti      Česká republika                     koňské maso        NaN             NaN
1380991379 13535.994        5660      78   93503            132             91     12 2024         97         19 Poražená hospodářská zvířata tuna jatečné hmotnosti      Česká republika drůbeží maso (drůbež a pštrosi)        NaN             NaN
```

### 122. [A] Zaměstnaní a nezaměstnaní podle výsledků výběrového šetření pracovních sil za kraje

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  ekak_cis  ekak_kod  pohlavi_cis  pohlavi_kod  rok  ctvrtleti  uzemi_cis  uzemi_kod       uzemi_txt                         stapro_txt     mj_txt pohlavi_txt
1170310791     67.9        3162      78   80403     221.0       4.0        102.0          2.0 2023        2.0         97         19 Česká republika                       Nezaměstnaní tisíc osob        žena
1170310806   2141.8        3162      78   80403     221.0       2.0        102.0          2.0 2023        2.0         97         19 Česká republika               Ekonomicky neaktivní tisíc osob        žena
1170308320   8666.9        3162      78   80403       NaN       NaN          NaN          NaN 2023        1.0         97         19 Česká republika Obyvatelstvo ve věku 15 a více let tisíc osob         NaN
1170308335   4232.2        3162      78   80403       NaN       NaN        102.0          1.0 2023        1.0         97         19 Česká republika Obyvatelstvo ve věku 15 a více let tisíc osob         muž
1170308350   4434.6        3162      78   80403       NaN       NaN        102.0          2.0 2023        1.0         97         19 Česká republika Obyvatelstvo ve věku 15 a více let tisíc osob        žena
```

#### TAIL

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  ekak_cis  ekak_kod  pohlavi_cis  pohlavi_kod  rok  ctvrtleti  uzemi_cis  uzemi_kod            uzemi_txt                  stapro_txt   mj_txt pohlavi_txt
1296595080      4.9        6290      78   83798       NaN       NaN        102.0          2.0 2024        1.0        100       3140 Moravskoslezský kraj Obecná míra nezaměstnanosti procento        žena
1296576632      3.2        6290      78   83798       NaN       NaN        102.0          1.0 2024        1.0        100       3140 Moravskoslezský kraj Obecná míra nezaměstnanosti procento         muž
1332566691      3.4        6290      78   83798       NaN       NaN        102.0          1.0 2024        2.0        100       3140 Moravskoslezský kraj Obecná míra nezaměstnanosti procento         muž
1332566722      3.4        6290      78   83798       NaN       NaN        102.0          2.0 2024        2.0        100       3140 Moravskoslezský kraj Obecná míra nezaměstnanosti procento        žena
1332566660      3.4        6290      78   83798       NaN       NaN          NaN          NaN 2024        2.0        100       3140 Moravskoslezský kraj Obecná míra nezaměstnanosti procento         NaN
```

### 123. [A] Školy a školská zařízení

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  ds_cis  ds_kod  fs_cis  fs_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do                           stapro_txt         ds_txt  fs_txt      vuzemi_txt
1463590852     5374        6043      78   99998     340       1     NaN     NaN          97          19 2023 2022-09-01 2023-08-31             Počet školských zařízení Mateřská škola     NaN Česká republika
1463590853    17120        6053      78   99998     340       1     NaN     NaN          97          19 2023 2022-09-01 2023-08-31                           Počet tříd Mateřská škola     NaN Česká republika
1463590854   369205        6059      78   80400     340       1     NaN     NaN          97          19 2023 2022-09-01 2023-08-31 Počet dětí v předškolních zařízeních Mateřská škola     NaN Česká republika
1463593411     4261        6043      78   99998     340       2     NaN     NaN          97          19 2023 2022-09-01 2023-08-31             Počet školských zařízení Základní škola     NaN Česká republika
1474737402    51190        6053      78   99998     340       2     NaN     NaN          97          19 2023 2022-09-01 2023-08-31                           Počet tříd Základní škola     NaN Česká republika
```

#### TAIL

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  ds_cis  ds_kod  fs_cis  fs_kod  vuzemi_cis  vuzemi_kod  rok  casref_od  casref_do               stapro_txt              ds_txt  fs_txt           vuzemi_txt
1349579249     2266        6053      78   99998     340       3     NaN     NaN         100        3140 2024 2023-09-01 2024-08-31               Počet tříd       Střední škola     NaN Moravskoslezský kraj
1349579250    52353        6057      78   80400     340       3     NaN     NaN         100        3140 2024 2023-09-01 2024-08-31               Počet žáků       Střední škola     NaN Moravskoslezský kraj
1463602212       13        6043      78   99998     340       5     NaN     NaN         100        3140 2024 2023-09-01 2024-08-31 Počet školských zařízení Vyšší odborná škola     NaN Moravskoslezský kraj
1463600850      106        6053      78   99998     340       5     NaN     NaN         100        3140 2024 2023-09-01 2024-08-31               Počet tříd Vyšší odborná škola     NaN Moravskoslezský kraj
1463600851     3485        6058      78   80400     340       5     NaN     NaN         100        3140 2024 2023-09-01 2024-08-31           Počet studentů Vyšší odborná škola     NaN Moravskoslezský kraj
```

### 124. [A] Hospodářská zvířata podle krajů

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  DRUHZVIRE_cis  DRUHZVIRE_kod  refobdobi  rok  uzemi_cis  uzemi_kod                 STAPRO_TXT                             uzemi_txt   DRUHZVIRE_txt
1248155766   153643        5560            132              1   20231231 2023         93          1 Počet hospodářských zvířat Hlavní město Praha + Středočeský kraj            Skot
1247675815   313557        5560            132             30   20231231 2023         93          1 Počet hospodářských zvířat Hlavní město Praha + Středočeský kraj         Prasata
1247674869    18255        5560            132             33   20231231 2023         93          1 Počet hospodářských zvířat Hlavní město Praha + Středočeský kraj Prasnice chovné
1284170295    21568        5560            132             50   20231231 2023         93          1 Počet hospodářských zvířat Hlavní město Praha + Středočeský kraj            Ovce
1271554560    21568        5560            132             50   20231231 2023         93          1 Počet hospodářských zvířat Hlavní město Praha + Středočeský kraj            Ovce
```

#### TAIL

```
     idhod  hodnota  stapro_kod  DRUHZVIRE_cis  DRUHZVIRE_kod  refobdobi  rok  uzemi_cis  uzemi_kod                 STAPRO_TXT            uzemi_txt    DRUHZVIRE_txt
1388195087    26125        5560            132             30   20241231 2024        100       3140 Počet hospodářských zvířat Moravskoslezský kraj          Prasata
1388195620     1686        5560            132             33   20241231 2024        100       3140 Počet hospodářských zvířat Moravskoslezský kraj  Prasnice chovné
1388129647    39064        5560            132              7   20241231 2024        100       3140 Počet hospodářských zvířat Moravskoslezský kraj     Skot - krávy
1388189433   315347        5560            132             81   20241231 2024        100       3140 Počet hospodářských zvířat Moravskoslezský kraj          Slepice
1388189264   926290        5560            132             91   20241231 2024        100       3140 Počet hospodářských zvířat Moravskoslezský kraj Drůbež a pštrosi
```

### 125. [A] Náklady na ochranu životního prostředí a ekonomický přínos těchto aktivit

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod    hodnota duvernost  stapro_kod  dnn_cis  dnn_kod  sektor_cis  sektor_kod  ozp_cis  ozp_kod  rok  uzemi_cis  uzemi_kod                             ukazatel_txt                                              ozp_txt       uzemi_txt       typ_uzemi
1480079433    52105.0   verejny         726      NaN      NaN         NaN         NaN   2307.0    115.0 2024         97         19 Investice na ochranu životního prostředí                                 Ochrana proti záření Česká republika Sídlo investora
1480078691  1538579.0   verejny         726      NaN      NaN         NaN         NaN   2307.0    114.0 2024         97         19 Investice na ochranu životního prostředí Ochrana krajiny a biodiverzity (druhová rozmanitost) Česká republika Sídlo investora
1480079601 11571584.0   verejny         726      NaN      NaN         NaN         NaN   2307.0    111.0 2024         97         19 Investice na ochranu životního prostředí              Ekologické nakládání s odpadními vodami Česká republika Sídlo investora
1480079431   207156.0   verejny         726      NaN      NaN         NaN         NaN   2307.0    116.0 2024         97         19 Investice na ochranu životního prostředí        Výzkum a vývoj na ochranu životního prostředí Česká republika Sídlo investora
1480079355  2691696.0   verejny         726      NaN      NaN         NaN         NaN   2307.0    112.0 2024         97         19 Investice na ochranu životního prostředí  Ochrana a sanace půdy, podzemních a povrchových vod Česká republika Sídlo investora
```

#### TAIL

```
     idhod  hodnota duvernost  stapro_kod  dnn_cis  dnn_kod  sektor_cis  sektor_kod  ozp_cis  ozp_kod  rok  uzemi_cis  uzemi_kod                        ukazatel_txt                                             ozp_txt            uzemi_txt  typ_uzemi
1331004674  34492.0   verejny        3932      NaN      NaN         NaN         NaN   2307.0    111.0 2023        100       3140 Tržby z prodeje vedlejších produktů             Ekologické nakládání s odpadními vodami Moravskoslezský kraj        NaN
1331004758      0.0   verejny        3932      NaN      NaN         NaN         NaN   2307.0    113.0 2023        100       3140 Tržby z prodeje vedlejších produktů Omezování hluku a vibrací (kromě ochrany pracovišť) Moravskoslezský kraj        NaN
1331004692      0.0   verejny        3932      NaN      NaN         NaN         NaN   2307.0    115.0 2023        100       3140 Tržby z prodeje vedlejších produktů                                Ochrana proti záření Moravskoslezský kraj        NaN
1331004701      0.0   verejny        3932      NaN      NaN         NaN         NaN   2307.0    116.0 2023        100       3140 Tržby z prodeje vedlejších produktů       Výzkum a vývoj na ochranu životního prostředí Moravskoslezský kraj        NaN
1331004766      NaN   duverny        3932      NaN      NaN         NaN         NaN   2307.0    180.0 2023        100       3140 Tržby z prodeje vedlejších produktů                             Ost.akt.na ochr.živ.pr. Moravskoslezský kraj        NaN
```

### 126. [A] Obyvatelstvo podle pětiletých věkových skupin a pohlaví

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis      vek_kod  vuzemi_cis  vuzemi_kod  casref_do  pohlavi_txt                                     vek_txt         vuzemi_txt uzemi_typ
1286408928  1384732        2406          NaN          NaN      NaN          NaN         100        3018 2023-12-31          NaN                                         NaN Hlavní město Praha      kraj
1284319375    12586        2406          NaN          NaN   7700.0 4.000006e+14         100        3018 2023-12-31          NaN     0 až 1 (více nebo rovno 0 a méně než 1) Hlavní město Praha      kraj
1284389234    58005        2406          NaN          NaN   7700.0 4.000016e+14         100        3018 2023-12-31          NaN     1 až 5 (více nebo rovno 1 a méně než 5) Hlavní město Praha      kraj
1284266315    74663        2406          NaN          NaN   7700.0 4.000056e+14         100        3018 2023-12-31          NaN   5 až 10 (více nebo rovno 5 a méně než 10) Hlavní město Praha      kraj
1284276193    73393        2406          NaN          NaN   7700.0 4.100106e+14         100        3018 2023-12-31          NaN 10 až 15 (více nebo rovno 10 a méně než 15) Hlavní město Praha      kraj
```

#### TAIL

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis      vek_kod  vuzemi_cis  vuzemi_kod  casref_do pohlavi_txt                                     vek_txt      vuzemi_txt uzemi_typ
1446047508   298814        2406        102.0          2.0   7700.0 4.100756e+14          97          19 2024-12-31        žena 75 až 80 (více nebo rovno 75 a méně než 80) Česká republika      stát
1446092575   192597        2406        102.0          2.0   7700.0 4.100806e+14          97          19 2024-12-31        žena 80 až 85 (více nebo rovno 80 a méně než 85) Česká republika      stát
1446006735    96551        2406        102.0          2.0   7700.0 4.100856e+14          97          19 2024-12-31        žena 85 až 90 (více nebo rovno 85 a méně než 90) Česká republika      stát
1446113914    41311        2406        102.0          2.0   7700.0 4.100906e+14          97          19 2024-12-31        žena 90 až 95 (více nebo rovno 90 a méně než 95) Česká republika      stát
1446026165     9577        2406        102.0          2.0   7700.0 4.100958e+14          97          19 2024-12-31        žena                  Od 95 (více nebo rovno 95) Česká republika      stát
```

### 127. [A] Průměrná hrubá měsíční mzda a medián mezd v krajích

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  SPKVANTIL_cis SPKVANTIL_kod  POHLAVI_cis  POHLAVI_kod  rok  uzemi_cis  uzemi_kod                         STAPRO_TXT       uzemi_txt SPKVANTIL_txt POHLAVI_txt
1448846369    48936        5958            NaN           NaN          NaN          NaN 2024         97         19 Průměrná hrubá mzda na zaměstnance Česká republika           NaN         NaN
1448846373    41742        5958         7636.0            Q5          NaN          NaN 2024         97         19 Průměrná hrubá mzda na zaměstnance Česká republika        medián         NaN
1448846377    53423        5958            NaN           NaN        102.0          1.0 2024         97         19 Průměrná hrubá mzda na zaměstnance Česká republika           NaN         muž
1448846381    44740        5958         7636.0            Q5        102.0          1.0 2024         97         19 Průměrná hrubá mzda na zaměstnance Česká republika        medián         muž
1448846385    43741        5958            NaN           NaN        102.0          2.0 2024         97         19 Průměrná hrubá mzda na zaměstnance Česká republika           NaN        žena
```

#### TAIL

```
     idhod  hodnota  stapro_kod  SPKVANTIL_cis SPKVANTIL_kod  POHLAVI_cis  POHLAVI_kod  rok  uzemi_cis  uzemi_kod                         STAPRO_TXT            uzemi_txt SPKVANTIL_txt POHLAVI_txt
1286716606    45284        5958            NaN           NaN        102.0          1.0 2023        100       3140 Průměrná hrubá mzda na zaměstnance Moravskoslezský kraj           NaN         muž
1286716607    37925        5958            NaN           NaN        102.0          2.0 2023        100       3140 Průměrná hrubá mzda na zaměstnance Moravskoslezský kraj           NaN        žena
1286716608    38073        5958         7636.0            Q5          NaN          NaN 2023        100       3140 Průměrná hrubá mzda na zaměstnance Moravskoslezský kraj        medián         NaN
1286716609    40741        5958         7636.0            Q5        102.0          1.0 2023        100       3140 Průměrná hrubá mzda na zaměstnance Moravskoslezský kraj        medián         muž
1286716610    34690        5958         7636.0            Q5        102.0          2.0 2023        100       3140 Průměrná hrubá mzda na zaměstnance Moravskoslezský kraj        medián        žena
```

### 128. [A] Sklizeň zemědělských plodin podle krajů

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod      hodnota  stapro_kod  MJ_CIS  MJ_KOD  DRUHZPLOD_cis  DRUHZPLOD_kod  rok  uzemi_cis  uzemi_kod                  STAPRO_TXT       uzemi_txt        DRUHZPLOD_txt
1393173448 4.625367e+06        5906      78   20103            209            103 2024         97         19 Sklizeň zemědělských plodin Česká republika              Pšenice
1393175172 7.130454e+06        5906      78   20103            209            502 2024         97         19 Sklizeň zemědělských plodin Česká republika   Kukuřice na zeleno
1393169642 1.056402e+05        5906      78   20103            208          10200 2024         97         19 Sklizeň zemědělských plodin Česká republika                 Žito
1393169723 4.347322e+06        5906      78   20103            209            505 2024         97         19 Sklizeň zemědělských plodin Česká republika Pícniny na orné půdě
1393177150 9.468908e+05        5906      78   20103            209            401 2024         97         19 Sklizeň zemědělských plodin Česká republika                Řepka
```

#### TAIL

```
     idhod   hodnota  stapro_kod  MJ_CIS  MJ_KOD  DRUHZPLOD_cis  DRUHZPLOD_kod  rok  uzemi_cis  uzemi_kod                                  STAPRO_TXT            uzemi_txt                                                                                                                               DRUHZPLOD_txt
1263381030 65.802558        5908      78   20103            208          30200 2023        100       3140 Hektarový výnos sklizně zemědělských plodin Moravskoslezský kraj                                                                                                                                Řepa cukrová
1263386436  5.132866        5908      78   20103            208          10200 2023        100       3140 Hektarový výnos sklizně zemědělských plodin Moravskoslezský kraj                                                                                                                                        Žito
1263383086  5.927721        5908      78   20103            209            112 2023        100       3140 Hektarový výnos sklizně zemědělských plodin Moravskoslezský kraj Obiloviny na zrno (pšenice, žito, ječmen, oves, tritikale, kukuřice na zrno, pohanka, směsi obilovin na zrno, jiné obiloviny včetně čiroku)
1263385962  3.400415        5908      78   20103            209            806 2023        100       3140 Hektarový výnos sklizně zemědělských plodin Moravskoslezský kraj                                                                                                                       Trvalé travní porosty
1263388608 33.638289        5908      78   20103            209            502 2023        100       3140 Hektarový výnos sklizně zemědělských plodin Moravskoslezský kraj                                                                                                                          Kukuřice na zeleno
```

### 129. [A] Ukazatele výzkumu a vývoje podle krajů

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota duvernost  stapro_kod  elpro_id  mj_cis  mj_kod  rok  uzemi_cis  uzemi_kod                                 ukazatel_txt mj_txt            uzemi_txt
1338236872      902   verejny         322   1336103      78   80400 2023        100       3069 Výzkumní pracovníci (fyzické osoby k 31.12.)  osoba         Ústecký kraj
1338236874     4086   verejny         322   1345880      78   80400 2023        100       3034      Zaměstnanci VaV (fyzické osoby k 31.12)  osoba       Jihočeský kraj
1338236889     1947   verejny         322   1336103      78   80400 2023        100       3085 Výzkumní pracovníci (fyzické osoby k 31.12.)  osoba Královéhradecký kraj
1338236890     2078   verejny         322   1336103      78   80400 2023        100       3034 Výzkumní pracovníci (fyzické osoby k 31.12.)  osoba       Jihočeský kraj
1338236909      828   verejny         322   1336103      78   80400 2023        100       3107 Výzkumní pracovníci (fyzické osoby k 31.12.)  osoba        Kraj Vysočina
```

#### TAIL

```
     idhod  hodnota duvernost  stapro_kod  elpro_id  mj_cis  mj_kod  rok  uzemi_cis  uzemi_kod                                              ukazatel_txt               mj_txt     uzemi_txt
1484913772       17   verejny        2927  10013204      78     206 2024        100       3107 Výdaje na VaV financované z veřejných zdrojů ze zahraničí milion korun českých Kraj Vysočina
1338237122     1427   verejny        2927  10022558      78     206 2023        100       3107        Výdaje na VaV financované z podnikatelských zdrojů milion korun českých Kraj Vysočina
1484913797     1558   verejny        2927  10022558      78     206 2024        100       3107        Výdaje na VaV financované z podnikatelských zdrojů milion korun českých Kraj Vysočina
1338237037     1497   verejny        2927  10022630      78     206 2023        100       3107                             Běžné výdaje na výzkum a vědu milion korun českých Kraj Vysočina
1484913798     1633   verejny        2927  10022630      78     206 2024        100       3107                             Běžné výdaje na výzkum a vědu milion korun českých Kraj Vysočina
```

### 130. [A] Úmrtnostní tabulky pro kraje

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis         vek_kod  vuzemi_cis  vuzemi_kod  casref_od  casref_do          stapro_txt pohlavi_txt  vek_txt         vuzemi_txt
1455246006 0.001621        8817          102            1     7700 400000600001000         100        3018 2023-01-01 2024-12-31 Míra úmrtnosti (mx)         muž        0 Hlavní město Praha
1455388444 0.000263        8817          102            1     7700 400001600002000         100        3018 2023-01-01 2024-12-31 Míra úmrtnosti (mx)         muž        1 Hlavní město Praha
1455172546 0.000133        8817          102            1     7700 400002600003000         100        3018 2023-01-01 2024-12-31 Míra úmrtnosti (mx)         muž        2 Hlavní město Praha
1455083086 0.000105        8817          102            1     7700 400003600004000         100        3018 2023-01-01 2024-12-31 Míra úmrtnosti (mx)         muž        3 Hlavní město Praha
1455083058 0.000083        8817          102            1     7700 400004600005000         100        3018 2023-01-01 2024-12-31 Míra úmrtnosti (mx)         muž        4 Hlavní město Praha
```

#### TAIL

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis         vek_kod  vuzemi_cis  vuzemi_kod  casref_od  casref_do                    stapro_txt pohlavi_txt  vek_txt           vuzemi_txt
1454948383    717.0        7193          102            2     7700 420101620102000         100        3140 2023-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      101 Moravskoslezský kraj
1454966357    417.0        7193          102            2     7700 420102620103000         100        3140 2023-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      102 Moravskoslezský kraj
1454941625    233.0        7193          102            2     7700 420103620104000         100        3140 2023-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      103 Moravskoslezský kraj
1454954653    125.0        7193          102            2     7700 420104620105000         100        3140 2023-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      104 Moravskoslezský kraj
1448830916    129.0        7193          102            2     7700 420105620106000         100        3140 2023-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      105 Moravskoslezský kraj
```

## Kategorie B

### 131. [B] Volby do zastupitelstev krajů 2024 - číselník navrhujících stran

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
 NSTRANA                    NAZEV_STRN                    ZKRATKAN30 ZKRATKAN8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
      24          Konzervativní strana          Konzervativní strana      KONS
```

#### TAIL

```
 NSTRANA                                        NAZEV_STRN                    ZKRATKAN30       ZKRATKAN8
    1292                     MÁ VLAST ČECHY MORAVA SLEZSKO MÁ VLAST ČECHY MORAVA SLEZSKO    MÁ VLAST ČMS
    1293            Nadační občansko-politické hnutí ReMeK Nadační obč.-pol. hnutí ReMeK           ReMeK
    1294 Nestraníci pro jižní Moravu-www.nestranici2024.cz   Nestraníci pro jižní Moravu  Nestranici2024
    9995                                           Koalice                       Koalice         Koalice
    9999                               Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

## Kategorie C

### 132. [C] Sčítání 2021 - Děti podle rodinného stavu, vzdělání a věku matky

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  stav_zeny_cis  stav_zeny_kod  vzdelani_zeny_cis  vzdelani_zeny_kod  vek_zeny_cis  vek_zeny_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                   ukaz_txt stav_zeny_txt  vzdelani_zeny_txt  vek_zeny_txt       uzemi_txt
983446234   580783      2501           5788              1                NaN                NaN          1035    1200159999         97         19      2021 2021-03-26 Počet živě narozených dětí      Svobodná                NaN 15 a více let Česká republika
983443618     3096      2501           5788              1                NaN                NaN          1035    1300150019         97         19      2021 2021-03-26 Počet živě narozených dětí      Svobodná                NaN   15 - 19 let Česká republika
983482131    28284      2501           5788              1                NaN                NaN          1035    1300200024         97         19      2021 2021-03-26 Počet živě narozených dětí      Svobodná                NaN   20 - 24 let Česká republika
983475445    81582      2501           5788              1                NaN                NaN          1035    1300250029         97         19      2021 2021-03-26 Počet živě narozených dětí      Svobodná                NaN   25 - 29 let Česká republika
983441931   123395      2501           5788              1                NaN                NaN          1035    1300300034         97         19      2021 2021-03-26 Počet živě narozených dětí      Svobodná                NaN   30 - 34 let Česká republika
```

#### TAIL

```
    idhod     hodnota  ukaz_kod  stav_zeny_cis  stav_zeny_kod  vzdelani_zeny_cis  vzdelani_zeny_kod  vek_zeny_cis  vek_zeny_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                                       ukaz_txt stav_zeny_txt vzdelani_zeny_txt  vek_zeny_txt            uzemi_txt
983513894 2500.000000      4938           5788             99             5784.0              109.0          1035    1300600064        100       3140      2021 2021-03-26 Podíl počtu živě narozených dětí na 1000 žen s aspoň 1 dítětem    Nezjištěno     Vysokoškolské   60 - 64 let Moravskoslezský kraj
983572861 1500.000000      4938           5788             99             5784.0              109.0          1035    1300650069        100       3140      2021 2021-03-26 Podíl počtu živě narozených dětí na 1000 žen s aspoň 1 dítětem    Nezjištěno     Vysokoškolské   65 - 69 let Moravskoslezský kraj
983557613 2000.000000      4938           5788             99             5784.0              109.0          1035    1300700074        100       3140      2021 2021-03-26 Podíl počtu živě narozených dětí na 1000 žen s aspoň 1 dítětem    Nezjištěno     Vysokoškolské   70 - 74 let Moravskoslezský kraj
983570679 1500.000000      4938           5788             99             5784.0              109.0          1035    1300750079        100       3140      2021 2021-03-26 Podíl počtu živě narozených dětí na 1000 žen s aspoň 1 dítětem    Nezjištěno     Vysokoškolské   75 - 79 let Moravskoslezský kraj
983514575 1777.777778      4938           5788             99             5784.0              109.0          1035    1200809999        100       3140      2021 2021-03-26 Podíl počtu živě narozených dětí na 1000 žen s aspoň 1 dítětem    Nezjištěno     Vysokoškolské 80 a více let Moravskoslezský kraj
```

### 133. [C] Sčítání 2021 - Obyvatelstvo podle ekonomické aktivity, jednoletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  aktivita_struktura  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt  aktivita_txt vek_txt pohlavi_txt       uzemi_txt uzemi_typ
1080013679        0      3162          3249            53                   1     1035 1000000000          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla   0 let         NaN Česká republika      stát
1079741836        0      3162          3249            53                   1     1035 1000000000        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla   0 let         muž Česká republika      stát
1080642190        0      3162          3249            53                   1     1035 1000000000        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla   0 let        žena Česká republika      stát
1080159644        0      3162          3249            53                   1     1035 1000010001          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla   1 rok         NaN Česká republika      stát
1080401675        0      3162          3249            53                   1     1035 1000010001        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Pracovní síla   1 rok         muž Česká republika      stát
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  aktivita_struktura  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt aktivita_txt        vek_txt pohlavi_txt            uzemi_txt uzemi_typ
1080017740        0      3162          3072            99                   3     1035 1000990099        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno         99 let         muž Moravskoslezský kraj      kraj
1080163477        0      3162          3072            99                   3     1035 1000990099        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno         99 let        žena Moravskoslezský kraj      kraj
1079852601        0      3162          3072            99                   3     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 100 a více let         NaN Moravskoslezský kraj      kraj
1080645250        0      3162          3072            99                   3     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 100 a více let         muž Moravskoslezský kraj      kraj
1080405267        0      3162          3072            99                   3     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Nezjištěno 100 a více let        žena Moravskoslezský kraj      kraj
```

### 134. [C] Sčítání 2021 - Obyvatelstvo podle mateřského jazyka a pohlaví (1 mateřský jazyk)

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt       jazyk_txt pohlavi_txt       uzemi_txt
947072940 10524167      3162        NaN        NaN          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem             NaN         NaN Česká republika
967320076  4365187      3162     5750.0        1.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český jazyk         muž Česká republika
967320310  4631288      3162     5750.0        1.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český jazyk        žena Česká republika
967320315    68822      3162     5750.0        2.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slovenský jazyk         muž Česká republika
967320316    81916      3162     5750.0        2.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slovenský jazyk        žena Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                        jazyk_txt pohlavi_txt            uzemi_txt
967322203      183      3162     5750.0       98.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                       Jiný jazyk        žena Moravskoslezský kraj
967321956    49565      3162     5750.0       99.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                       Nezjištěno         muž Moravskoslezský kraj
967321957    37256      3162     5750.0       99.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                       Nezjištěno        žena Moravskoslezský kraj
967321960    19402      3162     3295.0       20.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby se dvěma mateřskými jazyky         muž Moravskoslezský kraj
967322191    18733      3162     3295.0       20.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby se dvěma mateřskými jazyky        žena Moravskoslezský kraj
```

### 135. [C] Sčítání 2021 - Obyvatelstvo podle mateřského jazyka a pohlaví (1 nebo 2 mateřské jazyky)

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt        jazyk_txt pohlavi_txt       uzemi_txt
947072940 10524167      3162        NaN        NaN          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem              NaN         NaN Česká republika
968137568  4476299      3162     3295.0      201.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český celkem         muž Česká republika
968137569  4737688      3162     3295.0      201.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český celkem        žena Česká republika
968137570   105621      3162     3295.0      202.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slovenský celkem         muž Česká republika
968137571   119625      3162     3295.0      202.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slovenský celkem        žena Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt     jazyk_txt pohlavi_txt            uzemi_txt
968138265       16      3162     3295.0      255.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Perský celkem        žena Moravskoslezský kraj
968138525        7      3162     3295.0      256.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Urdský celkem         muž Moravskoslezský kraj
968138526        7      3162     3295.0      256.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Urdský celkem        žena Moravskoslezský kraj
967321956    49565      3162     5750.0       99.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Nezjištěno         muž Moravskoslezský kraj
967321957    37256      3162     5750.0       99.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Nezjištěno        žena Moravskoslezský kraj
```

### 136. [C] Sčítání 2021 - Obyvatelstvo podle mateřského jazyka, věku a pohlaví (1 mateřský jazyk)

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt jazyk_txt vek_txt pohlavi_txt       uzemi_txt
987347049    85782      3162       5750          1     1035 1000000000          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český   0 let         NaN Česká republika
987335928    43886      3162       5750          1     1035 1000000000        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český   0 let         muž Česká republika
987336800    41896      3162       5750          1     1035 1000000000        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český   0 let        žena Česká republika
987339037    89054      3162       5750          1     1035 1000010001          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český   1 rok         NaN Česká republika
987338541    45559      3162       5750          1     1035 1000010001        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem     Český   1 rok         muž Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt  jazyk_txt        vek_txt pohlavi_txt            uzemi_txt
987371171       12      3162       5750         99     1035 1300950099        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno    95 - 99 let         muž Moravskoslezský kraj
987371172       45      3162       5750         99     1035 1300950099        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno    95 - 99 let        žena Moravskoslezský kraj
987353601        5      3162       5750         99     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let         NaN Moravskoslezský kraj
987366851        0      3162       5750         99     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let         muž Moravskoslezský kraj
987366852        5      3162       5750         99     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let        žena Moravskoslezský kraj
```

### 137. [C] Sčítání 2021 - Obyvatelstvo podle mateřského jazyka, věku a pohlaví (1 nebo 2 mateřské jazyky)

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                            ukaz_txt      jazyk_txt vek_txt pohlavi_txt         uzemi_txt
987395721    89108      3162       3295        201     1035 1000000000          NaN          NaN         97         19      2021 2021-03-26 PoДЌet obyvatel s obvyklГЅm pobytem ДЊeskГЅ celkem   0 let         NaN ДЊeskГЎ republika
987395198    45612      3162       3295        201     1035 1000000000        102.0          1.0         97         19      2021 2021-03-26 PoДЌet obyvatel s obvyklГЅm pobytem ДЊeskГЅ celkem   0 let        muЕѕ ДЊeskГЎ republika
987395199    43496      3162       3295        201     1035 1000000000        102.0          2.0         97         19      2021 2021-03-26 PoДЌet obyvatel s obvyklГЅm pobytem ДЊeskГЅ celkem   0 let       Еѕena ДЊeskГЎ republika
987395722    92636      3162       3295        201     1035 1000010001          NaN          NaN         97         19      2021 2021-03-26 PoДЌet obyvatel s obvyklГЅm pobytem ДЊeskГЅ celkem   1 rok         NaN ДЊeskГЎ republika
987396080    47412      3162       3295        201     1035 1000010001        102.0          1.0         97         19      2021 2021-03-26 PoДЌet obyvatel s obvyklГЅm pobytem ДЊeskГЅ celkem   1 rok        muЕѕ ДЊeskГЎ republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  jazyk_cis  jazyk_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt      jazyk_txt        vek_txt pohlavi_txt            uzemi_txt
987421580        1      3162       3295        229     1035 1300950099        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slezský celkem    95 - 99 let         muž Moravskoslezský kraj
987421581        5      3162       3295        229     1035 1300950099        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slezský celkem    95 - 99 let        žena Moravskoslezský kraj
987411838        0      3162       3295        229     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slezský celkem 100 a více let         NaN Moravskoslezský kraj
987421582        0      3162       3295        229     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slezský celkem 100 a více let         muž Moravskoslezský kraj
987421583        0      3162       3295        229     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Slezský celkem 100 a více let        žena Moravskoslezský kraj
```

### 138. [C] Sčítání 2021 - Obyvatelstvo podle náboženské víry a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vira_cis  vira_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt            vira_txt pohlavi_txt       uzemi_txt
947072940 10524167      3162       NaN       NaN          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                 NaN         NaN Česká republika
946963121  2548297      3162    3078.0       1.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez náboženské víry         muž Česká republika
946963122  2478844      3162    3078.0       1.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez náboženské víry        žena Česká republika
946963833     2287      3162    3078.0       2.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Apoštolská církev         muž Česká republika
946963834     2671      3162    3078.0       2.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   Apoštolská církev        žena Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vira_cis  vira_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                                      vira_txt pohlavi_txt            uzemi_txt
946965584        4      3162    3078.0      77.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                               rastafariánství        žena Moravskoslezský kraj
946964177     4230      3162    3078.0      78.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem věřící - hlásící se k církvi - název neuveden         muž Moravskoslezský kraj
946964178     5260      3162    3078.0      78.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem věřící - hlásící se k církvi - název neuveden        žena Moravskoslezský kraj
946963947   174043      3162    3078.0      99.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                     Neuvedeno         muž Moravskoslezský kraj
946963948   170187      3162    3078.0      99.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                     Neuvedeno        žena Moravskoslezský kraj
```

### 139. [C] Sčítání 2021 - Obyvatelstvo podle náboženské víry, věku a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vira_cis  vira_kod  vira_cleneni  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt            vira_txt vek_txt pohlavi_txt       uzemi_txt
989095533    51397      3162      3078         1             1     1035 1000000000          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez náboženské víry   0 let         NaN Česká republika
989113507    26279      3162      3078         1             1     1035 1000000000        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez náboženské víry   0 let         muž Česká republika
989113508    25118      3162      3078         1             1     1035 1000000000        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez náboženské víry   0 let        žena Česká republika
989096570    52693      3162      3078         1             1     1035 1000010001          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez náboženské víry   1 rok         NaN Česká republika
989112602    26922      3162      3078         1             1     1035 1000010001        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez náboženské víry   1 rok         muž Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vira_cis  vira_kod  vira_cleneni  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt               vira_txt        vek_txt pohlavi_txt            uzemi_txt
989339304       28      3162      3078         9             3     1035 1300950099        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Církev římskokatolická    95 - 99 let         muž Moravskoslezský kraj
989339070      220      3162      3078         9             3     1035 1300950099        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Církev římskokatolická    95 - 99 let        žena Moravskoslezský kraj
989351018       23      3162      3078         9             3     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Církev římskokatolická 100 a více let         NaN Moravskoslezský kraj
989338228        3      3162      3078         9             3     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Církev římskokatolická 100 a více let         muž Moravskoslezský kraj
989349916       20      3162      3078         9             3     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Církev římskokatolická 100 a více let        žena Moravskoslezský kraj
```

### 140. [C] Sčítání 2021 - Obyvatelstvo podle národnosti, věku a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  narodnost_cis  narodnost_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt    narodnost_txt vek_txt pohlavi_txt       uzemi_txt
987569350        1      3162           3267            201     1035 1000000000          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem afghánská celkem   0 let         NaN Česká republika
987580198        1      3162           3267            201     1035 1000000000        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem afghánská celkem   0 let         muž Česká republika
987592433        0      3162           3267            201     1035 1000000000        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem afghánská celkem   0 let        žena Česká republika
987630662        2      3162           3267            201     1035 1000010001          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem afghánská celkem   1 rok         NaN Česká republika
987616862        1      3162           3267            201     1035 1000010001        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem afghánská celkem   1 rok         muž Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  narodnost_cis  narodnost_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt     narodnost_txt        vek_txt pohlavi_txt            uzemi_txt
987573987        0      3162           3267            273     1035 1000990099        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ukrajinská celkem         99 let         muž Moravskoslezský kraj
987647452        0      3162           3267            273     1035 1000990099        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ukrajinská celkem         99 let        žena Moravskoslezský kraj
987323045        0      3162           3267            273     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ukrajinská celkem 100 a více let         NaN Moravskoslezský kraj
987319900        0      3162           3267            273     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ukrajinská celkem 100 a více let         muž Moravskoslezský kraj
987319901        0      3162           3267            273     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ukrajinská celkem 100 a více let        žena Moravskoslezský kraj
```

### 141. [C] Sčítání 2021 - Obyvatelstvo podle rodinného stavu a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt          stav_txt pohlavi_txt       uzemi_txt
947072940 10524167      3162       NaN       NaN          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem               NaN         NaN Česká republika
936990231  2477037      3162    5788.0       1.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná         muž Česká republika
936990255  2031554      3162    5788.0       1.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná        žena Česká republika
936990230  2009738      3162    5788.0       2.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem      Ženatý/vdaná         muž Česká republika
936990254  1997604      3162    5788.0       2.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem      Ženatý/vdaná        žena Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                                                   stav_txt pohlavi_txt            uzemi_txt
936990200       76      3162    5788.0       7.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem         Registrované partnerství zaniklé rozhodnutím soudu        žena Moravskoslezský kraj
936990193        6      3162    5788.0       8.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Registrované partnerství zaniklé úmrtím partnera/partnerky         muž Moravskoslezský kraj
936990201        1      3162    5788.0       8.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Registrované partnerství zaniklé úmrtím partnera/partnerky        žena Moravskoslezský kraj
936990191     1853      3162    5788.0      99.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                                 Nezjištěno         muž Moravskoslezský kraj
936990199     1326      3162    5788.0      99.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                                                 Nezjištěno        žena Moravskoslezský kraj
```

### 142. [C] Sčítání 2021 - Obyvatelstvo podle rodinného stavu, desetiletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt          stav_txt     vek_txt pohlavi_txt       uzemi_txt
980446664  1110656      3162      5788         1     1035 1100000009          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná   0 - 9 let         NaN Česká republika
980383293   568961      3162      5788         1     1035 1100000009        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná   0 - 9 let         muž Česká republika
980445569   541695      3162      5788         1     1035 1100000009        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná   0 - 9 let        žena Česká republika
980385529  1069246      3162      5788         1     1035 1300100019          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná 10 - 19 let         NaN Česká republika
980447123   548129      3162      5788         1     1035 1300100019        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná 10 - 19 let         muž Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt   stav_txt        vek_txt pohlavi_txt            uzemi_txt
980417088       36      3162      5788        99     1035 1300900099        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno    90 - 99 let         muž Moravskoslezský kraj
980366806      113      3162      5788        99     1035 1300900099        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno    90 - 99 let        žena Moravskoslezský kraj
980374222        2      3162      5788        99     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let         NaN Moravskoslezský kraj
980427409        0      3162      5788        99     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let         muž Moravskoslezský kraj
980407074        2      3162      5788        99     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let        žena Moravskoslezský kraj
```

### 143. [C] Sčítání 2021 - Obyvatelstvo podle rodinného stavu, jednoletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt          stav_txt vek_txt pohlavi_txt       uzemi_txt
980415301   109186      3162      5788         1     1035 1000000000          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná   0 let         NaN Česká republika
980436823    55778      3162      5788         1     1035 1000000000        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná   0 let         muž Česká republika
980426747    53408      3162      5788         1     1035 1000000000        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná   0 let        žena Česká republika
980435653   110951      3162      5788         1     1035 1000010001          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná   1 rok         NaN Česká republika
980415090    56820      3162      5788         1     1035 1000010001        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná   1 rok         muž Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt   stav_txt        vek_txt pohlavi_txt            uzemi_txt
980414522        0      3162      5788        99     1035 1000990099        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno         99 let         muž Moravskoslezský kraj
980382104        6      3162      5788        99     1035 1000990099        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno         99 let        žena Moravskoslezský kraj
980374222        2      3162      5788        99     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let         NaN Moravskoslezský kraj
980427409        0      3162      5788        99     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let         muž Moravskoslezský kraj
980407074        2      3162      5788        99     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let        žena Moravskoslezský kraj
```

### 144. [C] Sčítání 2021 - Obyvatelstvo podle rodinného stavu, pětiletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt          stav_txt    vek_txt pohlavi_txt       uzemi_txt
980395735   560632      3162      5788         1     1035 1100000004          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná 0 - 4 roky         NaN Česká republika
980405143   286889      3162      5788         1     1035 1100000004        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná 0 - 4 roky         muž Česká republika
980383501   273743      3162      5788         1     1035 1100000004        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná 0 - 4 roky        žena Česká republika
980426005   550024      3162      5788         1     1035 1300050009          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná  5 - 9 let         NaN Česká republika
980383298   282072      3162      5788         1     1035 1300050009        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná  5 - 9 let         muž Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt   stav_txt        vek_txt pohlavi_txt            uzemi_txt
980367705        6      3162      5788        99     1035 1300950099        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno    95 - 99 let         muž Moravskoslezský kraj
980417520       27      3162      5788        99     1035 1300950099        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno    95 - 99 let        žena Moravskoslezský kraj
980374222        2      3162      5788        99     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let         NaN Moravskoslezský kraj
980427409        0      3162      5788        99     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let         muž Moravskoslezský kraj
980407074        2      3162      5788        99     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 100 a více let        žena Moravskoslezský kraj
```

### 145. [C] Sčítání 2021 - Obyvatelstvo podle rodinného stavu, velikostních skupin obcí a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  velikostobce_cis  velikostobce_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt          stav_txt   velikostobce_txt pohlavi_txt       uzemi_txt
947072940 10524167      3162       NaN       NaN               NaN               NaN          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem               NaN                NaN         NaN Česká republika
980415191    71690      3162    5788.0       1.0            1234.0              98.0          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná    do 199 obyvatel         NaN Česká republika
980436915    41011      3162    5788.0       1.0            1234.0              98.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná    do 199 obyvatel         muž Česká republika
980447096    30679      3162    5788.0       1.0            1234.0              98.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná    do 199 obyvatel        žena Česká republika
980383452   268817      3162    5788.0       1.0            1234.0              99.0          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Svobodný/svobodná 200 - 499 obyvatel         NaN Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  stav_cis  stav_kod  velikostobce_cis  velikostobce_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt   stav_txt        velikostobce_txt pohlavi_txt            uzemi_txt
980406604      272      3162    5788.0      99.0            1234.0               8.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 50000 až 99999 obyvatel         muž Moravskoslezský kraj
980447143      226      3162    5788.0      99.0            1234.0               8.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno 50000 až 99999 obyvatel        žena Moravskoslezský kraj
980415521     1041      3162    5788.0      99.0            1234.0               9.0          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno  100000 a více obyvatel         NaN Moravskoslezský kraj
980416595      601      3162    5788.0      99.0            1234.0               9.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno  100000 a více obyvatel         muž Moravskoslezský kraj
980416596      440      3162    5788.0      99.0            1234.0               9.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno  100000 a více obyvatel        žena Moravskoslezský kraj
```

### 146. [C] Sčítání 2021 - Obyvatelstvo podle státního občanství a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  obcanstvi_cis  obcanstvi_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                  obcanstvi_txt pohlavi_txt       uzemi_txt
947072940 10524167      3162            NaN            NaN          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                            NaN         NaN Česká republika
957681860    21893      3162         3181.0            5.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                Dvojí občanství         muž Česká republika
957681863    23483      3162         3181.0            5.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                Dvojí občanství        žena Česká republika
954943279      145      3162         3228.0            4.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Islámská republika Afghánistán         muž Česká republika
954943753      104      3162         3228.0            4.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Islámská republika Afghánistán        žena Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  obcanstvi_cis  obcanstvi_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt          obcanstvi_txt pohlavi_txt            uzemi_txt
954945561        0      3162         3228.0          894.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    Zambijská republika        žena Moravskoslezský kraj
954941461       10      3162         3228.0          900.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem bez státního občanství         muž Moravskoslezský kraj
954944507        3      3162         3228.0          900.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem bez státního občanství        žena Moravskoslezský kraj
954942464      696      3162         3228.0         9999.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem             Nezjištěno         muž Moravskoslezský kraj
954945570      469      3162         3228.0         9999.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem             Nezjištěno        žena Moravskoslezský kraj
```

### 147. [C] Sčítání 2021 - Obyvatelstvo podle státního občanství, věku a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  obcan_cis  obcan_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt  obcan_txt vek_txt pohlavi_txt       uzemi_txt
1009172017      455      3162       3228       9999     1035 1000000000          102            1         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno   0 let         muž Česká republika
1008947722      486      3162       3228       9999     1035 1000000000          102            2         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno   0 let        žena Česká republika
1009025193      260      3162       3228       9999     1035 1000010001          102            1         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno   1 rok         muž Česká republika
1008654019      236      3162       3228       9999     1035 1000010001          102            2         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno   1 rok        žena Česká republika
1008951351      182      3162       3228       9999     1035 1000020002          102            1         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nezjištěno  2 roky         muž Česká republika
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  obcan_cis  obcan_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt        obcan_txt        vek_txt pohlavi_txt            uzemi_txt
1005546369        0      3162       5837      95000     1035 1300900094          102            2        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Republika Kosovo    90 - 94 let        žena Moravskoslezský kraj
1005189793        0      3162       5837      95000     1035 1300950099          102            1        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Republika Kosovo    95 - 99 let         muž Moravskoslezský kraj
1004477179        0      3162       5837      95000     1035 1300950099          102            2        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Republika Kosovo    95 - 99 let        žena Moravskoslezský kraj
1006232266        0      3162       5837      95000     1035 1201009999          102            1        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Republika Kosovo 100 a více let         muž Moravskoslezský kraj
1006978850        0      3162       5837      95000     1035 1201009999          102            2        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Republika Kosovo 100 a více let        žena Moravskoslezský kraj
```

### 148. [C] Sčítání 2021 - Obyvatelstvo podle velikostních skupin obcí a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  velikostobce_cis  velikostobce_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt   velikostobce_txt pohlavi_txt       uzemi_txt
947072940 10524167      3162               NaN               NaN          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                NaN         NaN Česká republika
978399248   178213      3162            1234.0              98.0          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    do 199 obyvatel         NaN Česká republika
978179816    91305      3162            1234.0              98.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    do 199 obyvatel         muž Česká republika
978070391    86908      3162            1234.0              98.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    do 199 obyvatel        žena Česká republika
978124969   654469      3162            1234.0              99.0          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 200 - 499 obyvatel         NaN Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  velikostobce_cis  velikostobce_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt        velikostobce_txt pohlavi_txt            uzemi_txt
978343646    85625      3162            1234.0               8.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 50000 až 99999 obyvatel         muž Moravskoslezský kraj
978233912    91372      3162            1234.0               8.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 50000 až 99999 obyvatel        žena Moravskoslezský kraj
978453663   282450      3162            1234.0               9.0          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem  100000 a více obyvatel         NaN Moravskoslezský kraj
978069588   137575      3162            1234.0               9.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem  100000 a více obyvatel         muž Moravskoslezský kraj
978124271   144875      3162            1234.0               9.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem  100000 a více obyvatel        žena Moravskoslezský kraj
```

### 149. [C] Sčítání 2021 - Obyvatelstvo podle vzdělání a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  vzdelani_cleneni  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                                ukaz_txt              vzdelani_txt pohlavi_txt       uzemi_txt
978179474  8832407      3162           NaN           NaN                 0          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let                       NaN         NaN Česká republika
944998080    56100      3162        1294.0           1.0                 1          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let              Bez vzdělání         NaN Česká republika
936989751    28660      3162        1294.0           1.0                 1        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let              Bez vzdělání         muž Česká republika
936989758    27440      3162        1294.0           1.0                 1        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let              Bez vzdělání        žena Česká republika
944985497  1107860      3162        5784.0         117.0                 1          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Základní vč. neukončeného         NaN Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  vzdelani_cleneni  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                                ukaz_txt                       vzdelani_txt pohlavi_txt            uzemi_txt
980448817    53777      3162        1294.0          13.0                 2        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Vysokoškolské magisterské vzdělání         muž Moravskoslezský kraj
980448818    58905      3162        1294.0          13.0                 2        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Vysokoškolské magisterské vzdělání        žena Moravskoslezský kraj
980454103     5520      3162        1294.0          14.0                 2          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let   Vysokoškolské doktorské vzdělání         NaN Moravskoslezský kraj
980448819     3490      3162        1294.0          14.0                 2        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let   Vysokoškolské doktorské vzdělání         muž Moravskoslezský kraj
980448820     2030      3162        1294.0          14.0                 2        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let   Vysokoškolské doktorské vzdělání        žena Moravskoslezský kraj
```

### 150. [C] Sčítání 2021 - Obyvatelstvo podle vzdělání, velikostních skupin obcí a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  vzdelani_cleneni  velikostobce_cis  velikostobce_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                                ukaz_txt vzdelani_txt   velikostobce_txt pohlavi_txt       uzemi_txt
978179474  8832407      3162           NaN           NaN                 0               NaN               NaN          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let          NaN                NaN         NaN Česká republika
980448207      916      3162        1294.0           1.0                 1            1234.0              98.0          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Bez vzdělání    do 199 obyvatel         NaN Česká republika
980447782      463      3162        1294.0           1.0                 1            1234.0              98.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Bez vzdělání    do 199 obyvatel         muž Česká republika
980448231      453      3162        1294.0           1.0                 1            1234.0              98.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Bez vzdělání    do 199 obyvatel        žena Česká republika
980448205     3610      3162        1294.0           1.0                 1            1234.0              99.0          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Bez vzdělání 200 - 499 obyvatel         NaN Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  vzdelani_cleneni  velikostobce_cis  velikostobce_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                                                ukaz_txt                     vzdelani_txt        velikostobce_txt pohlavi_txt            uzemi_txt
980447965      471      3162        1294.0          14.0                 2            1234.0               8.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Vysokoškolské doktorské vzdělání 50000 až 99999 obyvatel         muž Moravskoslezský kraj
980448417      262      3162        1294.0          14.0                 2            1234.0               8.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Vysokoškolské doktorské vzdělání 50000 až 99999 obyvatel        žena Moravskoslezský kraj
980452357     2284      3162        1294.0          14.0                 2            1234.0               9.0          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Vysokoškolské doktorské vzdělání  100000 a více obyvatel         NaN Moravskoslezský kraj
980447959     1441      3162        1294.0          14.0                 2            1234.0               9.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Vysokoškolské doktorské vzdělání  100000 a více obyvatel         muž Moravskoslezský kraj
980448411      843      3162        1294.0          14.0                 2            1234.0               9.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem ve věku 15 a více let Vysokoškolské doktorské vzdělání  100000 a více obyvatel        žena Moravskoslezský kraj
```

### 151. [C] Sčítání 2021 - Obyvatelstvo podle vzdělání, věku a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt vzdelani_txt vek_txt pohlavi_txt       uzemi_txt
987497214     6136      3162          1294             1     1035 1000150015          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem bez vzdělání  15 let         NaN Česká republika
987516921     3517      3162          1294             1     1035 1000150015        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem bez vzdělání  15 let         muž Česká republika
987445083     2619      3162          1294             1     1035 1000150015        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem bez vzdělání  15 let        žena Česká republika
987465226     1227      3162          1294             1     1035 1000160016          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem bez vzdělání  16 let         NaN Česká republika
987446375      733      3162          1294             1     1035 1000160016        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem bez vzdělání  16 let         muž Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                   vzdelani_txt        vek_txt pohlavi_txt            uzemi_txt
987450751        1      3162          5784           121     1035 1000990099        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem úplné střední odborné vzdělání         99 let         muž Moravskoslezský kraj
987509243        2      3162          5784           121     1035 1000990099        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem úplné střední odborné vzdělání         99 let        žena Moravskoslezský kraj
987513618        3      3162          5784           121     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem úplné střední odborné vzdělání 100 a více let         NaN Moravskoslezský kraj
987487958        2      3162          5784           121     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem úplné střední odborné vzdělání 100 a více let         muž Moravskoslezský kraj
987466885        1      3162          5784           121     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem úplné střední odborné vzdělání 100 a více let        žena Moravskoslezský kraj
```

### 152. [C] Sčítání 2021 - Obyvatelstvo podle vzdělání, věku, velikostních skupin obcí a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  vzdelani_cleneni  vek_cis    vek_kod  velikostobce_cis  velikostobce_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt vzdelani_txt     vek_txt velikostobce_txt pohlavi_txt       uzemi_txt
982793118       96      3162          1294             1                 1     1035 1300150019              1234                98          102            1         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez vzdělání 15 - 19 let  do 199 obyvatel         muž Česká republika
982747858       58      3162          1294             1                 1     1035 1300150019              1234                98          102            2         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez vzdělání 15 - 19 let  do 199 obyvatel        žena Česká republika
982749936       25      3162          1294             1                 1     1035 1300200024              1234                98          102            1         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez vzdělání 20 - 24 let  do 199 obyvatel         muž Česká republika
982753537       17      3162          1294             1                 1     1035 1300200024              1234                98          102            2         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez vzdělání 20 - 24 let  do 199 obyvatel        žena Česká republika
982751979       30      3162          1294             1                 1     1035 1300250029              1234                98          102            1         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Bez vzdělání 25 - 29 let  do 199 obyvatel         muž Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vzdelani_cis  vzdelani_kod  vzdelani_cleneni  vek_cis    vek_kod  velikostobce_cis  velikostobce_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                                                  vzdelani_txt       vek_txt       velikostobce_txt pohlavi_txt            uzemi_txt
982801591     3239      3162          5784           132                 1     1035 1300700074              1234                 9          102            2        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Úplné střední (s maturitou), vč. nástavbového a pomaturitního   70 - 74 let 100000 a více obyvatel        žena Moravskoslezský kraj
982777889     1273      3162          5784           132                 1     1035 1300750079              1234                 9          102            1        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Úplné střední (s maturitou), vč. nástavbového a pomaturitního   75 - 79 let 100000 a více obyvatel         muž Moravskoslezský kraj
982740001     2288      3162          5784           132                 1     1035 1300750079              1234                 9          102            2        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Úplné střední (s maturitou), vč. nástavbového a pomaturitního   75 - 79 let 100000 a více obyvatel        žena Moravskoslezský kraj
982738273     1073      3162          5784           132                 1     1035 1200809999              1234                 9          102            1        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Úplné střední (s maturitou), vč. nástavbového a pomaturitního 80 a více let 100000 a více obyvatel         muž Moravskoslezský kraj
982789562     1968      3162          5784           132                 1     1035 1200809999              1234                 9          102            2        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Úplné střední (s maturitou), vč. nástavbového a pomaturitního 80 a více let 100000 a více obyvatel        žena Moravskoslezský kraj
```

### 153. [C] Sčítání 2021 - Obyvatelstvo podle věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  vek_cis      vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt       vek_txt pohlavi_txt       uzemi_txt
947072940 10524167      3162      NaN          NaN          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem           NaN         NaN Česká republika
936989583   866322      3162   1035.0 1100000014.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    0 - 14 let         muž Česká republika
936989586   825438      3162   1035.0 1100000014.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    0 - 14 let        žena Česká republika
936989584   903375      3162   1035.0 1200659999.0        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 65 a více let         muž Česká republika
936989587  1244673      3162   1035.0 1200659999.0        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 65 a více let        žena Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  vek_cis      vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt       vek_txt pohlavi_txt            uzemi_txt
936989652    87758      3162   1035.0 1100000014.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem    0 - 14 let        žena Moravskoslezský kraj
936989650    99471      3162   1035.0 1200659999.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 65 a více let         muž Moravskoslezský kraj
936989653   143640      3162   1035.0 1200659999.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem 65 a více let        žena Moravskoslezský kraj
936989648   378254      3162   1035.0 1300150064.0        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   15 - 64 let         muž Moravskoslezský kraj
936989651   361352      3162   1035.0 1300150064.0        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem   15 - 64 let        žena Moravskoslezský kraj
```

### 154. [C] Sčítání 2021 - Obyvatelstvo podle způsobu bydlení, velikostních skupin obcí a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  bydleni_cis  bydleni_kod  bydleni_cleneni  velikostobce_cis  velikostobce_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                                                  bydleni_txt   velikostobce_txt pohlavi_txt       uzemi_txt
989231321   178204      3162         3335           56                1              1234                98          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)    do 199 obyvatel         NaN Česká republika
989232817    91298      3162         3335           56                1              1234                98        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)    do 199 obyvatel         muž Česká republika
989250187    86906      3162         3335           56                1              1234                98        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)    do 199 obyvatel        žena Česká republika
989248848   654432      3162         3335           56                1              1234                99          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců) 200 - 499 obyvatel         NaN Česká republika
989215560   332373      3162         3335           56                1              1234                99        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců) 200 - 499 obyvatel         muž Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  bydleni_cis  bydleni_kod  bydleni_cleneni  velikostobce_cis  velikostobce_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                    bydleni_txt        velikostobce_txt pohlavi_txt            uzemi_txt
989222413     1606      3162         3335           55                2              1234                 8        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v jiných obydlích 50000 až 99999 obyvatel         muž Moravskoslezský kraj
989187548      597      3162         3335           55                2              1234                 8        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v jiných obydlích 50000 až 99999 obyvatel        žena Moravskoslezský kraj
989164153     5072      3162         3335           55                2              1234                 9          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v jiných obydlích  100000 a více obyvatel         NaN Moravskoslezský kraj
989257279     3821      3162         3335           55                2              1234                 9        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v jiných obydlích  100000 a více obyvatel         muž Moravskoslezský kraj
989187549     1251      3162         3335           55                2              1234                 9        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v jiných obydlích  100000 a více obyvatel        žena Moravskoslezský kraj
```

### 155. [C] Sčítání 2021 - Obyvatelstvo podle způsobu bydlení, věku a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  bydleni_cis  bydleni_kod  bydleni_cleneni  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                                                  bydleni_txt vek_txt pohlavi_txt       uzemi_txt
989214475   109185      3162         3335           56                1     1035 1000000000          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)   0 let         NaN Česká republika
989145591    55778      3162         3335           56                1     1035 1000000000        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)   0 let         muž Česká republika
989214804    53407      3162         3335           56                1     1035 1000000000        102.0          2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)   0 let        žena Česká republika
989179221   110950      3162         3335           56                1     1035 1000010001          NaN          NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)   1 rok         NaN Česká republika
989127848    56820      3162         3335           56                1     1035 1000010001        102.0          1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Obyvatelstvo podle způsobu bydlení celkem (kromě bezdomovců)   1 rok         muž Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  bydleni_cis  bydleni_kod  bydleni_cleneni  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                    bydleni_txt        vek_txt pohlavi_txt            uzemi_txt
989216395        0      3162         3335           55                2     1035 1000990099        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v jiných obydlích         99 let         muž Moravskoslezský kraj
989163748        1      3162         3335           55                2     1035 1000990099        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v jiných obydlích         99 let        žena Moravskoslezský kraj
989154879        0      3162         3335           55                2     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v jiných obydlích 100 a více let         NaN Moravskoslezský kraj
989181515        0      3162         3335           55                2     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v jiných obydlích 100 a více let         muž Moravskoslezský kraj
989198472        0      3162         3335           55                2     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Osoby žijící v jiných obydlích 100 a více let        žena Moravskoslezský kraj
```

### 156. [C] Sčítání 2021 - Zaměstnaní podle odvětví ekonomické činnosti, jednoletých věkových skupin a pohlaví

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  odvetvi_cis odvetvi_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum           ukaz_txt                       odvetvi_txt       vek_txt pohlavi_txt       uzemi_txt uzemi_typ
1093547828   167161      3162         5103           A     1035 1200159999          NaN          NaN         97         19      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství 15 a více let         NaN Česká republika      stát
1093549544   120787      3162         5103           A     1035 1200159999        102.0          1.0         97         19      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství 15 a více let         muž Česká republika      stát
1094149390    46374      3162         5103           A     1035 1200159999        102.0          2.0         97         19      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství 15 a více let        žena Česká republika      stát
1093617536       61      3162         5103           A     1035 1000150015          NaN          NaN         97         19      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství        15 let         NaN Česká republika      stát
1094267937       48      3162         5103           A     1035 1000150015        102.0          1.0         97         19      2021 2021-03-26 Počet zaměstnaných Zemědělství, lesnictví, rybářství        15 let         muž Česká republika      stát
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  odvetvi_cis odvetvi_kod  vek_cis    vek_kod  pohlavi_cis  pohlavi_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum           ukaz_txt odvetvi_txt        vek_txt pohlavi_txt            uzemi_txt uzemi_typ
1093996780        0      3162         5103           X     1035 1000990099        102.0          1.0        100       3140      2021 2021-03-26 Počet zaměstnaných  Nezjištěno         99 let         muž Moravskoslezský kraj      kraj
1094286985        0      3162         5103           X     1035 1000990099        102.0          2.0        100       3140      2021 2021-03-26 Počet zaměstnaných  Nezjištěno         99 let        žena Moravskoslezský kraj      kraj
1094039203        0      3162         5103           X     1035 1201009999          NaN          NaN        100       3140      2021 2021-03-26 Počet zaměstnaných  Nezjištěno 100 a více let         NaN Moravskoslezský kraj      kraj
1094286986        0      3162         5103           X     1035 1201009999        102.0          1.0        100       3140      2021 2021-03-26 Počet zaměstnaných  Nezjištěno 100 a více let         muž Moravskoslezský kraj      kraj
1093567148        0      3162         5103           X     1035 1201009999        102.0          2.0        100       3140      2021 2021-03-26 Počet zaměstnaných  Nezjištěno 100 a více let        žena Moravskoslezský kraj      kraj
```

### 157. [C] Sčítání 2021 - Ženy ve věku 15 a více let podle rodinného stavu, vzdělání, věku a počtu dětí

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
    idhod  hodnota  ukaz_kod  pohlavi_cis  pohlavi_kod  stav_cis  stav_kod  vzdelani_cis  vzdelani_kod  vek_cis    vek_kod  pocet_deti_cis  pocet_deti_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt pohlavi_txt  stav_txt  vzdelani_txt     vek_txt  pocet_deti_txt       uzemi_txt
983095156   238290      3162          102            2       NaN       NaN           NaN           NaN     1035 1300150019             NaN             NaN         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena       NaN           NaN 15 - 19 let             NaN Česká republika
982844265   234041      3162          102            2       NaN       NaN           NaN           NaN     1035 1300150019          7600.0             0.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena       NaN           NaN 15 - 19 let             0.0 Česká republika
982844369     2400      3162          102            2       NaN       NaN           NaN           NaN     1035 1300150019          7600.0             1.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena       NaN           NaN 15 - 19 let             1.0 Česká republika
982879802      322      3162          102            2       NaN       NaN           NaN           NaN     1035 1300150019          7600.0             2.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena       NaN           NaN 15 - 19 let             2.0 Česká republika
983057787       53      3162          102            2       NaN       NaN           NaN           NaN     1035 1300150019          7600.0             3.0         97         19      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena       NaN           NaN 15 - 19 let             3.0 Česká republika
```

#### TAIL

```
    idhod  hodnota  ukaz_kod  pohlavi_cis  pohlavi_kod  stav_cis  stav_kod  vzdelani_cis  vzdelani_kod  vek_cis    vek_kod  pocet_deti_cis  pocet_deti_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt pohlavi_txt stav_txt  vzdelani_txt       vek_txt pocet_deti_txt            uzemi_txt
982841613        0      3162          102            2    5798.0       2.0        5784.0         109.0     1035 1200809999          7600.0             7.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena    Vdaná Vysokoškolské 80 a více let              7 Moravskoslezský kraj
983019193        0      3162          102            2    5798.0       2.0        5784.0         109.0     1035 1200809999          7600.0             8.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena    Vdaná Vysokoškolské 80 a více let              8 Moravskoslezský kraj
982911448        0      3162          102            2    5798.0       2.0        5784.0         109.0     1035 1200809999          7600.0             9.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena    Vdaná Vysokoškolské 80 a více let              9 Moravskoslezský kraj
983090603        0      3162          102            2    5798.0       2.0        5784.0         109.0     1035 1200809999          7601.0        109999.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena    Vdaná Vysokoškolské 80 a více let      10 a více Moravskoslezský kraj
982911991        8      3162          102            2    5798.0       2.0        5784.0         109.0     1035 1200809999          5768.0             9.0        100       3140      2021 2021-03-26 Počet obyvatel s obvyklým pobytem        žena    Vdaná Vysokoškolské 80 a více let     Nezjištěno Moravskoslezský kraj
```

### 158. [C] Obyvatelstvo podle jednotek věku a pohlaví - rok 2022

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis      vek_kod  uzemi_cis  uzemi_kod     obdobi  pohlavi_txt  vek_txt          uzemi_txt uzemi_typ
1119722047  1357326        2406          NaN          NaN      NaN          NaN        100       3018 2022-12-31          NaN      NaN Hlavní město Praha      kraj
1121688816    13565        2406          NaN          NaN   7700.0 4.000006e+14        100       3018 2022-12-31          NaN      0.0 Hlavní město Praha      kraj
1121688916    15701        2406          NaN          NaN   7700.0 4.000016e+14        100       3018 2022-12-31          NaN      1.0 Hlavní město Praha      kraj
1121689016    14125        2406          NaN          NaN   7700.0 4.000026e+14        100       3018 2022-12-31          NaN      2.0 Hlavní město Praha      kraj
1121689116    14459        2406          NaN          NaN   7700.0 4.000036e+14        100       3018 2022-12-31          NaN      3.0 Hlavní město Praha      kraj
```

#### TAIL

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis      vek_kod  uzemi_cis  uzemi_kod     obdobi pohlavi_txt  vek_txt       uzemi_txt uzemi_typ
1121688307     2054        2406        102.0          2.0   7700.0 4.100966e+14         97         19 2022-12-31        žena     96.0 Česká republika      stát
1121688407     1394        2406        102.0          2.0   7700.0 4.100976e+14         97         19 2022-12-31        žena     97.0 Česká republika      stát
1121688507      923        2406        102.0          2.0   7700.0 4.100986e+14         97         19 2022-12-31        žena     98.0 Česká republika      stát
1121688607      617        2406        102.0          2.0   7700.0 4.100996e+14         97         19 2022-12-31        žena     99.0 Česká republika      stát
1121688707      696        2406        102.0          2.0   7700.0 4.201008e+14         97         19 2022-12-31        žena    100.0 Česká republika      stát
```

### 159. [C] Obyvatelstvo podle jednotek věku a pohlaví - rok 2023

                        hodnota
polozka                        
target_years_present       2023
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis      vek_kod  uzemi_cis  uzemi_kod     obdobi  pohlavi_txt  vek_txt          uzemi_txt uzemi_typ
1286408928  1384732        2406          NaN          NaN      NaN          NaN        100       3018 2023-12-31          NaN      NaN Hlavní město Praha      kraj
1284319375    12586        2406          NaN          NaN   7700.0 4.000006e+14        100       3018 2023-12-31          NaN      0.0 Hlavní město Praha      kraj
1284269706    13722        2406          NaN          NaN   7700.0 4.000016e+14        100       3018 2023-12-31          NaN      1.0 Hlavní město Praha      kraj
1284358398    15702        2406          NaN          NaN   7700.0 4.000026e+14        100       3018 2023-12-31          NaN      2.0 Hlavní město Praha      kraj
1284259038    14172        2406          NaN          NaN   7700.0 4.000036e+14        100       3018 2023-12-31          NaN      3.0 Hlavní město Praha      kraj
```

#### TAIL

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis      vek_kod  uzemi_cis  uzemi_kod     obdobi pohlavi_txt  vek_txt       uzemi_txt uzemi_typ
1284233115     2083        2406        102.0          2.0   7700.0 4.100966e+14         97         19 2023-12-31        žena     96.0 Česká republika      stát
1284292696     1453        2406        102.0          2.0   7700.0 4.100976e+14         97         19 2023-12-31        žena     97.0 Česká republika      stát
1284400520      970        2406        102.0          2.0   7700.0 4.100986e+14         97         19 2023-12-31        žena     98.0 Česká republika      stát
1284384407      603        2406        102.0          2.0   7700.0 4.100996e+14         97         19 2023-12-31        žena     99.0 Česká republika      stát
1284363602      794        2406        102.0          2.0   7700.0 4.201008e+14         97         19 2023-12-31        žena    100.0 Česká republika      stát
```

### 160. [C] Obyvatelstvo podle jednotek věku a pohlaví - rok 2024

                        hodnota
polozka                        
target_years_present       2024
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis      vek_kod  uzemi_cis  uzemi_kod     obdobi  pohlavi_txt  vek_txt          uzemi_txt uzemi_typ
1446328288  1397880        2406          NaN          NaN      NaN          NaN        100       3018 2024-12-31          NaN      NaN Hlavní město Praha      kraj
1446020251    12083        2406          NaN          NaN   7700.0 4.000006e+14        100       3018 2024-12-31          NaN      0.0 Hlavní město Praha      kraj
1446058963    12716        2406          NaN          NaN   7700.0 4.000016e+14        100       3018 2024-12-31          NaN      1.0 Hlavní město Praha      kraj
1445962976    13675        2406          NaN          NaN   7700.0 4.000026e+14        100       3018 2024-12-31          NaN      2.0 Hlavní město Praha      kraj
1446063539    15577        2406          NaN          NaN   7700.0 4.000036e+14        100       3018 2024-12-31          NaN      3.0 Hlavní město Praha      kraj
```

#### TAIL

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis      vek_kod  uzemi_cis  uzemi_kod     obdobi pohlavi_txt  vek_txt       uzemi_txt uzemi_typ
1446093575     2303        2406        102.0          2.0   7700.0 4.100966e+14         97         19 2024-12-31        žena     96.0 Česká republika      stát
1446176020     1479        2406        102.0          2.0   7700.0 4.100976e+14         97         19 2024-12-31        žena     97.0 Česká republika      stát
1446075580     1004        2406        102.0          2.0   7700.0 4.100986e+14         97         19 2024-12-31        žena     98.0 Česká republika      stát
1446174708      655        2406        102.0          2.0   7700.0 4.100996e+14         97         19 2024-12-31        žena     99.0 Česká republika      stát
1446093577      848        2406        102.0          2.0   7700.0 4.201008e+14         97         19 2024-12-31        žena    100.0 Česká republika      stát
```

## Kategorie D

### 161. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - číselník volebních krajů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VOLKRAJ   NAZVOLKRAJ  KRAJ  MAXKAND
       1 Hl. m. Praha  1100       36
       2  Středočeský  2100       34
       3    Jihočeský  3100       22
       4     Plzeňský  3200       20
       5  Karlovarský  4100       14
```

#### TAIL

```
 VOLKRAJ      NAZVOLKRAJ  KRAJ  MAXKAND
      10        Vysočina  6100       20
      11    Jihomoravský  6200       34
      12       Olomoucký  7100       23
      13         Zlínský  7200       22
      14 Moravskoslezský  8100       36
```

### 162. [D] Volby do zastupitelstev krajů 2020 - okrsková data

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KSTRANA  POC_HLASU  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  HLASY_23  HLASY_24  HLASY_25  HLASY_26  HLASY_27  HLASY_28  HLASY_29  HLASY_30  HLASY_31  HLASY_32  HLASY_33  HLASY_34  HLASY_35  HLASY_36  HLASY_37  HLASY_38  HLASY_39  HLASY_40  HLASY_41  HLASY_42  HLASY_43  HLASY_44  HLASY_45  HLASY_46  HLASY_47  HLASY_48  HLASY_49  HLASY_50  HLASY_51  HLASY_52  HLASY_53  HLASY_54  HLASY_55  HLASY_56  HLASY_57  HLASY_58  HLASY_59  HLASY_60  HLASY_61  HLASY_62  HLASY_63  HLASY_64  HLASY_65  HLASY_66  HLASY_67  HLASY_68  HLASY_69  HLASY_70  KC_3  KC_4  KC_5  POSL_KAND  KC_SUM
         1         2       0      0   7204 500011       1     6        5          1     6         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     0     6          0  507236
         1         2       0      0   7204 500011       1     6        6         33    39         6         2         2         2         1         1         1         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   120     0   159         44  507586
         1         2       0      0   7204 500011       1     6        7         39    46         6         5         3         1         2         0         0         2         0         0         0         0         0         0         1         0         1         0         0         0         0         2         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         1         3         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   173   199   418         50  508110
         1         2       0      0   7204 500011       1     6       12         22    34         8         0         1         0         7         1         0         2         1         2         0         1         1         0         0         6         0         0         2         0         1         0         0         0         0         1         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   330     0   364         27  507979
         1         2       0      0   7204 500011       1     6       16         24    40         2         0         0         2         0         0         1         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   110     0   150         44  507568
```

#### TAIL

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KSTRANA  POC_HLASU  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  HLASY_23  HLASY_24  HLASY_25  HLASY_26  HLASY_27  HLASY_28  HLASY_29  HLASY_30  HLASY_31  HLASY_32  HLASY_33  HLASY_34  HLASY_35  HLASY_36  HLASY_37  HLASY_38  HLASY_39  HLASY_40  HLASY_41  HLASY_42  HLASY_43  HLASY_44  HLASY_45  HLASY_46  HLASY_47  HLASY_48  HLASY_49  HLASY_50  HLASY_51  HLASY_52  HLASY_53  HLASY_54  HLASY_55  HLASY_56  HLASY_57  HLASY_58  HLASY_59  HLASY_60  HLASY_61  HLASY_62  HLASY_63  HLASY_64  HLASY_65  HLASY_66  HLASY_67  HLASY_68  HLASY_69  HLASY_70  KC_3  KC_4  KC_5  POSL_KAND  KC_SUM
     13656         2       0      0   8104 599999       2     0       54         32    86         0         0         4         0         1         0         0         0         0         0         9         1         0         0         3         1         0         1         1         0         0         0         0         0         2         0         0         0         0         0         2         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   371    49   506         49  609168
     13656         2       0      0   8104 599999       2     0       63         24    87         1         2         3         2         1         0         0         0         0         2         0         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   102    55   244         55  608650
     13656         2       0      0   8104 599999       2     0       70         14    84         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     0    84          0  608275
     13656         2       0      0   8104 599999       2     0       79          3    82         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     9     0    91          9  608298
     13656         2       0      0   8104 599999       2     0       81          7    88         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     0    88          0  608283
```

### 163. [D] Volby do zastupitelstev krajů 2020 - číselníky

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRAJ  OKRES  CPOU  ORP   OBEC                NAZEVOBCE  KRZAST  MINOKRSEK1  MAXOKRSEK1  OBEC_PREZ
 7200   7204   662 7213 500011 Želechovice nad Dřevnicí      12           1           3     500011
 7100   7105   860 7111 500020        Petrov nad Desnou      11           1           2     500020
 8100   8104   792 8115 500046                  Libhošť      13           1           1     500046
 7200   7203   871 7210 500062                   Krhová      12           1           1     500062
 7200   7203   871 7210 500071                  Poličná      12           1           1     500071
```

#### TAIL

```
 KRAJ  OKRES  CPOU  ORP   OBEC         NAZEVOBCE  KRZAST  MINOKRSEK1  MAXOKRSEK1  OBEC_PREZ
 8100   8104   792 8115 599930 Suchdol nad Odrou      13           1           2     599930
 8100   8104   791 8112 599948         Štramberk      13           1           4     599948
 8100   8104   789 8105 599956             Tichá      13           1           1     599956
 8100   8104   788 8101 599964             Tísek      13           1           1     599964
 8100   8104   789 8105 599999       Trojanovice      13           1           2     599999
```

### 164. [D] Volby do zastupitelstev krajů 2024 - Příloha č.1 k tiskopisu T/6 (strany, kandidáti)

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KSTRANA  POC_HLASU  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  HLASY_23  HLASY_24  HLASY_25  HLASY_26  HLASY_27  HLASY_28  HLASY_29  HLASY_30  HLASY_31  HLASY_32  HLASY_33  HLASY_34  HLASY_35  HLASY_36  HLASY_37  HLASY_38  HLASY_39  HLASY_40  HLASY_41  HLASY_42  HLASY_43  HLASY_44  HLASY_45  HLASY_46  HLASY_47  HLASY_48  HLASY_49  HLASY_50  HLASY_51  HLASY_52  HLASY_53  HLASY_54  HLASY_55  HLASY_56  HLASY_57  HLASY_58  HLASY_59  HLASY_60  HLASY_61  HLASY_62  HLASY_63  HLASY_64  HLASY_65  HLASY_66  HLASY_67  HLASY_68  HLASY_69  HLASY_70  KC_3  KC_4  KC_5  POSL_KAND  KC_SUM
         1         2       0      0   7204 500011       1     6       15          3    18         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     0    18          0  507260
         1         2       0      0   7204 500011       1     6       18         10    28         2         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     7     0    35          5  507299
         1         2       0      0   7204 500011       1     6       21          7    28         1         0         0         1         0         0         0         0         0         0         0         0         0         1         1         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    58     0    86         24  507420
         1         2       0      0   7204 500011       1     6       30          1    31         0         1         0         0         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    38     0    69         21  507383
         1         2       0      0   7204 500011       1     6       39         98   137        23         4         9         0         4         0         0         0         0         0         0         0         0         0         0         0         9         0         0         0         0         0         0         0         1         0         0         0         0         0         0         1         0         0         0         0         4         0         0         0         0         0         0         0         9         0         4         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   841   237  1215         49  509703
```

#### TAIL

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KSTRANA  POC_HLASU  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  HLASY_23  HLASY_24  HLASY_25  HLASY_26  HLASY_27  HLASY_28  HLASY_29  HLASY_30  HLASY_31  HLASY_32  HLASY_33  HLASY_34  HLASY_35  HLASY_36  HLASY_37  HLASY_38  HLASY_39  HLASY_40  HLASY_41  HLASY_42  HLASY_43  HLASY_44  HLASY_45  HLASY_46  HLASY_47  HLASY_48  HLASY_49  HLASY_50  HLASY_51  HLASY_52  HLASY_53  HLASY_54  HLASY_55  HLASY_56  HLASY_57  HLASY_58  HLASY_59  HLASY_60  HLASY_61  HLASY_62  HLASY_63  HLASY_64  HLASY_65  HLASY_66  HLASY_67  HLASY_68  HLASY_69  HLASY_70  KC_3  KC_4  KC_5  POSL_KAND  KC_SUM
     13591         2       0      0   8104 599999       2     0       70          2    72         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     0    72          0  608251
     13591         2       0      0   8104 599999       2     0       76          1    77         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     0    77          0  608261
     13591         2       0      0   8104 599999       2     0       77         26   103         1         2         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    51     0   154         36  608451
     13591         2       0      0   8104 599999       2     0       88         84   172         5         7         0        12         2         3         2         2         2         1         0         2         0         1         1         0         1         1         0         0         0         0         0         0         1         0         1         0         0         0         0         0         0         5         0         0         0         4         0         0         0         0         0         0         0         0         0         0         1         0         0         1         0         0         0         0         2         0         0         0         0         0         0         0         0         0         0         0         0         0   615   215  1002         57  610168
     13591         2       0      0   8104 599999       2     0       95          1    96         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     0    96          0  608299
```

### 165. [D] Volby do zastupitelstev krajů 2024 - registr kandidátních listin

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRZAST  KSTRANA  VSTRANA                                      NAZEVCELK                                     NAZEV_STRK             ZKRATKAK30       ZKRATKAK8  POCSTRVKO        SLOZENI  STAVREG PLAT_STR  SLOZNEPLAT
      1        7     1639                           SPD, Trikolora a PRO                           SPD, Trikolora a PRO   SPD, Trikolora a PRO  SPD+Trikol+PRO          3 1114,1227,1265        0        A         NaN
      1       14     1449                                Zelení a SEN 21                                Zelení a SEN 21        Zelení a SEN 21   Zelení+SEN 21          2       005,1187        0        A         NaN
      1       15      715 Demokratická strana zelených - ZA PRÁVA ZVÍŘAT Demokratická strana zelených - ZA PRÁVA ZVÍŘAT  DSZ - ZA PRÁVA ZVÍŘAT DSZ-ZA PR.ZVÍŘ.          1            715        0        A         NaN
      1       16     1245                         PŘÍSAHA občanské hnutí                         PŘÍSAHA občanské hnutí PŘÍSAHA občanské hnutí         PŘÍSAHA          1           1245        0        A         NaN
      1       21      720                          Česká pirátská strana                          Česká pirátská strana  Česká pirátská strana          Piráti          1            720        0        A         NaN
```

#### TAIL

```
 KRZAST  KSTRANA  VSTRANA                                                                           NAZEVCELK                                         NAZEV_STRK                    ZKRATKAK30      ZKRATKAK8  POCSTRVKO     SLOZENI  STAVREG PLAT_STR  SLOZNEPLAT
     13       70        7                                                                 Sociální demokracie                                Sociální demokracie           Sociální demokracie         SOCDEM          1         007        0        A         NaN
     13       76      752                                  Švýcarská demokracie (www.svycarska-demokracie.cz) Švýcarská demokracie (www.svycarska-demokracie.cz)          Švýcarská demokracie Švýcarská dem.          1         752        0        A         NaN
     13       77     1642 STAČILO!, koalice Komunistické strany Čech a Moravy a České strany národně sociální                      STAČILO!, koalice KSČM a ČSNS STAČILO!, koalice KSČM a ČSNS      ČSNS+KSČM          2     002,047        0        A         NaN
     13       88     1327                                                                           SPOLU MSK                                          SPOLU MSK                     SPOLU MSK KDU+ODS+TOP 09          3 001,053,721        0        A         NaN
     13       95     1512                                                          ČSSD A NEZÁVISLÉ OSOBNOSTI                         ČSSD A NEZÁVISLÉ OSOBNOSTI    ČSSD A NEZÁVISLÉ OSOBNOSTI     ČSSD+DOMOV          2    759,1221        0        A         NaN
```

### 166. [D] Volby do zastupitelstev krajů 2024 - registr kandidátů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRZAST  KSTRANA  PORCISLO   JMENO PRIJMENI TITULPRED TITULZA  VEK                                                                                  POVOLANI BYDLISTEN  PSTRANA  NSTRANA PLATNOST  POCHLASU  POCPROC MANDAT  PORADIMAND  PORADINAHR
      1        7         1    Jiří    Kobza      Mgr.     NaN   68                                                                        poslanec, diplomat    Petrov     1114     1114        A      1807     9.56      A         1.0         NaN
      1        7         2   Tomáš  Doležal Ing. Mgr.     NaN   51 ekonom, politolog, odborný mluvčí SPD pro oblast sociální politiky, člen spolku Svatopluk  Kamenice     1114     1114        A      1011     5.35      A         2.0         NaN
      1        7         3 Oldřich    Černý       NaN     NaN   59                                                         poslanec, zastupitel města Kladno    Kladno     1114     1114        A       387     2.04      A         3.0         NaN
      1        7         4    Jiří  Novotný      Mgr.     NaN   48                                             bezpečnostní expert, zastupitel města Příbram   Příbram     1114     1114        A       466     2.46      A         4.0         NaN
      1        7         5  Václav    Bošek      Mgr.     MBA   47                                    živnostník, obchodní zástupce, zastupitel města Kladno    Kladno     1114     1114        A       240     1.27      N         NaN         1.0
```

#### TAIL

```
 KRZAST  KSTRANA  PORCISLO    JMENO PRIJMENI  TITULPRED TITULZA  VEK                                          POVOLANI      BYDLISTEN  PSTRANA  NSTRANA PLATNOST  POCHLASU  POCPROC MANDAT  PORADIMAND  PORADINAHR
     13       95        66    Robin     Król        NaN    DiS.   24                                        student VŠ       Rychvald       99      759        A         9     0.50      N         0.0         0.0
     13       95        67  Martina Jarošová        NaN     NaN   31                                   operátor výroby Nové Heřminovy       99      759        A         9     0.50      N         0.0         0.0
     13       95        68    Pavel  Jelínek        NaN    DiS.   39                                              OSVČ        Karviná       99      759        A         6     0.33      N         0.0         0.0
     13       95        69   Martin     Braš        NaN     NaN   26                                    elektrotechnik        Ostrava       99      759        A         6     0.33      N         0.0         0.0
     13       95        70 Miroslav  Demeter        NaN     NaN   57 majitel agentury MARCO, organizátor akcí pro děti        Ostrava      759      759        A         6     0.33      N         0.0         0.0
```

### 167. [D] Volby do zastupitelstev krajů 2024 - složení registru kandidátních listin

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KSTRANA TYPSLOZENI  NSTRANA
       1          P      714
       1          P      716
       2          P      766
       3          P       53
       3          P      721
```

#### TAIL

```
 KSTRANA TYPSLOZENI  NSTRANA
      93          P        1
      93          P     1014
      94          P      121
      95          P      759
      95          P     1221
```

### 168. [D] Volby do zastupitelstev krajů 2024 - složení číselníku volebních stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA  NSTRANA
       1        1
       2        2
       3        3
       4        4
       5        5
```

#### TAIL

```
 VSTRANA  NSTRANA
    1679     1285
    1680      143
    1680     1228
    9995     9995
    9999     9999
```

### 169. [D] Volby do zastupitelstev krajů 2024 - souhrnný registr kandidátních listin (ČR)

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KSTRANA  VSTRANA                                                       NAZEVCELK                                       NAZEV_STRK                     ZKRATKAK30       ZKRATKAK8  POCSTRVKO       SLOZENI       STAVREG PLAT_STR  SLOZNEPLAT  POCMANDCR                                                       NAZEVPLNY
       1     1141                                        SPOLU PRO Liberecký kraj                         SPOLU PRO Liberecký kraj       SPOLU PRO Liberecký kraj  Svobod+Soukrom          2       714,716 2222202222222        A         NaN        0.0                                        SPOLU PRO Liberecký kraj
       2      766                                                   JIHOČEŠI 2012                                    JIHOČEŠI 2012                  JIHOČEŠI 2012          JIH 12          1           766 2022222222222        A         NaN        0.0                                                   JIHOČEŠI 2012
       3     1637                                 Společně se Starosty pro občany                  Společně se Starosty pro občany Společně se Starosty p. občany  ODS+TOP 09+STO          3   053,721,779 2222222202222        A         NaN       11.0                                 Společně se Starosty pro občany
       4     1663                                               ČSSD – ČISTÝ KRAJ                                ČSSD – ČISTÝ KRAJ              ČSSD – ČISTÝ KRAJ       ČSSD+ČiKR          2      759,1021 2222022222222        A         NaN        0.0                                               ČSSD – ČISTÝ KRAJ
       5     1669 HLAS samospráv – pro spravedlivý rozvoj Královéhradeckého kraje HLAS samospráv – pro spravedlivý rozvoj HK kraje                 HLAS samospráv SOCDEM+SproK+RH          3 007,1228,1267 2222220222222        A         NaN        3.0 HLAS samospráv – pro spravedlivý rozvoj Královéhradeckého kraje
```

#### TAIL

```
 KSTRANA  VSTRANA                                                                                                                NAZEVCELK                                    NAZEV_STRK                     ZKRATKAK30       ZKRATKAK8  POCSTRVKO      SLOZENI       STAVREG PLAT_STR  SLOZNEPLAT  POCMANDCR                                                                                                                                                                                                          NAZEVPLNY
      91     1118                                                                                                           Volba pro kraj                                Volba pro kraj                 Volba pro kraj             VOK          1         1118 2220222222222        A         NaN        3.0                                                                                                                                                                                                     Volba pro kraj
      92     1654                                                                                   3PK - Pro prosperující Pardubický kraj        3PK - Pro prosperující Pardubický kraj 3PK-Pro prosperující Pard. kr. SOCDEM+VČ+SproK          3 007,770,1228 2222222022222        A         NaN       11.0                                                                                                                                                                             3PK - Pro prosperující Pardubický kraj
      93     1661                                PRO NÁŠ KRAJ – PRO PLZEŇ a KDU-ČSL s podporou Svobodných, agrárníků, starostů a sportovců PRO NÁŠ KRAJ – PRO PLZEŇ a KDU-ČSL s podporou PRO NÁŠ KRAJ–PRO PLZEŇ,KDU-ČSL KDUČSL+PROPLZEŇ          2     001,1014 2202222222222        A         NaN        4.0                                                                                                                          PRO NÁŠ KRAJ – PRO PLZEŇ a KDU-ČSL s podporou Svobodných, agrárníků, starostů a sportovců
      94      121 LEPŠÍ ŽIVOT PRO LIDI-min.mzda 70.000 Kč,min.důchod 50.000 Kč,ceny energií 2019,v obchodech zboží nej. kvality,STOP válce                          LEPŠÍ ŽIVOT PRO LIDI           LEPŠÍ ŽIVOT PRO LIDI            LŽPL          1          121  202222222222        A         NaN        0.0 LEPŠÍ ŽIVOT PRO LIDI - min. mzda 70.000 Kč, min. důchod 50.000 Kč, návrat cen energií na ceny z roku 2019, v obchodech zboží nejvyšší kvality za ceny dostupné pro každého, zrušení daně z nemovitostí, STOP válce
      95     1512                                                                                               ČSSD A NEZÁVISLÉ OSOBNOSTI                    ČSSD A NEZÁVISLÉ OSOBNOSTI     ČSSD A NEZÁVISLÉ OSOBNOSTI      ČSSD+DOMOV          2     759,1221 2222222222220        A         NaN        0.0                                                                                                                                                                                         ČSSD A NEZÁVISLÉ OSOBNOSTI
```

### 170. [D] Volby do zastupitelstev krajů 2024 - tiskopisy T/6 (okrsky)

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2                                                                                          ZAKRSTRANA
         1         1       0      0   7204 500011       1     6         718         271         270         267  1526 000000000000001001001000000001000000001000000000000000100000000000001100000100101001100000000000000
         2         1       0      0   7204 500011       2     0         415         143         143         143   844 000000000000000001001000000001000000001000000000000000100000000000001100000000101000100000000000000
         3         1       0      0   7204 500011       3     1         407         125         125         125   782 000000000000000001001000000010100000001000000000000000000000000000001100000000101001100000000000000
         4         1       0      0   7105 500020       1     2         272          83          83          79   517 000000000100001100000000000000000000001000000001000100000000001000000000000000000000100000000000000
         5         1       0      0   7105 500020       2     3         742         196         196         193  1327 000000000100001110000000000000000000001000000001001100000101001000000000000000000000100000000000000
```

#### TAIL

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2                                                                                          ZAKRSTRANA
     13587         1       0      0   8104 599948       4     6         714         262         262         262  1500 000000100000001100001010000100000000001000000000000000000001000000000100000110000000000100000000000
     13588         1       0      0   8104 599956       1     1        1519         588         588         586  3281 000000100000000100001000000100000000001000000000000000000001000000000100000110000000000100000010000
     13589         1       0      0   8104 599964       1     6         763         271         271         271  1576 000000100000000100001010000100000000001000000000000000000001000000000100000110000000000100000010000
     13590         1       0      0   8104 599999       1     6         489         161         161         159   970 000000100000001100001010000100000000001000000000000000000001000000000000000110000000000100000000000
     13591         1       0      0   8104 599999       2     0        1620         553         553         548  3274 000000100000001100001010000100000000001000000000000000000001000000000100000110000000000100000010000
```

### 171. [D] Volby do zastupitelstev krajů 2024 - číselník obcí, městských částí, městských obvodů a volebních okrsků

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRAJ  OKRES  CPOU  ORP   OBEC                NAZEVOBCE  KRZAST  MINOKRSEK1  MAXOKRSEK1  OBEC_PREZ
 7200   7204   662 7213 500011 Želechovice nad Dřevnicí      12           1           3     500011
 7100   7105   860 7111 500020        Petrov nad Desnou      11           1           2     500020
 8100   8104   792 8115 500046                  Libhošť      13           1           1     500046
 7200   7203   871 7210 500062                   Krhová      12           1           1     500062
 7200   7203   871 7210 500071                  Poličná      12           1           1     500071
```

#### TAIL

```
 KRAJ  OKRES  CPOU  ORP   OBEC         NAZEVOBCE  KRZAST  MINOKRSEK1  MAXOKRSEK1  OBEC_PREZ
 8100   8104   792 8115 599930 Suchdol nad Odrou      13           1           2     599930
 8100   8104   791 8112 599948         Štramberk      13           1           4     599948
 8100   8104   789 8105 599956             Tichá      13           1           1     599956
 8100   8104   788 8101 599964             Tísek      13           1           1     599964
 8100   8104   789 8105 599999       Trojanovice      13           1           2     599999
```

### 172. [D] Volby do zastupitelstev krajů 2024 - číselník politické příslušnosti kandidátů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 PSTRANA                    NAZEV_STRP                    ZKRATKAP30 ZKRATKAP8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
       9    Nezávislá iniciativa (NEI)    Nezávislá iniciativa (NEI)       NEI
```

#### TAIL

```
 PSTRANA                                        NAZEV_STRP                    ZKRATKAP30       ZKRATKAP8
    1291                                    Hnutí Generace                Hnutí Generace        Generace
    1292                     MÁ VLAST ČECHY MORAVA SLEZSKO MÁ VLAST ČECHY MORAVA SLEZSKO    MÁ VLAST ČMS
    1293            Nadační občansko-politické hnutí ReMeK Nadační obč.-pol. hnutí ReMeK           ReMeK
    1294 Nestraníci pro jižní Moravu-www.nestranici2024.cz   Nestraníci pro jižní Moravu  Nestranici2024
    9999                               Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 173. [D] Volby do zastupitelstev krajů 2024 - číselník volebních stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA                     NAZEVCELK                    NAZEV_STRV                    ZKRATKAV30 ZKRATKAV8  POCSTR_SLO  SLOZENI ZKRATKA_OF TYPVS  PLNYNAZEV
       1                       KDU-ČSL                       KDU-ČSL                       KDU-ČSL   KDU-ČSL           1        1    KDU-ČSL     S        NaN
       2 Česká strana národně sociální Česká strana národně sociální Česká strana národně sociální      ČSNS           1        2       ČSNS     S        NaN
       3 Křesťanskodemokratická strana Křesťanskodemokratická strana Křesťanskodemokratická strana       KDS           1        3        KDS     S        NaN
       4 Liberálně demokratická strana Liberálně demokratická strana Liberálně demokratická strana       LDS           1        4        LDS     S        NaN
       5               Strana zelených               Strana zelených               Strana zelených    Zelení           1        5     Zelení     S        NaN
```

#### TAIL

```
 VSTRANA             NAZEVCELK            NAZEV_STRV            ZKRATKAV30       ZKRATKAV8  POCSTR_SLO  SLOZENI          ZKRATKA_OF TYPVS  PLNYNAZEV
    1678  Koalice Piráti a MHS  Koalice Piráti a MHS   Koalice Piráti, MHS      Piráti+MHS           2 720,1194                 NaN     K        NaN
    1679 Sdružení Vize KVK, NK Sdružení Vize KVK, NK Sdružení Vize KVK, NK     Vize KVK+NK           2 080,1285                 NaN     D        NaN
    1680 Koalice SD-SN a SproK Koalice SD-SN a SproK  Koalice SD-SN, SproK     SD-SN+SproK           2 143,1228                 NaN     K        NaN
    9995               Koalice               Koalice               Koalice         Koalice           1     9995             koalice     S        NaN
    9999   Neregistrováno u MV   Neregistrováno u MV   Neregistrováno u MV Neregistr. u MV           1     9999 Neregistrováno u MV     S        NaN
```

### 174. [D] Volby do zastupitelstev krajů 2024 - číselník zastupitelstev v krajích

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRZAST    NAZEVKRZ  MANDATYKRZ  KRAJ
      1 Středočeský          65  2100
      2   Jihočeský          55  3100
      3    Plzeňský          55  3200
      4 Karlovarský          45  4100
      5     Ústecký          55  4200
```

#### TAIL

```
 KRZAST        NAZEVKRZ  MANDATYKRZ  KRAJ
      9        Vysočina          45  6100
     10    Jihomoravský          65  6200
     11       Olomoucký          55  7100
     12         Zlínský          45  7200
     13 Moravskoslezský          65  8100
```

## Kategorie A

### 175. [A] Úmrtnostní tabulky pro regiony soudržnosti

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis         vek_kod  vuzemi_cis  vuzemi_kod  casref_od  casref_do          stapro_txt pohlavi_txt  vek_txt vuzemi_txt
1287897762 0.001659        8817          102            1     7700 400000600001000          99         213 2023-01-01 2023-12-31 Míra úmrtnosti (mx)         muž        0      Praha
1287712335 0.000488        8817          102            1     7700 400001600002000          99         213 2023-01-01 2023-12-31 Míra úmrtnosti (mx)         muž        1      Praha
1287449159 0.000209        8817          102            1     7700 400002600003000          99         213 2023-01-01 2023-12-31 Míra úmrtnosti (mx)         muž        2      Praha
1287863473 0.000114        8817          102            1     7700 400003600004000          99         213 2023-01-01 2023-12-31 Míra úmrtnosti (mx)         muž        3      Praha
1287835284 0.000080        8817          102            1     7700 400004600005000          99         213 2023-01-01 2023-12-31 Míra úmrtnosti (mx)         muž        4      Praha
```

#### TAIL

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis         vek_kod  vuzemi_cis  vuzemi_kod  casref_od  casref_do                    stapro_txt pohlavi_txt  vek_txt      vuzemi_txt
1455247144    903.0        7193          102            2     7700 420101620102000          99         281 2024-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      101 Moravskoslezsko
1455098017    544.0        7193          102            2     7700 420102620103000          99         281 2024-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      102 Moravskoslezsko
1455247187    315.0        7193          102            2     7700 420103620104000          99         281 2024-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      103 Moravskoslezsko
1455174307    176.0        7193          102            2     7700 420104620105000          99         281 2024-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      104 Moravskoslezsko
1448830664    198.0        7193          102            2     7700 420105620106000          99         281 2024-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      105 Moravskoslezsko
```

### 176. [A] Pracovní neschopnost pro nemoc a úraz podle okresů a krajů

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod    hodnota duvernost  stapro_kod  spjmen_cis spjmen_kod  rok  uzemi_cis  uzemi_kod       uzemi_txt                                                stapro_txt                                            spjmen_txt  mesic
1179401782 4751976.00   verejny        3126         NaN        NaN 2023         97         19 Česká republika                Průměrný počet nemocensky pojištěných osob                                                   NaN      6
1286663462 4766867.00   verejny        3126         NaN        NaN 2023         97         19 Česká republika                Průměrný počet nemocensky pojištěných osob                                                   NaN     12
1457982861 4764802.00   verejny        3126         NaN        NaN 2024         97         19 Česká republika                Průměrný počet nemocensky pojištěných osob                                                   NaN     12
1179416638 1327877.00   verejny        3136         NaN        NaN 2023         97         19 Česká republika Počet nově hlášených případů pracovní neschopnosti celkem                                                   NaN      6
1179385250      27.94   verejny        3136      7605.0        HAX 2023         97         19 Česká republika Počet nově hlášených případů pracovní neschopnosti celkem průměrný počet nemocensky pojištěných osob (100 osob)      6
```

#### TAIL

```
     idhod      hodnota duvernost  stapro_kod  spjmen_cis spjmen_kod  rok  uzemi_cis  uzemi_kod       uzemi_txt                              stapro_txt                                            spjmen_txt  mesic
1457982904 78482115.000   verejny        3605         NaN        NaN 2024         97         19 Česká republika     Doba pracovní neschopnosti - celkem                                                   NaN     12
1457981566       31.700   verejny        3605      7605.0        HNX 2024         97         19 Česká republika     Doba pracovní neschopnosti - celkem             nově hlášený případ pracovní neschopnosti     12
1179377050        4.931   verejny        6049      7605.0        HAX 2023         97         19 Česká republika Průměrné procento pracovní neschopnosti průměrný počet nemocensky pojištěných osob (100 osob)      6
1286652142        4.573   verejny        6049      7605.0        HAX 2023         97         19 Česká republika Průměrné procento pracovní neschopnosti průměrný počet nemocensky pojištěných osob (100 osob)     12
1457928320        4.500   verejny        6049      7605.0        HAX 2024         97         19 Česká republika Průměrné procento pracovní neschopnosti průměrný počet nemocensky pojištěných osob (100 osob)     12
```

### 177. [A] Stavy turů a prasat

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  druhzvire_cis  druhzvire_kod  vek_cis  vek_kod  vekmes_cis  vekmes_kod  hmotkg_cis   hmotkg_kod      datum  uzemi_cis  uzemi_kod       uzemi_txt     mj_txt       key                         alttext_cz                          alttext_en
1247675855 1362.275        5560      78   80203            132             30      NaN      NaN         NaN         NaN         NaN          NaN 2023-12-31         97         19 Česká republika tisíc kusů         3                            Prasata                                Pigs
1388196153 1421.823        5560      78   80203            132             30      NaN      NaN         NaN         NaN         NaN          NaN 2024-12-31         97         19 Česká republika tisíc kusů         3                            Prasata                                Pigs
1247676187   54.431        5560      78   80203            132             35      NaN      NaN         NaN         NaN      7700.0 4.201108e+14 2023-12-31         97         19 Česká republika tisíc kusů     3.3.3      Prasata ve výkrmu, nad 110 kg         Fattening pigs, over 110 kg
1388195340   67.675        5560      78   80203            132             35      NaN      NaN         NaN         NaN      7700.0 4.201108e+14 2024-12-31         97         19 Česká republika tisíc kusů     3.3.3      Prasata ve výkrmu, nad 110 kg         Fattening pigs, over 110 kg
1247675065   22.331        5560      78   80203            131             41      NaN      NaN         NaN         NaN         NaN          NaN 2023-12-31         97         19 Česká republika tisíc kusů 3.4.2.2.1 Prasničky, nad 50 kg - nezapuštěné Gilts, over 50 kg - not yet covered
```

#### TAIL

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  druhzvire_cis  druhzvire_kod  vek_cis  vek_kod  vekmes_cis   vekmes_kod  hmotkg_cis  hmotkg_kod      datum  uzemi_cis  uzemi_kod       uzemi_txt     mj_txt       key                                       alttext_cz                                                 alttext_en
1388129268    0.000        5560      78   80203            132            207      NaN      NaN         NaN          NaN         NaN         NaN 2024-12-31         99        281 Moravskoslezsko tisíc kusů     2.2.1                                   Buvoli - krávy                                           Buffaloes - cows
1248154856   15.853        5560      78   80203            132            325      NaN      NaN      7700.0 3.999996e+14         NaN         NaN 2023-12-31         99        281 Moravskoslezsko tisíc kusů 2.0.2.2.2 Tuři, do 1 roku - jiní než k porážce - jalovičky Bovines, up to 1 year - other than for slaughter - females
1388131263   16.189        5560      78   80203            132            325      NaN      NaN      7700.0 3.999996e+14         NaN         NaN 2024-12-31         99        281 Moravskoslezsko tisíc kusů 2.0.2.2.2 Tuři, do 1 roku - jiní než k porážce - jalovičky Bovines, up to 1 year - other than for slaughter - females
1248157638   38.868        5560      78   80203            132            307      NaN      NaN         NaN          NaN         NaN         NaN 2023-12-31         99        281 Moravskoslezsko tisíc kusů 2.0.4.2.2                         Tuři, nad 2 roky - krávy                               Bovines, over 2 years - cows
1388129465   39.064        5560      78   80203            132            307      NaN      NaN         NaN          NaN         NaN         NaN 2024-12-31         99        281 Moravskoslezsko tisíc kusů 2.0.4.2.2                         Tuři, nad 2 roky - krávy                               Bovines, over 2 years - cows
```

### 178. [A] Úmrtnostní tabulky pro ČR

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key             True
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis         vek_kod  vuzemi_cis  vuzemi_kod  casref_od  casref_do          stapro_txt pohlavi_txt  vek_txt      vuzemi_txt
1287496751 0.002254        8817          102            1     7700 400000600001000          97          19 2023-01-01 2023-12-31 Míra úmrtnosti (mx)         muž        0 Česká republika
1287658095 0.000185        8817          102            1     7700 400001600002000          97          19 2023-01-01 2023-12-31 Míra úmrtnosti (mx)         muž        1 Česká republika
1287486432 0.000110        8817          102            1     7700 400002600003000          97          19 2023-01-01 2023-12-31 Míra úmrtnosti (mx)         muž        2 Česká republika
1287496379 0.000123        8817          102            1     7700 400003600004000          97          19 2023-01-01 2023-12-31 Míra úmrtnosti (mx)         muž        3 Česká republika
1287699045 0.000109        8817          102            1     7700 400004600005000          97          19 2023-01-01 2023-12-31 Míra úmrtnosti (mx)         muž        4 Česká republika
```

#### TAIL

```
     idhod  hodnota  stapro_kod  pohlavi_cis  pohlavi_kod  vek_cis         vek_kod  vuzemi_cis  vuzemi_kod  casref_od  casref_do                    stapro_txt pohlavi_txt  vek_txt      vuzemi_txt
1455098397   1276.0        7193          102            2     7700 420101620102000          97          19 2024-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      101 Česká republika
1455248287    796.0        7193          102            2     7700 420102620103000          97          19 2024-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      102 Česká republika
1455247230    478.0        7193          102            2     7700 420103620104000          97          19 2024-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      103 Česká republika
1455393599    277.0        7193          102            2     7700 420104620105000          97          19 2024-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      104 Česká republika
1448830520    339.0        7193          102            2     7700 420105620106000          97          19 2024-01-01 2024-12-31 Tabulkový počet žijících (Lx)        žena      105 Česká republika
```

## Kategorie B

### 179. [B] Pohyb zboží přes hranice podle vybraných zemí

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod      hodnota  stapro_kod  mj_cis  mj_kod  czem_cis czem_kod  vuzemi_cis  vuzemi_kod  rok  mesic                        stapro_txt           czem_txt
1320835559 50365.450565        5757      78     206       NaN      NaN          97          19 2023      3 Bilance pohybu zboží přes hranice                NaN
1320810302 10959.803328        5757      78     206    5584.0       GB          97          19 2023      3 Bilance pohybu zboží přes hranice Spojené království
1320911598 68358.523779        5757      78     206    5584.0       DE          97          19 2023      3 Bilance pohybu zboží přes hranice            Německo
1320927520 11409.695644        5757      78     206    5584.0       FR          97          19 2023      3 Bilance pohybu zboží přes hranice            Francie
1320944467  -186.638772        5757      78     206    5584.0       US          97          19 2023      3 Bilance pohybu zboží přes hranice      Spojené státy
```

#### TAIL

```
     idhod      hodnota  stapro_kod  mj_cis  mj_kod  czem_cis czem_kod  vuzemi_cis  vuzemi_kod  rok  mesic                      stapro_txt    czem_txt
1321027792  1538.041300        5756      78     206    5584.0       AU          97          19 2023      6 Obrat pohybu zboží přes hranice   Austrálie
1320571745  2279.863313        5756      78     206    5584.0       AZ          97          19 2023      6 Obrat pohybu zboží přes hranice Ázerbájdžán
1321122165  3161.474546        5756      78     206    5584.0       IL          97          19 2023      6 Obrat pohybu zboží přes hranice      Izrael
1321219511  4590.012640        5756      78     206    5584.0       SI          97          19 2023      6 Obrat pohybu zboží přes hranice   Slovinsko
1321000811 23562.748682        5756      78     206    5584.0       ES          97          19 2023      6 Obrat pohybu zboží přes hranice   Španělsko
```

### 180. [B] Stavební zakázky

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  misto_cis  misto_kod  stavprace_cis  stavprace_kod            obdobiod            obdobido  ctvrtleti  rok  uzemi_cis  uzemi_kod                 stapro_txt  mj_txt misto_txt  stavprace_txt
1267067570    10758         278      78     206     2478.0       10.0            NaN            NaN 2023-12-31 00:00:00 2023-12-31 00:00:00          4 2023         97         19 Hodnota stavebních zakázek mil. Kč zahraničí            NaN
1267067536   262150         278      78     206        NaN        NaN            NaN            NaN 2023-12-31 00:00:00 2023-12-31 00:00:00          4 2023         97         19 Hodnota stavebních zakázek mil. Kč       NaN            NaN
1421917798     9702         278      78     206     2478.0       10.0            NaN            NaN 2024-12-31 00:00:00 2024-12-31 00:00:00          4 2024         97         19 Hodnota stavebních zakázek mil. Kč zahraničí            NaN
1421917663   330009         278      78     206        NaN        NaN            NaN            NaN 2024-12-31 00:00:00 2024-12-31 00:00:00          4 2024         97         19 Hodnota stavebních zakázek mil. Kč       NaN            NaN
1421917660     8363         278      78     206     2478.0       10.0            NaN            NaN 2024-06-30 00:00:00 2024-06-30 00:00:00          2 2024         97         19 Hodnota stavebních zakázek mil. Kč zahraničí            NaN
```

#### TAIL

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  misto_cis  misto_kod  stavprace_cis  stavprace_kod            obdobiod            obdobido  ctvrtleti  rok  uzemi_cis  uzemi_kod                        stapro_txt  mj_txt misto_txt           stavprace_txt
1421917793    39115        5959      78     206     2478.0        9.0          175.0           23.0 2024-10-01 00:00:00 2024-12-31 00:00:00          4 2024         97         19 Hodnota nových stavebních zakázek mil. Kč  tuzemsko    Pozemní stavitelství
1421917656    60313        5959      78     206     2478.0        9.0          175.0           24.0 2024-10-01 00:00:00 2024-12-31 00:00:00          4 2024         97         19 Hodnota nových stavebních zakázek mil. Kč  tuzemsko Inženýrské stavitelství
1421917654   100464        5959      78     206     2478.0        9.0            NaN            NaN 2024-07-01 00:00:00 2024-09-30 00:00:00          3 2024         97         19 Hodnota nových stavebních zakázek mil. Kč  tuzemsko                     NaN
1421917801    44799        5959      78     206     2478.0        9.0          175.0           23.0 2024-07-01 00:00:00 2024-09-30 00:00:00          3 2024         97         19 Hodnota nových stavebních zakázek mil. Kč  tuzemsko    Pozemní stavitelství
1421917655    55665        5959      78     206     2478.0        9.0          175.0           24.0 2024-07-01 00:00:00 2024-09-30 00:00:00          3 2024         97         19 Hodnota nových stavebních zakázek mil. Kč  tuzemsko Inženýrské stavitelství
```

### 181. [B] Zahraniční obchod se zbožím podle vybraných zemí

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod      hodnota  stapro_kod  mj_cis  mj_kod  czem_cis czem_kod  vuzemi_cis  vuzemi_kod  rok  mesic           stapro_txt  czem_txt
1473731975   294.842766        8476      78     206    5584.0       LV          97          19 2024      7 Hodnota dovozu zboží  Lotyšsko
1473732864  4020.600296        8476      78     206    5584.0       CH          97          19 2024     10 Hodnota dovozu zboží Švýcarsko
1473733729  1008.724238        8476      78     206    5584.0       GR          97          19 2024      2 Hodnota dovozu zboží     Řecko
1473734662   655.246918        8476      78     206    5584.0       PH          97          19 2024      8 Hodnota dovozu zboží  Filipíny
1473734683 20584.589092        8476      78     206    5584.0       SK          97          19 2024      9 Hodnota dovozu zboží Slovensko
```

#### TAIL

```
     idhod      hodnota  stapro_kod  mj_cis  mj_kod  czem_cis czem_kod  vuzemi_cis  vuzemi_kod  rok  mesic    stapro_txt           czem_txt
1320698219   874.304253        8500      78     206    5584.0       IL          97          19 2023      9 Bilance zboží             Izrael
1320701897  3161.570017        8500      78     206    5584.0       ES          97          19 2023      5 Bilance zboží          Španělsko
1320699576 -2586.767433        8500      78     206    5584.0       TW          97          19 2023     11 Bilance zboží          Tchaj-wan
1320703870 -7425.629783        8500      78     206    5584.0       KR          97          19 2023      4 Bilance zboží Korejská republika
1320704707   129.192583        8500      78     206    5584.0       SG          97          19 2023      3 Bilance zboží           Singapur
```

### 182. [B] Zaměstnanci a průměrné hrubé měsíční mzdy podle odvětví

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  typosoby_kod  odvetvi_cis odvetvi_kod  rok  ctvrtleti  uzemi_cis  uzemi_kod                       stapro_txt               mj_txt typosoby_txt                                                 odvetvi_txt
1457005882    380.9         316      78   80403           100       5103.0           P 2023          2         97         19 Průměrný počet zaměstnaných osob tis. osob (tis. os.)      fyzický                                                  Vzdělávání
1457005886     74.3         316      78   80403           100       5103.0           K 2023          2         97         19 Průměrný počet zaměstnaných osob tis. osob (tis. os.)      fyzický                                Peněžnictví a pojišťovnictví
1457005887    223.1         316      78   80403           100       5103.0           F 2023          2         97         19 Průměrný počet zaměstnaných osob tis. osob (tis. os.)      fyzický                                                Stavebnictví
1457014089     34.8         316      78   80403           200       5103.0           D 2023          2         97         19 Průměrný počet zaměstnaných osob tis. osob (tis. os.)   přepočtený Výroba a rozvod elektřiny, plynu, tepla a klimatiz. vzduchu
1457006580     18.5         316      78   80403           100       5103.0           B 2023          2         97         19 Průměrný počet zaměstnaných osob tis. osob (tis. os.)      fyzický                                            Těžba a dobývání
```

#### TAIL

```
     idhod  hodnota  stapro_kod  mj_cis  mj_kod  typosoby_kod  odvetvi_cis odvetvi_kod  rok  ctvrtleti  uzemi_cis  uzemi_kod                         stapro_txt mj_txt typosoby_txt                                                odvetvi_txt
1504623066  35980.0        5958      78     200           200       5103.0           A 2024          3         97         19 Průměrná hrubá mzda na zaměstnance     Kč   přepočtený                          Zemědělství, lesnictví, rybářství
1504628619  32541.0        5958      78     200           200       5103.0           N 2024          3         97         19 Průměrná hrubá mzda na zaměstnance     Kč   přepočtený                        Administrativní a podpůrné činnosti
1504618392  67924.0        5958      78     200           100       5103.0           K 2024          3         97         19 Průměrná hrubá mzda na zaměstnance     Kč      fyzický                               Peněžnictví a pojišťovnictví
1504618390  29830.0        5958      78     200           100       5103.0           S 2024          3         97         19 Průměrná hrubá mzda na zaměstnance     Kč      fyzický                                           Ostatní činnosti
1504618976  40906.0        5958      78     200           200       5103.0           E 2024          3         97         19 Průměrná hrubá mzda na zaměstnance     Kč   přepočtený Zásobování vodou; činnosti související s odpady a sanacemi
```

### 183. [B] Zemřelí podle měsíců a věkových skupin v České republice

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  vek_cis      vek_kod  vuzemi_cis  vuzemi_kod  obdobi  rok  mesic vek_txt  priznak
1289710969       30        5393   7700.0 4.000006e+14          97          19 2023-01 2023      1    0-14      NaN
1289710970      279        5393   7700.0 4.100156e+14          97          19 2023-01 2023      1   15-44      NaN
1289710971     1351        5393   7700.0 4.100456e+14          97          19 2023-01 2023      1   45-64      NaN
1289710972     2501        5393   7700.0 4.100656e+14          97          19 2023-01 2023      1   65-74      NaN
1289710973     3804        5393   7700.0 4.100756e+14          97          19 2023-01 2023      1   75-84      NaN
```

#### TAIL

```
     idhod  hodnota  stapro_kod  vek_cis      vek_kod  vuzemi_cis  vuzemi_kod  obdobi  rok  mesic   vek_txt  priznak
1457075564     1297        5393   7700.0 4.100456e+14          97          19 2024-12 2024     12     45-64      NaN
1457074178     2118        5393   7700.0 4.100656e+14          97          19 2024-12 2024     12     65-74      NaN
1457074179     3438        5393   7700.0 4.100756e+14          97          19 2024-12 2024     12     75-84      NaN
1457075563     3029        5393   7700.0 4.100858e+14          97          19 2024-12 2024     12 85 a více      NaN
1457090052    10177        5393      NaN          NaN          97          19 2024-12 2024     12    celkem      NaN
```

### 184. [B] Zemřelí podle týdnů a věkových skupin v České republice

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column    vuzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  vek_cis      vek_kod  vuzemi_cis  vuzemi_kod  rok  tyden roktyden  casref_od  casref_do vek_txt  priznak
1289712319        3        5393   7700.0 4.000006e+14          97          19 2023      1 2023-W01 2023-01-02 2023-01-08    0-14      NaN
1289712320       74        5393   7700.0 4.100156e+14          97          19 2023      1 2023-W01 2023-01-02 2023-01-08   15-44      NaN
1289712321      307        5393   7700.0 4.100456e+14          97          19 2023      1 2023-W01 2023-01-02 2023-01-08   45-64      NaN
1289712322      634        5393   7700.0 4.100656e+14          97          19 2023      1 2023-W01 2023-01-02 2023-01-08   65-74      NaN
1289712323      968        5393   7700.0 4.100756e+14          97          19 2023      1 2023-W01 2023-01-02 2023-01-08   75-84      NaN
```

#### TAIL

```
     idhod  hodnota  stapro_kod  vek_cis      vek_kod  vuzemi_cis  vuzemi_kod  rok  tyden roktyden  casref_od  casref_do   vek_txt  priznak
1457033488      284        5393   7700.0 4.100456e+14          97          19 2024     52 2024-W52 2024-12-23 2024-12-29     45-64      NaN
1457045671      451        5393   7700.0 4.100656e+14          97          19 2024     52 2024-W52 2024-12-23 2024-12-29     65-74      NaN
1457033579      813        5393   7700.0 4.100756e+14          97          19 2024     52 2024-W52 2024-12-23 2024-12-29     75-84      NaN
1457033486      720        5393   7700.0 4.100858e+14          97          19 2024     52 2024-W52 2024-12-23 2024-12-29 85 a více      NaN
1457089529     2324        5393      NaN          NaN          97          19 2024     52 2024-W52 2024-12-23 2024-12-29    celkem      NaN
```

### 185. [B] Těžba dřeva podle druhů dřevin a typu nahodilé těžby

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column     uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  dd_cis  dd_kod  druhtez_cis  druhtez_kod  prictez_cis  prictez_kod  rok  uzemi_cis  uzemi_kod                     dd_txt  druhtez_txt  prictez_txt  ELPRO_ID
1454501090   353634        5966   202.0    17.0          NaN          NaN          NaN          NaN 2024         97         19                      Jasan          NaN          NaN   1845098
1454501321      154        5966   202.0    10.0          NaN          NaN          NaN          NaN 2024         97         19 Ostatní jehličnaté dřeviny          NaN          NaN   1845137
1454501299  2132670        5966   203.0     2.0          NaN          NaN          NaN          NaN 2024         97         19           Listnaté dřeviny          NaN          NaN   1845106
1454501300    58945        5966   202.0    16.0          NaN          NaN          NaN          NaN 2024         97         19                      Javor          NaN          NaN   1845155
1454501088 15674286        5966   203.0     1.0          NaN          NaN          NaN          NaN 2024         97         19         Jehličnaté dřeviny          NaN          NaN   1845116
```

#### TAIL

```
     idhod  hodnota  stapro_kod  dd_cis  dd_kod  druhtez_cis  druhtez_kod  prictez_cis  prictez_kod  rok  uzemi_cis  uzemi_kod dd_txt          druhtez_txt                                   prictez_txt  ELPRO_ID
1287999222   754180        5966   202.0    14.0          NaN          NaN          NaN          NaN 2023         97         19    Buk                  NaN                                           NaN   1845097
1287999223    54251        5966   202.0    22.0          NaN          NaN          NaN          NaN 2023         97         19   Lípa                  NaN                                           NaN   1845110
1287999048   414698        5966   203.0    21.0          NaN          NaN          NaN          NaN 2023         97         19    Dub                  NaN                                           NaN   1845096
1287999057     4258        5966     NaN     NaN        199.0         22.0        206.0          2.0 2023         97         19    NaN Nahodilá těžba dřeva                             Exhalační příčina  10009764
1287999090  2028183        5966     NaN     NaN        199.0         22.0        206.0          9.0 2023         97         19    NaN Nahodilá těžba dřeva Příčina jiná než živelní, exhalační a hmyzová  10009760
```

### 186. [B] Index průmyslové produkce

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
     idhod  hodnota  stapro_kod  casz_cis casz_kod  cznace_cis  cznace_kod  mesic  rok  mesicz  rokz                stapro_txt                       casz_txt                                                       cznace_txt
1498105299     86.1        5249      7626        C        5104           5     11 2025    11.0  2024 Index průmyslové produkce stejné období předchozího roku                            Těžba a úprava černého a hnědého uhlí
1498026772    102.0        5249      7626        C        5104          22     11 2025    11.0  2024 Index průmyslové produkce stejné období předchozího roku                            Výroba pryžových a plastových výrobků
1498075377     98.7        5249      7626        C        5104          33     11 2025    11.0  2024 Index průmyslové produkce stejné období předchozího roku                             Opravy a instalace strojů a zařízení
1498140451    101.9        5249      7626        C        5104          26     11 2025    11.0  2024 Index průmyslové produkce stejné období předchozího roku Výroba počítačů, elektronických a optických přístrojů a zařízení
1498105300     98.5        5249      7626        C        5104          27     11 2025    11.0  2024 Index průmyslové produkce stejné období předchozího roku                                     Výroba elektrických zařízení
```

#### TAIL

```
     idhod  hodnota  stapro_kod  casz_cis casz_kod  cznace_cis  cznace_kod  mesic  rok  mesicz  rokz                stapro_txt                       casz_txt                                                            cznace_txt
1474422534    103.0        5249      7626        C        5104          17      6 2025     6.0  2024 Index průmyslové produkce stejné období předchozího roku                                      Výroba papíru a výrobků z papíru
1474508540    103.2        5249      7626        C        5724     5350001      6 2025     6.0  2024 Index průmyslové produkce stejné období předchozího roku                                                Průmysl celkem (B+C+D)
1474472181      NaN        5249      7626        C        5104          19      6 2025     6.0  2024 Index průmyslové produkce stejné období předchozího roku                          Výroba koksu a rafinovaných ropných produktů
1474452360    106.2        5249      7626        C        5104          32      6 2025     6.0  2024 Index průmyslové produkce stejné období předchozího roku                                        Ostatní zpracovatelský průmysl
1474471139     92.3        5249      7626        C        5104          21      6 2025     6.0  2024 Index průmyslové produkce stejné období předchozího roku Výroba základních farmaceutických výrobků a farmaceutických přípravků
```

### 187. [B] Index stavební produkce

                         hodnota
polozka                         
target_years_present  2023, 2024
has_primary_key            False
primary_key_column          None

#### HEAD

```
     idhod  hodnota  stapro_kod  casz_cis casz_kod  stavprace_cis  stavprace_kod  oceneni_cis oceneni_kod  ocisteni_cis ocisteni_kod  mesic  rok  mesicz  rokz              stapro_txt              casz_txt           stavprace_txt                oceneni_txt                                         ocisteni_txt
1267031514    107.9        5939      7626        Z            NaN            NaN          NaN         NaN           NaN          NaN      3 2023     NaN  2021 Index stavební produkce průměr bazického roku   Stavební práce celkem                 běžné ceny                                           neočištěno
1267045548     84.2        5939      7626        Z          175.0           24.0          NaN         NaN           NaN          NaN      3 2023     NaN  2021 Index stavební produkce průměr bazického roku Inženýrské stavitelství                 běžné ceny                                           neočištěno
1267060055    120.3        5939      7626        Z          175.0           23.0          NaN         NaN           NaN          NaN      3 2023     NaN  2021 Index stavební produkce průměr bazického roku    Pozemní stavitelství                 běžné ceny                                           neočištěno
1267031517    101.8        5939      7626        Z          175.0           23.0       7603.0           P           NaN          NaN      3 2023     NaN  2021 Index stavební produkce průměr bazického roku    Pozemní stavitelství stálé (průměrné) ceny roku                                           neočištěno
1502904526    106.7        5939      7626        Z          175.0           23.0       7603.0           P        7604.0            O      3 2023     NaN  2021 Index stavební produkce průměr bazického roku    Pozemní stavitelství stálé (průměrné) ceny roku sezónně očištěno, včetně očištění o kalendářní vlivy
```

#### TAIL

```
     idhod  hodnota  stapro_kod  casz_cis casz_kod  stavprace_cis  stavprace_kod  oceneni_cis oceneni_kod  ocisteni_cis ocisteni_kod  mesic  rok  mesicz  rokz              stapro_txt              casz_txt           stavprace_txt                oceneni_txt                                               ocisteni_txt
1267028275    138.7        5939      7626        Z          175.0           24.0       7603.0           P           NaN          NaN     10 2023     NaN  2021 Index stavební produkce průměr bazického roku Inženýrské stavitelství stálé (průměrné) ceny roku                                                 neočištěno
1267043189    123.6        5939      7626        Z            NaN            NaN       7603.0           P           NaN          NaN     10 2023     NaN  2021 Index stavební produkce průměr bazického roku   Stavební práce celkem stálé (průměrné) ceny roku                                                 neočištěno
1502907512    105.3        5939      7626        Z          175.0           24.0       7603.0           P        7604.0            O     10 2023     NaN  2021 Index stavební produkce průměr bazického roku Inženýrské stavitelství stálé (průměrné) ceny roku       sezónně očištěno, včetně očištění o kalendářní vlivy
1502904051    122.6        5939      7626        Z            NaN            NaN       7603.0           P        7604.0            P     10 2023     NaN  2021 Index stavební produkce průměr bazického roku   Stavební práce celkem stálé (průměrné) ceny roku očištěno o kalendářní vlivy, není očištěno o sezónní vlivy
1502906065    101.9        5939      7626        Z            NaN            NaN       7603.0           P        7604.0            O     10 2023     NaN  2021 Index stavební produkce průměr bazického roku   Stavební práce celkem stálé (průměrné) ceny roku       sezónně očištěno, včetně očištění o kalendářní vlivy
```

## Kategorie D

### 188. [D] Příjmy domácností zaměstnanců a důchodců

                        hodnota
polozka                        
target_years_present       2023
has_primary_key           False
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  stapro_kod  ekakocd_cis  ekakocd_kod  pvdom_cis  pvdom_kod  rok  uzemi_cis  uzemi_kod                               stapro_txt       ekakocd_txt                                      pvdom_txt
1441283496   278673        6010          NaN          NaN        NaN        NaN 2023         97         19 Průměrné čisté peněžní příjmy domácností Domácnosti celkem                                            NaN
1441283497   154702        6010          NaN          NaN      213.0       14.0 2023         97         19 Průměrné čisté peněžní příjmy domácností Domácnosti celkem Příjmy ze závislé činnosti (hlavní zaměstnání)
1441283498   286954        6010        221.0          6.0        NaN        NaN 2023         97         19 Průměrné čisté peněžní příjmy domácností       Zaměstnanci                                            NaN
1441283499   235015        6010        221.0          6.0      213.0       14.0 2023         97         19 Průměrné čisté peněžní příjmy domácností       Zaměstnanci Příjmy ze závislé činnosti (hlavní zaměstnání)
1441283528   310594        6010        221.0          5.0        NaN        NaN 2023         97         19 Průměrné čisté peněžní příjmy domácností  Samostatně činní                                            NaN
```

#### TAIL

```
     idhod  hodnota  stapro_kod  ekakocd_cis  ekakocd_kod  pvdom_cis  pvdom_kod  rok  uzemi_cis  uzemi_kod                                    stapro_txt        ekakocd_txt  pvdom_txt
1441283193   282872        8620        221.0          6.0        NaN        NaN 2023         97         19 Průměrné disponibilní čisté příjmy domácností        Zaměstnanci        NaN
1441283196   303691        8620        221.0          5.0        NaN        NaN 2023         97         19 Průměrné disponibilní čisté příjmy domácností   Samostatně činní        NaN
1441283197   249566        8620        220.0         14.0        NaN        NaN 2023         97         19 Průměrné disponibilní čisté příjmy domácností           Důchodci        NaN
1441283198   100525        8620        221.0          4.0        NaN        NaN 2023         97         19 Průměrné disponibilní čisté příjmy domácností       Nezaměstnaní        NaN
1441283199   123707        8620        221.0         11.0        NaN        NaN 2023         97         19 Průměrné disponibilní čisté příjmy domácností Ostatní domácnosti        NaN
```

### 189. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - okrsková data, počty hlasů pro strany

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KSTRANA  POC_HLASU  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  HLASY_23  HLASY_24  HLASY_25  HLASY_26  HLASY_27  HLASY_28  HLASY_29  HLASY_30  HLASY_31  HLASY_32  HLASY_33  HLASY_34  HLASY_35  HLASY_36  KC_3  KC_4  POSL_KAND  KC_SUM
         1         2       0      0   7204 500011       1     6        1          1     2         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     2          0  507228
         1         2       0      0   7204 500011       1     6        2          1     3         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0     3          0  507230
         1         2       0      0   7204 500011       1     6        3          8    11         0         1         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     5    16          3  507259
         1         2       0      0   7204 500011       1     6        4         67    71         6         4         3         4         1         2         0         0         0         0         0         2         2         2         1         0         1         1         0         1         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0   226   297         22  507840
         1         2       0      0   7204 500011       1     6        5         28    33         8         0         0         0         3         2         2         0         0         0         0         0         1         0         0         0         0         0         0         0         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0    84   117         22  507480
```

#### TAIL

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KSTRANA  POC_HLASU  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  HLASY_23  HLASY_24  HLASY_25  HLASY_26  HLASY_27  HLASY_28  HLASY_29  HLASY_30  HLASY_31  HLASY_32  HLASY_33  HLASY_34  HLASY_35  HLASY_36  KC_3  KC_4  POSL_KAND  KC_SUM
     14886         2       0      0   9999 999997     111     3       15          1    16         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0    16          0 1010144
     14886         2       0      0   9999 999997     111     3       17        103   120        32         6        10        21         8         7        17        11         7         2         2         0        12         0         6         0         2         0         0         5         0         8         0         0         1         2         0         0         0         0         0         0         0         0         0         0  1185  1305         26 1012748
     14886         2       0      0   9999 999997     111     3       18          2    20         1         0         0         0         0         0         2         0         1         0         0         0         1         0         0         0         2         0         1         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    90   110         19 1010351
     14886         2       0      0   9999 999997     111     3       20          5    25         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         1         1         1         0         0         0         0         0         0         0         0         0         0    75   100         26 1010338
     14886         2       0      0   9999 999997     111     3       21          1    22         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0     0    22          0 1010156
```

### 190. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - okrsková data, počty voličů a hlasů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KC_2                                                   ZAKRSTRANA  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK
         1         1       0      0   7204 500011       1     6  2231 111110110101101111011100000000000000000000000000000000000000         717         505         505         504
         2         1       0      0   7204 500011       2     0  1295 111110111101100011010000000000000000000000000000000000000000         435         288         288         284
         3         1       0      0   7204 500011       3     1  1261 101110011001101111011000000000000000000000000000000000000000         394         289         289         289
         4         1       0      0   7105 500020       1     2   747 111110010101100011010100000000000000000000000000000000000000         268         160         160         159
         5         1       0      0   7105 500020       2     3  2091 101110110101101011011100000000000000000000000000000000000000         729         455         455         452
```

#### TAIL

```
 ID_OKRSKY  TYP_FORM  OPRAVA  CHYBA  OKRES   OBEC  OKRSEK  KC_1  KC_2                                                   ZAKRSTRANA  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK
     14882         1       0      0   9999 999997     107     6   104 101000000000100010000000000000000000000000000000000000000000          32          24          24          24
     14883         1       0      0   9999 999997     108     0   247 001110010001100010010000000000000000000000000000000000000000          72          59          59          57
     14884         1       0      0   9999 999997     109     1   100 000010010001100010010000000000000000000000000000000000000000          25          25          25          25
     14885         1       0      0   9999 999997     110     2   144 100110000000100010000000000000000000000000000000000000000000          69          25          25          25
     14886         1       0      0   9999 999997     111     3  1270 111110110001101011011000000000000000000000000000000000000000         568         234         234         234
```

### 191. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - registr kandidátních listin

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KSTRANA  VSTRANA                                          NAZEVCELK                                         NAZEV_STRK                     ZKRATKAK30       ZKRATKAK8  POCSTRVKO  SLOZENI  STAVREG PLAT_STR  SLOZNEPLAT  POCMANDCR                                          NAZEVPLNY
       1        5                                    Strana zelených                                    Strana zelených                Strana zelených          Zelení          1        5        0        A         NaN          0                                    Strana zelených
       2      752 Švýcarská demokracie (www.svycarska-demokracie.cz) Švýcarská demokracie (www.svycarska-demokracie.cz)           Švýcarská demokracie Švýcar. demokr.          1      752        0        A         NaN          0 Švýcarská demokracie (www.svycarska-demokracie.cz)
       3      759                                         VOLNÝ blok                                         VOLNÝ blok                     VOLNÝ blok      Volný blok          1      759        0        A         NaN          0                                         VOLNÝ blok
       4     1114                   Svoboda a přímá demokracie (SPD)                   Svoboda a přímá demokracie (SPD) Svoboda a př. demokracie (SPD)             SPD          1     1114        0        A         NaN         20                   Svoboda a přímá demokracie (SPD)
       5        7                 Česká strana sociálně demokratická                 Česká strana sociálně demokratická   Česká str.sociálně demokrat.            ČSSD          1        7        0        A         NaN          0                 Česká strana sociálně demokratická
```

#### TAIL

```
 KSTRANA  VSTRANA                         NAZEVCELK                        NAZEV_STRK                     ZKRATKAK30 ZKRATKAK8  POCSTRVKO  SLOZENI        STAVREG PLAT_STR  SLOZNEPLAT  POCMANDCR                         NAZEVPLNY
      18       47 Komunistická strana Čech a Moravy Komunistická strana Čech a Moravy Komunistická str.Čech a Moravy      KSČM          1       47              0        A         NaN          0 Komunistická strana Čech a Moravy
      19     1190             Moravské zemské hnutí             Moravské zemské hnutí          Moravské zemské hnutí       MZH          1     1190 22222222200022        A         NaN          0             Moravské zemské hnutí
      20      768                          ANO 2011                          ANO 2011                       ANO 2011       ANO          1      768              0        A         NaN         72                          ANO 2011
      21     1244  Otevřeme Česko normálnímu životu  Otevřeme Česko normálnímu životu  Otevřeme ČR normálnímu životu      OtČe          1     1244              0        A         NaN          0  Otevřeme Česko normálnímu životu
      22       83                          Moravané                          Moravané                       Moravané  Moravané          1       83  2022222000000        A         NaN          0                          Moravané
```

### 192. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - registr kandidátů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VOLKRAJ  KSTRANA  PORCISLO  JMENO PRIJMENI TITULPRED TITULZA  VEK                                                                                                                              POVOLANI BYDLISTEN  BYDLISTEK  PSTRANA  NSTRANA PLATNOST  POCHLASU  POCPROC MANDAT  SKRUTINIUM  PORADIMAND  PORADINAHR
       1        1         1    Eva  Kavková      Mgr.     NaN   45                                                           ředitelka vzdělávací a poradenské organizace, lektorka, terapeutka a koučka     Praha          1        5        5        A       716    11.81      N           0           0           0
       1        1         2    Vít   Masare      Mgr.     NaN   34                               poradce pro udržitelnou politiku ve městech, terénní sociální pracovník, spolupředseda Zelených v Praze     Praha          1        5        5        A       349     5.76      N           0           0           0
       1        1         3   Jana   Jebavá      Mgr.     NaN   38            grafička a editorka, členka Komise životního prostředí a péče o veřejný prostor Prahy 7, spolupředsedkyně Zelených v Praze     Praha          1        5        5        A       593     9.78      N           0           0           0
       1        1         4 Ondřej Mirovský      Mgr.    M.EM   42 radní Prahy 7 pro dopravu, bezpečnost a integraci cizinců, ekolog, podnikatel, odborník na družicové systémy pro dálkový průzkum Země     Praha          1        5        5        A       230     3.79      N           0           0           0
       1        1         5  Petra Urbanová      Mgr.   LL.M.   30                                                                                                             environmentální právnička     Praha          1        5        5        A       555     9.16      N           0           0           0
```

#### TAIL

```
 VOLKRAJ  KSTRANA  PORCISLO JMENO PRIJMENI  TITULPRED  TITULZA  VEK        POVOLANI      BYDLISTEN  BYDLISTEK  PSTRANA  NSTRANA PLATNOST  POCHLASU  POCPROC MANDAT  SKRUTINIUM  PORADIMAND  PORADINAHR
      14       22        32 Roman Zvoníček        NaN      NaN 46.0 elektromechanik Brumov-Bylnice   585114.0     99.0     83.0        A         9     0.31      N           0           0           0
      14       22        33 Tomáš   Kleibl        NaN      NaN 25.0        strojník         Uničov   505587.0     99.0     83.0        A        25     0.88      N           0           0           0
      14       22        34 Alois  Nezbeda        NaN      NaN 77.0          řezník        Loštice   540196.0     99.0     83.0        A        23     0.81      N           0           0           0
      14       22        35  Jiří   Žváček        NaN      NaN 58.0        strojník     Bílá Lhota   500623.0     99.0     83.0        A        14     0.49      N           0           0           0
      14       22        36  Petr  Srovnal        NaN      NaN 61.0          dělník        Senička   552267.0     99.0     83.0        A        20     0.70      N           0           0           0
```

### 193. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - registr zvláštních volebních okrsků – zahraničí

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
  OBEC  OKRSEK  KC1 NAZEVOKRSK TYPURADU  KODZEME ZKRZEME           NAZEVZEME SVETADIL  CASPOSUNLC NAZEVOKRSA             NAZEVZEMEA SUBKONTINENT
999997       1    5     Tirana       vv        8      AL             Albánie       EV         0.0     Tirana                Albania           EV
999997       2    6      Vídeň       vv       40      AT            Rakousko       EV         0.0     Vienna                Austria           EV
999997       3    0     Brusel       vv       56      BE              Belgie       EV         0.0   Brussels                Belgium           EV
999997       4    1   Sarajevo       vv       70      BA Bosna a Hercegovina       EV         0.0   Sarajevo Bosnia and Herzegovina           EV
999997       5    2      Sofie       vv      100      BG           Bulharsko       EV         1.0      Sofia               Bulgaria           EV
```

#### TAIL

```
  OBEC  OKRSEK  KC1 NAZEVOKRSK TYPURADU  KODZEME ZKRZEME NAZEVZEME SVETADIL  CASPOSUNLC NAZEVOKRSA NAZEVZEMEA SUBKONTINENT
999997     107    6     Lusaka       vv      894      ZM    Zambie       AF         0.0     Lusaka     Zambia           AF
999997     108    0     Bamako       vv      466      ML      Mali       AF        -2.0     Bamako       Mali           AF
999997     109    1     Ménaka       kj      466      ML      Mali       AF        -2.0     Ménaka       Mali           AF
999997     110    2   Canberra       vv       36      AU Austrálie       AO         9.0   Canberra  Australia           AO
999997     111    3     Sydney       gk       36      AU Austrálie       AO         9.0     Sydney  Australia           AO
```

### 194. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - složení kandidátních listin

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KSTRANA TYPSLOZENI  NSTRANA
       1          P        5
       2          P      752
       3          P      759
       4          P     1114
       5          P        7
```

#### TAIL

```
 KSTRANA TYPSLOZENI  NSTRANA
      18          P       47
      19          P     1190
      20          P      768
      21          P     1244
      22          P       83
```

### 195. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - složení volebních stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA  NSTRANA
       1        1
       2        2
       5        5
       7        7
       9        9
```

#### TAIL

```
 VSTRANA  NSTRANA
    1477      721
    1478     1012
    1478     1175
    9995     9995
    9999     9999
```

### 196. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - číselník navrhujících stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NSTRANA                         NAZEV_STRN                    ZKRATKAN30 ZKRATKAN8
       1                            KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2      Česká strana národně sociální Česká strana národně sociální      ČSNS
       5                    Strana zelených               Strana zelených    Zelení
       7 Česká strana sociálně demokratická  Česká str.sociálně demokrat.      ČSSD
       9         Nezávislá iniciativa (NEI)    Nezávislá iniciativa (NEI)       NEI
```

#### TAIL

```
 NSTRANA                   NAZEV_STRN                   ZKRATKAN30       ZKRATKAN8
    1248  Trikolora - spojená pravice  Trikolora - spojená pravice           Triko
    1249       Strana národní svobody       Strana národní svobody             SNS
    1250 Urza.cz: Nechceme vaše hlasy Urza.cz: Nechceme vaše hlasy Nevolte Urza.cz
    9995                      Koalice                      Koalice         Koalice
    9999          Neregistrováno u MV          Neregistrováno u MV Neregistr. u MV
```

### 197. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - číselník obcí pro prezentaci

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBEC_PREZ                NAZEVOBCE
    500011 Želechovice nad Dřevnicí
    500020        Petrov nad Desnou
    500046                  Libhošť
    500062                   Krhová
    500071                  Poličná
```

#### TAIL

```
 OBEC_PREZ         NAZEVOBCE
    599930 Suchdol nad Odrou
    599948         Štramberk
    599956             Tichá
    599964             Tísek
    599999       Trojanovice
```

### 198. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - číselník obcí, městských částí, městských obvodů a volebních okrsků

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRAJ  OKRES  CPOU  ORP   OBEC                NAZEVOBCE  VOLKRAJ  MINOKRSEK1  MAXOKRSEK1  OBEC_PREZ
 7200   7204   662 7213 500011 Želechovice nad Dřevnicí       13           1           3     500011
 7100   7105   860 7111 500020        Petrov nad Desnou       12           1           2     500020
 8100   8104   792 8115 500046                  Libhošť       14           1           1     500046
 1100   1100     1 1000 500054                  Praha 1        1        1000        1021     554782
 7200   7203   871 7210 500062                   Krhová       13           1           1     500062
```

#### TAIL

```
 KRAJ  OKRES  CPOU  ORP   OBEC   NAZEVOBCE  VOLKRAJ  MINOKRSEK1  MAXOKRSEK1  OBEC_PREZ
 8100   8104   791 8112 599948   Štramberk       14           1           4     599948
 8100   8104   789 8105 599956       Tichá       14           1           1     599956
 8100   8104   788 8101 599964       Tísek       14           1           1     599964
 8100   8104   789 8105 599999 Trojanovice       14           1           2     599999
 9900   9999   999 9999 999997   Zahraničí        6           1         111     999997
```

### 199. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - číselník politické příslušnosti kandidátů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 PSTRANA                         NAZEV_STRP                    ZKRATKAP30 ZKRATKAP8
       1                            KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2      Česká strana národně sociální Česká strana národně sociální      ČSNS
       5                    Strana zelených               Strana zelených    Zelení
       7 Česká strana sociálně demokratická  Česká str.sociálně demokrat.      ČSSD
       9         Nezávislá iniciativa (NEI)    Nezávislá iniciativa (NEI)       NEI
```

#### TAIL

```
 PSTRANA                                     NAZEV_STRP                   ZKRATKAP30       ZKRATKAP8
    1247 Občanský Manifest - Pravá Svoboda a Prosperita            Občanský Manifest     Manifest.cz
    1248                    Trikolora - spojená pravice  Trikolora - spojená pravice           Triko
    1249                         Strana národní svobody       Strana národní svobody             SNS
    1250                   Urza.cz: Nechceme vaše hlasy Urza.cz: Nechceme vaše hlasy Nevolte Urza.cz
    9999                            Neregistrováno u MV          Neregistrováno u MV Neregistr. u MV
```

### 200. [D] Volby do Poslanecké sněmovny Parlamentu ČR 2021 - číselník volebních stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA                          NAZEVCELK                         NAZEV_STRV                    ZKRATKAV30 ZKRATKAV8  POCSTR_SLO  SLOZENI ZKRATKA_OF TYPVS
       1                            KDU-ČSL                            KDU-ČSL                       KDU-ČSL   KDU-ČSL           1        1    KDU-ČSL     S
       2      Česká strana národně sociální      Česká strana národně sociální Česká strana národně sociální      ČSNS           1        2       ČSNS     S
       5                    Strana zelených                    Strana zelených               Strana zelených    Zelení           1        5     Zelení     S
       7 Česká strana sociálně demokratická Česká strana sociálně demokratická  Česká str.sociálně demokrat.      ČSSD           1        7       ČSSD     S
       9         Nezávislá iniciativa (NEI)         Nezávislá iniciativa (NEI)    Nezávislá iniciativa (NEI)       NEI           1        9        NEI     S
```

#### TAIL

```
 VSTRANA                          NAZEVCELK                         NAZEV_STRV                     ZKRATKAV30       ZKRATKAV8  POCSTR_SLO         SLOZENI          ZKRATKA_OF TYPVS
    1476         Koalice STAN, Zelení a NEZ         Koalice STAN, Zelení a NEZ      Koalice STAN, Zelení, NEZ STAN+Zelení+NEZ           3     005,088,166                 NaN     K
    1477 Koalice ODS, TOP 09, KDU-ČSL a KAN Koalice ODS, TOP 09, KDU-ČSL a KAN Koalice ODS,TOP 09,KDU-ČSL,KAN ODS+TOP+KDU+KAN           4 001,040,053,721                 NaN     K
    1478              Koalice UFO a ProMOST              Koalice UFO a ProMOST           Koalice UFO, ProMOST     UFO+ProMOST           2       1012,1175                 NaN     K
    9995                            Koalice                            Koalice                        Koalice         Koalice           1            9995             koalice     S
    9999                Neregistrováno u MV                Neregistrováno u MV            Neregistrováno u MV Neregistr. u MV           1            9999 Neregistrováno u MV     S
```

### 201. [D] Volby do Senátu Parlamentu ČR 2020 konané dne 2.10. - 3.10.2020 - okrsková data

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 TYP_FORM  OPRAVA  CHYBA   OBEC  OKRSEK  KC_1  OBVOD  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0 503916       1     1      3     1         454         152         151         150   911         7         9        17        34        22        22         0        32         7         0         0         0         0         0         0         0         0         0         0         0         0         0   773  1684          9  507296
        1       0      0 503916       1     1      3     2         455          47          47          47   601         0         0        13         0        34         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   209   810          5  505544
        1       0      0 538795       1     5      3     1         506         151         151         143   955         5        21        28         7        52         9         1        11         9         0         0         0         0         0         0         0         0         0         0         0         0         0   649  1604          9  542019
        1       0      0 538795       1     5      3     2         508          62          62          61   698         0         0        14         0        47         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   277   975          5  540757
        1       0      0 538817       1     3      3     1         160          53          48          48   313         4        11         7         2        12         3         2         2         5         0         0         0         0         0         0         0         0         0         0         0         0         0   208   521          9  539873
```

#### TAIL

```
 TYP_FORM  OPRAVA  CHYBA   OBEC  OKRSEK  KC_1  OBVOD  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0 592820       1     0     81     2        1201         188         188         187  1847         0       134         0         0        53         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   533  2380          5  597587
        1       0      0 592820       2     1     81     1        1240         479         470         448  2719        36       126       140        21       125         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0  1417  4136          5  601101
        1       0      0 592820       2     1     81     2        1244         236         236         236  2035         0       163         0         0        73         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   691  2726          5  598281
        1       0      0 592862       1     0     81     1        1334         518         508         489  2931        43       150        86        25       185         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0  1626  4557          5  601983
        1       0      0 592862       1     0     81     2        1336         294         294         294  2301         0       176         0         0       118         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   942  3243          5  599355
```

### 202. [D] Volby do Senátu Parlamentu ČR 2020 konané dne 2.10. - 3.10.2020 - číselníky

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRAJ  OKRES  CPOU  ORP   OBEC                NAZEVOBCE  OBVOD  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  OBEC_PREZ
 7200   7204   662 7213 500011 Želechovice nad Dřevnicí     78           1           3           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500011
 1100   1100     1 1000 500054                  Praha 1     27        1000        1021           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500054
 1100   1100     2 1000 500089                  Praha 2     27        2032        2045           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500089
 1100   1100    11 1000 500143                  Praha 5     21        5003        5081        5000        5000           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500143
 1100   1100    11 1000 500143                  Praha 5     27        5001        5002           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500143
```

#### TAIL

```
 KRAJ  OKRES  CPOU  ORP   OBEC         NAZEVOBCE  OBVOD  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  OBEC_PREZ
 2100   2111   197 2120 599751         Modřovice     18           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599751
 2100   2112   206 2121 599760            Račice      6           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599760
 8100   8104   793 8116 599867            Spálov     63           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599867
 8100   8104   792 8115 599905       Starý Jičín     63           1           8           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599905
 8100   8104   792 8115 599930 Suchdol nad Odrou     63           1           2           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599930
```

### 203. [D] Volby do Senátu Parlamentu ČR 2022 - registr kandidátů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBVOD  CKAND  VSTRANA   JMENO    PRIJMENI TITULPRED TITULZA  VEK                                                                     POVOLANI    BYDLISTEN  BYDLISTEK  PSTRANA  NSTRANA PLATNOST  HLASY_K1  PROC_K1  URIZ_PR_K1  ZVOLEN_K1  LOS_K1  HLASY_K2  PROC_K2  URIZ_PR_K2  ZVOLEN_K2  LOS_K2                         NAZEV_VS
     1      1       80   Pavel    Petričko       NaN     NaN   71                                                            zdravotní potřeby       Ostrov     555428       99       80        A      1376     4.26    4.265741          0       0         0     0.00    0.000000          0       0               Nezávislý kandidát
     1      2     1114     Eva   Chromcová      Ing.     NaN   45                       operátor Zdravotnické záchranné služby - vedoucí směny Karlovy Vary     554961       99     1114        A      4557    14.12   14.127166          2       0      2791    32.02   32.025244          0       0 Svoboda a přímá demokracie (SPD)
     1      3      720  Bohdan       Vaněk      Ing.    M.A.   48                                     ekonomický analytik a projektový manažer Karlovy Vary     554961      720      720        A      1838     5.69    5.697988          0       0         0     0.00    0.000000          0       0            Česká pirátská strana
     1      4     1244 Bedřich      Šmudla       NaN     NaN   60                                                                      manažer        Sadov     555533     1244     1244        A       524     1.62    1.624454          0       0         0     0.00    0.000000          0       0                        Hnutí PES
     1      5      768    Věra Procházková     MUDr.     NaN   68 bývalá poslankyně, lékařka Zdravotnické záchranné služby Karlovarského kraje Karlovy Vary     554961      768      768        A      8343    25.86   25.864154          2       0      5924    67.97   67.974756          1       0                         ANO 2011
```

#### TAIL

```
 OBVOD  CKAND  VSTRANA     JMENO   PRIJMENI TITULPRED TITULZA  VEK                                                                                     POVOLANI BYDLISTEN  BYDLISTEK  PSTRANA  NSTRANA PLATNOST  HLASY_K1  PROC_K1  URIZ_PR_K1  ZVOLEN_K1  LOS_K1  HLASY_K2  PROC_K2  URIZ_PR_K2  ZVOLEN_K2  LOS_K2                                                      NAZEV_VS
    79      3      768 Ladislava Brančíková     PhDr.     NaN   58                                             ředitelka Centra služeb pro seniory Kyjov, p. o.    Vracov     586765       99      768        A     12211    27.70   27.706934          2       0     10919    48.38   48.386954          0       0                                                      ANO 2011
    79      4       47     Lenka    Ingrová      Mgr.    DiS.   44 projektová manažerka, předsedkyně Okresního výboru Komunistické strany Čech a Moravy Hodonín   Hodonín     586021       47       47        A      2461     5.58    5.584044          0       0         0     0.00    0.000000          0       0                             Komunistická strana Čech a Moravy
    79      5      720       Ivo    Vašíček   PaedDr.     NaN   60                                                                           krajský zastupitel Čejkovice     586102      720      720        A      1515     3.43    3.437557          0       0         0     0.00    0.000000          0       0                                         Česká pirátská strana
    79      6     1114 Vítězslav   Krabička     JUDr.     NaN   63                                                           advokát, zastupitel města Hodonína   Hodonín     586021     1114     1114        A      5245    11.90   11.900980          0       0         0     0.00    0.000000          0       0                              Svoboda a přímá demokracie (SPD)
    79      7     1520    Zbyněk   Pastyřík      Ing.     MBA   41                                                                      starosta obce Dambořice Dambořice     586129       99     1190        A      3631     8.23    8.238791          0       0         0     0.00    0.000000          0       0 Koalice Moravského zemského hnutí a politické strany Moravané
```

### 204. [D] Volby do Senátu Parlamentu ČR 2022 - registr kandidátů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBVOD  CKAND  VSTRANA   JMENO    PRIJMENI TITULPRED TITULZA  VEK                                                                     POVOLANI    BYDLISTEN  BYDLISTEK  PSTRANA  NSTRANA PLATNOST  HLASY_K1  PROC_K1  URIZ_PR_K1  ZVOLEN_K1  LOS_K1  HLASY_K2  PROC_K2  URIZ_PR_K2  ZVOLEN_K2  LOS_K2                         NAZEV_VS
     1      1       80   Pavel    Petričko       NaN     NaN   71                                                            zdravotní potřeby       Ostrov     555428       99       80        A      1376     4.26    4.265741          0       0         0     0.00    0.000000          0       0               Nezávislý kandidát
     1      2     1114     Eva   Chromcová      Ing.     NaN   45                       operátor Zdravotnické záchranné služby - vedoucí směny Karlovy Vary     554961       99     1114        A      4557    14.12   14.127166          2       0      2791    32.02   32.025244          0       0 Svoboda a přímá demokracie (SPD)
     1      3      720  Bohdan       Vaněk      Ing.    M.A.   48                                     ekonomický analytik a projektový manažer Karlovy Vary     554961      720      720        A      1838     5.69    5.697988          0       0         0     0.00    0.000000          0       0            Česká pirátská strana
     1      4     1244 Bedřich      Šmudla       NaN     NaN   60                                                                      manažer        Sadov     555533     1244     1244        A       524     1.62    1.624454          0       0         0     0.00    0.000000          0       0                        Hnutí PES
     1      5      768    Věra Procházková     MUDr.     NaN   68 bývalá poslankyně, lékařka Zdravotnické záchranné služby Karlovarského kraje Karlovy Vary     554961      768      768        A      8343    25.86   25.864154          2       0      5924    67.97   67.974756          1       0                         ANO 2011
```

#### TAIL

```
 OBVOD  CKAND  VSTRANA     JMENO   PRIJMENI TITULPRED TITULZA  VEK                                                                                     POVOLANI BYDLISTEN  BYDLISTEK  PSTRANA  NSTRANA PLATNOST  HLASY_K1  PROC_K1  URIZ_PR_K1  ZVOLEN_K1  LOS_K1  HLASY_K2  PROC_K2  URIZ_PR_K2  ZVOLEN_K2  LOS_K2                                                      NAZEV_VS
    79      3      768 Ladislava Brančíková     PhDr.     NaN   58                                             ředitelka Centra služeb pro seniory Kyjov, p. o.    Vracov     586765       99      768        A     12211    27.70   27.706934          2       0     10919    48.38   48.386954          0       0                                                      ANO 2011
    79      4       47     Lenka    Ingrová      Mgr.    DiS.   44 projektová manažerka, předsedkyně Okresního výboru Komunistické strany Čech a Moravy Hodonín   Hodonín     586021       47       47        A      2461     5.58    5.584044          0       0         0     0.00    0.000000          0       0                             Komunistická strana Čech a Moravy
    79      5      720       Ivo    Vašíček   PaedDr.     NaN   60                                                                           krajský zastupitel Čejkovice     586102      720      720        A      1515     3.43    3.437557          0       0         0     0.00    0.000000          0       0                                         Česká pirátská strana
    79      6     1114 Vítězslav   Krabička     JUDr.     NaN   63                                                           advokát, zastupitel města Hodonína   Hodonín     586021     1114     1114        A      5245    11.90   11.900980          0       0         0     0.00    0.000000          0       0                              Svoboda a přímá demokracie (SPD)
    79      7     1520    Zbyněk   Pastyřík      Ing.     MBA   41                                                                      starosta obce Dambořice Dambořice     586129       99     1190        A      3631     8.23    8.238791          0       0         0     0.00    0.000000          0       0 Koalice Moravského zemského hnutí a politické strany Moravané
```

### 205. [D] Volby do Senátu Parlamentu ČR 2024 - registr kandidátů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBVOD  CKAND  VSTRANA    JMENO              PRIJMENI TITULPRED  TITULZA  VEK                                                               POVOLANI     BYDLISTEN  PSTRANA  NSTRANA PLATNOST  HLASY_K1  PROC_K1  URIZ_PR_K1  ZVOLEN_K1  LOS_K1  HLASY_K2  PROC_K2  URIZ_PR_K2  ZVOLEN_K2  LOS_K2                                                  NAZEV_VS
     2      1     1487    Josef                 Vaněk     JUDr.      NaN   75 právník, živnostník v oblasti cestovního ruchu, zastupitel obce Hazlov        Hazlov       99     1114        A      1173     5.20    5.208241          0       0         0      0.0         0.0          0       0                                           SPD a Trikolora
     2      2      768     Jana Mračková Vildumetzová      Mgr.      NaN   51                                               poslankyně Parlamentu ČR  Karlovy Vary      768      768        A     11424    50.72   50.723737          1       0         0      0.0         0.0          0       0                                                  ANO 2011
     2      3     1270     Dana            Wittnerová      Mgr.      NaN   60                                                 středoškolská učitelka       Sokolov       99     1270        A       743     3.29    3.298997          0       0         0      0.0         0.0          0       0                                            SRDCEM PRO ...
     2      4      112 Alexandr                 Terek       NaN      NaN   44                                                         starosta města Horní Slavkov       99      112        A       833     3.69    3.698606          0       0         0      0.0         0.0          0       0 MÍSTNÍ HNUTÍ NEZÁVISLÝCH ZA HARMONICKÝ ROZVOJ OBCÍ A MĚST
     2      5     1118      Jan                 Picka       Bc.      NaN   58                                            místostarosta města Sokolov       Sokolov     1118     1118        A      2626    11.65   11.659711          0       0         0      0.0         0.0          0       0                                            Volba pro kraj
```

#### TAIL

```
 OBVOD  CKAND  VSTRANA        JMENO    PRIJMENI        TITULPRED    TITULZA  VEK                                                                                                                                                                                              POVOLANI    BYDLISTEN  PSTRANA  NSTRANA PLATNOST  HLASY_K1  PROC_K1  URIZ_PR_K1  ZVOLEN_K1  LOS_K1  HLASY_K2  PROC_K2  URIZ_PR_K2  ZVOLEN_K2  LOS_K2               NAZEV_VS
    80      2       80        David      Rumpík            MUDr.      Ph.D.   54                                                                                                                                        lékař, ředitel Kliniky reprodukční medicíny a gynekologie Zlín   Luhačovice       99       80        A      4196    14.71   14.715578          0       0         0     0.00    0.000000          0       0     Nezávislý kandidát
    80      3        1       Patrik      Kunčar             Ing.        NaN   51                                                                                                                                                                                               senátor Uherský Brod        1        1        A      7460    26.16   26.162587          2       0      8095    47.83   47.839962          0       0                KDU-ČSL
    80      4      768      Oldřich       Hájek doc. RNDr. PhDr. Ph.D., MBA   43 ekonom a včelař, děkan Fakulty veřejnosprávních a ekonomických studií v UH a garant programu Včelařství, realizátor bezplatných přednášek na téma ŠÍŘENÍ SRŠNĚ ASIJSKÉ, provozovatel www.senator24.cz         Zlín       99      768        A     10534    36.94   36.943256          2       0      8826    52.16   52.160038          1       0               ANO 2011
    80      5       88         Jana Juřenčáková             Ing.        NaN   61                                                                                                                                                                    daňový poradce a ekonomický expert    Rokytnice       99       88        A      2940    10.31   10.310725          0       0         0     0.00    0.000000          0       0              NEZÁVISLÍ
    80      6      166 Zbyněk Ziggy     Horváth              NaN        NaN   54                                                                                                                                                          lektor osvěty a primární prevence, písničkář    Spytihněv      166      166        A      1556     5.45    5.456969          0       0         0     0.00    0.000000          0       0 STAROSTOVÉ A NEZÁVISLÍ
```

### 206. [D] Volby do Senátu Parlamentu ČR 2024 - registr kandidátů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBVOD  CKAND  VSTRANA    JMENO              PRIJMENI TITULPRED  TITULZA  VEK                                                               POVOLANI     BYDLISTEN  PSTRANA  NSTRANA PLATNOST  HLASY_K1  PROC_K1  URIZ_PR_K1  ZVOLEN_K1  LOS_K1  HLASY_K2  PROC_K2  URIZ_PR_K2  ZVOLEN_K2  LOS_K2                                                  NAZEV_VS
     2      1     1487    Josef                 Vaněk     JUDr.      NaN   75 právník, živnostník v oblasti cestovního ruchu, zastupitel obce Hazlov        Hazlov       99     1114        A      1173     5.20    5.208241          0       0         0      0.0         0.0          0       0                                           SPD a Trikolora
     2      2      768     Jana Mračková Vildumetzová      Mgr.      NaN   51                                               poslankyně Parlamentu ČR  Karlovy Vary      768      768        A     11424    50.72   50.723737          1       0         0      0.0         0.0          0       0                                                  ANO 2011
     2      3     1270     Dana            Wittnerová      Mgr.      NaN   60                                                 středoškolská učitelka       Sokolov       99     1270        A       743     3.29    3.298997          0       0         0      0.0         0.0          0       0                                            SRDCEM PRO ...
     2      4      112 Alexandr                 Terek       NaN      NaN   44                                                         starosta města Horní Slavkov       99      112        A       833     3.69    3.698606          0       0         0      0.0         0.0          0       0 MÍSTNÍ HNUTÍ NEZÁVISLÝCH ZA HARMONICKÝ ROZVOJ OBCÍ A MĚST
     2      5     1118      Jan                 Picka       Bc.      NaN   58                                            místostarosta města Sokolov       Sokolov     1118     1118        A      2626    11.65   11.659711          0       0         0      0.0         0.0          0       0                                            Volba pro kraj
```

#### TAIL

```
 OBVOD  CKAND  VSTRANA        JMENO    PRIJMENI        TITULPRED    TITULZA  VEK                                                                                                                                                                                              POVOLANI    BYDLISTEN  PSTRANA  NSTRANA PLATNOST  HLASY_K1  PROC_K1  URIZ_PR_K1  ZVOLEN_K1  LOS_K1  HLASY_K2  PROC_K2  URIZ_PR_K2  ZVOLEN_K2  LOS_K2               NAZEV_VS
    80      2       80        David      Rumpík            MUDr.      Ph.D.   54                                                                                                                                        lékař, ředitel Kliniky reprodukční medicíny a gynekologie Zlín   Luhačovice       99       80        A      4196    14.71   14.715578          0       0         0     0.00    0.000000          0       0     Nezávislý kandidát
    80      3        1       Patrik      Kunčar             Ing.        NaN   51                                                                                                                                                                                               senátor Uherský Brod        1        1        A      7460    26.16   26.162587          2       0      8095    47.83   47.839962          0       0                KDU-ČSL
    80      4      768      Oldřich       Hájek doc. RNDr. PhDr. Ph.D., MBA   43 ekonom a včelař, děkan Fakulty veřejnosprávních a ekonomických studií v UH a garant programu Včelařství, realizátor bezplatných přednášek na téma ŠÍŘENÍ SRŠNĚ ASIJSKÉ, provozovatel www.senator24.cz         Zlín       99      768        A     10534    36.94   36.943256          2       0      8826    52.16   52.160038          1       0               ANO 2011
    80      5       88         Jana Juřenčáková             Ing.        NaN   61                                                                                                                                                                    daňový poradce a ekonomický expert    Rokytnice       99       88        A      2940    10.31   10.310725          0       0         0     0.00    0.000000          0       0              NEZÁVISLÍ
    80      6      166 Zbyněk Ziggy     Horváth              NaN        NaN   54                                                                                                                                                          lektor osvěty a primární prevence, písničkář    Spytihněv      166      166        A      1556     5.45    5.456969          0       0         0     0.00    0.000000          0       0 STAROSTOVÉ A NEZÁVISLÍ
```

### 207. [D] Volby do Senátu Parlamentu ČR 2022 - složení volebních stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA  NSTRANA
       1        1
       2        2
       4        4
       5        5
       7        7
```

#### TAIL

```
 VSTRANA  NSTRANA
    1628     1114
    1628     1227
    1628     1244
    9995     9995
    9999     9999
```

### 208. [D] Volby do Senátu Parlamentu ČR 2024 - složení volebních stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA  NSTRANA
       1        1
       2        2
       3        3
       4        4
       5        5
```

#### TAIL

```
 VSTRANA  NSTRANA
    1679     1285
    1680      143
    1680     1228
    9995     9995
    9999     9999
```

### 209. [D] Volby do Senátu Parlamentu ČR 2022 - výsledky za okrsky

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 TYP_FORM  OPRAVA  CHYBA   OBEC  OKRSEK  KC_1  OBVOD  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0 500101       1     1      1     1         170          71          71          69   383         0        10         1         0        34         7         0         1         5         8         3         0         0         0         0         0         0         0         0         0         0         0   401   784         11  501683
        1       0      0 500101       1     1      1     2         170          11          11          11   206         0         3         0         0         8         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    46   252          5  500613
        1       0      0 500127       1     5      1     1         130          57          57          56   302         2        11         2         1        14        14         0         0         6         2         4         0         0         0         0         0         0         0         0         0         0         0   306   608         11  501361
        1       0      0 500127       1     5      1     2         130          23          23          23   202         0         7         0         0        16         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    94   296          5  500731
        1       0      0 506486       1     6      1     1         198         127         127         127   581         5         2         5         0         5        21         0         0        18         2        69         0         0         0         0         0         0         0         0         0         0         0  1116  1697         11  509899
```

#### TAIL

```
 TYP_FORM  OPRAVA  CHYBA   OBEC  OKRSEK  KC_1  OBVOD  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0 586811       1     6     79     2         440         100         100          98   819         0        55        43         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   239  1058          3  588938
        1       0      0 586820       1     2     79     1         859         373         365         353  2030        90        41       125        17         2        38        40         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0  1133  3163          7  593157
        1       0      0 586820       1     2     79     2         861         165         165         163  1435         0        53       110         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   436  1871          3  590569
        1       0      0 593354       1     3     79     1         258         109         109         106   662        19         3        40         7         2        28         7         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   400  1062          7  595490
        1       0      0 593354       1     3     79     2         258          38          38          37   452         0         4        33         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   107   559          3  594480
```

### 210. [D] Volby do Senátu Parlamentu ČR 2022 - výsledky za okrsky

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 TYP_FORM  OPRAVA  CHYBA   OBEC  OKRSEK  KC_1  OBVOD  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0 500101       1     1      1     1         170          71          71          69   383         0        10         1         0        34         7         0         1         5         8         3         0         0         0         0         0         0         0         0         0         0         0   401   784         11  501683
        1       0      0 500101       1     1      1     2         170          11          11          11   206         0         3         0         0         8         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    46   252          5  500613
        1       0      0 500127       1     5      1     1         130          57          57          56   302         2        11         2         1        14        14         0         0         6         2         4         0         0         0         0         0         0         0         0         0         0         0   306   608         11  501361
        1       0      0 500127       1     5      1     2         130          23          23          23   202         0         7         0         0        16         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0    94   296          5  500731
        1       0      0 506486       1     6      1     1         198         127         127         127   581         5         2         5         0         5        21         0         0        18         2        69         0         0         0         0         0         0         0         0         0         0         0  1116  1697         11  509899
```

#### TAIL

```
 TYP_FORM  OPRAVA  CHYBA   OBEC  OKRSEK  KC_1  OBVOD  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0 586811       1     6     79     2         440         100         100          98   819         0        55        43         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   239  1058          3  588938
        1       0      0 586820       1     2     79     1         859         373         365         353  2030        90        41       125        17         2        38        40         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0  1133  3163          7  593157
        1       0      0 586820       1     2     79     2         861         165         165         163  1435         0        53       110         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   436  1871          3  590569
        1       0      0 593354       1     3     79     1         258         109         109         106   662        19         3        40         7         2        28         7         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   400  1062          7  595490
        1       0      0 593354       1     3     79     2         258          38          38          37   452         0         4        33         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   107   559          3  594480
```

### 211. [D] Volby do Senátu Parlamentu ČR 2024 - výsledky za okrsky

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 TYP_FORM  OPRAVA  CHYBA   OBEC  OKRSEK  KC_1  OBVOD  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0 511587       1     3      2     1         331         118         118         117   687        14        50         5         6        21        21         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   384  1071          6  513740
        1       0      0 538337       1     4      2     1         596         191         191         186  1167         9        83         6        15        26        47         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   665  1832          6  542013
        1       0      0 538396       1     5      2     1         329         124         124         123   703         6        42         2         1        22        50         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   510  1213          6  540835
        1       0      0 538434       1     6      2     1        1328         416         404         397  2548        15       202        13        11        44       112         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0  1394  3942          6  546332
        1       0      0 538591       1     0      2     1        1060         361         361         359  2144        14       156        12        12        62       103         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0  1338  3482          6  545563
```

#### TAIL

```
 TYP_FORM  OPRAVA  CHYBA   OBEC  OKRSEK  KC_1  OBVOD  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0 592846       1     4     80     2         821         142         142         140  1327         0         0        63        77         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   497  1824          4  596504
        1       0      0 592854       1     2     80     1         256          84          84          83   588         7         5        21        35         2        13         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   308   896          6  594656
        1       0      0 592854       1     2     80     2         256          41          41          41   461         0         0        19        22         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   145   606          4  594074
        1       0      0 592871       1     3     80     1         138          56          55          55   385         7         1        10        32         1         4         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   196   581          6  594044
        1       0      0 592871       1     3     80     2         138          33          33          33   319         0         0         8        25         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   124   443          4  593766
```

### 212. [D] Volby do Senátu Parlamentu ČR 2024 - výsledky za okrsky

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 TYP_FORM  OPRAVA  CHYBA   OBEC  OKRSEK  KC_1  OBVOD  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0 511587       1     3      2     1         331         118         118         117   687        14        50         5         6        21        21         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   384  1071          6  513740
        1       0      0 538337       1     4      2     1         596         191         191         186  1167         9        83         6        15        26        47         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   665  1832          6  542013
        1       0      0 538396       1     5      2     1         329         124         124         123   703         6        42         2         1        22        50         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   510  1213          6  540835
        1       0      0 538434       1     6      2     1        1328         416         404         397  2548        15       202        13        11        44       112         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0  1394  3942          6  546332
        1       0      0 538591       1     0      2     1        1060         361         361         359  2144        14       156        12        12        62       103         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0  1338  3482          6  545563
```

#### TAIL

```
 TYP_FORM  OPRAVA  CHYBA   OBEC  OKRSEK  KC_1  OBVOD  KOLO  VOL_SEZNAM  VYD_OBALKY  ODEVZ_OBAL  PL_HL_CELK  KC_2  HLASY_01  HLASY_02  HLASY_03  HLASY_04  HLASY_05  HLASY_06  HLASY_07  HLASY_08  HLASY_09  HLASY_10  HLASY_11  HLASY_12  HLASY_13  HLASY_14  HLASY_15  HLASY_16  HLASY_17  HLASY_18  HLASY_19  HLASY_20  HLASY_21  HLASY_22  KC_3  KC_4  POSL_KAND  KC_SUM
        1       0      0 592846       1     4     80     2         821         142         142         140  1327         0         0        63        77         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   497  1824          4  596504
        1       0      0 592854       1     2     80     1         256          84          84          83   588         7         5        21        35         2        13         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   308   896          6  594656
        1       0      0 592854       1     2     80     2         256          41          41          41   461         0         0        19        22         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   145   606          4  594074
        1       0      0 592871       1     3     80     1         138          56          55          55   385         7         1        10        32         1         4         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   196   581          6  594044
        1       0      0 592871       1     3     80     2         138          33          33          33   319         0         0         8        25         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0   124   443          4  593766
```

### 213. [D] Volby do Senátu Parlamentu ČR 2022 - číselník navrhujících stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NSTRANA                         NAZEV_STRN                    ZKRATKAN30 ZKRATKAN8
       1                            KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2      Česká strana národně sociální Česká strana národně sociální      ČSNS
       4      Liberálně demokratická strana Liberálně demokratická strana       LDS
       5                    Strana zelených               Strana zelených    Zelení
       7 Česká strana sociálně demokratická  Česká str.sociálně demokrat.      ČSSD
```

#### TAIL

```
 NSTRANA               NAZEV_STRN               ZKRATKAN30       ZKRATKAN8
    1278                Hnutí NEJ                Hnutí NEJ             NEJ
    1279      HNUTÍ SPRÁVNÁ CESTA      HNUTÍ SPRÁVNÁ CESTA   SPRÁVNÁ CESTA
    1280 Malá strana velkých cílů Malá strana velkých cílů            MSVC
    9995                  Koalice                  Koalice         Koalice
    9999      Neregistrováno u MV      Neregistrováno u MV Neregistr. u MV
```

### 214. [D] Volby do Senátu Parlamentu ČR 2022 - číselník navrhujících stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NSTRANA                         NAZEV_STRN                    ZKRATKAN30 ZKRATKAN8
       1                            KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2      Česká strana národně sociální Česká strana národně sociální      ČSNS
       4      Liberálně demokratická strana Liberálně demokratická strana       LDS
       5                    Strana zelených               Strana zelených    Zelení
       7 Česká strana sociálně demokratická  Česká str.sociálně demokrat.      ČSSD
```

#### TAIL

```
 NSTRANA               NAZEV_STRN               ZKRATKAN30       ZKRATKAN8
    1278                Hnutí NEJ                Hnutí NEJ             NEJ
    1279      HNUTÍ SPRÁVNÁ CESTA      HNUTÍ SPRÁVNÁ CESTA   SPRÁVNÁ CESTA
    1280 Malá strana velkých cílů Malá strana velkých cílů            MSVC
    9995                  Koalice                  Koalice         Koalice
    9999      Neregistrováno u MV      Neregistrováno u MV Neregistr. u MV
```

### 215. [D] Volby do Senátu Parlamentu ČR 2024 - číselník navrhujících stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NSTRANA                    NAZEV_STRN                    ZKRATKAN30 ZKRATKAN8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       4 Liberálně demokratická strana Liberálně demokratická strana       LDS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
```

#### TAIL

```
 NSTRANA                                        NAZEV_STRN                    ZKRATKAN30       ZKRATKAN8
    1292                     MÁ VLAST ČECHY MORAVA SLEZSKO MÁ VLAST ČECHY MORAVA SLEZSKO    MÁ VLAST ČMS
    1293            Nadační občansko-politické hnutí ReMeK Nadační obč.-pol. hnutí ReMeK           ReMeK
    1294 Nestraníci pro jižní Moravu-www.nestranici2024.cz   Nestraníci pro jižní Moravu  Nestranici2024
    9995                                           Koalice                       Koalice         Koalice
    9999                               Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 216. [D] Volby do Senátu Parlamentu ČR 2024 - číselník navrhujících stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NSTRANA                    NAZEV_STRN                    ZKRATKAN30 ZKRATKAN8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       4 Liberálně demokratická strana Liberálně demokratická strana       LDS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
```

#### TAIL

```
 NSTRANA                                        NAZEV_STRN                    ZKRATKAN30       ZKRATKAN8
    1292                     MÁ VLAST ČECHY MORAVA SLEZSKO MÁ VLAST ČECHY MORAVA SLEZSKO    MÁ VLAST ČMS
    1293            Nadační občansko-politické hnutí ReMeK Nadační obč.-pol. hnutí ReMeK           ReMeK
    1294 Nestraníci pro jižní Moravu-www.nestranici2024.cz   Nestraníci pro jižní Moravu  Nestranici2024
    9995                                           Koalice                       Koalice         Koalice
    9999                               Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 217. [D] Volby do Senátu Parlamentu ČR 2022 - číselník obcí, městských částí, městských obvodů, katastrů a volebních okrsků

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRAJ  OKRES  CPOU  ORP   OBEC          NAZEVOBCE  OBVOD  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  OBEC_PREZ
 8100   8104   792 8115 500046            Libhošť     67           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500046
 4100   4102   308 4103 500101             Bražec      1           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500101
 4100   4102   310 4106 500127 Doupovské Hradiště      1           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500127
 7100   7102   803 7107 500135             Kozlov     61           1           2           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500135
 7100   7102   804 7110 500160       Město Libavá     61           1           2           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500160
```

#### TAIL

```
 KRAJ  OKRES  CPOU  ORP   OBEC   NAZEVOBCE  OBVOD  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  OBEC_PREZ
 8100   8104   795 8101 599921    Studénka     67           1           8           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599921
 8100   8104   791 8112 599948   Štramberk     67           1           4           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599948
 8100   8104   789 8105 599956       Tichá     67           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599956
 8100   8104   788 8101 599964       Tísek     67           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599964
 8100   8104   789 8105 599999 Trojanovice     67           1           2           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599999
```

### 218. [D] Volby do Senátu Parlamentu ČR 2022 - číselník obcí, městských částí, městských obvodů, katastrů a volebních okrsků

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRAJ  OKRES  CPOU  ORP   OBEC          NAZEVOBCE  OBVOD  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  OBEC_PREZ
 8100   8104   792 8115 500046            Libhošť     67           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500046
 4100   4102   308 4103 500101             Bražec      1           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500101
 4100   4102   310 4106 500127 Doupovské Hradiště      1           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500127
 7100   7102   803 7107 500135             Kozlov     61           1           2           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500135
 7100   7102   804 7110 500160       Město Libavá     61           1           2           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500160
```

#### TAIL

```
 KRAJ  OKRES  CPOU  ORP   OBEC   NAZEVOBCE  OBVOD  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  OBEC_PREZ
 8100   8104   795 8101 599921    Studénka     67           1           8           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599921
 8100   8104   791 8112 599948   Štramberk     67           1           4           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599948
 8100   8104   789 8105 599956       Tichá     67           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599956
 8100   8104   788 8101 599964       Tísek     67           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599964
 8100   8104   789 8105 599999 Trojanovice     67           1           2           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599999
```

### 219. [D] Volby do Senátu Parlamentu ČR 2024 - číselník obcí, městských částí, městských obvodů, katastrů a volebních okrsků

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRAJ  OKRES  CPOU  ORP   OBEC         NAZEVOBCE  OBVOD  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  OBEC_PREZ
 7100   7105   860 7111 500020 Petrov nad Desnou     65           1           2           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500020
 7200   7203   871 7210 500062            Krhová     77           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500062
 7200   7203   871 7210 500071           Poličná     77           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500071
 1100   1100     2 1000 500089           Praha 2     26        2001        2032           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500089
 1100   1100     3 1000 500097           Praha 3     26        3001        3052           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500097
```

#### TAIL

```
 KRAJ  OKRES  CPOU  ORP   OBEC    NAZEVOBCE  OBVOD  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  OBEC_PREZ
 2100   2107   157 2115 599522   Husí Lhota     38           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599522
 2100   2107   155 2115 599531 Horní Slivno     38           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599531
 2100   2107   158 2116 599557       Koryta     38           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599557
 2100   2107   158 2116 599573     Sezemice     38           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599573
 2100   2109   178 2122 599719      Tehovec     41           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599719
```

### 220. [D] Volby do Senátu Parlamentu ČR 2024 - číselník obcí, městských částí, městských obvodů, katastrů a volebních okrsků

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 KRAJ  OKRES  CPOU  ORP   OBEC         NAZEVOBCE  OBVOD  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  OBEC_PREZ
 7100   7105   860 7111 500020 Petrov nad Desnou     65           1           2           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500020
 7200   7203   871 7210 500062            Krhová     77           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500062
 7200   7203   871 7210 500071           Poličná     77           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500071
 1100   1100     2 1000 500089           Praha 2     26        2001        2032           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500089
 1100   1100     3 1000 500097           Praha 3     26        3001        3052           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     500097
```

#### TAIL

```
 KRAJ  OKRES  CPOU  ORP   OBEC    NAZEVOBCE  OBVOD  MINOKRSEK1  MAXOKRSEK1  MINOKRSEK2  MAXOKRSEK2  MINOKRSEK3  MAXOKRSEK3  MINOKRSEK4  MAXOKRSEK4  MINOKRSEK5  MAXOKRSEK5  MINOKRSEK6  MAXOKRSEK6  MINOKRSEK7  MAXOKRSEK7  MINOKRSEK8  MAXOKRSEK8  MINOKRSEK9  MAXOKRSEK9  MINOKRSE10  MAXOKRSE10  OBEC_PREZ
 2100   2107   157 2115 599522   Husí Lhota     38           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599522
 2100   2107   155 2115 599531 Horní Slivno     38           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599531
 2100   2107   158 2116 599557       Koryta     38           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599557
 2100   2107   158 2116 599573     Sezemice     38           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599573
 2100   2109   178 2122 599719      Tehovec     41           1           1           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0           0     599719
```

### 221. [D] Volby do Senátu Parlamentu ČR 2022 - číselník politické příslušnosti kandidátů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 PSTRANA                         NAZEV_STRP                    ZKRATKAP30 ZKRATKAP8
       1                            KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2      Česká strana národně sociální Česká strana národně sociální      ČSNS
       4      Liberálně demokratická strana Liberálně demokratická strana       LDS
       5                    Strana zelených               Strana zelených    Zelení
       7 Česká strana sociálně demokratická  Česká str.sociálně demokrat.      ČSSD
```

#### TAIL

```
 PSTRANA               NAZEV_STRP               ZKRATKAP30       ZKRATKAP8
    1277         Hnutí pro Žabiny         Hnutí pro Žabiny             HpŽ
    1278                Hnutí NEJ                Hnutí NEJ             NEJ
    1279      HNUTÍ SPRÁVNÁ CESTA      HNUTÍ SPRÁVNÁ CESTA   SPRÁVNÁ CESTA
    1280 Malá strana velkých cílů Malá strana velkých cílů            MSVC
    9999      Neregistrováno u MV      Neregistrováno u MV Neregistr. u MV
```

### 222. [D] Volby do Senátu Parlamentu ČR 2022 - číselník politické příslušnosti kandidátů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 PSTRANA                         NAZEV_STRP                    ZKRATKAP30 ZKRATKAP8
       1                            KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2      Česká strana národně sociální Česká strana národně sociální      ČSNS
       4      Liberálně demokratická strana Liberálně demokratická strana       LDS
       5                    Strana zelených               Strana zelených    Zelení
       7 Česká strana sociálně demokratická  Česká str.sociálně demokrat.      ČSSD
```

#### TAIL

```
 PSTRANA               NAZEV_STRP               ZKRATKAP30       ZKRATKAP8
    1277         Hnutí pro Žabiny         Hnutí pro Žabiny             HpŽ
    1278                Hnutí NEJ                Hnutí NEJ             NEJ
    1279      HNUTÍ SPRÁVNÁ CESTA      HNUTÍ SPRÁVNÁ CESTA   SPRÁVNÁ CESTA
    1280 Malá strana velkých cílů Malá strana velkých cílů            MSVC
    9999      Neregistrováno u MV      Neregistrováno u MV Neregistr. u MV
```

### 223. [D] Volby do Senátu Parlamentu ČR 2024 - číselník politické příslušnosti kandidátů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 PSTRANA                    NAZEV_STRP                    ZKRATKAP30 ZKRATKAP8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       4 Liberálně demokratická strana Liberálně demokratická strana       LDS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
```

#### TAIL

```
 PSTRANA                                        NAZEV_STRP                    ZKRATKAP30       ZKRATKAP8
    1291                                    Hnutí Generace                Hnutí Generace        Generace
    1292                     MÁ VLAST ČECHY MORAVA SLEZSKO MÁ VLAST ČECHY MORAVA SLEZSKO    MÁ VLAST ČMS
    1293            Nadační občansko-politické hnutí ReMeK Nadační obč.-pol. hnutí ReMeK           ReMeK
    1294 Nestraníci pro jižní Moravu-www.nestranici2024.cz   Nestraníci pro jižní Moravu  Nestranici2024
    9999                               Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 224. [D] Volby do Senátu Parlamentu ČR 2024 - číselník politické příslušnosti kandidátů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 PSTRANA                    NAZEV_STRP                    ZKRATKAP30 ZKRATKAP8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       4 Liberálně demokratická strana Liberálně demokratická strana       LDS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
```

#### TAIL

```
 PSTRANA                                        NAZEV_STRP                    ZKRATKAP30       ZKRATKAP8
    1291                                    Hnutí Generace                Hnutí Generace        Generace
    1292                     MÁ VLAST ČECHY MORAVA SLEZSKO MÁ VLAST ČECHY MORAVA SLEZSKO    MÁ VLAST ČMS
    1293            Nadační občansko-politické hnutí ReMeK Nadační obč.-pol. hnutí ReMeK           ReMeK
    1294 Nestraníci pro jižní Moravu-www.nestranici2024.cz   Nestraníci pro jižní Moravu  Nestranici2024
    9999                               Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 225. [D] Volby do Senátu Parlamentu ČR 2022 - číselník volebních obvodů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBVOD    NAZEV_OBV  OKRES  PRVNI_VO PLATNOST
     1 Karlovy Vary   4102         2        A
     2      Sokolov   4103         4        A
     3         Cheb   4101         6        A
     4         Most   4205         2        A
     5     Chomutov   4202         4        A
```

#### TAIL

```
 OBVOD        NAZEV_OBV  OKRES  PRVNI_VO PLATNOST
    77           Vsetín   7203         4        A
    78             Zlín   7204         6        A
    79          Hodonín   6205         2        A
    80             Zlín   7204         4        A
    81 Uherské Hradiště   7202         6        A
```

### 226. [D] Volby do Senátu Parlamentu ČR 2022 - číselník volebních obvodů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBVOD    NAZEV_OBV  OKRES  PRVNI_VO PLATNOST
     1 Karlovy Vary   4102         2        A
     2      Sokolov   4103         4        A
     3         Cheb   4101         6        A
     4         Most   4205         2        A
     5     Chomutov   4202         4        A
```

#### TAIL

```
 OBVOD        NAZEV_OBV  OKRES  PRVNI_VO PLATNOST
    77           Vsetín   7203         4        A
    78             Zlín   7204         6        A
    79          Hodonín   6205         2        A
    80             Zlín   7204         4        A
    81 Uherské Hradiště   7202         6        A
```

### 227. [D] Volby do Senátu Parlamentu ČR 2024 - číselník volebních obvodů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBVOD    NAZEV_OBV  OKRES  PRVNI_VO PLATNOST
     1 Karlovy Vary   4102         2        A
     2      Sokolov   4103         4        A
     3         Cheb   4101         6        A
     4         Most   4205         2        A
     5     Chomutov   4202         4        A
```

#### TAIL

```
 OBVOD        NAZEV_OBV  OKRES  PRVNI_VO PLATNOST
    77           Vsetín   7203         4        A
    78             Zlín   7204         6        A
    79          Hodonín   6205         2        A
    80             Zlín   7204         4        A
    81 Uherské Hradiště   7202         6        A
```

### 228. [D] Volby do Senátu Parlamentu ČR 2024 - číselník volebních obvodů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBVOD    NAZEV_OBV  OKRES  PRVNI_VO PLATNOST
     1 Karlovy Vary   4102         2        A
     2      Sokolov   4103         4        A
     3         Cheb   4101         6        A
     4         Most   4205         2        A
     5     Chomutov   4202         4        A
```

#### TAIL

```
 OBVOD        NAZEV_OBV  OKRES  PRVNI_VO PLATNOST
    77           Vsetín   7203         4        A
    78             Zlín   7204         6        A
    79          Hodonín   6205         2        A
    80             Zlín   7204         4        A
    81 Uherské Hradiště   7202         6        A
```

### 229. [D] Volby do Senátu Parlamentu ČR 2022 - číselník volebních stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA                          NAZEVCELK                         NAZEV_STRV                    ZKRATKAV30 ZKRATKAV8  POCSTR_SLO  SLOZENI ZKRATKA_OF TYPVS  PLNYNAZEV
       1                            KDU-ČSL                            KDU-ČSL                       KDU-ČSL   KDU-ČSL           1        1    KDU-ČSL     S        NaN
       2      Česká strana národně sociální      Česká strana národně sociální Česká strana národně sociální      ČSNS           1        2       ČSNS     S        NaN
       4      Liberálně demokratická strana      Liberálně demokratická strana Liberálně demokratická strana       LDS           1        4        NaN     S        NaN
       5                    Strana zelených                    Strana zelených               Strana zelených    Zelení           1        5     Zelení     S        NaN
       7 Česká strana sociálně demokratická Česká strana sociálně demokratická  Česká str.sociálně demokrat.      ČSSD           1        7       ČSSD     S        NaN
```

#### TAIL

```
 VSTRANA                                  NAZEVCELK                                 NAZEV_STRV                    ZKRATKAV30       ZKRATKAV8  POCSTR_SLO                SLOZENI          ZKRATKA_OF TYPVS  PLNYNAZEV
    1626                           Sdružení HpŽ, NK                           Sdružení HpŽ, NK              Sdružení HpŽ, NK          HpŽ+NK           2               080,1277                 NaN     D        NaN
    1627                      Sdružení PRO 2022, NK                      Sdružení PRO 2022, NK         Sdružení PRO 2022, NK     PRO 2022+NK           2               080,1265                 NaN     D        NaN
    1628 Sdružení Svobodní, SPD, Trikolora, PES, NK Sdružení Svobodní, SPD, Trikolora, PES, NK Svobodní,SPD,Trikolora,PES,NK SvoSPDTrikPESNK           5 080,714,1114,1227,1244                 NaN     D        NaN
    9995                                    Koalice                                    Koalice                       Koalice         Koalice           1                   9995             koalice     S        NaN
    9999                        Neregistrováno u MV                        Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV           1                   9999 Neregistrováno u MV     S        NaN
```

### 230. [D] Volby do Senátu Parlamentu ČR 2022 - číselník volebních stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA                          NAZEVCELK                         NAZEV_STRV                    ZKRATKAV30 ZKRATKAV8  POCSTR_SLO  SLOZENI ZKRATKA_OF TYPVS  PLNYNAZEV
       1                            KDU-ČSL                            KDU-ČSL                       KDU-ČSL   KDU-ČSL           1        1    KDU-ČSL     S        NaN
       2      Česká strana národně sociální      Česká strana národně sociální Česká strana národně sociální      ČSNS           1        2       ČSNS     S        NaN
       4      Liberálně demokratická strana      Liberálně demokratická strana Liberálně demokratická strana       LDS           1        4        NaN     S        NaN
       5                    Strana zelených                    Strana zelených               Strana zelených    Zelení           1        5     Zelení     S        NaN
       7 Česká strana sociálně demokratická Česká strana sociálně demokratická  Česká str.sociálně demokrat.      ČSSD           1        7       ČSSD     S        NaN
```

#### TAIL

```
 VSTRANA                                  NAZEVCELK                                 NAZEV_STRV                    ZKRATKAV30       ZKRATKAV8  POCSTR_SLO                SLOZENI          ZKRATKA_OF TYPVS  PLNYNAZEV
    1626                           Sdružení HpŽ, NK                           Sdružení HpŽ, NK              Sdružení HpŽ, NK          HpŽ+NK           2               080,1277                 NaN     D        NaN
    1627                      Sdružení PRO 2022, NK                      Sdružení PRO 2022, NK         Sdružení PRO 2022, NK     PRO 2022+NK           2               080,1265                 NaN     D        NaN
    1628 Sdružení Svobodní, SPD, Trikolora, PES, NK Sdružení Svobodní, SPD, Trikolora, PES, NK Svobodní,SPD,Trikolora,PES,NK SvoSPDTrikPESNK           5 080,714,1114,1227,1244                 NaN     D        NaN
    9995                                    Koalice                                    Koalice                       Koalice         Koalice           1                   9995             koalice     S        NaN
    9999                        Neregistrováno u MV                        Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV           1                   9999 Neregistrováno u MV     S        NaN
```

### 231. [D] Volby do Senátu Parlamentu ČR 2024 - číselník volebních stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA                     NAZEVCELK                    NAZEV_STRV                    ZKRATKAV30 ZKRATKAV8  POCSTR_SLO  SLOZENI ZKRATKA_OF TYPVS  PLNYNAZEV
       1                       KDU-ČSL                       KDU-ČSL                       KDU-ČSL   KDU-ČSL           1        1    KDU-ČSL     S        NaN
       2 Česká strana národně sociální Česká strana národně sociální Česká strana národně sociální      ČSNS           1        2       ČSNS     S        NaN
       3 Křesťanskodemokratická strana Křesťanskodemokratická strana Křesťanskodemokratická strana       KDS           1        3        KDS     S        NaN
       4 Liberálně demokratická strana Liberálně demokratická strana Liberálně demokratická strana       LDS           1        4        LDS     S        NaN
       5               Strana zelených               Strana zelených               Strana zelených    Zelení           1        5     Zelení     S        NaN
```

#### TAIL

```
 VSTRANA             NAZEVCELK            NAZEV_STRV            ZKRATKAV30       ZKRATKAV8  POCSTR_SLO  SLOZENI          ZKRATKA_OF TYPVS  PLNYNAZEV
    1678  Koalice Piráti a MHS  Koalice Piráti a MHS   Koalice Piráti, MHS      Piráti+MHS           2 720,1194                 NaN     K        NaN
    1679 Sdružení Vize KVK, NK Sdružení Vize KVK, NK Sdružení Vize KVK, NK     Vize KVK+NK           2 080,1285                 NaN     D        NaN
    1680 Koalice SD-SN a SproK Koalice SD-SN a SproK  Koalice SD-SN, SproK     SD-SN+SproK           2 143,1228                 NaN     K        NaN
    9995               Koalice               Koalice               Koalice         Koalice           1     9995             koalice     S        NaN
    9999   Neregistrováno u MV   Neregistrováno u MV   Neregistrováno u MV Neregistr. u MV           1     9999 Neregistrováno u MV     S        NaN
```

### 232. [D] Volby do Senátu Parlamentu ČR 2024 - číselník volebních stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA                     NAZEVCELK                    NAZEV_STRV                    ZKRATKAV30 ZKRATKAV8  POCSTR_SLO  SLOZENI ZKRATKA_OF TYPVS  PLNYNAZEV
       1                       KDU-ČSL                       KDU-ČSL                       KDU-ČSL   KDU-ČSL           1        1    KDU-ČSL     S        NaN
       2 Česká strana národně sociální Česká strana národně sociální Česká strana národně sociální      ČSNS           1        2       ČSNS     S        NaN
       3 Křesťanskodemokratická strana Křesťanskodemokratická strana Křesťanskodemokratická strana       KDS           1        3        KDS     S        NaN
       4 Liberálně demokratická strana Liberálně demokratická strana Liberálně demokratická strana       LDS           1        4        LDS     S        NaN
       5               Strana zelených               Strana zelených               Strana zelených    Zelení           1        5     Zelení     S        NaN
```

#### TAIL

```
 VSTRANA             NAZEVCELK            NAZEV_STRV            ZKRATKAV30       ZKRATKAV8  POCSTR_SLO  SLOZENI          ZKRATKA_OF TYPVS  PLNYNAZEV
    1678  Koalice Piráti a MHS  Koalice Piráti a MHS   Koalice Piráti, MHS      Piráti+MHS           2 720,1194                 NaN     K        NaN
    1679 Sdružení Vize KVK, NK Sdružení Vize KVK, NK Sdružení Vize KVK, NK     Vize KVK+NK           2 080,1285                 NaN     D        NaN
    1680 Koalice SD-SN a SproK Koalice SD-SN a SproK  Koalice SD-SN, SproK     SD-SN+SproK           2 143,1228                 NaN     K        NaN
    9995               Koalice               Koalice               Koalice         Koalice           1     9995             koalice     S        NaN
    9999   Neregistrováno u MV   Neregistrováno u MV   Neregistrováno u MV Neregistr. u MV           1     9999 Neregistrováno u MV     S        NaN
```

### 233. [D] Volby do Senátu Parlamentu ČR 2024 - číselník obcí

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBEC_PREZ                NAZEVOBCE
    500011 Želechovice nad Dřevnicí
    500020        Petrov nad Desnou
    500046                  Libhošť
    500054                  Praha 1
    500062                   Krhová
```

#### TAIL

```
 OBEC_PREZ          NAZEVOBCE
    599964              Tísek
    599999        Trojanovice
    727181 Praha 2-Nové Město
    727598        Praha 4-Krč
    730106    Praha 6-Bubeneč
```

### 234. [D] Volby do Senátu Parlamentu ČR 2024 - číselník obcí

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBEC_PREZ                NAZEVOBCE
    500011 Želechovice nad Dřevnicí
    500020        Petrov nad Desnou
    500046                  Libhošť
    500054                  Praha 1
    500062                   Krhová
```

#### TAIL

```
 OBEC_PREZ          NAZEVOBCE
    599964              Tísek
    599999        Trojanovice
    727181 Praha 2-Nové Město
    727598        Praha 4-Krč
    730106    Praha 6-Bubeneč
```

### 235. [D] Sčítání 2021 - Vyjíždějící do zaměstnání a školy podle cílového území a pohlaví

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  bydliste_cis  bydliste_kod  cil_dojizdky_cis  cil_dojizdky_kod  pohlavi_cis  pohlavi_kod  sldb_rok sldb_datum                 ukaz_txt                aktivita_txt bydliste_txt                               bydliste_typ cil_dojizdky_txt                           cil_dojizdky_typ pohlavi_txt
1098782501   660139      2623          3249            58            65          1000               NaN               NaN          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Praha správní obvod obce s rozšířenou působností              NaN                                        NaN         NaN
1104581004   603462      2623          3249            58            65          1000              65.0            1000.0          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Praha správní obvod obce s rozšířenou působností            Praha správní obvod obce s rozšířenou působností         NaN
1104014690   292212      2623          3249            58            65          1000              65.0            1000.0        102.0          1.0      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Praha správní obvod obce s rozšířenou působností            Praha správní obvod obce s rozšířenou působností         muž
1104015289   311250      2623          3249            58            65          1000              65.0            1000.0        102.0          2.0      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Praha správní obvod obce s rozšířenou působností            Praha správní obvod obce s rozšířenou působností        žena
1104283076      720      2623          3249            58            65          1000              65.0            2101.0          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Praha správní obvod obce s rozšířenou působností          Benešov správní obvod obce s rozšířenou působností         NaN
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  bydliste_cis  bydliste_kod  cil_dojizdky_cis  cil_dojizdky_kod  pohlavi_cis  pohlavi_kod  sldb_rok sldb_datum                 ukaz_txt                aktivita_txt bydliste_txt bydliste_typ cil_dojizdky_txt cil_dojizdky_typ pohlavi_txt
1104047608       86      2623          3249            58           101         40924             101.0           40916.0        102.0          1.0      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Praha        okres    Ostrava-město            okres         muž
1104623981       49      2623          3249            58           101         40924             101.0           40916.0        102.0          2.0      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Praha        okres    Ostrava-město            okres        žena
1103869258   603462      2623          3249            58           101         40924             101.0           40924.0          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Praha        okres            Praha            okres         NaN
1104623913   292212      2623          3249            58           101         40924             101.0           40924.0        102.0          1.0      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Praha        okres            Praha            okres         muž
1104045487   311250      2623          3249            58           101         40924             101.0           40924.0        102.0          2.0      2021 2021-03-26 Počet vyjíždějících osob Zaměstnaní a žáci, studenti        Praha        okres            Praha            okres        žena
```

### 236. [D] Sčítání 2021 - Vyjíždějící do zaměstnání podle cílového území a pohlaví

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  bydliste_cis  bydliste_kod  cil_dojizdky_cis  cil_dojizdky_kod  pohlavi_cis  pohlavi_kod  sldb_rok sldb_datum                 ukaz_txt aktivita_txt bydliste_txt                               bydliste_typ cil_dojizdky_txt                           cil_dojizdky_typ pohlavi_txt
1098927893   496421      2623          3249            51            65          1000               NaN               NaN          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Praha správní obvod obce s rozšířenou působností              NaN                                        NaN         NaN
1104555327   447273      2623          3249            51            65          1000              65.0            1000.0          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Praha správní obvod obce s rozšířenou působností            Praha správní obvod obce s rozšířenou působností         NaN
1104102007   213527      2623          3249            51            65          1000              65.0            1000.0        102.0          1.0      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Praha správní obvod obce s rozšířenou působností            Praha správní obvod obce s rozšířenou působností         muž
1103939340   233746      2623          3249            51            65          1000              65.0            1000.0        102.0          2.0      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Praha správní obvod obce s rozšířenou působností            Praha správní obvod obce s rozšířenou působností        žena
1103936035      585      2623          3249            51            65          1000              65.0            2101.0          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Praha správní obvod obce s rozšířenou působností          Benešov správní obvod obce s rozšířenou působností         NaN
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  bydliste_cis  bydliste_kod  cil_dojizdky_cis  cil_dojizdky_kod  pohlavi_cis  pohlavi_kod  sldb_rok sldb_datum                 ukaz_txt aktivita_txt bydliste_txt bydliste_typ cil_dojizdky_txt cil_dojizdky_typ pohlavi_txt
1104365685       73      2623          3249            51           101         40924             101.0           40916.0        102.0          1.0      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Praha        okres    Ostrava-město            okres         muž
1104620190       30      2623          3249            51           101         40924             101.0           40916.0        102.0          2.0      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Praha        okres    Ostrava-město            okres        žena
1104042162   447273      2623          3249            51           101         40924             101.0           40924.0          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Praha        okres            Praha            okres         NaN
1104365174   213527      2623          3249            51           101         40924             101.0           40924.0        102.0          1.0      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Praha        okres            Praha            okres         muž
1104043351   233746      2623          3249            51           101         40924             101.0           40924.0        102.0          2.0      2021 2021-03-26 Počet vyjíždějících osob   Zaměstnaní        Praha        okres            Praha            okres        žena
```

### 237. [D] Sčítání 2021 - Vyjíždějící do školy podle cílového území a pohlaví

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  bydliste_cis  bydliste_kod  cil_dojizdky_cis  cil_dojizdky_kod  pohlavi_cis  pohlavi_kod  sldb_rok sldb_datum                 ukaz_txt   aktivita_txt bydliste_txt                               bydliste_typ cil_dojizdky_txt                           cil_dojizdky_typ pohlavi_txt
1099263671   163718      2623          3072             8            65          1000               NaN               NaN          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Praha správní obvod obce s rozšířenou působností              NaN                                        NaN         NaN
1104565200   156189      2623          3072             8            65          1000              65.0            1000.0          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Praha správní obvod obce s rozšířenou působností            Praha správní obvod obce s rozšířenou působností         NaN
1104575761    78685      2623          3072             8            65          1000              65.0            1000.0        102.0          1.0      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Praha správní obvod obce s rozšířenou působností            Praha správní obvod obce s rozšířenou působností         muž
1104684397    77504      2623          3072             8            65          1000              65.0            1000.0        102.0          2.0      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Praha správní obvod obce s rozšířenou působností            Praha správní obvod obce s rozšířenou působností        žena
1104106317      135      2623          3072             8            65          1000              65.0            2101.0          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Praha správní obvod obce s rozšířenou působností          Benešov správní obvod obce s rozšířenou působností         NaN
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  aktivita_cis  aktivita_kod  bydliste_cis  bydliste_kod  cil_dojizdky_cis  cil_dojizdky_kod  pohlavi_cis  pohlavi_kod  sldb_rok sldb_datum                 ukaz_txt   aktivita_txt bydliste_txt bydliste_typ cil_dojizdky_txt cil_dojizdky_typ pohlavi_txt
1104398440       13      2623          3072             8           101         40924             101.0           40916.0        102.0          1.0      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Praha        okres    Ostrava-město            okres         muž
1104513306       19      2623          3072             8           101         40924             101.0           40916.0        102.0          2.0      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Praha        okres    Ostrava-město            okres        žena
1104074350   156189      2623          3072             8           101         40924             101.0           40924.0          NaN          NaN      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Praha        okres            Praha            okres         NaN
1104074965    78685      2623          3072             8           101         40924             101.0           40924.0        102.0          1.0      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Praha        okres            Praha            okres         muž
1104074176    77504      2623          3072             8           101         40924             101.0           40924.0        102.0          2.0      2021 2021-03-26 Počet vyjíždějících osob Žáci, studenti        Praha        okres            Praha            okres        žena
```

## Kategorie C

### 238. [C] Sčítání 2021 - Domy podle obydlenosti a druhu domu

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  obydlen_cis  obydlen_kod  druh_cis  druh_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt     obydlen_txt                                       druh_txt uzemi_txt uzemi_typ
1029037181      247      2409          NaN          NaN       NaN       NaN         42         19      2021 2021-03-26 Počet domů             NaN                                            NaN  Abertamy část obce
1028548110      173      2409       3315.0          1.0       NaN       NaN         42         19      2021 2021-03-26 Počet domů Obvykle obydlen                                            NaN  Abertamy část obce
1029042181       32      2409       3315.0          1.0    3041.0       4.0         42         19      2021 2021-03-26 Počet domů Obvykle obydlen                                     Bytový dům  Abertamy část obce
1028846340      136      2409       3315.0          1.0    3240.0      51.0         42         19      2021 2021-03-26 Počet domů Obvykle obydlen                                   Rodinné domy  Abertamy část obce
1028456368        5      2409       3315.0          1.0    3240.0      55.0         42         19      2021 2021-03-26 Počet domů Obvykle obydlen Ostatní budovy (bez rodinných a bytových domů)  Abertamy část obce
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  obydlen_cis  obydlen_kod  druh_cis  druh_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt       obydlen_txt  druh_txt                    uzemi_txt  uzemi_typ
1105265850       50      2409       3315.0          1.0       NaN       NaN       5948  131134675      2021 2021-03-26 Počet domů   Obvykle obydlen       NaN CZ_CRS3035RES1000mN3113E4675        NaN
1105265851        6      2409       3241.0         52.0       NaN       NaN       5948  131134675      2021 2021-03-26 Počet domů Obvykle neobydlen       NaN CZ_CRS3035RES1000mN3113E4675        NaN
1105187998       41      2409          NaN          NaN       NaN       NaN       5948  131134676      2021 2021-03-26 Počet domů               NaN       NaN CZ_CRS3035RES1000mN3113E4676        NaN
1105233631       33      2409       3315.0          1.0       NaN       NaN       5948  131134676      2021 2021-03-26 Počet domů   Obvykle obydlen       NaN CZ_CRS3035RES1000mN3113E4676        NaN
1105250516        8      2409       3241.0         52.0       NaN       NaN       5948  131134676      2021 2021-03-26 Počet domů Obvykle neobydlen       NaN CZ_CRS3035RES1000mN3113E4676        NaN
```

### 239. [C] Sčítání 2021 - Počet obyvatel a počet obydlených bytů za části obce, části obce - díl, ZSJ, ZDJ - díl,

                        hodnota
polozka                        
target_years_present       None
has_primary_key            True
primary_key_column    uzemi_cis

#### HEAD

```
     idhod  hodnota  ukaz_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum   ukaz_txt      uzemi_txt uzemi_typ
1000356176      355      2607         42         19      2021 2021-03-26 Počet bytů       Abertamy část obce
1000372657       21      2607         42         27      2021 2021-03-26 Počet bytů       Hřebečná část obce
1000344922      349      2607         42         35      2021 2021-03-26 Počet bytů         Adamov část obce
1000374146       63      2607         42         51      2021 2021-03-26 Počet bytů Dolní Adršpach část obce
1000316913      140      2607         42         60      2021 2021-03-26 Počet bytů Horní Adršpach část obce
```

#### TAIL

```
     idhod  hodnota  ukaz_kod  uzemi_cis  uzemi_kod  sldb_rok sldb_datum                          ukaz_txt                           uzemi_txt     uzemi_typ
1000209784        6      3162         60     415995      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                          Dvůr Leveč část obce díl
1000186956        7      3162         60     416002      2021 2021-03-26 Počet obyvatel s obvyklým pobytem                   Smrček-Na sádkách část obce díl
1053584079        0      3162         60     416011      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Nový Lískovec (Brno-Starý Lískovec) část obce díl
1053479901        0      3162         60     416029      2021 2021-03-26 Počet obyvatel s obvyklým pobytem Starý Lískovec (Brno-Nový Lískovec) část obce díl
1000226219        4      3162         60     416037      2021 2021-03-26 Počet obyvatel s obvyklým pobytem  Bitozeves-Průmyslová zóna Triangle část obce díl
```

## Kategorie D

### 240. [D] Databáze KROK - data 2020

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 rok  kodukaz  koduzemi  hodnota 
2020    10101         0 7887101.0
2020    10101       100   49621.0
2020    10101       110   49621.0
2020    10101       200 1092850.0
2020    10101       210 1092850.0
```

#### TAIL

```
 rok  kodukaz  koduzemi  hodnota 
2020   507091      8118       0.0
2020   507091      8119     118.0
2020   507091      8120       7.0
2020   507091      8121       4.0
2020   507091      8122       0.0
```

### 241. [D] Databáze KROK - data 2021

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 rok  kodukaz  koduzemi  hodnota 
2021    10101         0 7887104.0
2021    10101       100   49621.0
2021    10101       110   49621.0
2021    10101       200 1092847.0
2021    10101       210 1092847.0
```

#### TAIL

```
 rok  kodukaz  koduzemi  hodnota 
2021   507091      8118       0.0
2021   507091      8119      70.0
2021   507091      8120       1.0
2021   507091      8121       0.0
2021   507091      8122       0.0
```

### 242. [D] Databáze MOS - data 2020

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 rok  kodukaz  koduzemi  hodnota 
2020    10000    500011       0.0
2020    10000    500020       0.0
2020    10000    500046       0.0
2020    10000    500062       0.0
2020    10000    500071       0.0
```

#### TAIL

```
 rok  kodukaz  koduzemi  hodnota 
2020   507091    599689         1
2020   507091    599701         1
2020   507091    599735         2
2020   507091    599808         1
2020   507091    599956         3
```

### 243. [D] Databáze MOS - data 2021

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 rok  kodukaz  koduzemi  hodnota 
2021    10000    500011       0.0
2021    10000    500020       0.0
2021    10000    500046       0.0
2021    10000    500062       0.0
2021    10000    500071       0.0
```

#### TAIL

```
 rok  kodukaz  koduzemi  hodnota 
2021   600811    599930         1
2021   600811    599948         0
2021   600811    599956         0
2021   600811    599964         0
2021   600811    599999         0
```

### 244. [D] Volby do Evropského parlamentu 2024 - registr kandidátních listin

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ESTRANA  VSTRANA                                                                                                                NAZEVCELK                           NAZEV_STRE                    ZKRATKAE30     ZKRATKAE8  POCSTRVKO   SLOZENI  STAVREG PLAT_STR  SLOZNEPLAT  POCMANDCR                                                                                                                                                                                                          NAZEVPLNY
       1       40                                                                                             Klub angažovaných nestraníků         Klub angažovaných nestraníků  Klub angažovaných nestraníků           KAN          1       040        0        A         NaN          0                                                                                                                                                                                       Klub angažovaných nestraníků
       2     1286                                                                                     Liberální aliance nezávislých občanů Liberální aliance nezávislých občanů Liberální aliance nez. občanů          LANO          1      1286        0        A         NaN          0                                                                                                                                                                               Liberální aliance nezávislých občanů
       3     1487                                                                                                          SPD a Trikolora                      SPD a Trikolora               SPD a Trikolora SPD+Trikolora          2 1114,1227        0        A         NaN          1                                                                                                                                                                                                    SPD a Trikolora
       4     1260                                                                                                Mourek – politická strana           Mourek –  politická strana     Mourek – politická strana        Mourek          1      1260        0        A         NaN          0                                                                                                                                                                                          Mourek – politická strana
       5      121 LEPŠÍ ŽIVOT PRO LIDI-min.mzda 70.000 Kč,min.důchod 50.000 Kč,ceny energií 2019,v obchodech zboží nej. kvality,STOP válce                 LEPŠÍ ŽIVOT PRO LIDI          LEPŠÍ ŽIVOT PRO LIDI          LŽPL          1       121        0        A         NaN          0 LEPŠÍ ŽIVOT PRO LIDI - min. mzda 70.000 Kč, min. důchod 50.000 Kč, návrat cen energií na ceny z roku 2019, v obchodech zboží nejvyšší kvality za ceny dostupné pro každého, zrušení daně z nemovitostí, STOP válce
```

#### TAIL

```
 ESTRANA  VSTRANA                                                                                                                NAZEVCELK                                     NAZEV_STRE                    ZKRATKAE30       ZKRATKAE8  POCSTRVKO     SLOZENI  STAVREG PLAT_STR  SLOZNEPLAT  POCMANDCR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      NAZEVPLNY
      26     1632                                                                                      STAČILO!, koalice KSČM, SD-SN, ČSNS            STAČILO!, koalice KSČM, SD-SN, ČSNS   STAČILO!, KSČM, SD-SN, ČSNS ČSNS+KSČM+SD-SN          3 002,047,143        0        A         NaN          2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 STAČILO!, koalice Komunistické strany Čech a Moravy, Spojených demokratů – Sdružení nezávislých, České strany národně sociální
      27      715                                                                           Demokratická strana zelených - ZA PRÁVA ZVÍŘAT Demokratická strana zelených - ZA PRÁVA ZVÍŘAT         DSZ - ZA PRÁVA ZVÍŘAT DSZ-ZA PR.ZVÍŘ.          1         715        0        A         NaN          0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Demokratická strana zelených - ZA PRÁVA ZVÍŘAT
      28       98 Volte Pravý Blok-stranu za ODVOLAT.polit.,NÍZKÉ daně,VYROVN.rozp.,MIN.byrokr.,SPRAV.just.,PŘÍMOU demokr. WWW.CIBULKA.NET               Volte Pravý Blok www.cibulka.net Volte Pr.Blok www.cibulka.net              PB          1         098        0        A         NaN          0 Volte Pravý Blok - stranu za snadnou a rychlou ODVOLATELNOST politiků a státních úředníků PŘÍMO OBČANY, za NÍZKÉ daně, VYROVNANÝ rozpočet, MINIMALIZACI byrokracie, SPRAVEDLIVOU a NEZKORUMPOVANOU policii a justici, REFERENDA a PŘÍMOU demokracii WWW.CIBULKA.NET, kandidující s nejlepším protikriminálním programem PŘÍMÉ demokracie a hlubokého národního, duchovního a mravního obrození VY NEVĚŘÍTE POLITIKŮM A JEJICH NOVINÁŘŮM? NO KONEČNĚ! VĚŘME SAMI SOBĚ!!! - ale i s mnoha dalšími DŮVODY, proč bychom měli jít tentokrát VŠICHNI K VOLBÁM, ale - pokud nechceme být ZNOVU obelháni, podvedeni a okradeni - NEVOLIT ŽÁDNOU PARLAMENTNÍ TUNEL - STRANU vládnoucí (post) komunistické RUSKO - ČESKÉ totalitní FÍZLOKRACIE a jejich likvidační protinárodní politiku ČÍM HŮŘE, TÍM LÉPE!!! - jenž žádá o volební podporu VŠECHNY ČESKÉ OBČANY a daňové poplatníky, kteří chtějí změnit dnešní kriminální poměry, jejichž jsme všichni obětí, v jejich pravý opak! V BOJI MEZI DOBREM A ZLEM, PRAVDOU A LŽÍ, NELZE BÝT NEUTRÁLNÍ A PŘESTO ZŮSTAT SLUŠNÝ!!! Proto děkujeme za Vaši podporu!!! Nevěříte-li na pokoru u popravčí káry, zdá-li se vám naše kandidátka málo dokonalá nebo postrádáte-li na ní zástupce své obce nebo města a přitom MÁTE ODVAHU v této válce Lidí Dobra s vládnoucími Lidmi Zla povstat z jimi naordinovaného občanského bezvědomí, kterým nás ničí a dnešní DEMOKRATURU, SKRYTOU TOTALITU a OTROKÁŘSTVÍ VYŠŠÍHO ŘÁDU zásadním způsobem změnit, KANDIDUJTE ZA NÁS!!! Kontakt: Volte Pravý Blok www.cibulka.net, PO BOX 595, 170 00 Praha 7
      29     1240                                                                                                             SENIOŘI SOBĚ                                   SENIOŘI SOBĚ                  SENIOŘI SOBĚ            SESO          1        1240        0        A         NaN          0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   SENIOŘI SOBĚ
      30       74                                                                                                                   Levice                                         Levice                        Levice          Levice          1         074        0        A         NaN          0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Levice
```

### 245. [D] Volby do Evropského parlamentu 2024 - registr kandidátních listin

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ESTRANA  VSTRANA                                                                                                                NAZEVCELK                           NAZEV_STRE                    ZKRATKAE30     ZKRATKAE8  POCSTRVKO   SLOZENI  STAVREG PLAT_STR  SLOZNEPLAT  POCMANDCR                                                                                                                                                                                                          NAZEVPLNY
       1       40                                                                                             Klub angažovaných nestraníků         Klub angažovaných nestraníků  Klub angažovaných nestraníků           KAN          1       040        0        A         NaN          0                                                                                                                                                                                       Klub angažovaných nestraníků
       2     1286                                                                                     Liberální aliance nezávislých občanů Liberální aliance nezávislých občanů Liberální aliance nez. občanů          LANO          1      1286        0        A         NaN          0                                                                                                                                                                               Liberální aliance nezávislých občanů
       3     1487                                                                                                          SPD a Trikolora                      SPD a Trikolora               SPD a Trikolora SPD+Trikolora          2 1114,1227        0        A         NaN          1                                                                                                                                                                                                    SPD a Trikolora
       4     1260                                                                                                Mourek – politická strana           Mourek –  politická strana     Mourek – politická strana        Mourek          1      1260        0        A         NaN          0                                                                                                                                                                                          Mourek – politická strana
       5      121 LEPŠÍ ŽIVOT PRO LIDI-min.mzda 70.000 Kč,min.důchod 50.000 Kč,ceny energií 2019,v obchodech zboží nej. kvality,STOP válce                 LEPŠÍ ŽIVOT PRO LIDI          LEPŠÍ ŽIVOT PRO LIDI          LŽPL          1       121        0        A         NaN          0 LEPŠÍ ŽIVOT PRO LIDI - min. mzda 70.000 Kč, min. důchod 50.000 Kč, návrat cen energií na ceny z roku 2019, v obchodech zboží nejvyšší kvality za ceny dostupné pro každého, zrušení daně z nemovitostí, STOP válce
```

#### TAIL

```
 ESTRANA  VSTRANA                                                                                                                NAZEVCELK                                     NAZEV_STRE                    ZKRATKAE30       ZKRATKAE8  POCSTRVKO     SLOZENI  STAVREG PLAT_STR  SLOZNEPLAT  POCMANDCR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      NAZEVPLNY
      26     1632                                                                                      STAČILO!, koalice KSČM, SD-SN, ČSNS            STAČILO!, koalice KSČM, SD-SN, ČSNS   STAČILO!, KSČM, SD-SN, ČSNS ČSNS+KSČM+SD-SN          3 002,047,143        0        A         NaN          2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 STAČILO!, koalice Komunistické strany Čech a Moravy, Spojených demokratů – Sdružení nezávislých, České strany národně sociální
      27      715                                                                           Demokratická strana zelených - ZA PRÁVA ZVÍŘAT Demokratická strana zelených - ZA PRÁVA ZVÍŘAT         DSZ - ZA PRÁVA ZVÍŘAT DSZ-ZA PR.ZVÍŘ.          1         715        0        A         NaN          0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Demokratická strana zelených - ZA PRÁVA ZVÍŘAT
      28       98 Volte Pravý Blok-stranu za ODVOLAT.polit.,NÍZKÉ daně,VYROVN.rozp.,MIN.byrokr.,SPRAV.just.,PŘÍMOU demokr. WWW.CIBULKA.NET               Volte Pravý Blok www.cibulka.net Volte Pr.Blok www.cibulka.net              PB          1         098        0        A         NaN          0 Volte Pravý Blok - stranu za snadnou a rychlou ODVOLATELNOST politiků a státních úředníků PŘÍMO OBČANY, za NÍZKÉ daně, VYROVNANÝ rozpočet, MINIMALIZACI byrokracie, SPRAVEDLIVOU a NEZKORUMPOVANOU policii a justici, REFERENDA a PŘÍMOU demokracii WWW.CIBULKA.NET, kandidující s nejlepším protikriminálním programem PŘÍMÉ demokracie a hlubokého národního, duchovního a mravního obrození VY NEVĚŘÍTE POLITIKŮM A JEJICH NOVINÁŘŮM? NO KONEČNĚ! VĚŘME SAMI SOBĚ!!! - ale i s mnoha dalšími DŮVODY, proč bychom měli jít tentokrát VŠICHNI K VOLBÁM, ale - pokud nechceme být ZNOVU obelháni, podvedeni a okradeni - NEVOLIT ŽÁDNOU PARLAMENTNÍ TUNEL - STRANU vládnoucí (post) komunistické RUSKO - ČESKÉ totalitní FÍZLOKRACIE a jejich likvidační protinárodní politiku ČÍM HŮŘE, TÍM LÉPE!!! - jenž žádá o volební podporu VŠECHNY ČESKÉ OBČANY a daňové poplatníky, kteří chtějí změnit dnešní kriminální poměry, jejichž jsme všichni obětí, v jejich pravý opak! V BOJI MEZI DOBREM A ZLEM, PRAVDOU A LŽÍ, NELZE BÝT NEUTRÁLNÍ A PŘESTO ZŮSTAT SLUŠNÝ!!! Proto děkujeme za Vaši podporu!!! Nevěříte-li na pokoru u popravčí káry, zdá-li se vám naše kandidátka málo dokonalá nebo postrádáte-li na ní zástupce své obce nebo města a přitom MÁTE ODVAHU v této válce Lidí Dobra s vládnoucími Lidmi Zla povstat z jimi naordinovaného občanského bezvědomí, kterým nás ničí a dnešní DEMOKRATURU, SKRYTOU TOTALITU a OTROKÁŘSTVÍ VYŠŠÍHO ŘÁDU zásadním způsobem změnit, KANDIDUJTE ZA NÁS!!! Kontakt: Volte Pravý Blok www.cibulka.net, PO BOX 595, 170 00 Praha 7
      29     1240                                                                                                             SENIOŘI SOBĚ                                   SENIOŘI SOBĚ                  SENIOŘI SOBĚ            SESO          1        1240        0        A         NaN          0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   SENIOŘI SOBĚ
      30       74                                                                                                                   Levice                                         Levice                        Levice          Levice          1         074        0        A         NaN          0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Levice
```

### 246. [D] Volby do Evropského parlamentu 2024 - registr kandidátů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ESTRANA  PORCISLO     JMENO     PRIJMENI    TITULPRED  TITULZA  VEK STATOBCAN                            POVOLANI BYDLISTEN  BYDLISTEK  PSTRANA  NSTRANA PLATNOST  POCHLASU  POCPROC MANDAT  PORADIMAND  PORADINAHR
       1         1 Stanislav      Pochman          NaN      NaN   60        CZ                    výrobní dispečer     Oloví     560588       40       40        A       113     2.47      N           0           0
       1         2 František       Laudát         Ing.      NaN   64        CZ        manager staveb, předseda KAN     Praha     554782       40       40        A       210     4.60      N           0           0
       1         3     Marie Gottfriedová         Mgr.      NaN   49        CZ            ředitelka základní školy    Trmice     553697       99       40        A       195     4.27      N           0           0
       1         4      Jiří      Schmidt Mgr. et Mgr.      NaN   68        CZ                             pedagog   Příbram     539911       99       40        A        73     1.60      N           0           0
       1         5    Romana      Šimková         Ing.      NaN   36        CZ Pricing & Merchandising Coordinator     Praha     554782       40       40        A       115     2.52      N           0           0
```

#### TAIL

```
 ESTRANA  PORCISLO    JMENO PRIJMENI TITULPRED  TITULZA  VEK STATOBCAN POVOLANI  BYDLISTEN  BYDLISTEK  PSTRANA  NSTRANA PLATNOST  POCHLASU  POCPROC MANDAT  PORADIMAND  PORADINAHR
      30        24      Jan   Široký       NaN      NaN   47        CZ jednatel    Liberec     563889       74       74        A         5     0.21      N           0           0
      30        25 Alexandr   Gluhov       NaN      NaN   21        CZ  student     Dobříš     540111       74       74        A         8     0.34      N           0           0
      30        26   Martin   Biskup      Mgr.      NaN   50        CZ  právník Nový Jičín     599191       74       74        A        22     0.95      N           0           0
      30        27     Petr    Rohel     PhDr.      NaN   76        CZ důchodce    Ostrava     554821       74       74        A         8     0.34      N           0           0
      30        28  Vojtěch   Juřica       NaN      NaN   34        CZ  technik      Praha     554782       74       74        A         6     0.26      N           0           0
```

### 247. [D] Volby do Evropského parlamentu 2024 - registr kandidátů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ESTRANA  PORCISLO     JMENO     PRIJMENI    TITULPRED  TITULZA  VEK STATOBCAN                            POVOLANI BYDLISTEN  BYDLISTEK  PSTRANA  NSTRANA PLATNOST  POCHLASU  POCPROC MANDAT  PORADIMAND  PORADINAHR
       1         1 Stanislav      Pochman          NaN      NaN   60        CZ                    výrobní dispečer     Oloví     560588       40       40        A       113     2.47      N           0           0
       1         2 František       Laudát         Ing.      NaN   64        CZ        manager staveb, předseda KAN     Praha     554782       40       40        A       210     4.60      N           0           0
       1         3     Marie Gottfriedová         Mgr.      NaN   49        CZ            ředitelka základní školy    Trmice     553697       99       40        A       195     4.27      N           0           0
       1         4      Jiří      Schmidt Mgr. et Mgr.      NaN   68        CZ                             pedagog   Příbram     539911       99       40        A        73     1.60      N           0           0
       1         5    Romana      Šimková         Ing.      NaN   36        CZ Pricing & Merchandising Coordinator     Praha     554782       40       40        A       115     2.52      N           0           0
```

#### TAIL

```
 ESTRANA  PORCISLO    JMENO PRIJMENI TITULPRED  TITULZA  VEK STATOBCAN POVOLANI  BYDLISTEN  BYDLISTEK  PSTRANA  NSTRANA PLATNOST  POCHLASU  POCPROC MANDAT  PORADIMAND  PORADINAHR
      30        24      Jan   Široký       NaN      NaN   47        CZ jednatel    Liberec     563889       74       74        A         5     0.21      N           0           0
      30        25 Alexandr   Gluhov       NaN      NaN   21        CZ  student     Dobříš     540111       74       74        A         8     0.34      N           0           0
      30        26   Martin   Biskup      Mgr.      NaN   50        CZ  právník Nový Jičín     599191       74       74        A        22     0.95      N           0           0
      30        27     Petr    Rohel     PhDr.      NaN   76        CZ důchodce    Ostrava     554821       74       74        A         8     0.34      N           0           0
      30        28  Vojtěch   Juřica       NaN      NaN   34        CZ  technik      Praha     554782       74       74        A         6     0.26      N           0           0
```

### 248. [D] Volby do Evropského parlamentu 2024 - složení kandidátních listin

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ESTRANA TYPSLOZENI  NSTRANA
       1          P       40
       2          P     1286
       3          P     1114
       3          P     1227
       4          P     1260
```

#### TAIL

```
 ESTRANA TYPSLOZENI  NSTRANA
      26          P        2
      27          P      715
      28          P       98
      29          P     1240
      30          P       74
```

### 249. [D] Volby do Evropského parlamentu 2024 - složení kandidátních listin

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 ESTRANA TYPSLOZENI  NSTRANA
       1          P       40
       2          P     1286
       3          P     1114
       3          P     1227
       4          P     1260
```

#### TAIL

```
 ESTRANA TYPSLOZENI  NSTRANA
      26          P        2
      27          P      715
      28          P       98
      29          P     1240
      30          P       74
```

### 250. [D] Volby do Evropského parlamentu 2024 - složení volebních stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA  NSTRANA
       1        1
       2        2
       3        3
       4        4
       5        5
```

#### TAIL

```
 VSTRANA  NSTRANA
    1635     1272
    1636     1265
    1636     1269
    9995     9995
    9999     9999
```

### 251. [D] Volby do Evropského parlamentu 2024 - složení volebních stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA  NSTRANA
       1        1
       2        2
       3        3
       4        4
       5        5
```

#### TAIL

```
 VSTRANA  NSTRANA
    1635     1272
    1636     1265
    1636     1269
    9995     9995
    9999     9999
```

### 252. [D] Volby do Evropského parlamentu 2024 - číselník navrhujících stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NSTRANA                    NAZEV_STRN                    ZKRATKAN30 ZKRATKAN8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
      24          Konzervativní strana          Konzervativní strana      KONS
```

#### TAIL

```
 NSTRANA                                         NAZEV_STRN                    ZKRATKAN30       ZKRATKAN8
    1286               Liberální aliance nezávislých občanů Liberální aliance nez. občanů            LANO
    1287                                 Osobnosti pro kraj            Osobnosti pro kraj              OK
    1288 ANO LEPŠÍ EU S MIMOZEMŠŤANY (zast.drahotu a válku)   ANO LEPŠÍ EU S MIMOZEMŠŤANY mimozemstani.eu
    9995                                            Koalice                       Koalice         Koalice
    9999                                Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 253. [D] Volby do Evropského parlamentu 2024 - číselník navrhujících stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NSTRANA                    NAZEV_STRN                    ZKRATKAN30 ZKRATKAN8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
      24          Konzervativní strana          Konzervativní strana      KONS
```

#### TAIL

```
 NSTRANA                                         NAZEV_STRN                    ZKRATKAN30       ZKRATKAN8
    1286               Liberální aliance nezávislých občanů Liberální aliance nez. občanů            LANO
    1287                                 Osobnosti pro kraj            Osobnosti pro kraj              OK
    1288 ANO LEPŠÍ EU S MIMOZEMŠŤANY (zast.drahotu a válku)   ANO LEPŠÍ EU S MIMOZEMŠŤANY mimozemstani.eu
    9995                                            Koalice                       Koalice         Koalice
    9999                                Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 254. [D] Volby do Evropského parlamentu 2024 - číselník obcí

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBEC_PREZ                NAZEVOBCE
    500011 Želechovice nad Dřevnicí
    500020        Petrov nad Desnou
    500046                  Libhošť
    500062                   Krhová
    500071                  Poličná
```

#### TAIL

```
 OBEC_PREZ   NAZEVOBCE
    599948   Štramberk
    599956       Tichá
    599964       Tísek
    599999 Trojanovice
    999997   Zahraničí
```

### 255. [D] Volby do Evropského parlamentu 2024 - číselník obcí

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 OBEC_PREZ                NAZEVOBCE
    500011 Želechovice nad Dřevnicí
    500020        Petrov nad Desnou
    500046                  Libhošť
    500062                   Krhová
    500071                  Poličná
```

#### TAIL

```
 OBEC_PREZ   NAZEVOBCE
    599948   Štramberk
    599956       Tichá
    599964       Tísek
    599999 Trojanovice
    999997   Zahraničí
```

### 256. [D] Volby do Evropského parlamentu 2024 - číselník politické příslušnosti kandidátů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 PSTRANA                    NAZEV_STRP                    ZKRATKAP30 ZKRATKAP8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
       9    Nezávislá iniciativa (NEI)    Nezávislá iniciativa (NEI)       NEI
```

#### TAIL

```
 PSTRANA                                         NAZEV_STRP                    ZKRATKAP30       ZKRATKAP8
    1285                          Vize pro Karlovarský kraj     Vize pro Karlovarský kraj        Vize KVK
    1286               Liberální aliance nezávislých občanů Liberální aliance nez. občanů            LANO
    1287                                 Osobnosti pro kraj            Osobnosti pro kraj              OK
    1288 ANO LEPŠÍ EU S MIMOZEMŠŤANY (zast.drahotu a válku)   ANO LEPŠÍ EU S MIMOZEMŠŤANY mimozemstani.eu
    9999                                Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 257. [D] Volby do Evropského parlamentu 2024 - číselník politické příslušnosti kandidátů

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 PSTRANA                    NAZEV_STRP                    ZKRATKAP30 ZKRATKAP8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
       9    Nezávislá iniciativa (NEI)    Nezávislá iniciativa (NEI)       NEI
```

#### TAIL

```
 PSTRANA                                         NAZEV_STRP                    ZKRATKAP30       ZKRATKAP8
    1285                          Vize pro Karlovarský kraj     Vize pro Karlovarský kraj        Vize KVK
    1286               Liberální aliance nezávislých občanů Liberální aliance nez. občanů            LANO
    1287                                 Osobnosti pro kraj            Osobnosti pro kraj              OK
    1288 ANO LEPŠÍ EU S MIMOZEMŠŤANY (zast.drahotu a válku)   ANO LEPŠÍ EU S MIMOZEMŠŤANY mimozemstani.eu
    9999                                Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 258. [D] Volby do Evropského parlamentu 2024 - číselník volebních stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA                     NAZEVCELK                    NAZEV_STRV                    ZKRATKAV30 ZKRATKAV8  POCSTR_SLO  SLOZENI ZKRATKA_OF TYPVS  PLNYNAZEV
       1                       KDU-ČSL                       KDU-ČSL                       KDU-ČSL   KDU-ČSL           1        1    KDU-ČSL     S        NaN
       2 Česká strana národně sociální Česká strana národně sociální Česká strana národně sociální      ČSNS           1        2       ČSNS     S        NaN
       3 Křesťanskodemokratická strana Křesťanskodemokratická strana Křesťanskodemokratická strana       KDS           1        3        KDS     S        NaN
       4 Liberálně demokratická strana Liberálně demokratická strana Liberálně demokratická strana       LDS           1        4        LDS     S        NaN
       5               Strana zelených               Strana zelených               Strana zelených    Zelení           1        5     Zelení     S        NaN
```

#### TAIL

```
 VSTRANA                    NAZEVCELK                   NAZEV_STRV                  ZKRATKAV30       ZKRATKAV8  POCSTR_SLO       SLOZENI          ZKRATKA_OF TYPVS  PLNYNAZEV
    1634   Koalice ČSSD, DOMOV a Směr   Koalice ČSSD, DOMOV a Směr   Koalice ČSSD, DOMOV, Směr ČSSD+DOMOV+Směr           3 759,1221,1248                 NaN     K        NaN
    1635        Koalice SEN 21 a Volt        Koalice SEN 21 a Volt        Koalice SEN 21, Volt     SEN 21+Volt           2     1187,1272                 NaN     K        NaN
    1636 Koalice PRO 2022 a SV PRO ZS Koalice PRO 2022 a SV PRO ZS Koalice PRO 2022, SV PRO ZS PRO2022+SVPROZS           2     1265,1269                 NaN     K        NaN
    9995                      Koalice                      Koalice                     Koalice         Koalice           1          9995             koalice     S        NaN
    9999          Neregistrováno u MV          Neregistrováno u MV         Neregistrováno u MV Neregistr. u MV           1          9999 Neregistrováno u MV     S        NaN
```

### 259. [D] Volby do Evropského parlamentu 2024 - číselník volebních stran

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA                     NAZEVCELK                    NAZEV_STRV                    ZKRATKAV30 ZKRATKAV8  POCSTR_SLO  SLOZENI ZKRATKA_OF TYPVS  PLNYNAZEV
       1                       KDU-ČSL                       KDU-ČSL                       KDU-ČSL   KDU-ČSL           1        1    KDU-ČSL     S        NaN
       2 Česká strana národně sociální Česká strana národně sociální Česká strana národně sociální      ČSNS           1        2       ČSNS     S        NaN
       3 Křesťanskodemokratická strana Křesťanskodemokratická strana Křesťanskodemokratická strana       KDS           1        3        KDS     S        NaN
       4 Liberálně demokratická strana Liberálně demokratická strana Liberálně demokratická strana       LDS           1        4        LDS     S        NaN
       5               Strana zelených               Strana zelených               Strana zelených    Zelení           1        5     Zelení     S        NaN
```

#### TAIL

```
 VSTRANA                    NAZEVCELK                   NAZEV_STRV                  ZKRATKAV30       ZKRATKAV8  POCSTR_SLO       SLOZENI          ZKRATKA_OF TYPVS  PLNYNAZEV
    1634   Koalice ČSSD, DOMOV a Směr   Koalice ČSSD, DOMOV a Směr   Koalice ČSSD, DOMOV, Směr ČSSD+DOMOV+Směr           3 759,1221,1248                 NaN     K        NaN
    1635        Koalice SEN 21 a Volt        Koalice SEN 21 a Volt        Koalice SEN 21, Volt     SEN 21+Volt           2     1187,1272                 NaN     K        NaN
    1636 Koalice PRO 2022 a SV PRO ZS Koalice PRO 2022 a SV PRO ZS Koalice PRO 2022, SV PRO ZS PRO2022+SVPROZS           2     1265,1269                 NaN     K        NaN
    9995                      Koalice                      Koalice                     Koalice         Koalice           1          9995             koalice     S        NaN
    9999          Neregistrováno u MV          Neregistrováno u MV         Neregistrováno u MV Neregistr. u MV           1          9999 Neregistrováno u MV     S        NaN
```

### 260. [D] Volby do Evropského parlamentu 2024 - číselník zemí

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
ZKRATKA2  KODZEME           NAZZEMECZ                NAZZEMEEN  NAZZKRCZ             NAZZKREN ZKRATKA3
      AT       40  Rakouská republika  the Republic of Austria  Rakousko              Austria      AUT
      BE       56 Belgické království   the Kingdom of Belgium    Belgie              Belgium      BEL
      BG      100 Bulharská republika the Republic of Bulgaria Bulharsko             Bulgaria      BGR
      CY      196  Kyperská republika   the Republic of Cyprus      Kypr               Cyprus      CYP
      CZ      203     Česká republika       the Czech Republic     Česko Czech Republic (the)      CZE
```

#### TAIL

```
ZKRATKA2  KODZEME             NAZZEMECZ                NAZZEMEEN    NAZZKRCZ NAZZKREN ZKRATKA3
      PT      620 Portugalská republika  the Portuguese Republic Portugalsko Portugal      PRT
      RO      642              Rumunsko                  Romania    Rumunsko  Romania      ROU
      SE      752    Švédské království    the Kingdom of Sweden     Švédsko   Sweden      SWE
      SI      705   Slovinská republika the Republic of Slovenia   Slovinsko Slovenia      SVN
      SK      703   Slovenská republika      the Slovak Republic   Slovensko Slovakia      SVK
```

### 261. [D] Volby do Evropského parlamentu 2024 - číselník zemí

                     hodnota
polozka                     
target_years_present    2024
has_primary_key        False
primary_key_column      None

#### HEAD

```
ZKRATKA2  KODZEME           NAZZEMECZ                NAZZEMEEN  NAZZKRCZ             NAZZKREN ZKRATKA3
      AT       40  Rakouská republika  the Republic of Austria  Rakousko              Austria      AUT
      BE       56 Belgické království   the Kingdom of Belgium    Belgie              Belgium      BEL
      BG      100 Bulharská republika the Republic of Bulgaria Bulharsko             Bulgaria      BGR
      CY      196  Kyperská republika   the Republic of Cyprus      Kypr               Cyprus      CYP
      CZ      203     Česká republika       the Czech Republic     Česko Czech Republic (the)      CZE
```

#### TAIL

```
ZKRATKA2  KODZEME             NAZZEMECZ                NAZZEMEEN    NAZZKRCZ NAZZKREN ZKRATKA3
      PT      620 Portugalská republika  the Portuguese Republic Portugalsko Portugal      PRT
      RO      642              Rumunsko                  Romania    Rumunsko  Romania      ROU
      SE      752    Švédské království    the Kingdom of Sweden     Švédsko   Sweden      SWE
      SI      705   Slovinská republika the Republic of Slovenia   Slovinsko Slovenia      SVN
      SK      703   Slovenská republika      the Slovak Republic   Slovensko Slovakia      SVK
```

### 262. [D] Volby do zastupitelstev obcí 2022 - složení volebních stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA  NSTRANA
       1        1
       2        2
       3        3
       4        4
       5        5
```

#### TAIL

```
 VSTRANA  NSTRANA
    1708     1708
    1709     1709
    1710     1710
    9995     9995
    9999     9999
```

### 263. [D] Volby do zastupitelstev obcí 2022 - složení volebních stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA  NSTRANA
       1        1
       2        2
       3        3
       4        4
       5        5
```

#### TAIL

```
 VSTRANA  NSTRANA
    1708     1708
    1709     1709
    1710     1710
    9995     9995
    9999     9999
```

### 264. [D] Volby do zastupitelstev obcí 2022 - číselník druhu zastupitelstva obce

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 DRUHZASTUP                                         NAZDRUHZAS
          1                                Zastupitelstvo obce
          2                               Zastupitelstvo města
          3                  Zastupitelstvo statutárního města
          4                          Zastupitelstvo hl.m.Prahy
          5 Zastupitelstvo městské části nebo městského obvodu
```

#### TAIL

```
 DRUHZASTUP                                         NAZDRUHZAS
          2                               Zastupitelstvo města
          3                  Zastupitelstvo statutárního města
          4                          Zastupitelstvo hl.m.Prahy
          5 Zastupitelstvo městské části nebo městského obvodu
          6                             Zastupitelstvo městysu
```

### 265. [D] Volby do zastupitelstev obcí 2022 - číselník druhu zastupitelstva obce

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 DRUHZASTUP                                         NAZDRUHZAS
          1                                Zastupitelstvo obce
          2                               Zastupitelstvo města
          3                  Zastupitelstvo statutárního města
          4                          Zastupitelstvo hl.m.Prahy
          5 Zastupitelstvo městské části nebo městského obvodu
```

#### TAIL

```
 DRUHZASTUP                                         NAZDRUHZAS
          2                               Zastupitelstvo města
          3                  Zastupitelstvo statutárního města
          4                          Zastupitelstvo hl.m.Prahy
          5 Zastupitelstvo městské části nebo městského obvodu
          6                             Zastupitelstvo městysu
```

### 266. [D] Volby do zastupitelstev obcí 2022 - číselník navrhujících stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NSTRANA                    NAZEV_STRN                    ZKRATKAN30 ZKRATKAN8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
      24          Konzervativní strana          Konzervativní strana      KONS
```

#### TAIL

```
 NSTRANA                         NAZEV_STRN                    ZKRATKAN30       ZKRATKAN8
    1708                               JSME                          JSME            JSME
    1709                      Svěží Týniště                 Svěží Týniště              ST
    1710 Zbrojovka a fotbal zpět za Lužánky Zbrojovka a fotbal za Lužánky      za Lužánky
    9995                            Koalice                       Koalice         Koalice
    9999                Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 267. [D] Volby do zastupitelstev obcí 2022 - číselník navrhujících stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 NSTRANA                    NAZEV_STRN                    ZKRATKAN30 ZKRATKAN8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
      24          Konzervativní strana          Konzervativní strana      KONS
```

#### TAIL

```
 NSTRANA                         NAZEV_STRN                    ZKRATKAN30       ZKRATKAN8
    1708                               JSME                          JSME            JSME
    1709                      Svěží Týniště                 Svěží Týniště              ST
    1710 Zbrojovka a fotbal zpět za Lužánky Zbrojovka a fotbal za Lužánky      za Lužánky
    9995                            Koalice                       Koalice         Koalice
    9999                Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 268. [D] Volby do zastupitelstev obcí 2022 - číselník politické příslušnosti kandidátů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 PSTRANA                    NAZEV_STRP                    ZKRATKAP30 ZKRATKAP8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
      24          Konzervativní strana          Konzervativní strana      KONS
```

#### TAIL

```
 PSTRANA                         NAZEV_STRP                    ZKRATKAP30       ZKRATKAP8
    1707                         Hnutí Kruh                    Hnutí Kruh            Kruh
    1708                               JSME                          JSME            JSME
    1709                      Svěží Týniště                 Svěží Týniště              ST
    1710 Zbrojovka a fotbal zpět za Lužánky Zbrojovka a fotbal za Lužánky      za Lužánky
    9999                Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 269. [D] Volby do zastupitelstev obcí 2022 - číselník politické příslušnosti kandidátů

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 PSTRANA                    NAZEV_STRP                    ZKRATKAP30 ZKRATKAP8
       1                       KDU-ČSL                       KDU-ČSL   KDU-ČSL
       2 Česká strana národně sociální Česká strana národně sociální      ČSNS
       5               Strana zelených               Strana zelených    Zelení
       7           Sociální demokracie           Sociální demokracie    SOCDEM
      24          Konzervativní strana          Konzervativní strana      KONS
```

#### TAIL

```
 PSTRANA                         NAZEV_STRP                    ZKRATKAP30       ZKRATKAP8
    1707                         Hnutí Kruh                    Hnutí Kruh            Kruh
    1708                               JSME                          JSME            JSME
    1709                      Svěží Týniště                 Svěží Týniště              ST
    1710 Zbrojovka a fotbal zpět za Lužánky Zbrojovka a fotbal za Lužánky      za Lužánky
    9999                Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV
```

### 270. [D] Volby do zastupitelstev obcí 2022 - číselník typu zastupitelstva obce

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 TYPZASTUP                                                  NAZTYPUZAS
         1 Zastupitelstvo obce,městysu,města,statutár.města,hl.m.Prahy
         2          Zastupitelstvo městské části nebo městského obvodu
```

#### TAIL

```
 TYPZASTUP                                                  NAZTYPUZAS
         1 Zastupitelstvo obce,městysu,města,statutár.města,hl.m.Prahy
         2          Zastupitelstvo městské části nebo městského obvodu
```

### 271. [D] Volby do zastupitelstev obcí 2022 - číselník typu zastupitelstva obce

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 TYPZASTUP                                                  NAZTYPUZAS
         1 Zastupitelstvo obce,městysu,města,statutár.města,hl.m.Prahy
         2          Zastupitelstvo městské části nebo městského obvodu
```

#### TAIL

```
 TYPZASTUP                                                  NAZTYPUZAS
         1 Zastupitelstvo obce,městysu,města,statutár.města,hl.m.Prahy
         2          Zastupitelstvo městské části nebo městského obvodu
```

### 272. [D] Volby do zastupitelstev obcí 2022 - číselník volebních stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA                     NAZEVCELK                    NAZEV_STRV                    ZKRATKAV30 ZKRATKAV8  POCSTR_SLO  SLOZENI ZKRATKA_OF TYPVS  PLNYNAZEV
       1                       KDU-ČSL                       KDU-ČSL                       KDU-ČSL   KDU-ČSL           1        1    KDU-ČSL     S        NaN
       2 Česká strana národně sociální Česká strana národně sociální Česká strana národně sociální      ČSNS           1        2       ČSNS     S        NaN
       3 Křesťanskodemokratická strana Křesťanskodemokratická strana Křesťanskodemokratická strana       KDS           1        3        KDS     S        NaN
       4 Liberálně demokratická strana Liberálně demokratická strana Liberálně demokratická strana       LDS           1        4        LDS     S        NaN
       5               Strana zelených               Strana zelených               Strana zelených    Zelení           1        5     Zelení     S        NaN
```

#### TAIL

```
 VSTRANA                          NAZEVCELK                         NAZEV_STRV                    ZKRATKAV30       ZKRATKAV8  POCSTR_SLO  SLOZENI          ZKRATKA_OF TYPVS  PLNYNAZEV
    1708                               JSME                               JSME                          JSME            JSME           1     1708                JSME     S        NaN
    1709                      Svěží Týniště                      Svěží Týniště                 Svěží Týniště              ST           1     1709                  ST     S        NaN
    1710 Zbrojovka a fotbal zpět za Lužánky Zbrojovka a fotbal zpět za Lužánky Zbrojovka a fotbal za Lužánky      za Lužánky           1     1710          za Lužánky     S        NaN
    9995                            Koalice                            Koalice                       Koalice         Koalice           1     9995             koalice     S        NaN
    9999                Neregistrováno u MV                Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV           1     9999 Neregistrováno u MV     S        NaN
```

### 273. [D] Volby do zastupitelstev obcí 2022 - číselník volebních stran

                     hodnota
polozka                     
target_years_present    None
has_primary_key        False
primary_key_column      None

#### HEAD

```
 VSTRANA                     NAZEVCELK                    NAZEV_STRV                    ZKRATKAV30 ZKRATKAV8  POCSTR_SLO  SLOZENI ZKRATKA_OF TYPVS  PLNYNAZEV
       1                       KDU-ČSL                       KDU-ČSL                       KDU-ČSL   KDU-ČSL           1        1    KDU-ČSL     S        NaN
       2 Česká strana národně sociální Česká strana národně sociální Česká strana národně sociální      ČSNS           1        2       ČSNS     S        NaN
       3 Křesťanskodemokratická strana Křesťanskodemokratická strana Křesťanskodemokratická strana       KDS           1        3        KDS     S        NaN
       4 Liberálně demokratická strana Liberálně demokratická strana Liberálně demokratická strana       LDS           1        4        LDS     S        NaN
       5               Strana zelených               Strana zelených               Strana zelených    Zelení           1        5     Zelení     S        NaN
```

#### TAIL

```
 VSTRANA                          NAZEVCELK                         NAZEV_STRV                    ZKRATKAV30       ZKRATKAV8  POCSTR_SLO  SLOZENI          ZKRATKA_OF TYPVS  PLNYNAZEV
    1708                               JSME                               JSME                          JSME            JSME           1     1708                JSME     S        NaN
    1709                      Svěží Týniště                      Svěží Týniště                 Svěží Týniště              ST           1     1709                  ST     S        NaN
    1710 Zbrojovka a fotbal zpět za Lužánky Zbrojovka a fotbal zpět za Lužánky Zbrojovka a fotbal za Lužánky      za Lužánky           1     1710          za Lužánky     S        NaN
    9995                            Koalice                            Koalice                       Koalice         Koalice           1     9995             koalice     S        NaN
    9999                Neregistrováno u MV                Neregistrováno u MV           Neregistrováno u MV Neregistr. u MV           1     9999 Neregistrováno u MV     S        NaN
```
