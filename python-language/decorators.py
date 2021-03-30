import datetime
#it will create logs.txt in a project root folder if you run this file from visual studio code -> run button.

def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Called function with " + " ".join([str(args) for arg in args]) )
        val = func(*args, **kwargs)
        return val
    return wrapper

@log
def run(a, b, c = 9):
    print(a+b+c)

run(1,3,c=9)