# Main file
import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.db.database import engine, Base

from app.users.routes import user_router, employee_router, employment_contract_router
from app.clients.routes import client_router, client_contract_router
from app.cost_centers.routes import cost_center_router
from app.suppliers.routes import supplier_router
from app.outgoing_invoices.routes import outgoing_invoice_router, outgoing_invoice_payments_router
from app.incoming_invoices.routes import incoming_invoice_router, incoming_invoice_payments_router
from app.equipment.routes import equipment_router, assigned_equipment_router
Base.metadata.create_all(bind=engine)


def init_app():
    """Functions that runs all routes"""
    app = FastAPI(ui_config={"syntaxHighlight.theme": "obsidian"})
    app.include_router(user_router)
    app.include_router(employee_router)
    app.include_router(employment_contract_router)
    app.include_router(cost_center_router)
    app.include_router(client_router)
    app.include_router(client_contract_router)
    app.include_router(supplier_router)
    app.include_router(outgoing_invoice_router)
    app.include_router(outgoing_invoice_payments_router)
    app.include_router(incoming_invoice_router)
    app.include_router(incoming_invoice_payments_router)
    app.include_router(equipment_router)
    app.include_router(assigned_equipment_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)
