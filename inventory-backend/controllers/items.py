from fastapi import APIRouter, Query
from schemas.item import NewItemDAO

from services.users import *
from schemas.user import *
from schemas.item import *
from cruds import items as item_funcs
from cruds import costumers as cst_funcs
from components.custom_exceptions import *

router = APIRouter()


@router.post("/item/add_item", tags=["items"])
async def add_item_to_cst(item_data: NewItemDAO, cst_id: int, current_user: User = Depends(get_current_active_user)):
    try:
        if not cst_funcs.get_costumer_from_id(cst_id):
            raise InvalidCostumerIDException

        check_if_employee(current_user.id, cst_id)

        if item_data.name == "" or item_data.category == "":
            raise InvalidItemException

        if item_data.description == "":
            item_data.description = None

        if item_data.rfid == "":
            item_data.rfid = None
        elif item_funcs.get_item_from_rfid(item_data.rfid):
            raise InvalidRFIDException
        

        new_item = Item(name=item_data.name,
                        description=item_data.description,
                        category=item_data.category,
                        costumer_id=cst_id,
                        rfid=item_data.rfid)
        item_funcs.add_item(new_item)

        return
    except InvalidItemException:
        raise HTTPException(status_code=403, detail="Invalid Item name or Category")
    except InvalidRFIDException:
        raise HTTPException(status_code=403, detail="RFID already in use")
    except InvalidCostumerIDException:
        raise HTTPException(status_code=403, detail="Invalid costumer ID")
    except NotAssociatedException:
        raise HTTPException(status_code=401, detail="You are not associated to costumer")
    except NoPermissionException:
        raise HTTPException(status_code=401, detail="You don't have permission")


@router.post("/item/remove_item", tags=["items"])
async def rmv_item(item_id: int, current_user: User = Depends(get_current_active_user)):
    try:
        rmv_item = item_funcs.get_item_from_id(item_id)
        if not rmv_item:
            raise InvalidItemException

        if not cst_funcs.get_costumer_from_id(rmv_item.costumer_id):
            raise InvalidCostumerIDException

        check_if_employee(current_user.id, rmv_item.costumer_id)

        item_funcs.remove_item(rmv_item.id)

        return
    except InvalidItemException:
        raise HTTPException(status_code=403, detail="Invalid Item ID")
    except InvalidCostumerIDException:
        raise HTTPException(status_code=403, detail="Invalid costumer ID")
    except NotAssociatedException:
        raise HTTPException(status_code=401, detail="You are not associated to costumer")
    except NoPermissionException:
        raise HTTPException(status_code=401, detail="You don't have permission")



@router.post("/item/change_item_description", tags=["items"])
async def change_description(item_id: int,new_description: str, current_user: User = Depends(get_current_active_user)):
    try:
        chg_item = item_funcs.get_item_from_id(item_id)
        if not chg_item:
            raise InvalidItemException

        if not cst_funcs.get_costumer_from_id(chg_item.costumer_id):
            raise InvalidCostumerIDException

        check_if_employee(current_user.id, chg_item.costumer_id)

        item_funcs.update_description(item_id, new_description)

        return
    except InvalidItemException:
        raise HTTPException(status_code=403, detail="Invalid Item ID")
    except InvalidCostumerIDException:
        raise HTTPException(status_code=403, detail="Invalid costumer ID")
    except NotAssociatedException:
        raise HTTPException(status_code=401, detail="You are not associated to costumer")
    except NoPermissionException:
        raise HTTPException(status_code=401, detail="You don't have permission")



@router.post("/item/change_item_category", tags=["items"])
async def change_categ(item_id: int,new_categ: str, current_user: User = Depends(get_current_active_user)):
    try:
        chg_item = item_funcs.get_item_from_id(item_id)
        if not chg_item:
            raise InvalidItemException

        if not cst_funcs.get_costumer_from_id(chg_item.costumer_id):
            raise InvalidCostumerIDException

        check_if_employee(current_user.id, chg_item.costumer_id)

        item_funcs.update_category(item_id, new_categ)

        return
    except InvalidItemException:
        raise HTTPException(status_code=403, detail="Invalid Item ID")
    except InvalidCostumerIDException:
        raise HTTPException(status_code=403, detail="Invalid costumer ID")
    except NotAssociatedException:
        raise HTTPException(status_code=401, detail="You are not associated to costumer")
    except NoPermissionException:
        raise HTTPException(status_code=401, detail="You don't have permission")



@router.get("/item/all_items_from_cst", tags=["items"])
async def items_from_cst(cst_id:int):
    try:
        if not cst_funcs.get_costumer_from_id(cst_id):
            raise InvalidCostumerIDException

        data=item_funcs.get_all_items_from_cst(cst_id)

        item_list=[]
        idx=len(data)
        for i in range(idx):
            item_list.append({"id": data[i][0],
                              "name": data[i][1],
                              "description": data[i][2],
                              "category": data[i][3]})

        return item_list
    except InvalidCostumerIDException:
        raise HTTPException(status_code=403, detail="Invalid costumer ID")

