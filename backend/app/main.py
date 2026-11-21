from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.errors import AppException
from app.modules.skins.router import router

app = FastAPI(debug=settings.DEBUG)

app.include_router(router)


@app.exception_handler(AppException)
async def app_exception_handler(
    request: Request,
    exc:AppException
):
    return JSONResponse(
       status_code= exc.code,
       content={
           "message" : exc.message,
           "code":exc.code,
           "details":exc.details
       }
    )
