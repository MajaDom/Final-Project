import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.db.database import engine, Base

from app.users.routes import user_router, employee_router, employment_contract_router
from app.clients.routes import client_router
from app.cost_centers.routes import cost_center_router
from app.suppliers.routes import supplier_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(employee_router)
    app.include_router(employment_contract_router)
    app.include_router(client_router)
    app.include_router(cost_center_router)
    app.include_router(supplier_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)
