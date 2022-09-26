from models import user, address

user = (user.find({'id': {id}}))

address_user = address.find({'user._id': user[id]})

async def create_order(orders_collection):
    try:
        order = await orders_collection.insert_one({'user': {user}, 'address': {address_user}}, order)

        if order.inserted_id:
            order = await get_order(orders_collection, order.inserted_id)
            return order

    except Exception as e:
        print(f'create_order.error: {e}')
        

async def get_order(orders_collection, order_id):
    try:
        data = await orders_collection.find_one({'_id': order_id})
        if data:
            return data
    except Exception as e:
        print(f'get_order.error: {e}')          
        

async def get_order_total_price(orders_collection):
    try:
        order_total = orders_collection.aggregate([
            {
                "$group":{
                    "_id": "$order_items";
                    "sum_price": {$sum: '$product.price'}
                }
            }
        ])
        return order_total
        
    except Exception as e:
        print(f'get_order.error: {e}')
        

async def delete_order(orders_collection):
    try:
        order = await orders_collection.delete_one(
            {'order': order}
            )
        if order.deleted_count:
            return {'status': f'{address_user} deleted'}
    except Exception as e:
        print(f'delete_order.error: {e}')