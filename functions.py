import data as d
from i_o import get_number,get_str
# שאלה 1
def get_id_and_number():
    """Get team ID and name from user."""
    id = get_number("what is team's id? ")
    name = get_str("what is team's name? ")
    return id,name

def check(id,name):
    for item in d.teams:
        if item["id"] == id:
            print("the id is alredy exists !!!")
            return False
    for item in d.teams:
        if item["name"] == name:
            print("the name is alredy exists !!!")
            return False
    return True

def create_team():
    id,name = get_id_and_number()
    return {"id":id,"name":name}
    
def add_team(teams: list):
    id,name = get_id_and_number()
    while not check(id,name):
        id,name = get_id_and_number()
    d.teams.append(create_team())
    print("Entered successfully")

# שאלה_2
def Show_all_teams():
    for item in d.teams:
        print(item["name"])

# שאלה_3
def get_id():
    home_team_id = int(input("what is id of teams home"))
    away_team_id =int(input("what is id of teams away?"))
    home_goals= int(input("how many goals were scored for the teams home ?"))
    away_goals =int(input("how many goals were scored for the teams away ?"))
    return home_team_id,away_team_id,home_goals,away_goals

def checking_home_id():
    home_team_id,away_team_id,home_goals,away_goals = get_id()
    for item in d.teams:
        if item["id"] == home_team_id and home_team_id != away_team_id:
            return  True
    return False
            

def checking_away_id():
    home_team_id,away_team_id,home_goals,away_goals = get_id()
    for item in d.teams:
        if item["id"] == away_team_id:
            return True
    return False
        

def checking_goals():
    home_team_id,away_team_id,home_goals,away_goals = get_id()
    if home_goals.isdigit() and away_goals.isdigit():
        return True
    return False
      
def checking_duble():
    home_team_id,away_team_id,home_goals,away_goals = get_id()
    for item in d.matches:
        if (home_team_id == item["home_team_id"] and away_team_id == item["away_team_id"]) or (home_team_id == item["away_team_id"] and away_team_id == item["home_team_id"]):
            return False
    return True


def create_matches():
    home_team_id,away_team_id,home_goals,away_goals = get_id()
    return {"home_team_id": home_team_id , "away_team_id": away_team_id, "home_goals":home_goals , "away_goals": away_goals}


def Add_match_result():
    home_team_id,away_team_id,home_goals,away_goals = get_id()
    function=[checking_home_id(),checking_away_id(),checking_goals()]
    while all(function):
        home_team_id,away_team_id,home_goals,away_goals = get_id()
    d.matches.append(create_matches())
    print("Entered successfully")

# שאלה_4
