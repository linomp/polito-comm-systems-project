from fastapi import APIRouter, HTTPException

from schemas.costumer import NewCostumerDAO, Costumer
from services.customers import *
from cruds import costumers as cst_func

router = APIRouter()


@router.post("/customers/new_cst", tags=["customers"])
def add_new_customer(customer_data: NewCostumerDAO):
    try:
        created_user = create_new_customer(Costumer(**customer_data.dict()))
        return created_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/customers/all_cst", tags=["customers"])
def get_all_costumers():
    data= cst_func.get_list_all_cst()

    cst_list=[]
    idx=len(data)
    for i in range(idx):
        cst_list.append({"id": data[i][0],
                         "name": data[i][1],
                         "category": data[i][2]})

    return cst_list

