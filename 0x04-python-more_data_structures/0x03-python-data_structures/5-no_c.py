#!/usr/bin/python3
def no_c(my_string):
    my_string = ''.join(ch for ch in my_string if ch not in 'Cc')
    return my_string
