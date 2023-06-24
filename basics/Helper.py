def is_integer(number):
    if isinstance(number,float):
        return number.is_integer()
    elif isinstance(number,int):
        return True
    else:
        return False