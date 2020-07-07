

def f():
    0/0
    return 1

def a():
    try: f()
    except:
        print("1"+1)

a()