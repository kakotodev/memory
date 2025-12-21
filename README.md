# MEMORY - Projet Vue JS

# TECHNOLOGIE
- Figma

- Vue.JS
- TailwindCSS
- FastAPI

- Git

# Structure du projet
```
MEMORY/
├── app/                      # Partie Front-end (Vue.js + Vite)
│   ├── public/               # Images et icônes statiques (favicon)
│   ├── src/                  # LE CŒUR DU FRONT-END
│   │   ├── assets/           # Tes images, logos et CSS
│   │   ├── components/       # Tes composants réutilisables
│   │   ├── router/           # Gestion des pages (URLs)
│   │   ├── stores/           # Gestion de l'état (Pinia/Vuex)
│   │   ├── views/            # Tes pages complètes
│   │   ├── App.vue           # Composant racine
│   │   └── main.js           # Point d'entrée JavaScript
│   ├── index.html            # Fichier HTML principal
│   └── package.json          # Liste des bibliothèques installées
│
├── fastapi/                  # Partie Back-end (Python)
│   ├── venv/                 # Environnement Python (ne pas toucher)
│   └── main.py               # (À créer) Ton API qui communiquera avec Vue
│
└── .gitignore                # Pour éviter d'envoyer les fichiers lourds sur Git
```

# Instalattion du projet 

1. Entre dans le dossier et installer les dependances :
    ```bash
    cd app
    npm install
    npm run dev
    ```
2. Pour FastAPI (à la racine) : 
    ```
    cd fastapi
    python -m venv venv
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```


