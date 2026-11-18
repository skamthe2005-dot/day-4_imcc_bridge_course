orders = [ 
    { 
        'id': 101, 
        'customer': 'Asha', 
        'status': 'DELIVERED', 
        'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)] 
    }, 
    { 
        'id': 102, 
        'customer': 'Ravi', 
        'status': 'CANCELLED', 
        'items': [('monitor', 1, 10999.0)] 
    }, 
    { 
        'id': 103, 
        'customer': 'Asha', 
        'status': 'DELIVERED', 
        'items': [('cable', 5, 199.0)] 
    }, 
    { 
        'id': 104, 
        'customer': 'Meera', 
        'status': 'SHIPPED', 
        'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)] 
    }, 
    { 
        'id': 105, 
        'customer': 'Ravi', 
        'status': 'DELIVERED', 
        'items': [('mouse', 3, 599.0)] 
    } 
] 

for order in orders:
    total=0
    x=order.get("items")
    for i in x:
        total+=i[2]

print(total)





# def fun(orders):
#     for order in orders:
#         if order["status"]=="DELIVERED" :
#             print(order)


# fun(orders)