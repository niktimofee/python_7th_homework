def get_operation():
    operation = int(input(
        " 1 - добавить пользователя \n 2 - вывести таблицу \n 3 - вывести только имя и фамилию \n 4 - отсортировать по именам \n 5 - отсортировать по id \n 6 - выход \n"))
    return operation

def add_user_entry():
    id = int(input("✏️  Введите порядковый номер записи: "))
    name = input("✏️  Введите имя: ")
    lastname = input("✏️  Введите фамилию: ")
    number = int(input("✏️  Введите номер телефона: "))
    comments = input("✏️  Добавьте комментарий к записи: ")
    line = f"{id}, {name}, {lastname}, {number}, {comments} \n"
    with open("phonebook.txt", "a") as file:
        file.write(line)
    print(" 💾 Сохранено")

def print_table():
    with open("phonebook.txt", "r") as file:
        for line in file.readlines():
            print(line, end ="")

def print_only_names():
    with open("phonebook.txt", "r") as file:
        for line in file.readlines():
            temp = line.split(",")
            print(f"Имя:{temp[1]}, Фамилия:{temp[2]}")