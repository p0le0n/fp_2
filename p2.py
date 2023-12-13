users = [
    {"name": "Alice", "expenses": [100, 50, 75, 200]},
    {"name": "Bob", "expenses": [50, 75, 80, 100]},
    {"name": "Charlie", "expenses": [200, 300, 50, 150]},
    {"name": "David", "expenses": [100, 200, 300, 400]},
    {"name": "Eve", "expenses": [50, 60, 70, 80]},
    {"name": "Frank", "expenses": [200, 300, 400, 500]},
    {"name": "Grace", "expenses": [75, 100, 125, 150]},
    {"name": "Hank", "expenses": [150, 200, 250, 300]},
    {"name": "Ivy", "expenses": [100, 150, 200, 250]},
    {"name": "Jack", "expenses": [50, 100, 150, 200]},
    {"name": "Kevin", "expenses": [200, 250, 300, 350]},
    {"name": "Linda", "expenses": [75, 80, 85, 90]},
    {"name": "Mike", "expenses": [100, 150, 200, 250]},
    {"name": "Nancy", "expenses": [50, 75, 100, 125]},
    {"name": "Oliver", "expenses": [200, 225, 250, 275]},
    {"name": "Paul", "expenses": [75, 150, 225, 300]},
    {"name": "Quinn", "expenses": [100, 200, 300, 400]},
    {"name": "Rachel", "expenses": [50, 100, 150, 200]},
    {"name": "Sam", "expenses": [200, 250, 300, 350]},
    {"name": "Tom", "expenses": [75, 80, 85, 90]}
]

# Критерии фильтрации (например, пользователи с общими расходами больше 500)
criteria = lambda user: sum(user["expenses"]) > 500

# Шаг 1: Фильтрация пользователей по критериям
filtered_users = list(filter(criteria, users))

# Шаг 2: Рассчитываем общие расходы для каждого пользователя
total_expenses_per_user = list(map(lambda user: (user["name"], sum(user["expenses"])), filtered_users))

# Шаг 3: Получаем общую сумму расходов всех отфильтрованных пользователей
total_expenses = sum(map(lambda user: sum(user["expenses"]), filtered_users))

print("Отфильтрованные пользователи:")
for user in filtered_users:
    print(user)

print("\nОбщая сумма расходов отфильтрованных пользователей:", total_expenses)
