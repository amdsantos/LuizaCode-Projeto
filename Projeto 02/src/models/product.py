
async def create_product(products_collection):
    try:
        product = await products_collection.insert_one(product)
        
        if product.inserted_id:
            product = await get_product(products_collection, product.inserted_id)
        return product

    except Exception as e:
        print(f'create_product.error: {e}')
        
async def get_product(products_collection, product_id):
    try:
        data = await products_collection.find_one({'_id': product_id})
        if data:
            return data
        
    except Exception as e:
        print(f'get_product.error: {e}')

async def get_products(products_collection, skip, limit):
    try:
        product_cursor = products_collection.find().skip(int(skip)).limit(int(limit))
        products = await product_cursor.to_list(length=int(limit))
        return products

    except Exception as e:
        print(f'get_products.error: {e}')

async def delete_product(products_collection, product_id):
    try:
        product = await products_collection.delete_one(
            {'_id': product_id}
        )
        if product.deleted_count:
            return {'status': f'{product_id} deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')