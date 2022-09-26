from src.models.address import (
    create_address,
    get_address_user,
    update_address,
    delete_address
)
from src.server.database import connect_db, db, disconnect_db


async def address_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    address_collection = db.address_collection
    
    address =  {
        "street": "Avenida Paulista" ,
        "cep": "05245-090",
        "district": "Centro",
        "city": "São Paulo",
        "state": "São Paulo",
        "is_delivery": True
    }

    if option == '1':
        # create address
        address = await create_address(
            address_collection,
            address
        )
        print(address)
    elif option == '2':
        # get address
        address = await get_address_user(
            address_collection,
            address["address_user"]
        )
        print(address)
    elif option == '3':
        # update
        address = await get_address_user(
            address_collection,
            address["address_user"]
        )

        is_updated, address_updated = await update_address(
            address_collection,
            address["address_user"],
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, endereço alterado {address_updated}")
        else:
            print("Atualização falhou!")
    elif option == '4':
        # delete
        address = await get_address_user(
            address_collection,
            address["address_user"]
        )

        result = await delete_address(
            address_collection,
            address["address_user"]
        )

        print(result)

    elif option == '5':
        # pagination
        address = await get_address_user(
            address_collection,
            skip=0,
            limit=2
        )
        print(address)

    await disconnect_db()
