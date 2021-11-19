import re
from myKoob.get_subject import subjects

def extract_task(text):
    task_extract_text = text
    name = re.match(r".*?\[(.*)].*", text)

    for s in subjects:
        task_extract_text = task_extract_text.replace(str(s), "")

    task_extract_text = re.sub(r"(Pievienots|Labots) jauns uzdevums", "", task_extract_text)
    task_extract_text = re.sub(r"jauns uzdevums", "", task_extract_text)
    task_extract_text = re.sub(r"(Tr|Ce|Ot|Pi|Pie|Pir|Se|Sv)[^\w\s]\s+([0-9][0-9]|[0-9])[^\w\s]\s+([a-z][a-z][a-z]|[a-z][a-z])", "", task_extract_text)
    task_extract_text = re.sub(r"priekšmetā", "", task_extract_text)
    task_extract_text = re.sub(r"Nodarbība", "", task_extract_text)
    task_extract_text = task_extract_text.replace(f"{name}", "")

    return task_extract_text