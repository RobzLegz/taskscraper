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
            task_type = "uzdevums"
            t_string = re.sub(r"(Pievienots|Labots) jauns uzdevums ", "", t_string)
            
            date_tuple = re.findall(r"(Tr|Ce|Ot|Pi|Pie|Pir|Se|Sv)[^\w\s]\s+([0-9][0-9]|[0-9])[^\w\s]\s+([a-z][a-z][a-z]|[a-z][a-z])", t_string)
            if not date_tuple:
                continue
            
            date_tuple = date_tuple[0]
            if not date_tuple:
                continue

            date_arr = np.asarray(date_tuple)
            task_out_date = f"{date_arr[0]}, {date_arr[1]}. {date_arr[2]}"

            subject = get_subject(t_string)

            task_text = extract_task(t_string)

            t_data.append(task_type)
            t_data.append(subject)
            t_data.append(task_text)
            t_data.append(task_out_date)

            table_data.append(t_data)
            table_data.append(["------------", "------------", "------------", "------------"])
        else:
            continue

    return_data = tabulate(table_data, headers=["Uzdevuma tips", "Priekšmets", "Uzdevums", "Izveidots"])
    return return_data