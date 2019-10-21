def is_odd(number):
    if number % 2 == 1: # 2로 나누었을떄 나머지가 1이면 홀수이다.
        return True
    else:
        return False

is_odd(3)
True
is_odd(4)
False

is_odd = lambda x: True if x % 2 == 1 else False
is_odd(3)
True
