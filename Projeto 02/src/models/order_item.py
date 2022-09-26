

async def create_order_item(order_items_collection, user, address_user, order, product):
    try:
        order_item  = await order_items_collection.insert_one({
            'user': {user},
            'address': {address_user},
            'order': {order},
            'product': {product}
        })

        if order_item.inserted_id:
            order = await get_order_item(order_items_collection, order_item.inserted_id)
            return order_item

    except Exception as e:
        print(f'create_order.error: {e}')
        

async def get_order_item(order_items_collection, order_item_id):
    try:
        data = await order_items_collection.find_one({'_id': order_item_id})
        if data:
            return data
    except Exception as e:
        print(f'get_order.error: {e}') 
        
async def add_order_item(order_items_collection):
    try:
        pass         

    except Exception as e:
        print(f'add_order_item.error: {e}')

async def delete_order_item(order_items_collection):
    try:
        order_item = await order_items_collection.delete_one(
            {'order_item': order_item}
            )
        if order_item.deleted_count:
            return {'status': f'{order_item} deleted'}
    except Exception as e:
        print(f'delete_order_item.error: {e}')