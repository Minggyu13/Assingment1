from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.item import item_router

app = FastAPI()

origins = [
    "http://localhost:5173",
]



app.include_router(item_router.router)
