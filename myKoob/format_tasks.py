from tabulate import tabulate
import re
import numpy as np
from myKoob.get_subject import get_subject
from myKoob.extract_task import extract_task

def format_tasks(tasks):
    table_data = []

    for t in tasks:
        t_data = []

        t_string = str(t).replace("salīdzināt ar klasesbiedriem", "")
        t_string = t_string.replace("]", "")
        t_string = t_string.replace("[", "")

        if "uzdevums" in t_string:
            t_string = re.sub(r"(Pievienots|Labots) jauns uzdevums ", "", t_string)
            
            subject = get_subject(t_string)

            task_text = extract_task(t_string)

            t_data.append(subject)
            t_data.append(task_text)

            table_data.append(t_data)
            table_data.append(["------------", "------------"])
        else:
            continue

    return_data = tabulate(table_data, headers=["Priekšmets", "Uzdevums"])
    return return_data