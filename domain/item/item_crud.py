from models import Item, ItemGroup
from sqlalchemy.orm import Session
from datetime import datetime
from domain.item.item_schema import ItemCreate, ItemGroupCreate

def get_item_list(db: Session):
    item_list = db.query(Item).all()
    return item_list



def create_item(db: Session, item_create:ItemCreate):
    db_item = Item(name=item_create.name)
    db.add(db_item)
    db.commit()


def create_item_group(db: Session, item_group_create: ItemGroupCreate):
    db_item_group = ItemGroup(group_name=item_group_create.group_name)
    db.add(db_item_group)
    db.commit()
