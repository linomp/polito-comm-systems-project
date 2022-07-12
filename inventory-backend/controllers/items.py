from fastapi import APIRouter, Query
from tables import Description
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

        
        check_if_admin(current_user.id, cst_id)

        if item_data.name == "None" or item_data.category == "None":
            raise InvalidItemNameorCategException

        if item_data.description == "None":
            item_data.description = None

        if item_data.rfid == "None":
            item_data.rfid = None

        new_item = Item(name=item_data.name,
                        description=item_data.description,
                        category=item_data.category,
                        costumer_id=cst_id,
                        rfid=item_data.rfid)
        item_funcs.add_item(new_item)

        return 
    except InvalidItemNameorCategException:
        raise HTTPException(status_code=403, detail="Invalid Item name or Category")
    except InvalidCostumerIDException:
        raise HTTPException(status_code=403, detail="Invalid costumer ID")
    except NotAssociatedException:
        raise HTTPException(status_code=401, detail="You are not associated to costumer")
    except NoPermissionException:
        raise HTTPException(status_code=401, detail="You don't have permission")

