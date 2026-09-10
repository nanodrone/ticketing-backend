from fastapi import FastAPI
from app.db import create_db_and_tables
from app.routers.assets import router as assets_router
from app.routers.users import router as users_router
from app.routers.tickets import router as tickets_router

app = FastAPI(title="Ticketing API")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def root():
    return {"message": "Ticketing API attiva"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(users_router)
app.include_router(assets_router)
app.include_router(tickets_router)