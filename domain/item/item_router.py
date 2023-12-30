from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from domain.item import item_schema, item_crud
from database import get_db
from domain.item.item_schema import Item, ItemGroup
router = APIRouter(
    prefix="/api/item",
)

@router.get("/list", response_model=item_schema.ItemList)
def item_list(db: Session = Depends(get_db)):
        item_list = item_crud.get_item_list(db)
        return {
            'item_list': item_list
                }



@router.post("/item_create", status_code=status.HTTP_204_NO_CONTENT)
def item_create(item_create: item_schema.ItemCreate, db: Session = Depends(get_db)):
    item_crud.create_item(db=db, item_create=item_create)



@router.post("/item_group_create", status_code=status.HTTP_204_NO_CONTENT)
def item_group_create(item_group_create: item_schema.ItemGroupCreate, db: Session = Depends(get_db)):
    item_crud.create_item_group(db=db, item_group_create=item_group_create)



#6번을 어떻게 해야할지 감이 잘 안잡힙니다
