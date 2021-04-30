"""function counter"""
def func_counter(num):
    def inner_func():
        nonlocal num
        num = num +1
        print(num)
    return inner_func
a = func_counter(8)
a()
a()