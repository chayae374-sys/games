def print_menu():
    menu = """
    ========== TOURNAMENT MANAGER ==========
    1. Add team
    2. Show all teams
    3. Add match result
    4. Show standings
    5. Show leading team
    6. Show best attacking team
    7. Show team success rate
    8. Show teams without wins
    9. Show tournament summary
    10. Check championship potential
    0. Exit
    Choose an option:
    """
    print(menu)

def get_input():
    user = None
    while True:
        try:
            user = int(input("what is your choise? "))
            if user >= 0 and user < 11:
                return user
            elif user > 10 or user < 0:
                print("invaild option, please try again")
        except ValueError:
            print("not vaild input")
get_input()



