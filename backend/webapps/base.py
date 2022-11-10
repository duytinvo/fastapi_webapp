from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from webapps.auth import route_login
from webapps.jobs import route_jobs
from webapps.texts import route_texts
from webapps.users import route_users

templates = Jinja2Templates(directory="templates")

api_router = APIRouter(include_in_schema=False)

@api_router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    return templates.TemplateResponse(
        "general_pages/index.html", {"request": request, "msg": msg}
    )

api_router.include_router(route_jobs.router, prefix="", tags=["jobs-webapp"])
api_router.include_router(route_users.router, prefix="", tags=["users-webapp"])
api_router.include_router(route_login.router, prefix="", tags=["auth-webapp"])
api_router.include_router(route_texts.router, prefix="/texts-webapp", tags=["texts-webapp"])
