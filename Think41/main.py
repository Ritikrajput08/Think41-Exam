from fastapi import fastapifrom 
app.routers import routers
app= FastAPI(title = "kanban Board API")
app.include_router(router)
