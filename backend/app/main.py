from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.modules.skins.router import router
from app.modules.skins.service import SkinNotFoundError

app = FastAPI()

app.include_router(router)


@app.exception_handler(SkinNotFoundError)
async def skin_not_found_handler(
    request: Request,
    exc: SkinNotFoundError
):
    return JSONResponse(
        status_code=404,
        content={"detail": "Skin not found"}
    )