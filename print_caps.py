def allcaps(func):
    def wrapper():
        print(func().upper())
    return wrapper
