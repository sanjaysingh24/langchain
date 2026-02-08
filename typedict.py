from typing import TypedDict
class Person(TypedDict):
    name:str
    age:int

new_person:Person={
    'name':"sanju",
    'ager':'45'
}

print(new_person)