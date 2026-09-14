from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.roles import router as role_router
from app.api.transactions import router as transaction_router
from app.api.users import router as user_router


app = FastAPI(
    title="RGS",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(
    user_router,
    prefix="/api/v1",
)

app.include_router(
    auth_router,
    prefix="/api/v1",
)

app.include_router(
    role_router,
    prefix="/api/v1",
)

app.include_router(
    transaction_router,
    prefix="/api/v1",
)
