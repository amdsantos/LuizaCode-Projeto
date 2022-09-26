from src.models.order import (
    create_order,
    get_order,
    get_order_total_price,
    delete_order,
)

from src.models.address import address_user
from src.models.user import get_user

from src.server.database import connect_db, db, disconnect_db


async def orders_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    orders_collection = db.orders_collection
    
    order = {
        "user": get_user,
        "price": 1000.0,
        "paid": True,
        "create": "",
        "address": address_user,
        "authority": ""
    }

    if option == '1':
        # create order
        order = await create_order(
            orders_collection,
            order
        )
        print(order)
    elif option == '2':
        # get order
        order = await get_order(
            orders_collection,
            order["_id"]
        )
        print(order)
    elif option == '3':
        # total
        order = await get_order(
            orders_collection,
            order["_id"]
        )
        print(order)
    elif option == '4':
        # delete
        order = await get_order_total_price(
            orders_collection,
            order["order_total"]
        )

        result = await delete_order(
            orders_collection,
            order["_id"]
        )

        print(result)
    
    await disconnect_db()