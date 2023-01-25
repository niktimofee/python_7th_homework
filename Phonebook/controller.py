import view, model_sorting

def start():
    while True:
        op = view.get_operation()
        if op == 1:
            view.add_user_entry()
        elif op == 2:
            view.print_table()
        elif op == 3:
            view.print_only_names()
        elif op == 4:
            model_sorting.sort_names()
        elif op == 5:
            model_sorting.sort_id()
        elif op == 6:
            break