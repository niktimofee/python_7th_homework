def sort_names():
    with open("phonebook.txt", "r+") as file:
        list_with_str = file.readlines()
        list_with_list = []
        for line in list_with_str:
            temp = line.split(",")
            list_with_list.append(temp)
        list_with_list = sorted(list_with_list, key = lambda x:x[1])
        file.seek(0)
        for user in list_with_list:
            file.write(",".join(user))
        print(" 📑 Отсортировано по имени")

def sort_id():
    with open("phonebook.txt", "r+") as file:
        list_with_str = file.readlines()
        list_with_list = []
        for line in list_with_str:
            temp = line.split(",")
            list_with_list.append(temp)
        list_with_list = sorted(list_with_list, key = lambda x:x[0])
        file.seek(0)
        for user in list_with_list:
            file.write(",".join(user))
        print(" 📑 Отсортировано по id")