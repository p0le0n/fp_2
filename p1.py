# Создаем список словарей с данными о студентах и их оценках
students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88, 92]},
    {"name": "Bob", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "David", "age": 19, "grades": [80, 85, 87, 91]},
    {"name": "Eva", "age": 23, "grades": [75, 82, 79, 88]},
    {"name": "Frank", "age": 20, "grades": [90, 92, 88, 95]},
    {"name": "Grace", "age": 22, "grades": [85, 86, 88, 90]},
    {"name": "Hannah", "age": 21, "grades": [88, 89, 92, 94]},
    {"name": "Ivy", "age": 19, "grades": [78, 82, 85, 88]},
    {"name": "Jack", "age": 24, "grades": [88, 89, 92, 94]},
    {"name": "Kate", "age": 20, "grades": [82, 85, 88, 90]},
    {"name": "Liam", "age": 21, "grades": [95, 96, 98, 97]},
    {"name": "Mia", "age": 22, "grades": [78, 79, 85, 88]},
    {"name": "Noah", "age": 20, "grades": [92, 93, 95, 94]},
    {"name": "Olivia", "age": 21, "grades": [88, 90, 92, 91]},
    {"name": "Peter", "age": 19, "grades": [75, 78, 82, 85]},
    {"name": "Quinn", "age": 23, "grades": [88, 89, 92, 94]},
    {"name": "Ryan", "age": 22, "grades": [85, 86, 88, 90]},
    {"name": "Samantha", "age": 20, "grades": [89, 90, 91, 94]},
    {"name": "Tyler", "age": 21, "grades": [82, 85, 88, 90]}
]

# Функция для фильтрации студентов определенного возраста
def filter_students_by_age(students, age):
    return filter(lambda student: student['age'] == age, students)

# Функция для фильтрации студентов по списку предметов
def filter_students_by_subjects(students, min_score):
    return filter(lambda student: all(grade >= 85 for grade in student['grades']), students)

# Функция для вычисления среднего балла студента
def calculate_student_average(student):
    return sum(student['grades']) / len(student['grades'])

# Функция для вычисления общего среднего балла по всем студентам
def calculate_overall_average(students):
    total_grades = sum(map(lambda student: sum(student['grades']), students))
    total_subjects = sum(map(lambda student: len(student['grades']), students))
    return total_grades / total_subjects

# Функция для нахождения студента с самым высоким средним баллом
def find_top_student(students):
    return max(students, key=calculate_student_average)

min_score = 85
# Примеры использования функций
filtered_students_by_age_20 = list(filter_students_by_age(students, 20))
students_who_passed = list(filter_students_by_subjects(students, min_score))
student_averages = list(map(calculate_student_average, students))
overall_average = calculate_overall_average(students)
top_student = find_top_student(students)

# Примеры использования
print("Студенты возраста 20 лет:")
for student in filtered_students_by_age_20:
    print(student['name'])

print("\nСтуденты, набравшие более 85 баллов по всем предметам:")
for student in students_who_passed:
    print(student['name'])

print("\nСредний балл для каждого студента:")
for i, student in enumerate(students):
    print(f"{student['name']}: {student_averages[i]:.2f}")

print("\nОбщий средний балл по всем студентам:", overall_average)

print("\nСтудент с самым высоким средним баллом:", top_student['name'])
