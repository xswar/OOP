from .models import Person

def create(f_name, f_last, age):
    person = Person(
        name=f_name,
        last=f_last,
        age=age
    )
    return person
