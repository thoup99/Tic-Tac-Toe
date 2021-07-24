import random

game_slots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
game_end = False

#makes sure the entered value is not currently taken by an X or O
def check_input(inp):
    if str(inp) in game_slots:
        return(True)
    else:
        return(False)

class Game():

    def __init__(self):
        pass

    ##Gets the players input
    def p_inp(self):
        inp = int(input("Enter a number from the board: "))
        is_valid = check_input(inp)
        while is_valid == False:
            inp = int(input("Enter a number from the board: "))
            is_valid = check_input(inp)
        game_slots.pop(inp - 1)
        game_slots.insert(inp - 1, "X")
            

    ##The computer takes a turn
    def comp_turn(self):
        comp_inp = random.randint(1, 9)
        is_valid = check_input(comp_inp)
        while is_valid == False:
            comp_inp = random.randint(1, 9)
            is_valid = check_input(comp_inp)
        game_slots.pop(comp_inp - 1)
        game_slots.insert(comp_inp - 1, "O")
        pass


    ##Draws the game board
    def draw_board(self):
        loop_it = 0
        lp2 = 0
        while(loop_it < 5):
            line_to_draw = ""
            ##if odd
            if (not loop_it % 2 == 0):
                print("---+---+---")
            else:
                list_spot = loop_it + lp2
                num_set = game_slots[list_spot:list_spot+3]

                for num in num_set:
                    line_to_draw = line_to_draw + " "+num+" |"
                lp2 += 1
                print(line_to_draw)
            loop_it += 1
    
    def check_win(self, let):
        letter = []
        letter.append(let)
        sl1 = game_slots[:1]
        sl2 = game_slots[1:2]
        sl3 = game_slots[2:3]
        sl4 = game_slots[3:4]
        sl5 = game_slots[4:5]
        sl6 = game_slots[5:6]
        sl7 = game_slots[6:7]
        sl8 = game_slots[7:8]
        sl9 = game_slots[8:]

        ##Across
        if ((sl1 == sl2 and sl2 == sl3 and sl3 == letter) or (sl4 == sl5 and sl5 == sl6 and sl6 == letter) or (sl7 == sl8 and sl8 == sl9 and sl9 == letter)):
            print(let+" Won!")
            return(True)
        ##Up/Down
        elif((sl1 == sl4 and sl4 == sl7 and sl7 == letter) or (sl2 == sl5 and sl5 == sl5 and sl7 == letter) or (sl3 == sl6 and sl6 == sl9 and sl9 == letter)):
            print(let+" Won!")
            return(True)
        ##Diagnal
        elif((sl1 == sl5 and sl5 == sl9 and sl9 == letter) or (sl3 == sl5 and sl5 == sl7 and sl7 == letter)):
            print(let+" Won!")
            return(True)
        ##No winner
        else:
            return(False)
                 
game = Game()

game.draw_board()
while game_end == False:
    game.p_inp()
    game.draw_board()
    c = game.check_win("X")
    if (c == True):
        game_end == True
        break
    print("Computers turn")
    game.comp_turn()
    game.draw_board()
    c = game.check_win("O")
    if (c == True):
        game_end == True
        break