def my_steps(n):
    if not isinstance(n, int) or not (1 <= n <= 25):
        raise ValueError
    if n == 1 or n == 2:
        return n
    else:
        return my_steps(n-1) + my_steps(n-2)

print(my_steps(0))
