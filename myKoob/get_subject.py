import re

def get_subject(text):
    task_class_short_tuple = re.findall(r"priekšmetā\s+(Matem|Algorim|Dabaszin|Datorsis|nozares tehnisko darbu pamatiemaņas|Sabiedrība|Fizika|Svešvaloda|Sports|Otra|Latviešu)", text)
    
    if not task_class_short_tuple:
        return None

    task_class_short_tuple = task_class_short_tuple[0]
    if not task_class_short_tuple:
        return None
    
    return return_subject(task_class_short_tuple)

subjects = [
    "Matemātika 1",
    "Fizika 1",
    "EIKT pamatprocesi un darbu veidi PA1",
    "EIKT nozares tehnisko darbu pamatiemaņas PA2",
    "Informācijas un komunikācijas tehnoloģijas (1., 2.līmenis) M2",
    "Preču un pakalpojumu izvēle EIKT infrastruktūras izveidei PA4",
    "Algorimēšanas un programmēšanas pamati PA3", 
    "Dabaszinības (Ķīmija, ģeogrāfija, bioloģija)", 
    "Latviešu valoda un literatūra 1",
    "Datorsistēmas un datortīkli PB1",
    "Otra svešvaloda B1",
    "Sabiedrība un cilvēka drošība M1",
    "matemātika", 
    "Datorsistēmas un datortīkli", 
    "Sabiedrība un cilvēka drošība", 
    "Sistēmu programmēšana PB2",
    "Svešvaloda 1",
    "Fizika", 
    "Svešvaloda", 
    "Sports", 
    "Otra svešvaloda", 
    "Latviešu valoda un literatūra",
]

def return_subject(short):
    if short == "Matem":
        return "matemātika"
    elif short == "Algorim":
        return "Algorimēšanas un programmēšanas pamati PA3"
    elif short == "Dabaszin":
        return "Dabaszinības (Ķīmija, ģeogrāfija, bioloģija)"
    elif short == "Datorsis":
        return "Datorsistēmas un datortīkli"
    elif short == "Sabiedrība":
        return "Sabiedrība un cilvēka drošība"
    elif short == "Fizika":
        return "Fizika"
    elif short == "Svešvaloda":
        return "Svešvaloda"
    elif short == "Sports":
        return "Sports"
    elif short == "Otra":
        return "Otra svešvaloda"
    elif short == "Latviešu":
        return "Latviešu valoda un literatūra"