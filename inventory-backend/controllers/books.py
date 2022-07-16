from fastapi import APIRouter, Query
from pymysql import NULL

from schemas.book import *
from services.users import *
from schemas.user import *
from schemas.item import *
from cruds import items as item_funcs
from cruds import costumers as cst_funcs
from cruds import books as book_funcs
from components.custom_exceptions import *

router = APIRouter()

@router.post("/books/add_book_information", tags=["books"])
async def add_book(cst_id: int, item_id: int, book_data: BookDAO, current_user: User = Depends(get_current_active_user)):
    try:
        if not cst_funcs.get_costumer_from_id(cst_id):
            raise InvalidCostumerIDException

        check_if_employee(current_user.id, cst_id)

        book_item=item_funcs.get_item_from_id(item_id)
        if not book_item:
            raise InvalidItemException
        if book_item.costumer_id != cst_id:
            raise WrongCsttoItemException
        if book_funcs.get_book_from_book_id(item_id):
            raise AlreadyBookException

        if book_data.author == "":
            raise InvalidBookException

        if book_data.year == 0:
            book_data.year = None
        if book_data.publisher == "":
            book_data.publisher = None
        if book_data.language == "":
            book_data.language = None
        

        new_book = Book(book_id=item_id,
                        author=book_data.author,
                        year=book_data.year,
                        publisher=book_data.publisher,
                        language=book_data.language)
        book_funcs.add_book(new_book)

        return
    except AlreadyBookException:
        raise HTTPException(status_code=403, detail="Item already in Book table")
    except InvalidBookException:
        raise HTTPException(status_code=403, detail="Invalid book author")
    except WrongCsttoItemException:
        raise HTTPException(status_code=403, detail="Item does not belong to that costumer")
    except InvalidItemException:
        raise HTTPException(status_code=403, detail="Invalid item ID")
    except NotAssociatedException:
        raise HTTPException(status_code=401, detail="You are not associated to costumer")
    except NoPermissionException:
        raise HTTPException(status_code=401, detail="You don't have permission")
