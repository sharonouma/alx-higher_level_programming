#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    arr = [size, None]
    if size == 0:
        return tuple(arr)
    else:
        arr = [size, sentence[0]]
        return tuple(arr)
