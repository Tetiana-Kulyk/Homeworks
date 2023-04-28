from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from typing import List

from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column
from db_sqlalchemy.session import __engine

Base = declarative_base()


class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(VARCHAR(50))
    price = Column(Integer)
    children: Mapped[List["Orders"]] = relationship(back_populates="parent")

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, price: {self.price}"


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity = Column(Integer)
    parent: Mapped["Products"] = relationship(back_populates="children")

    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity


Base.metadata.create_all(__engine, Base.metadata.tables.values(), checkfirst=True)
