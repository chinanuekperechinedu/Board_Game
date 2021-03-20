from termcolor import colored

def create_board(rows, columns, field): 
    columns = (2 * columns) - 1
    rows = (2 * rows) - 1
    for row in range(rows):
        if row % 2 == 0:
            for col in range(columns):                
                if col % 2 == 0:
                    column_space = int(col / 2)
                    row_space = int(row / 2)
                    if col == (columns - 1):
                        print(field[row_space][column_space])
                    else:
                        print(field[row_space][column_space], end=' ')
                else:
                    print('|', end='')
        else:
            print('--' * rows)
            
            
def create_field():
    
    while True:
        try:
            rows = int(input('Enter number of rows: '))
            break
        except:
            continue
        
    while True:
        try:
            columns = int(input('Enter number of columns: '))
            break
        except:
            continue

    fields = []
    
    for row in range(rows):
        row_field = []
        for column in range(columns):
            row_field.append(" ")
        fields.append(row_field)
    
    create_board(rows, columns, fields)
        
    return fields


def check_winner(row_length, col_length, current_field, player):
    count = 0
    play = ' '
    
    if player == 1:
        play = colored(u'\u2B24', 'white')
        
    if player == 2:
        play = colored(u'\u2B24', 'magenta')
    
#    HORIZONTAL WIN
    for rw in range(row_length):
        for col in range(col_length):
            if current_field[rw][col] == play:
                count += 1
            else:
                count = 0
                
            if count >= 4:
                return player
            
#       VERTICAL WIN
    for col in range(col_length):
        for rw in range(row_length):
            if current_field[rw][col] == play:
                count += 1
            else:
                count = 0
                
            if count >= 4:
                return player
            

    for rw in range(row_length - 3):
        for col in range(3, col_length):
            if current_field[rw][col] == play and current_field[rw+1][col-1] == play and current_field[rw+2][col-2] == play and current_field[rw+3][col-3] == play:
                return player
            

    for rw in range(row_length - 3):
        for col in range(col_length - 3):
            if current_field[rw][col] == play and current_field[rw+1][col+1] == play and current_field[rw+2][col+2] == play and current_field[rw+3][col+3] == play:
                return player
        
            
def play_board_game():
    current_field = create_field()
    
    winner = 0
    
    player = 1
    while True:
        print("\nPlayer's turn: ", player)
        
        col_length = len(current_field[0])
        row_length = len(current_field)
            
        move_column = -1
        
        try:                  
            
            while move_column not in range(0, col_length):
                try:
                    move_column = int(input('Enter a valid column between 1 to {}: '.format(col_length)))
                    move_column = move_column - 1
                    break
                except:
                    continue     
            
            row_length_index = row_length - 1
            
            if player == 1:
                for move_row in range(row_length_index, -1, -1 ):
                    if current_field[move_row][move_column] == ' ':
                        current_field[move_row][move_column] = colored(u'\u2B24', 'white')
                        break
                winner = check_winner(row_length, col_length, current_field, player)
                player = 2
                
            else:
                for move_row in range(row_length_index, -1, -1):
                    if current_field[move_row][move_column] == " ":
                        current_field[move_row][move_column] = colored(u'\u2B24', 'magenta')
                        break
                winner = check_winner(row_length, col_length, current_field, player)
                player = 1            
                            
            create_board(row_length, col_length, current_field)
            
            if winner == 1 or winner == 2:
                print('\nPlayer {} is the winner'.format(winner))
                break
            
            
        except Exception as e:
            print(e)
            continue
            
            
if __name__ == '__main__':
    play_board_game()
    
       
    
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        