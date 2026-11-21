from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.modules.skins.router import router
from app.modules.skins.exceptions import AppException 

app = FastAPI()

app.include_router(router)


@app.exception_handler(AppException)
async def App_Handler(
    request: Request,
    exc:AppException
):
    return JSONResponse(
       status_code= exc.error_code,
       content={
           "message" : exc.message,
           "error_code":exc.error_code,
           "details":exc.details
       }
    )