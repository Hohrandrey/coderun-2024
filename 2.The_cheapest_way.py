import sys

# Ввод N и M
print("Введите N и M через пробел:")
N, M = map(int, input().split())


# Создание словаря для хранения данных
data = {}

# Чтение данных
for i in range(N):
    print(f"Введите строку {i + 1}:")
    value = input()  # Читаем одну строку
    data[f'var_{i}'] = value
    
for key in data.items():
    for b in range(len(key)):
        print(key[b])
# Вывод результатов
print("\nРезультирующий словарь:")
print(data)
print(f"\nN: {N}, M: {M}")