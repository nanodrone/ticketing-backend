# Ticketing Backend API

Backend API realizzata con FastAPI e SQLModel per gestire utenti, asset IT e ticket di assistenza.

## Funzionalità

- Gestione utenti
- Gestione asset aziendali
- Creazione ticket di assistenza
- Aggiornamento stato e priorità ticket
- Validazione dati con FastAPI e Pydantic
- Test automatici con pytest
- Esecuzione locale con SQLite
- Esecuzione containerizzata con Docker e PostgreSQL

## Stack

- Python
- FastAPI
- SQLModel
- SQLite
- PostgreSQL
- pytest
- Docker Compose

## Struttura progetto

```text
.
├── app/
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── users.py
│       ├── assets.py
│       └── tickets.py
├── tests/
│   ├── conftest.py
│   └── test_tickets.py
├── Dockerfile
├── compose.yaml
├── requirements.txt
└── README.md
```

## Avvio locale

### 1. Clona il progetto

```bash
git clone [https://github.com/TUO-USERNAME/ticketing-backend.git](https://github.com/TUO-USERNAME/ticketing-backend.git)
cd ticketing-backend
```

### 2. Crea ambiente virtuale

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installa dipendenze

```bash
pip install -r requirements.txt
```

### 4. Avvia l'app

```bash
uvicorn app.main:app --reload
```

### 5. Apri documentazione API

```text
http://127.0.0.1:8000/docs
```

## Avvio con Docker

### 1. Build e avvio servizi

```bash
docker compose up --build
```

### 2. Documentazione API

```text
http://localhost:8000/docs
```

### 3. Arresto servizi

```bash
docker compose down
```

## Test

Esegui i test con:

```bash
pytest
```

## Endpoint principali

### Users
- `POST /users/`
- `GET /users/`
- `GET /users/{user_id}`

### Assets
- `POST /assets/`
- `GET /assets/`
- `GET /assets/{asset_id}`

### Tickets
- `POST /tickets/`
- `GET /tickets/`
- `GET /tickets/{ticket_id}`
- `PATCH /tickets/{ticket_id}`

## Esempio request ticket

```json
{
  "title": "Laptop non si avvia",
  "description": "Schermo nero dopo accensione",
  "priority": "high",
  "user_id": 1,
  "asset_id": 1
}
```

## Obiettivi del progetto

Questo progetto è stato realizzato per esercitarsi con:

- progettazione API REST
- gestione database SQL
- testing backend
- versionamento con Git e GitHub
- containerizzazione con Docker

## Roadmap

- autenticazione utenti
- ruoli e permessi
- filtro ticket per stato e priorità
- paginazione
- CI con GitHub Actions

## Autore

Progetto sviluppato da Denis Canepa.