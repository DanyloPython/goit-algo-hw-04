def get_cats_info(path1):
    cats_list = []  
    try:
        with open(path1, 'r', encoding='utf-8') as file: 
            for line in file: 
                id, name, age = line.strip().split(',') 
                cats_list.append({"id": id, "name": name, "age": age})  
    except FileNotFoundError:
        print(f"Помилка: Файл {path1} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    return cats_list  

cats_info = get_cats_info("C:\\Users\\Admin\\Documents\\Homework\\Hw4\\path1.txt")
print(cats_info)
