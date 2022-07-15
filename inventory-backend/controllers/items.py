from fastapi import APIRouter, Query
from pymysql import NULL
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
async def items_from_cst(cst_id:int, current_user: User = Depends(get_current_active_user)):
    try:
        if not cst_funcs.get_costumer_from_id(cst_id):
            raise InvalidCostumerIDException

        data=item_funcs.get_all_items_from_cst(cst_id)

        role = user_funcs.get_role_costumer(current_user.id, cst_id)
        
        item_list=[]
        idx=len(data)
        if role==USER_ROLE_ADMIN or role==USER_ROLE_OPERATOR:
            for i in range(idx):
                item_list.append({"id": data[i][0],
                                "name": data[i][1],
                                "description": data[i][2],
                                "category": data[i][3],
                                "renter_user_id": data[i][6]})
        else:
            for i in range(idx):
                if data[i][6] == None:
                    avail = True
                else: avail = False
                item_list.append({"id": data[i][0],
                                "name": data[i][1],
                                "description": data[i][2],
                                "category": data[i][3],
                                "available_for_rent": avail})

        return item_list
    except InvalidCostumerIDException:
        raise HTTPException(status_code=403, detail="Invalid costumer ID")



@router.post("/item/update_rfid", tags=["items"])
async def update_items_rfid(item_id:int, new_rfid: str, current_user: User = Depends(get_current_active_user)):
    try:

        item = item_funcs.get_item_from_id(item_id)
        if not item:
            raise InvalidItemException
        
        check_if_employee(current_user.id, item.costumer_id)

        checkitem = item_funcs.get_item_from_rfid(new_rfid)

        if checkitem:
            if checkitem.id == item_id:
                raise AlreadyRFIDException
            else: 
                raise InvalidRFIDException

        

        item_funcs.update_rfid(item_id, new_rfid)

        return

    except InvalidItemException:
        raise HTTPException(status_code=403, detail="Invalid Item ID")
    except AlreadyRFIDException:
        raise HTTPException(status_code=403, detail="RFID already set to this item")
    except InvalidRFIDException:
        raise HTTPException(status_code=403, detail="New RFID already in use")
    except NotAssociatedException:
        raise HTTPException(status_code=401, detail="You are not associated to costumer")
    except NoPermissionException:
        raise HTTPException(status_code=401, detail="You don't have permission")



@router.post("/item/delete_rfid", tags=["items"])
async def delete_items_rfid(item_id:int, current_user: User = Depends(get_current_active_user)):
    try:

        item = item_funcs.get_item_from_id(item_id)
        if not item:
            raise InvalidItemException
        
        check_if_employee(current_user.id, item.costumer_id)

        item_funcs.delete_rfid(item_id)

        return
    except InvalidItemException:
        raise HTTPException(status_code=403, detail="Invalid Item ID")
    except NotAssociatedException:
        raise HTTPException(status_code=401, detail="You are not associated to costumer")
    except NoPermissionException:
        raise HTTPException(status_code=401, detail="You don't have permission")


@router.post("/item/rent_item", tags=["items"])
async def rent_items_by_rfid(item_rfid: str, current_user: User = Depends(get_current_active_user)):
    try:
        rent_item = item_funcs.get_item_from_rfid(item_rfid)
        if not rent_item:
            raise InvalidRFIDException

        if not user_funcs.get_role_costumer(current_user.id, rent_item.costumer_id):
            raise NotAssociatedException

        
        renters_id=item_funcs.get_renters_id(rent_item.id)
        if renters_id==current_user.id:
            raise AlreadyRentedbymeException
        if renters_id!=None:
            raise AlreadyRentedException

        item_funcs.rent_item(rent_item.id, current_user.id)

        return
    except AlreadyRentedbymeException:
        raise HTTPException(status_code=403, detail="Item already in your possession")
    except NotAssociatedException:
        raise HTTPException(status_code=403, detail="You are not associated to costumer")
    except InvalidRFIDException:
        raise HTTPException(status_code=403, detail="Invalid Item RFID")
    except AlreadyRentedException:
        raise HTTPException(status_code=403, detail="Item already rented by someone")


@router.post("/item/return_item", tags=["items"])
async def return_item_by_rfid(item_rfid: str, current_user: User = Depends(get_current_active_user)):
    try:
        rent_item = item_funcs.get_item_from_rfid(item_rfid)
        if not rent_item:
            raise InvalidRFIDException
        
        renters_id=item_funcs.get_renters_id(rent_item.id)
        if renters_id!=current_user.id:
            raise NoPermissionException

        item_funcs.return_item(rent_item.id)

        return
    except InvalidRFIDException:
        raise HTTPException(status_code=403, detail="Invalid Item RFID")
    except NoPermissionException:
        raise HTTPException(status_code=403, detail="Item not in your possession")