# app/pkg/middleware/error_handler.py

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import traceback
import logging

logger = logging.getLogger("uvicorn.error")

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            # Log completo del error para debug
            logger.error(f"❌ Unhandled error: {str(exc)}\n{traceback.format_exc()}")
            return JSONResponse(
                status_code=500,
                content={
                    "isError": True,
                    "message": "Internal Server Error",
                    "data": str(exc)
                }
            )
