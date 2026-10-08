import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()

bearer = HTTPBearer(auto_error=False)

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")


async def verify_bearer_token(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer)],
):
    if credentials is None:
        raise HTTPException(status_code=401, detail="Missing bearer token")

    if credentials.credentials != BEARER_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid bearer token")

    return credentials.credentials


@app.get("/protected")
async def protected(
    token: Annotated[str, Depends(verify_bearer_token)],
):
    return {"message": "Bearer authentication successful"}
