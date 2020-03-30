import random as rd




print("Welcome to Daniel's Tic-Tac-Toe. A game for legends.")
print("_____________________________________________________\n")
name = input("What's your name? ")
print(f"Hello {name}, please select a position to place an 'X' (1-9)")

a = {'pl1': '   ', 'pl2': '   ', 'pl3': '   ', 'pl4': '   ', 'pl5': '   ', 
     'pl6': '   ', 'pl7': '   ', 'pl8': '   ', 'pl9': '   '}

def reset_placeholders():
    index = 1
    for place in a.keys():
        a[f'pl{index}'] = '   '
        index += 1

def change_placeholders():
    index = 1
    for place in a.keys():
        a[f'pl{index}'] = f' {index} '
        index += 1

def draw_board():
    print(f"     |     |")
    print(f" {a['pl1']} | {a['pl2']} | {a['pl3']} ")
    print(f"     |     |")
    print("-------------------")
    print(f"     |     |")
    print(f" {a['pl4']} | {a['pl5']} | {a['pl6']} ")
    print(f"     |     |")
    print("-------------------")
    print(f"     |     |")
    print(f" {a['pl7']} | {a['pl8']} | {a['pl9']} ")
    print(f"     |     |")
    print('\n')
    
def player():
    position = input()
    print("\n")
    a[f"pl{position}"] = ' X '
          
def computer():
    global computer_choice
    global computer_store
          
    while True:
        computer_choice = rd.randrange(1, 10, 2)
        if a[f"pl{computer_choice}"] != "   ":
            continue
        else:
            computer_store = computer_choice
            break

def check():
    global name
          
    if a['pl1'] == a['pl2'] == a['pl3'] == " X " or a['pl1'] == a['pl2'] == a['pl3'] == " O ":
          if "X" in a['pl1']:
              name = name
          elif "O" in a['pl1']:
              name = "Computer"
          print(f"{name} has won this game!")
          return True
          
    elif a['pl1'] == a['pl4'] == a['pl7'] == " X " or a['pl1'] == a['pl4'] == a['pl7'] == " O ":
          if "X" in a['pl1']:
              name = name
          elif "O" in a['pl1']:
              name = "Computer"
          print(f"{name} has won this game!")
          return True
          
    elif a['pl1'] == a['pl5'] == a['pl9'] == " X " or a['pl1'] == a['pl5'] == a['pl9'] == " O ":
          if "X" in a['pl1']:
              name = name
          elif "O" in a['pl1']:
              name = "Computer"
          print(f"{name} has won this game!")
          return True
          
    elif a['pl4'] == a['pl5'] == a['pl6'] == " X " or a['pl4'] == a['pl5'] == a['pl6'] == " O ":
          if "X" in a['pl4']:
              name = name
          elif "O" in a['pl4']:
              name = "Computer"
          print(f"{name} has won this game!")
          return True
          
    elif a['pl7'] == a['pl8'] == a['pl9'] == " X " or a['pl7'] == a['pl8'] == a['pl9'] == " O ":
          if "X" in a['pl7']:
              name = name
          elif "O" in a['pl7']:
              name = "Computer"
          print(f"{name} has won this game!")
          return True
          
    elif a['pl3'] == a['pl6'] == a['pl9'] == " X " or a['pl3'] == a['pl6'] == a['pl9'] == " O ":
          if "X" in a['pl7']:
              name = name
          elif "O" in a['pl7']:
              name = "Computer"
          print(f"{name} has won this game!")
          return True
          
    elif a['pl2'] == a['pl5'] == a['pl8'] == " X " or a['pl2'] == a['pl5'] == a['pl8'] == " O ":
          if "X" in a['pl7']:
              name = name
          elif "O" in a['pl7']:
              name = "Computer"
          print(f"{name} has won this game!")
          return True
          
    elif a['pl3'] == a['pl5'] == a['pl7'] == " X " or a['pl3'] == a['pl5'] == a['pl7'] == " O ":
          if "X" in a['pl7']:
              name = name
          elif "O" in a['pl7']:
              name = "Computer"
          print(f"{name} has won this game!")
          return True
        
    else:
        return False
          
          
