def solution(number):
    """ function returns the sum of all the multiples of 3 or 5 below the number passed in"""
    return sum(x for x in range(1, number) if x % 3 == 0 or x % 5 == 0)