def get_number(msg):
    is_num = False
    while not is_num:
        result = input(msg)
        if result.isdigit():
            is_num = True
    return int(result)

def get_str(msg):
    is_vaild_str = False
    while not is_vaild_str:
        result = input(msg).strip()
        if result.isalpha():
            is_vaild_str = True
    return result.lower()

