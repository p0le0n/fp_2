orders = [
    {"order_id": 1, "customer_id": 101, "amount": 150.0},
    {"order_id": 2, "customer_id": 102, "amount": 200.0},
    {"order_id": 3, "customer_id": 101, "amount": 75.0},
    {"order_id": 4, "customer_id": 103, "amount": 100.0},
    {"order_id": 5, "customer_id": 101, "amount": 50.0},
    {"order_id": 6, "customer_id": 102, "amount": 120.0},
    {"order_id": 7, "customer_id": 103, "amount": 90.0},
    {"order_id": 8, "customer_id": 104, "amount": 80.0},
    {"order_id": 9, "customer_id": 102, "amount": 60.0},
    {"order_id": 10, "customer_id": 101, "amount": 30.0},
    {"order_id": 11, "customer_id": 105, "amount": 110.0},
    {"order_id": 12, "customer_id": 101, "amount": 70.0},
    {"order_id": 13, "customer_id": 103, "amount": 95.0},
    {"order_id": 14, "customer_id": 105, "amount": 200.0},
    {"order_id": 15, "customer_id": 102, "amount": 85.0},
    {"order_id": 16, "customer_id": 104, "amount": 40.0},
    {"order_id": 17, "customer_id": 103, "amount": 120.0},
    {"order_id": 18, "customer_id": 105, "amount": 70.0},
    {"order_id": 19, "customer_id": 104, "amount": 55.0},
    {"order_id": 20, "customer_id": 101, "amount": 45.0},
]

def filter_orders(orders, customer_id):
    filtered_orders = filter(lambda order: order["customer_id"] == customer_id, orders)
    return list(filtered_orders)

def calculate_total_amount(orders):
    total_amount = sum(map(lambda order: order["amount"], orders))
    return total_amount

def calculate_average_amount(orders):
    total_amount = calculate_total_amount(orders)
    num_orders = len(orders)
    average_amount = total_amount / num_orders if num_orders > 0 else 0
    return average_amount

customer_id_to_filter = 101
filtered_orders = filter_orders(orders, customer_id_to_filter)
total_amount_for_customer = calculate_total_amount(filtered_orders)
average_amount_for_customer = calculate_average_amount(filtered_orders)

print(f"Заказы для клиента с ID {customer_id_to_filter}:")
for order in filtered_orders:
    print(order)

print(f"Общая сумма заказов для клиента: {total_amount_for_customer}")
print(f"Средняя стоимость заказов для клиента: {average_amount_for_customer}")
