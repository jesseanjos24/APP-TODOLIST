
from pathlib import Path
import os
import json

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
DADOS = DATA / "saves"

if not DADOS.exists():
    DADOS.mkdir(parents=True)
    
JASON_FILE = DADOS / "tasks.json"
    
def load_data():
    print("executando load_data")
    if not JASON_FILE.exists():
        dados = []
        with open(JASON_FILE, "w", encoding="utf-8") as file:
            json.dump(dados, file)
        
        return dados
    
    with open(JASON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

  
def save_tasks(teskes):
    print("executando save_tasks")
    with open(JASON_FILE, "w", encoding="utf-8") as f:
        json.dump(teskes, f, indent=5, ensure_ascii=False)