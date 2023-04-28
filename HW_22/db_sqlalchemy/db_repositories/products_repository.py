from db_sqlalchemy.session import session
from db_sqlalchemy.models import Products, Orders


class ProductsRepository:
    def __init__(self):
        self.__session = session

    def insert_one(self, product: Products):
        self.__session.add(product)
        self.__session.commit()

    def get_orders_with_products_total(self):
        lst = []
        for p, o in self.__session.query(Products, Orders).filter(Products.id == Orders.product_id).all():
            lst.append("ID: {} Name: {} Price: {} Quantity: {} Total: {}".format(p.id, p.name, p.price, o.quantity,
                                                                                 p.price * o.quantity))
        return "\n".join(lst)
