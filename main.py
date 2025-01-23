from contextlib import asynccontextmanager
import pathlib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from sqlmodel import SQLModel
from database.db import engine
from strawberry.fastapi import GraphQLRouter
from graphql_schema import schema

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

graphql_app = GraphQLRouter(schema)

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graphql_app, prefix='/graphql')


# DO NOT INCLUDE THIS FUNC IN THE INSTRUCTIONS
# ALSO REMOVE ASSOCIATED IMPORTS
@app.get('/', response_class=HTMLResponse)
async def serve_html():
    html_file = pathlib.Path('welcome/welcome_page.html')
    return HTMLResponse(content=html_file.read_text())