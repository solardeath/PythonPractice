#one.py

def func():
    print("FUNC() in ONE.py")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print("ONE.PY IS BEING RUN DIRECTLY")
else:
    print("One.py has been imported")