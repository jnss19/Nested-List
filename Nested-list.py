products = [
    {
        "id": 1,
        "name": "IPHONE 13",
        "category": "Electronics",
        "price": 2500,
        "colors": ["gray", "black"],
        "size": ["small", "medium", "large"],
        "stock": [{
            "gray-small": 25,
            "gray-medium": 30,
            "gray-large": 34
        },
        {
            "black-small": 23,
            "black-medium": 23,
            "black-large": 25
        }],
    },
    {
        "id": 2,
        "name": "IPHONE 15",
        "category": "Electronics",
        "price": 2500,
        "colors": ["gray", "black"],
        "size": ["small", "medium", "large"],
        "stock": [{
            "gray-small": 25,
            "gray-medium": 30,
            "gray-large": 34
        },
        {
            "black-small": 23,
            "black-medium": 23,
            "black-large": 25
        }],
    },
    {
        "id": 3,
        "name": "IPHONE 16",
        "category": "Electronics",
        "price": 2500,
        "colors": ["gray", "black"],
        "size": ["small", "medium", "large"],
        "stock": [{
            "gray-small": 25,
            "gray-medium": 30,
            "gray-large": 34
        },
        {
            "black-small": 23,
            "black-medium": 23,
            "black-large": 25
        }],
    }
]

print(products)

products[2]["name"] = "IPHONE 16 PROMAX"

stock_of_product_2 = products[2]["stock"]
print("Stock of product 2:", stock_of_product_2)

index_1_stock_of_product_2 = products[2]["stock"][1]
print("Index 1 stock of product 2:", index_1_stock_of_product_2)

products[2]["stock"][1]["black-small"] = 30 
print("Updated index 1 stock of product 2:", products[2]["stock"][1])
