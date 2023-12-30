from pydantic import BaseModel, validator


class Item(BaseModel):
    id: int
    name: str


class ItemList(BaseModel):
    item_list: list[Item] = []

class ItemGroup(BaseModel):
    id: int
    group_name: str


class ItemCreate(BaseModel):
    name: str
    @validator('name', 'name')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class ItemGroupCreate(BaseModel):
    group_name: str
    @validator('group_name', 'group_name')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v