def avg_numbers(*args): # 입력 개수에 상관없이 사용하기 위해*args를 사용
    result = 0
    for i in args:
        result += i
    return result / len(args)

avg_numbers(1,2)
1.5 
avg_numbers(1,2,3,4,5)
3.0
