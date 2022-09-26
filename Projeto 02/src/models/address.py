import user
import address


USER = (user.find({'id': {id}}))

address_user = address.find({'user._id': USER[id]})

async def create_address(address_collection):
    
    try:
        address_user == None
        
        if user.iserted_address:
            address_user =  await address_collection.insert_one({'user': {user}, 'address': {address_user}})
        return address_user

    except Exception as e:
        print(f'create_address.error: {e}')

async def get_address_user(address_collection):
    
    address_user = await address_collection.find({'user._id': USER[id]})
    return address_user

    # address_user = await users_collection.find_one({'anddress': address})
    # return address_user

async def update_address(address_collection, address_user):
    try:
        address_user == address_user
        
        address_user = await address_collection.update_one(
            {'user._id': USER[id]},
            {
                '$addToSet': {
                    'address': {address_user}
                }
            }
        );           

    except Exception as e:
        print(f'update_address.error: {e}')

async def delete_address(address_collection, user):
    try:
        address_user = await address_collection.delete_one(
            {'user._address': address_user}
            )
        if user.deleted_count:
            return {'status': f'{address_user} deleted'}
        
    except Exception as e:
        print(f'delete_address.error: {e}')