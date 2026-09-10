## Run the API

From the project root, activate the virtual environment before starting
Uvicorn:

```bash
source .venv/bin/activate
uvicorn app.main:app --reload
```

Alternatively, run Uvicorn directly without activating the environment:

```bash
.venv/bin/python -m uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`.
