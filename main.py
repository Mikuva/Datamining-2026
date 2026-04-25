import os
import sys
import pandas as pd

# 1. Nastavení cest k /src
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    from pyczso_lkod_bridge import LKODBridge
    print(f"✅ Moduly načteny z: {src_path}")
except ImportError as e:
    print(f"❌ Chyba importu: {e}")
    sys.exit(1)

def main():
    print("🚀 START PIPELINE: INDEX KVALITY ŽIVOTA")
    bridge = LKODBridge()
    
    # Seznam datasetů (ID z ČSÚ)
    datasets = [
        {"id": "110080", "name": "nadeje_doziti"},
        {"id": "130141r25", "name": "nezamestnanost"}
    ]
    
    # Složka pro uložení výsledků
    raw_dir = os.path.join(current_dir, "data", "raw")
    os.makedirs(raw_dir, exist_ok=True)
    
    for ds in datasets:
        try:
            print(f"Stahuji {ds['id']} ({ds['name']})...")
            
            # OPRAVA: Používáme metodu 'get_table', kterou tvůj terminál potvrdil
            df = bridge.get_table(ds['id'])
            
            if df is not None and isinstance(df, pd.DataFrame):
                path = os.path.join(raw_dir, f"{ds['name']}.csv")
                df.to_csv(path, index=False)
                print(f"   ✅ Úspěšně uloženo do: {path}")
            else:
                print(f"   ⚠️ Varování: Dataset {ds['id']} nevrátil DataFrame.")
                
        except Exception as e:
            print(f"   ❌ Chyba u {ds['id']}: {e}")

if __name__ == "__main__":
    main()