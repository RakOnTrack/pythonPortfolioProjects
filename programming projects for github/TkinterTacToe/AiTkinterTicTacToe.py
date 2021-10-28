import random
import copy
from tkinter import *

window = Tk()
window.title('Tic-Tac-Toe Tkinter vs AI')
window.config(padx=100, pady=100)
two_players = False
orig_vals ={1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

vals = copy.copy(orig_vals)

def show_map():
    map = f'{vals[1]}|{vals[2]}|{vals[3]}\n' \
          f'-+-+-\n' \
          f'{vals[4]}|{vals[5]}|{vals[6]}\n' \
          f'-+-+-\n' \
          f'{vals[7]}|{vals[8]}|{vals[9]}\n'
    print(map)

def has_won(le,one,two,three, testing):
    if testing == False:
        winning_three= [one,two,three]
        for i in winning_three:
            i -= 1
            button_list[i]["highlightbackground"] = "red"
        print(f'{le} wins!')
        for button in button_list:
            button['state'] = 'disabled'
    return True

def check_if_won(vals, le, button_list, testing):
    global game_on
    # 4 horizontal, 4 vertical, 3 diagonal.
    if vals[1] == le and vals[2] == le and vals[3] == le:
        has_won(le, 1, 2,3, testing)
        return True
    elif vals[4] == le and vals[5] == le and vals[6] == le:
        has_won(le,4,5,6, testing)
        return True
    elif vals[7] == le and vals[8] == le and vals[9] == le:
        has_won(le,7,8,9, testing)
        return True
    elif vals[1] == le and vals[4] == le and vals[7] == le:
        has_won(le,1,4,7, testing)
        return True
    elif vals[2] == le and vals[5] == le and vals[8] == le:
        has_won(le,2,5,8, testing)
        return True
    elif vals[3] == le and vals[6] == le and vals[9] == le:
        has_won(le,3,6,9, testing)
        return True

    elif vals[1] == le and vals[5] == le and vals[9] == le:
        has_won(le,1,5,9, testing)
        return True
    elif vals[3] == le and vals[5] == le and vals[7] == le:
        has_won(le,3,5,7, testing)
        return True
    else:
        return False


def turn(le,b, num):
    choice = num
    try:
        if vals[choice] == " ":
            vals[choice] = le
            b['text'] = le
            show_map()
            b['state'] = 'disabled'
            # finished_turn = True
        else:
            print('please choose an empty spot.')
    except KeyError or ValueError:
        print('select a position between 1-9.')

def check_if_tied():
    # default game is tied
    not_tied = False
    for val in vals:
        # game isnt tied if theres a blank space.
        if vals[val] == ' ':
            not_tied = True
            break
    if not_tied == False:
        print('Game is tied.')
        for button in button_list:
            button['state'] = 'disabled'
        return True

def reset_game():
    global vals
    vals = copy.copy(orig_vals)
    who_goes_first()


def who_goes_first():
    global x_turn
    # game_on = True
    if random.choice([2, 3]) == 2:#deciding who will go first, randomly.
        print("O will go first.")
        x_turn = False
        if two_players == False:
            ai_move('O', "X")

    else:
        print("X will go first.")
        x_turn = True
    if x_turn == False:
        update_label('O')
    else:
        update_label('X')
    return x_turn

def clicked(b, num):
    global x_turn
    if two_players == True: #two players mode
        global x_turn
        if  x_turn == True:
            # if b.text == ' ':
            turn('X', b, num)
            x_turn = False
            update_label('O')
            if check_if_won(vals, 'X', button_list, False) == False:
                pass

        elif x_turn == False:
            turn('O', b, num)
            x_turn = True
            update_label('X')
            if check_if_won(vals, 'O', button_list, False) == False:
                pass
    elif two_players == False: #vs cpu mode
        print('Go X.')
        turn('X', b, num)
        if check_if_won(vals,'X',button_list, False) == False:
            print('Go O.')
            ai_move('O', "X")
            check_if_won(vals, 'O', button_list, False)

        # update_label()

def update_label(le):
    turnLabel['text'] = f'{le}'
    return le

def ai_move(le, opp):
    global vals
    if two_players == True:
        pass
    else:
        board_copy = copy.copy(vals)
        open_spaces = []
        moves_list = []
        move_decided = False
        for position, val in board_copy.items():
            if val == ' ':
                open_spaces.append(position)

    # check if theres a move that will win.
        for val in open_spaces:
            board_copy[val] = le
            if check_if_won(board_copy, le, button_list, True) == True:
                moves_list.append(val)
                move_decided = True
                break
            else:
                board_copy = copy.copy(vals)

    #  check if theres a move that will stop user from winning
        if move_decided == False:
            for val in open_spaces:
                board_copy[val] = opp
                if check_if_won(board_copy, opp, button_list, True) == True:
                    moves_list.append(val)
                    move_decided = True
                    break
                else:
                    board_copy = copy.copy(vals)

        # if ai can neither win or block opponent, go for a free corner, or middle, then side
        if move_decided == False:
            corners = [1, 3, 7, 9]
            # middle = [5] #keep as comment
            sides = [2, 4, 6, 8]
            corner_available = False
            middle_available = False
            for corner in corners:
                if corner in open_spaces:
                    moves_list.append(corner)
                    corner_available = True
            if corner_available == False:
                if 5 in open_spaces:
                    moves_list.append(5)
                    middle_available = True
            if corner_available == False and middle_available == False:
                for side in sides:
                    if side in open_spaces:
                        moves_list.append(side)

        decided_move = random.choice(moves_list)
        choice = decided_move
        print(f'ai has moved to {decided_move}.')
        vals[choice] = le
        val_button_dict = {1:Button1, 2:Button2, 3:Button3, 4:Button4, 5:Button5, 6:Button6, 7:Button7, 8:Button8, 9:Button9}
        b = val_button_dict[choice]
        b['text'] = le
        b['state'] = 'disabled'
        show_map()

def reset_buttons(list):
    for button in list:
        button['text'] = ' '
        button['state'] = 'normal'
        button['highlightbackground'] = 'white'
    reset_game()

Button1 = Button(text=f'{vals[1]}', width=10, height=5, command=lambda: clicked(Button1, 1))  # 1
Button2 = Button(text=f'{vals[2]}', width=10, height=5, command=lambda: clicked(Button2, 2))  # 2
Button3 = Button(text=f'{vals[3]}', width=10, height=5, command=lambda: clicked(Button3, 3))  # 3
Button4 = Button(text=f'{vals[4]}', width=10, height=5, command=lambda: clicked(Button4, 4))  # 4
Button5 = Button(text=f'{vals[5]}', width=10, height=5, command=lambda: clicked(Button5, 5))  # 5
Button6 = Button(text=f'{vals[6]}', width=10, height=5, command=lambda: clicked(Button6, 6))  # 6
Button7 = Button(text=f'{vals[7]}', width=10, height=5, command=lambda: clicked(Button7, 7))  # 7
Button8 = Button(text=f'{vals[8]}', width=10, height=5, command=lambda: clicked(Button8, 8))  # 8
Button9 = Button(text=f'{vals[9]}', width=10, height=5, command=lambda: clicked(Button9, 9))  # 9

button_list = [Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9]

Button1.grid(column=0, row=0)
Button2.grid(column=1, row=0)
Button3.grid(column=2, row=0)
Button4.grid(column=0, row=1)
Button5.grid(column=1, row=1)
Button6.grid(column=2, row=1)
Button7.grid(column=0, row=2)
Button8.grid(column=1, row=2)
Button9.grid(column=2, row=2)

resetButton = Button(text='Reset', width=5, height=5, command=lambda: reset_buttons(button_list))
turnLabel = Label(text=f' ', width=5, height=5)

turnLabel.grid(column=2, row=4)
resetButton.grid(column=1, row=4)

reset_game()
show_map()

window.mainloop()
