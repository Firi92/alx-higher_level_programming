#!/usr/bin/python3


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

2-main.py


vi 2-safe_print_list_integers.py

#!/usr/bin/python3
