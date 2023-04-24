from db_sqlalchemy.session import session
from db_sqlalchemy.models import Orders


class OrdersRepository:
    def __init__(self):
        self.__session = session

    def insert_one(self, order: Orders):
        self.__session.add(order)
        self.__session.commit()
