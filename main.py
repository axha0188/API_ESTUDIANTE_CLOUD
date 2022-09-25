from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.estudiante_routes import estudiante


app = FastAPI(
    title="Estudiantes API",
    description="REST API de Estudiantes usando python y mysql",
    version="0.0.1",
    # openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(estudiante)
