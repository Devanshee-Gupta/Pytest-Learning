
class Student:

    def __init__(self,name : str ,age : int) -> None:
        self.name = name 
        self.age = age

    def get_age(self) -> int :
        return self.age



def print_dict(_dict):
    print(_dict)