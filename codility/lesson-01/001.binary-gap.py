# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # write your code in Python 3.6
    binary_number = bin(N).replace('0b', '')

    max_count = 0
    temp_count = 0

    for i in binary_number:
        if i == "1":
            if max_count < temp_count:
                max_count = temp_count
            temp_count = 0
        else:
            temp_count += 1

    return max_count
