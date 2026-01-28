from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from svc.backendsvc.drivers.rest.exception_handlers import exception_container
from svc.backendsvc.drivers.rest.routers import leads

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(leads.router)

exception_container(app)
