from fastapi import FastAPI
from routers import user_router

app = FastAPI()

@app.get("/")
def root():
    return "Welcome To FastAPI."

app.include_router(user_router.router, prefix="/users", tags=["Users"])
