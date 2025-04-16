def sum_lists(list1, list2):
    # Перевірка, що списки мають однакову довжину
    if len(list1) != len(list2):
        raise ValueError("Списки повинні бути однакової довжини.")
    
    # Обчислення попарних сум
    result = [a + b for a, b in zip(list1, list2)]
    
    return result

# Якщо запускаємо main.py без імпорту з іншого файлу
if __name__ == "__main__":
    # Приклад виклику функції для демонстрації
    result = sum_lists([1, 2, 3], [4, 5, 6])
    print("Результат:", result)

