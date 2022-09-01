#!/usr/bin/python3


def safe_print_division(a, b):    
    try:
        num = a / b
    except: 
        num = None;
        print(ZeroDivisionError)
    finally:
        print("Inside result: {}".format(num))
        return num

    if __name__ == "__main__":
        safe_print_division()
