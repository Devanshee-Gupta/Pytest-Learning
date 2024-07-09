
def function_true():
    return True

def print_hello_world():
    print("hello world")

def add(num1,num2):
    return num1+num2

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be less than 0")
    else:
        return age