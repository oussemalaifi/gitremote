from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

# Chemin vers le fichier chats.json
BASE_DIR = Path(__file__).parent
CHATS_FILE = BASE_DIR / "chats.json"

@app.get("/")
def read_root():
    return {"message": "Hello World FastAPI"}


# Endpoint GET /chats/{id} → retourne un chat par son identifiant
@app.get("/chats/{id}")
def get_chat(id: int):
    try:
        with open(CHATS_FILE, "r", encoding="utf-8") as f:
            chats = json.load(f)
        # Vérifie si l'id est valide
        if 0 <= id < len(chats):
            return {"chat": chats[id]}
        else:
            return {"error": "Chat non trouvé pour cet identifiant"}
    except FileNotFoundError:
        return {"error": "Fichier chats.json non trouvé"}