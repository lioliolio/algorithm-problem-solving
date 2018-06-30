# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]

    A.sort()

    for i in range(0, len(A), 2):
        if i == len(A) - 1:
            return A[i]

        if A[i] != A[i+1]:
            return A[i]
