""" main """

from fastapi import FastAPI
from routers import broken_access_control 


app = FastAPI()
app.include_router(broken_access_control.router)

@app.get("/")
async def root():
    """ root """
    return {"message": "Hello Bigger Applications!"}
