def total_salary(path):
    try:
        total_sum = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
              
                name, salary = line.strip().split(',')
                total_sum += int(salary)
                count += 1
       
        average_salary = total_sum / count if count > 0 else 0
        return total_sum, average_salary
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return 0, 0


total, average = total_salary("C:\\Users\\Admin\\Documents\\Homework\\Hw4\\path.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
