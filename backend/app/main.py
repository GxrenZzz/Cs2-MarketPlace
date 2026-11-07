from fastapi import FastAPI
from app.modules.skins.router import router
app = FastAPI()

app.include_router(router)