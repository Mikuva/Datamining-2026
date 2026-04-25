# CZSO IKZ v10 robust + display fix

Toto je **čistý a konzistentní bundle** pro CZSO IKZ workflow v Pythonu.
Všechny notebooky i moduly v tomto balíku jsou sladěné na stejnou verzi:

- robustní detekce časových sloupců z v10,
- cleanup stažených datasetů po vytvoření preview,
- filtrování `head()`/`tail()` na target years,
- územní řazení začínající obcemi,
- **display fix** pro `display_results_by_territory(categories=..., scopes=...)`.

## Co používat

Pro nový plný běh použij:
- `CZSO_IKZ_A_to_Z_v10_display_fixed.ipynb`

Pro opravu / přerovnání již existujícího outputu použij:
- `CZSO_IKZ_reorder_existing_outputs_v10_display_fixed.ipynb`

Pro audit možných falešných negativů použij:
- `CZSO_IKZ_audit_false_negatives_v10.ipynb`

## Instalace

```bash
conda env create -f environment_czso_ikz_v10_display_fixed.yml
conda activate czso-ikz-v10
```

## Příkazová řádka

Plný běh:

```bash
python run_czso_ikz_v10_display_fixed.py --catalog-xlsx czso_katalog_trideny.xlsx --output-dir czso_ikz_a_to_z_output
```

Repair / reorder existujícího outputu:

```bash
python repair_czso_ikz_existing_outputs_v10_display_fixed.py --output-dir czso_ikz_a_to_z_output
```

Audit falešných negativů:

```bash
python run_czso_ikz_audit_false_negatives.py --base-dir .
```

## Důležité

Tento bundle **neobsahuje starší v5/v8 notebooky pod původními názvy**, aby se předešlo záměně verzí.
Pokud jsi měl dříve v jedné složce rozbalené různé ZIP balíky, doporučený postup je vytvořit novou čistou složku
a rozbalit do ní pouze tento bundle.
