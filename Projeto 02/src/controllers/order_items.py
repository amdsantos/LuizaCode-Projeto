from src.models.order_item import (
    create_order_item,
    get_order_item,
    add_order_item,
    delete_order_item,
)

from src.models.order import get_order
from src.models.product import get_product

from src.server.database import connect_db, db, disconnect_db


async def order_items_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_items_collection = db.order_items_collection
    
    order_item = {
        "order": get_order,
        "product": get_product
    }

    if option == '1':
        # create order_item
        order_item = await create_order_item(
            order_items_collection,
            order_item
        )
        print(order_item)
    elif option == '2':
        # add order_item
        order_item = await add_order_item(
            order_items_collection,
            order_item["_id"]
        )
        print(order_item)
    elif option == '3':
        # delete
        order_item = await get_order_item(
            order_items_collection,
            order_item["order._id"]
        )

        result = await delete_order_item(
            order_items_collection,
            order_item["_id"]
        )

        print(result)
        
    await disconnect_db()
