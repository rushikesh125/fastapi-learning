products = [
    {
        "id": 1,
        "name": "Wireless Bluetooth Headphones",
        "price": 1999,
        "category": "Electronics",
        "stock": 25,
        "rating": 4.5
    },
    {
        "id": 2,
        "name": "Men's Casual T-Shirt",
        "price": 499,
        "category": "Clothing",
        "stock": 50,
        "rating": 4.2
    },
    {
        "id": 3,
        "name": "Smart Watch",
        "price": 2999,
        "category": "Electronics",
        "stock": 15,
        "rating": 4.6
    },
    {
        "id": 4,
        "name": "Running Shoes",
        "price": 2499,
        "category": "Footwear",
        "stock": 30,
        "rating": 4.4
    },
    {
        "id": 5,
        "name": "Backpack",
        "price": 999,
        "category": "Accessories",
        "stock": 40,
        "rating": 4.3
    },
    {
        "id": 6,
        "name": "Laptop Stand",
        "price": 799,
        "category": "Electronics",
        "stock": 20,
        "rating": 4.1
    },
    {
        "id": 7,
        "name": "Bluetooth Speaker",
        "price": 1499,
        "category": "Electronics",
        "stock": 35,
        "rating": 4.5
    },
    {
        "id": 8,
        "name": "Women's Handbag",
        "price": 1799,
        "category": "Fashion",
        "stock": 18,
        "rating": 4.4
    },
    {
        "id": 9,
        "name": "Gaming Mouse",
        "price": 899,
        "category": "Electronics",
        "stock": 22,
        "rating": 4.6
    },
    {
        "id": 10,
        "name": "Sunglasses",
        "price": 699,
        "category": "Accessories",
        "stock": 45,
        "rating": 4.2
    }
]




# print([p for p in products if p["category"]=="Electronics"])


# nums = [1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15]
# nums = [[n,n*n] for n in nums if n%2 != 0]

# print(nums)

result = [n for n in products if n["category"]=="Electronics"]

print(result)