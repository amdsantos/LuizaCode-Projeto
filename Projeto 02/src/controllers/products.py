from src.models.product import (
    create_product,
    get_product,
    delete_product,
    get_products
)
from src.server.database import connect_db, db, disconnect_db


async def products_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    products_collection = db.products_collection
    
    product =  {
        "name": "Bicicleta Aro 29 Freio a Disco 21M. Velox Branca/Verde - Ello Bike",
        "description": "Bicicleta produzida com materiais de qualidade e foi criada pensando nas pessoas que desejam praticar o ciclismo e ter uma vida saudável sem abrir mão de conforto um excelente custo x benefício.",
        "price": 898.2,
        "image": "https://a-static.mlcdn.com.br/800x560/fritadeira-eletrica-sem-oleo-air-fryer-nell-fit-preto-32l-com-timer/magazineluiza/222479100/64ef4d6200a6efc6cce6d265588910a9.jpg",
        "code": 97880.0
    }

    if option == '1':
        # create product
        product = await create_product(
            products_collection,
            product
        )
        print(product)
    elif option == '2':
        # get product
        product = await get_product(
            products_collection,
            product["_id"]
        )
        print(product)
   
    elif option == '4':
        # delete
        product = await get_product(
            products_collection,
            product["_id"]
        )

        result = await delete_product(
            products_collection,
            product["_id"]
        )

        print(result)

    elif option == '5':
        # pagination
        products = await get_products(
            products_collection,
            skip=0,
            limit=2
        )
        print(products)

    await disconnect_db()
