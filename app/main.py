from fastapi import FastAPI

from app.features.resume.router import router as resume_router
from app.features.job_descri.router import router as job_descrip_router

app = FastAPI()

app.include_router(resume_router)
app.include_router(job_descrip_router)


@app.get("/health")
def check_health():
    return {"message": "API running !!"}