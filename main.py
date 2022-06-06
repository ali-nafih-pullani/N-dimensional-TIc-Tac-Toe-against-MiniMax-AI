# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 23:26:02 2022

@author: ali_nafih_pullani
"""

import random
#Playing board as a class
#Creating a class for the board is not required, all the functions can be defined independantly as well
class Board:
    def __init__(self,n):
        '''input: None, 
        prints the welcome message, instructions and rules,
        attributes of the class: board_as_list -> shows the board in a list format'''
        #n is added as an attribute of the class
        self.n = n
        #setting up the board for printing instructions
        board = ['position_holder']
        board.extend(list(i for i in range(1,(self.n**2)+1)))
        self.board_as_list = board
        
        #printing of instructions
        print("Welcome to the Tic-Tac-Toe")
        print('\n')
        print("You are playing against MiniMax AI player, which is UNBEATABLE!")
        print("However, the AI makes first (n-1) moves randomly,thus giving you an edge. If you make good decisions, you can get a draw! Good Luck :)")
        print('\n')
        print("Use your numpad to play ")
        self.print_board(True)
        print('\n')
        print("Computer's moves are marked by 'X' and your's by 'O'")
        print('Free squares are marked in the board using (). For eg. (7) indicates that square 7 is free.')
        print("Game starts now!!!")
        
        #clearing and updating the board for the game
        board = ['position_holder']
        board.extend(list(" " for i in range(1,(self.n**2)+1)))
        self.board_as_list = board
        
        #generation of the winning combinations
        self.winning_combinations = self.winning_combination_generator()
        
    def print_board(self,isInstruction=False):
        '''input: None, 
        Ouput: None,
        prints the current layout of the board'''
        
        if isInstruction:
            for i in range(1,((self.n**2)+1),self.n):
                    row_strings = []
                    if (i!=1):
                        print("-"*(9*self.n))
                    for j in range(self.n):
                        if self.board_as_list[i+j] ==' ':
                            row_strings.append('('+str(i+j)+')')
                        else:
                            row_strings.append(self.board_as_list[i+j])
                    print('|'.join((f"{k: ^8}" for k in row_strings)))
        
        else:
            for i in range(1,((self.n**2)+1),self.n):
                    row_strings = []
                    if (i!=1):
                        print("-"*(9*self.n))
                    for j in range(self.n):
                        if self.board_as_list[i+j] ==' ':
                            row_strings.append(self.board_as_list[i+j])
                        else:
                            row_strings.append(self.board_as_list[i+j])
                    print('|'.join((f"{k: ^8}" for k in row_strings)))

    def is_free(self,num):
        '''input: int(a board position),
        output: Boolean'''
        return self.board_as_list[num]==' '
    
    def winning_combination_generator(self):
        '''the function generates the winnining combinations for the given n*n board
        input: None
        output: winning_combinations (list(tuples))'''
        horizontal_list,vertical_list, first_diagonal_as_list, second_diagonal_as_list,winning_combinations = [],[],[],[],[]
        for i in range(1,(self.n*self.n)+1,self.n): 
            list_seq = []
            for j in range(self.n):
                list_seq.append(i+j)
            horizontal_list.append(tuple(list_seq))
        winning_combinations.extend(horizontal_list)
        
        for i in range(1,self.n+1): 
            list_seq = []
            for j in range(self.n):
                list_seq.append(i+j*self.n)
            vertical_list.append(tuple(list_seq))
        winning_combinations.extend(vertical_list)
        
        for i in range(self.n):
            first_diagonal_as_list.append(1+(self.n+1)*i)
            second_diagonal_as_list.append(self.n+(self.n-1)*i)
        diagonal_list = list(tuple(i) for i in [first_diagonal_as_list, second_diagonal_as_list])
        winning_combinations.extend(diagonal_list)
        return winning_combinations
            
    
    def winning_combination_search(self,marker):
            for combination in self.winning_combinations:
                a = True
                #print(combination)
                for i in combination:
                    if self.board_as_list[i] != marker:
                        a = False
                if a:
                    #print(f'winning combination found--> {combination}')
                    return True
            return False
    
    def end_check(self):
        '''input: None,
        output: Boolean (True('X','O','Draw') or False)'''
        if self.winning_combination_search('X'):
            return 'X'
        elif self.winning_combination_search('O'):
            return 'O'
        elif ' ' not in self.board_as_list:
            return 'draw'
        return False
    
    def add_to_board(self,pos_num,player_mark):
        '''input: str(board position), 
        output: None,
        add player's marker to the input position and print the resulting state of the board'''
        while not self.board_as_list[pos_num]==" ":
            try:
                pos_num = int(input("position is taken, try again! :"))
            except:
                print("Invalid input! Enter a number between 1 and 9 !")
                continue
                
        self.board_as_list[int(pos_num)] = player_mark
        print("\n")
        self.print_board()
        print("\n")
    
    def add(self,pos_num,player_mark):
        '''input: str(board position), 
        output: None,
        add player's marker to the input position without printing the resulting state of the board'''
        self.board_as_list[int(pos_num)] = player_mark
        
    def reset_position(self,position):
        '''input: int(board position), 
        output: None,
        resets the marker in the position'''
        self.board_as_list[position] = ' '
        
        
#Function for player's input
def player_move(board_object):
    while True:
        try:
            pos_num = int(input("Player, Enter your move: "))
            break
        except:
            print('Invalid input! Enter a number between 1 and 9')
        
    board_object.add_to_board(pos_num,'O')

#Function for AI's move
#Initiates the MiniMax recursion for decision making
def comp_move(board_object,round_number):
    print('Computer playing ........')
    print('\n')
    
    if round_number < n:
      while True:
        current_move = random.randint(1,n*n)
        if board_object.is_free(current_move):
          board_object.add(current_move,'X')
          board_object.print_board()
          break

    else:
      current_max = -10000
      current_move = 0
      for i in range(1,(n**2)+1):
          if board_object.is_free(i):
              board_object.add(i,'X')
              cost = minimax(board_object,False)
              board_object.reset_position(i)
              if (cost>current_max):
                  current_max = cost
                  current_move = i
              
      board_object.add(current_move,'X')
      board_object.print_board()



#Minimax AI as a recursive function
def minimax(board,isMaximizing):
    isOver = board.end_check()
    if isOver:
        if isOver=='X':
            a = 1
        elif isOver=='O':
            a = -1
        else:
            a = 0
        if ' ' in board.board_as_list:
            b = board.board_as_list.count(' ') + 1
        else:
            b = 1
        return a*b
    if isMaximizing:
        current_max = -10000
        for i in range(1,(n**2)+1):
            if board.is_free(i):
                board.add(i,'X')
                cost = minimax(board,False)
                board.reset_position(i)
                current_max = max(current_max,cost)
        return current_max
    
    else:
        current_min = 10000
        for i in range(1,(n**2)+1):
            if board.is_free(i):
                board.add(i,'O')
                cost = minimax(board,True)
                board.reset_position(i)
                #pdb.set_trace()
                current_min = min(current_min,cost)
        return current_min




#Game Logic
game_on = True

while game_on:
    round_count = 0
    print('\n')
    print('='*20)
    while True:
        try:
            n = int(input("Enter the dimension of the board: "))
        except:
            print('Please enter an integer! Try again!')
            continue
        break
    playing_board = Board(n)
    while True:
        round_count += 1
        end = playing_board.end_check()
        if end:
            if end=='X':
                print('\n')
                print("Computer wins!")
            elif end=='O':
                print('\n')
                print("Player wins!")
            else:
                print('\n')
                print("Game tied")
            print("\nFinal board: \n")
            playing_board.print_board()
            break
        
        print("\n")
        comp_move(playing_board,round_count)
        print("\n")
        playing_board.print_board(True)
        end = playing_board.end_check()
        if end:
            if end=='X':
                print('\n')
                print("Computer wins!")
            elif end=='O':
                print('\n')
                print("Player wins!")
            else:
                print('\n')
                print("Game tied")
            print("\nFinal board: \n")
            playing_board.print_board()
            break
        print("\n")
        player_move(playing_board)
    print("\n")
    game_on = (input("play again? (Enter 'y' for yes!)").lower() == 'y')
