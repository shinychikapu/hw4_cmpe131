def my_step(n):
    if n == 1 or n == 0:
        return '1 step '
    else:
        return my_step(n-1) + my_step(n-2)
print(my_step(5)) 