def smart_computer():
    global computer_choice
          
    list1 = [a['pl1'], a['pl2'], a['pl3']]
    list2 = [a['pl1'], '.', '.', a['pl4'], '.', '.', a['pl7']]
    list3 = [a['pl1'], '.', '.', '.', a['pl5'], '.', '.', '.', a['pl9']]
    list4 = ['.', '.', '.', a['pl4'], a['pl5'], a['pl6']]
    list5 = ['.', '.', '.', '.', '.', '.', a['pl7'], a['pl8'], a['pl9']]
    list6 = ['.', '.', a['pl3'], '.', '.', a['pl6'], '.', '.', a['pl9']]
    list7 = ['.', a['pl2'], '.', '.', a['pl5'], '.', '.', a['pl8']]
    list8 = ['.', '.', a['pl3'], '.', a['pl5'], '.', a['pl7']]

    if '   ' in list1 and ' O ' in list1 and ' X ' not in list1 and list1.count('   ') == 1 or '   ' in list1 and ' X ' in list1 and ' O ' not in list1 and list1.count('   ') == 1:
        computer_choice = list1.index("   ") + 1

    elif '   ' in list2 and ' O ' in list2 and ' X ' not in list2 and list2.count('   ') == 1 or '   ' in list2 and ' X ' in list2 and ' O ' not in list2 and list2.count('   ') == 1:
        computer_choice = list2.index("   ") + 1

    elif '   ' in list3 and ' O ' in list3 and ' X ' not in list3 and list3.count('   ') == 1 or '   ' in list3 and ' X ' in list3 and ' O ' not in list3 and list3.count('   ') == 1:
        computer_choice = list3.index("   ") + 1

    elif '   ' in list4 and ' O ' in list4 and ' X ' not in list4 and list4.count('   ') == 1 or '   ' in list4 and ' X ' in list4 and ' O ' not in list4 and list4.count('   ') == 1:
        computer_choice = list4.index("   ") + 1

    elif '   ' in list5 and ' O ' in list5 and ' X ' not in list5 and list5.count('   ') == 1 or '   ' in list5 and ' X ' in list5 and ' O ' not in list5 and list5.count('   ') == 1:
        computer_choice = list5.index("   ") + 1

    elif '   ' in list6 and ' O ' in list6 and ' X ' not in list6 and list6.count('   ') == 1 or '   ' in list6 and ' X ' in list6 and ' O ' not in list6 and list6.count('   ') == 1:
        computer_choice = list6.index("   ") + 1

    elif '   ' in list7 and ' O ' in list7 and ' X ' not in list7 and list7.count('   ') == 1 or '   ' in list7 and ' X ' in list7 and ' O ' not in list7 and list7.count('   ') == 1:
        computer_choice = list7.index("   ") + 1

    elif '   ' in list8 and ' O ' in list8 and ' X ' not in list8 and list8.count('   ') == 1 or '   ' in list8 and ' X ' in list8 and ' O ' not in list8 and list8.count('   ') == 1:
        computer_choice = list8.index("   ") + 1
    else:
        pass
                
def tie_check():
    global tie
    tie = True
    for item in a.values():
        if item == "   ":
            tie = False
        else:
            tie = tie
    return tie
          
          
def play_again():
    Question = input("Do you want to play again? [Y/N] ")
    if Question == "Y" or Question == "y":
        starting()
        main_game()
    else:
        print("That was quite a game.")
        exit()
          
          
def starting():         
    change_placeholders()  
    draw_board()
    reset_placeholders()

          
def main_game():    
    while True:
        player()
        draw_board()

        if tie_check() == True:
            print("It's a tie")
            play_again()
        else:
            pass
          
        if check() == True:
            play_again()

        computer()
        smart_computer()

        a[f"pl{computer_choice}"] = " O "

        draw_board()
          
        if tie_check() == True:
            print("It's a tie")
            play_again()
        else:
            pass

        if check() == True:
            play_again()
        else:
            continue
          
starting()
main_game()
          