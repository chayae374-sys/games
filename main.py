from menu import print_menu
from i_o import get_number,get_str
from functions import get_id_and_number,check,create_team,Add_team,Show_all_teams,get_id,checking_home_id,checking_away_id,checking_goals,checking_duble,create_matches,Add_match_result

def main():
    while True:
        print_menu()
        choose_number = get_input()
        if choose_number == 0:
            print("by by")
            break
        if choose_number == 1:
            Add_team()
        if choose_number == 2:
            Show_all_teams()
        if choose_number == 3:
            Add_match_result()
        if choose_number == 4:
            Show_standings()
        if choose_number == 5:
            Show_leading_team()
        if choose_number == 6:
            Show_best_attacking_team()
        if choose_number == 7:
            Show_team_success_rate()
        if choose_number == 8: 
            Show_teams_without_wins()
        if choose_number == 9:
            Show_tournament_summary()
        if choose_number == 10:
            Check_championship_potential()

if __name__ == "__main__":
    main()
            








