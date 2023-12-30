from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from database import Base



association_table = Table( # many to many 관계를 사용해본적도 관계도 잘 몰라서 어려웠습니다.
    'item_to_item_group',
    Base.metadata,
    Column('item_id', Integer, ForeignKey('item.id')),
    Column('item_group_id', Integer, ForeignKey('item_group.id'))
)


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    groups = relationship(
        "ItemGroup", #관계를 설정하려는 모델 이름.
        secondary=association_table, # 중간 테이블지정.
        back_populates="items" #역참조 itemgroup의 items와.
    )

class ItemGroup(Base):
    __tablename__ = 'item_group'

    id = Column(Integer, primary_key=True)
    group_name = Column(String, nullable=False)

    items = relationship(
        "Item",
        secondary=association_table,
        back_populates="groups"
    )