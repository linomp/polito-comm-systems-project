from fastapi import APIRouter

from schemas.costumer import NewCostumerDAO, Costumer
from services.customers import create_new_customer

router = APIRouter()


@router.post("/customers", tags=["customers"])
def add_new_customer(customer_data: NewCostumerDAO):
    created_user = create_new_customer(Costumer(**customer_data.dict()))

    return created_user
