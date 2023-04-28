from db_repositories.orders_repository import OrdersRepository
from db_repositories.products_repository import ProductsRepository
from models import Products, Orders

if __name__ == '__main__':
    products_repo = ProductsRepository()

    products_repo.insert_one(Products(name='Chocolate', price=50))
    products_repo.insert_one(Products(name='Chips', price=40))
    products_repo.insert_one(Products(name='Cakes', price=60))
    products_repo.insert_one(Products(name='Cola', price=40))
    products_repo.insert_one(Products(name='Candy', price=20))

    orders_repo = OrdersRepository()

    orders_repo.insert_one(Orders(product_id=1, quantity=3))
    orders_repo.insert_one(Orders(product_id=2, quantity=5))
    orders_repo.insert_one(Orders(product_id=3, quantity=1))
    orders_repo.insert_one(Orders(product_id=4, quantity=10))
    orders_repo.insert_one(Orders(product_id=2, quantity=25))

    print(products_repo.get_orders_with_products_total())
