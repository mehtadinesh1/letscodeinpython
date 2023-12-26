def dashboard(char_list):
    print(f'''  
      Tic-Tac-Toe
    ~~~~~~~~~~~~~~~~~
    || {char_list[0]} || {char_list[1]} || {char_list[2]} ||
    ~~~~~~~~~~~~~~~~~
    || {char_list[3]} || {char_list[4]} || {char_list[5]} ||
    ~~~~~~~~~~~~~~~~~
    || {char_list[6]} || {char_list[7]} || {char_list[8]} ||
    ~~~~~~~~~~~~~~~~~''')
def player_input(char_list,Player_char):
    while True:
     player_move = int(input(f"{Player_char}: Where would you like to place your piece (1-9): "))
     if player_move <= 9 and player_move >= 1:
         if char_list[player_move-1] == "_":
             return player_move
         else:
             print("Spot already choosed")
     else:
         print("Spot is not on dashboard")

def change_dashborad(player_move,p_char,char_l):
    char_l[player_move-1] = p_char

def winning_conditions(d_l,p_m):
         return (d_l[0]==d_l[1]==d_l[2]==p_m or d_l[3]==d_l[4]==d_l[5]==p_m or d_l[6]==d_l[7]==d_l[8]==p_m  #row
                or d_l[0]==d_l[3]==d_l[6]==p_m or d_l[1]==d_l[4]==d_l[7]==p_m or d_l[2]==d_l[5]==d_l[8]==p_m #column
                or d_l[0]==d_l[4]==d_l[8]==p_m or d_l[2]==d_l[4]==d_l[6]==p_m ) #diagonal

#main program
Player1 = 'X'
Player2 = '0'
dash_list = ['_'] * 9
num_list=['1','2','3','4','5','6','7','8','9']
dashboard(num_list)
dashboard(dash_list)
while True:
    player1_move = player_input(dash_list,Player1)
    change_dashborad(player1_move, Player1, dash_list)
    dashboard(num_list)
    dashboard(dash_list)
    if winning_conditions(dash_list,Player1):
        print("Player 1 wins!!!")
        break;
    elif '_' not in dash_list:
        print(("Its Tie"))
    player2_move = player_input(dash_list,Player2)
    change_dashborad(player2_move,Player2,dash_list)
    dashboard(num_list)
    dashboard(dash_list)
    if winning_conditions(dash_list,Player2):
        print(("Player 2 wins!!!"))
        break;

print("Thank you using our services")