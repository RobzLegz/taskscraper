from get_mykoob_data import get_mykoob_tasks

def get_data():
    print("A: E-klase")
    print("B: MyKoob")

    task_page = input("select Your task page: ")
    tasks = None

    if task_page == "A":
        pass
    elif task_page == "B":
        tasks = get_mykoob_tasks()
    else:
        get_data()

    if tasks:
        print(tasks)

get_data()