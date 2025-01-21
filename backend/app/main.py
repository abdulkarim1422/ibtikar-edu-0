import fastapi
from app.routers import all_routers


app = fastapi.FastAPI()

# Include routers
app.include_router(all_routers.router)
