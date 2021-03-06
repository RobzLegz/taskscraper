import re

def get_tasks(task_str):
    text = task_str.replace("(", "[")
    text = text.replace(")", "]")

    name = re.findall(r"(?<=\[).+?(?=\])", text)[0]

    tasks = task_str.split(f"({name})")

    return tasks