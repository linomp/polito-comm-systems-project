from fastapi import APIRouter, HTTPException

from schemas.costumer import NewCostumerDAO, Costumer
from services.customers import *
from cruds import costumers as cst_func

from components.custom_exceptions import *

router = APIRouter()


@router.post("/customers/new_cst", tags=["customers"])
async def add_new_customer(customer_data: NewCostumerDAO):
    try:
        if cst_func.get_costumer_from_name(customer_data.name):
            raise InvalidNameException
        created_user = create_new_customer(Costumer(**customer_data.dict()))
        return created_user
    except InvalidNameException:
        raise HTTPException(status_code=403, detail="Name already in use")


@router.get("/customers/all_cst", tags=["customers"])
async def get_all_costumers():
    data = cst_func.get_list_all_cst()

    cst_list = []
    idx = len(data)
    for i in range(idx):
        cst_list.append({"id": data[i][0],
                         "name": data[i][1],
                         "category": data[i][2]})

    return cst_list
