import copy
import math


class game_state():
    def __init__(Self):
        Self.defaultboard = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        Self.piece_value={}
        Self.piece_value['wp']=1
        Self.piece_value['bp']=-1
        Self.piece_value['wN']=3
        Self.piece_value['bN']=-3
        Self.piece_value['wB']=3
        Self.piece_value['bB']=-3
        Self.piece_value['wR']=5
        Self.piece_value['bR']=-5
        Self.piece_value['wQ']=9
        Self.piece_value['bQ']=-9    
        Self.piece_value['wK']=100
        Self.piece_value['bK']=-100
        Self.piece_value['--']=0        
        Self.board=[Self.defaultboard]
        Self.white_to_move=True
        Self.black_king_moved=False
        Self.white_king_moved=False
        Self.white_a_rook_moved=False
        Self.white_h_rook_moved=False
        Self.black_a_rook_moved=False
        Self.black_h_rook_moved=False

def is_white(board,row,col):
    if board[row][col]=="wp" or board[row][col]=="wN" or board[row][col]=="wB" or board[row][col]=="wR" or board[row][col]=="wQ" or board[row][col]=="wK":
        return True
    return False
        
def is_black(board,row,col):
    if board[row][col]=="bp" or board[row][col]=="bN" or board[row][col]=="bB" or board[row][col]=="bR" or board[row][col]=="bQ" or board[row][col]=="bK":
        return True
    return False

def is_check(board,white_to_move):
    if(white_to_move==True):
        color='b'
        k_color='w'
    else:
        color='w'
        k_color='b'
    for row in range(8):
        for col in range(8):
            if board[row][col]==k_color+'K':
                if row-1>=0 and col-1>=0:
                    if board[row-1][col-1]==color+'K':
                        return True
                if row-1>=0 and col<8:
                    if board[row-1][col]==color+'K':
                        return True
                if row-1>=0 and col+1<8:
                    if board[row-1][col+1]==color+'K':
                        return True
                if row<8 and col+1<8:
                    if board[row][col+1]==color+'K':
                        return True
                if row+1<8 and col+1<8:
                    if board[row+1][col+1]==color+'K':
                        return True
                if row+1<8 and col<8:
                    if board[row+1][col]==color+'K':
                        return True                 
                if row+1<8 and col-1>=0:
                    if board[row+1][col-1]==color+'K':
                        return True
                if row>=0 and col-1>=0:
                    if board[row][col-1]==color+'K':
                        return True                                       
                if k_color=='w':
                    if row-1>=0 and col-1>=0:
                        if board[row-1][col-1]==color+'p':
                            return True
                    if row-1>=0 and col+1<8:
                        if board[row-1][col+1]==color+'p':
                            return True                 
                else:
                    if row+1<8 and col-1>=0:
                        if board[row+1][col-1]==color+'p':
                            return True
                    if row+1<8 and col+1<8:
                        if board[row+1][col+1]==color+'p':
                            return True                                                                                        
                if row-2>=0 and col-1>=0:
                    if board[row-2][col-1]==color+'N':
                        return True
                if row-2>=0 and col+1<8:
                    if board[row-2][col+1]==color+'N':
                        return True                        
                if row-1>=0 and col-2>=0:
                    if board[row-1][col-2]==color+'N':
                        return True                        
                if row+1<8 and col-2>=0:
                    if board[row+1][col-2]==color+'N':
                        return True
                if row+2<8 and col-1>=0:
                    if board[row+2][col-1]==color+'N':
                        return True                        
                if row+2<8 and col+1<8:
                    if board[row+2][col+1]==color+'N':
                        return True                        
                if row-1>=0 and col+2<8:
                    if board[row-1][col+2]==color+'N':
                        return True                        
                if row+1<8 and col+2<8:
                    if board[row+1][col+2]==color+'N':
                        return True       
                for i in range(8):
                    check_row=row-i-1
                    check_col=col-i-1
                    if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                        break
                    if board[check_row][check_col]==color+'Q' or board[check_row][check_col]==color+'B':
                        return True
                    if(board[check_row][check_col]!='--'):
                        break
                for i in range(8):
                    check_row=row-i-1
                    check_col=col+i+1
                    if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                        break
                    if board[check_row][check_col]==color+'Q' or board[check_row][check_col]==color+'B':
                        return True
                    if(board[check_row][check_col]!='--'):
                        break
                for i in range(8):
                    check_row=row+i+1
                    check_col=col+i+1
                    if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                        break
                    if board[check_row][check_col]==color+'Q' or board[check_row][check_col]==color+'B':
                        return True
                    if(board[check_row][check_col]!='--'):
                        break
                for i in range(8):
                    check_row=row+i+1
                    check_col=col-i-1
                    if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                        break            
                    if board[check_row][check_col]==color+'Q' or board[check_row][check_col]==color+'B':
                        return True
                    if(board[check_row][check_col]!='--'):
                        break
                for i in range(8):
                    check_row=row
                    check_col=col-i-1
                    if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                        break            
                    if board[check_row][check_col]==color+'Q' or board[check_row][check_col]==color+'R':
                        return True
                    if(board[check_row][check_col]!='--'):
                        break
                for i in range(8):
                    check_row=row-i-1
                    check_col=col
                    if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                        break            
                    if board[check_row][check_col]==color+'Q' or board[check_row][check_col]==color+'R':
                        return True
                    if(board[check_row][check_col]!='--'):
                        break
                for i in range(8):
                    check_row=row
                    check_col=col+i+1
                    if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                        break            
                    if board[check_row][check_col]==color+'Q' or board[check_row][check_col]==color+'R':
                        return True
                    if(board[check_row][check_col]!='--'):
                        break
                for i in range(8):
                    check_row=row+i+1
                    check_col=col
                    if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                        break            
                    if board[check_row][check_col]==color+'Q' or board[check_row][check_col]==color+'R':
                        return True
                    if(board[check_row][check_col]!='--'):
                        break
                return False

def find_legal_moves(board, prev_board, white_to_move, white_king_moved, black_king_moved, white_a_rook_moved, white_h_rook_moved, black_a_rook_moved, black_h_rook_moved):
    all_moves=[]
    all_pieces=[]
    if white_to_move==True:
        color='w'
        r_color='b'
    else:
        color='b'
        r_color='w'
    for row in range(8):
        for col in range(8):
            if white_to_move==True:
                if is_white(board,row,col):
                    this_tuple=(row,col,board[row][col])
                    all_pieces.append(this_tuple)
            else:
                if is_black(board,row,col):
                    this_tuple=(row,col,board[row][col])
                    all_pieces.append(this_tuple)
    test_board=copy.deepcopy(board)
    for piece in all_pieces:
        if piece[2]==color+'p':
            if piece[0]==1 and board[piece[0]][piece[1]]=='bp':
                if(board[piece[0]+2][piece[1]]=="--" and board[piece[0]+1][piece[1]]=="--"):
                    this_tuple=(piece[0],piece[1],piece[0]+2,piece[1])
                    all_moves.append(this_tuple)
            if piece[0]==6 and board[piece[0]][piece[1]]=='wp':
                if(board[piece[0]-2][piece[1]]=="--" and board[piece[0]-1][piece[1]]=="--"):
                    this_tuple=(piece[0],piece[1],piece[0]-2,piece[1])
                    all_moves.append(this_tuple)
            if white_to_move==True:
                if piece[0]==3:
                    if piece[0]-2>=0 and piece[1]+1<8:
                        if board[piece[0]][piece[1]+1]=='bp' and prev_board[piece[0]-2][piece[1]+1]=='--' and board[piece[0]-2][piece[1]+1]=='--' and prev_board[piece[0]-2][piece[1]+1]=='bp':
                            this_tuple=(piece[0],piece[1],piece[0]-1,piece[1]+1,'En passant')
                            all_moves.append(this_tuple)
                    if piece[0]-2>=0 and piece[1]-1>=0:
                        if board[piece[0]][piece[1]-1]=='bp' and prev_board[piece[0]-2][piece[1]-1]=='--' and board[piece[0]-2][piece[1]-1]=='--' and prev_board[piece[0]-2][piece[1]-1]=='bp':
                            this_tuple=(piece[0],piece[1],piece[0]-1,piece[1]-1,'En passant')
                            all_moves.append(this_tuple)
                if board[piece[0]-1][piece[1]]=='--':
                    this_tuple=(board,piece[0],piece[1],piece[0]-1,piece[1])
                    all_moves.append(this_tuple)
                if piece[0]-1>=0 and piece[1]+1<8:
                    if is_black(board,piece[0]-1,piece[1]+1):
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]-1>=0 and piece[1]-1>=0:
                    if is_black(board,piece[0]-1,piece[1]-1):
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]-1)
                        all_moves.append(this_tuple)
            else:
                if piece[0]==4:
                    if piece[0]+2<8 and piece[1]+1<8:
                        if board[piece[0]][piece[1]+1]=='wp' and prev_board[piece[0]+2][piece[1]+1]=='--' and board[piece[0]+2][piece[1]+1]=='--' and prev_board[piece[0]+2][piece[1]+1]=='wp':
                            this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]+1)
                            all_moves.append(this_tuple)
                    if piece[0]+2<8 and piece[1]-1>=0:                            
                        if board[piece[0]][piece[1]-1]=='wp' and prev_board[piece[0]+2][piece[1]-1]=='--' and board[piece[0]+2][piece[1]-1]=='--' and prev_board[piece[0]+2][piece[1]-1]=='wp':
                            this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]-1)
                            all_moves.append(this_tuple)
                if piece[0]+1<8:
                    if board[piece[0]+1][piece[1]]=='--':
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1])
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]+1<8:
                    if is_white(board,piece[0]+1,piece[1]+1):
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]-1>=0:
                    if is_white(board,piece[0]+1,piece[1]-1):
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]-1)
                        all_moves.append(this_tuple)
        if (piece[2]=='wN' and white_to_move==True) or (piece[2]=='bN' and white_to_move==False):
            if white_to_move==True:
                if piece[0]-2>=0 and piece[1]-1>=0:
                    if is_white(board,piece[0]-2,piece[1]-1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-2,piece[1]-1)
                        all_moves.append(this_tuple)
                if piece[0]-2>=0 and piece[1]+1<8:
                    if is_white(board,piece[0]-2,piece[1]+1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-2,piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]-1>=0 and piece[1]-2>=0:
                    if is_white(board,piece[0]-1,piece[1]-2)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-1,piece[1]-2)
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]-2>=0:
                    if is_white(board,piece[0]+1,piece[1]-2)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]-2)
                        all_moves.append(this_tuple)
                if piece[0]+2<8 and piece[1]-1>=0:
                    if is_white(board,piece[0]+2,piece[1]-1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+2,piece[1]-1)
                        all_moves.append(this_tuple)
                if piece[0]+2<8 and piece[1]+1<8:
                    if is_white(board,piece[0]+2,piece[1]+1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+2,piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]-1>=0 and piece[1]+2<8:
                    if is_white(board,piece[0]-1,piece[1]+2)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-1,piece[1]+2)
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]+2<8:
                    if is_white(board,piece[0]+1,piece[1]+2)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]+2)
                        all_moves.append(this_tuple)
            else:
                if piece[0]-2>=0 and piece[1]-1>=0:
                    if is_black(board,piece[0]-2,piece[1]-1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-2,piece[1]-1)
                        all_moves.append(this_tuple)
                if piece[0]-2>=0 and piece[1]+1<8:
                    if is_black(board,piece[0]-2,piece[1]+1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-2,piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]-1>=0 and piece[1]-2>=0:
                    if is_black(board,piece[0]-1,piece[1]-2)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-1,piece[1]-2)
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]-2>=0:
                    if is_black(board,piece[0]+1,piece[1]-2)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]-2)
                        all_moves.append(this_tuple)
                if piece[0]+2<8 and piece[1]-1>=0:
                    if is_black(board,piece[0]+2,piece[1]-1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+2,piece[1]-1)
                        all_moves.append(this_tuple)
                if piece[0]+2<8 and piece[1]+1<8:
                    if is_black(board,piece[0]+2,piece[1]+1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+2,piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]-1>=0 and piece[1]+2<8:
                    if is_black(board,piece[0]-1,piece[1]+2)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-1,piece[1]+2)
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]+2<8:
                    if is_black(board,piece[0]+1,piece[1]+2)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]+2)
                        all_moves.append(this_tuple)
        if (piece[2]=='wK' and white_to_move==True) or (piece[2]=='bK' and white_to_move==False):
            if white_to_move==True:
                if white_king_moved==False:
                    if white_h_rook_moved==False:
                        not_viable=False
                        for i in range(1,3):
                            if piece[0]<0 or piece[0]>7 or piece[1]+i<0 or piece[1]+i>7:
                                break                            
                            if board[piece[0]][piece[1]+i]!='--':
                                not_viable=True
                                break
                            test_board[piece[0]][piece[1]+i]='wK'
                            test_board[piece[0]][piece[1]]='--'
                            if is_check(test_board,white_to_move)==True:
                                not_viable=True
                                break
                            else:
                                test_board=copy.deepcopy(board)
                        if not_viable==False:
                            this_tuple=(piece[0],piece[1],piece[0],piece[1]+2,'short castle')
                            all_moves.append(this_tuple)
                                                
                    if white_a_rook_moved==False:
                        not_viable=False
                        for i in range(1,3):
                            if piece[0]<0 or piece[0]>7 or piece[1]-i<0 or piece[1]-i>7:
                                break                            
                            if board[piece[0]][piece[1]-i]!='--':
                                not_viable=True
                                break
                            test_board[piece[0]][piece[1]-i]='wK'
                            test_board[piece[0]][piece[1]]='--'
                            if is_check(test_board,white_to_move)==True:
                                not_viable=True
                                break
                            else:
                                test_board=copy.deepcopy(board)
                        if not_viable==False:
                            this_tuple=(piece[0],piece[1],piece[0],piece[1]-2,'long castle')
                            all_moves.append(this_tuple)
            else:
                if black_king_moved==False:
                    if black_h_rook_moved==False:
                        not_viable=False
                        for i in range(1,3):
                            if piece[0]<0 or piece[0]>7 or piece[1]+i<0 or piece[1]+i>7:
                                break
                            if board[piece[0]][piece[1]+i]!='--':
                                not_viable=True
                                break
                            test_board[piece[0]][piece[1]+i]='bK'
                            test_board[piece[0]][piece[1]]='--'
                            if is_check(test_board,white_to_move)==True:
                                not_viable=True
                                break
                            else:
                                test_board=copy.deepcopy(board)
                        if not_viable==False:
                            this_tuple=(piece[0],piece[1],piece[0],piece[1]+2,'short castle')
                            all_moves.append(this_tuple)
                    if black_a_rook_moved==False:
                        not_viable=False
                        for i in range(1,3):
                            if piece[0]<0 or piece[0]>7 or piece[1]+i<0 or piece[1]+i>7:
                                break                            
                            if board[piece[0]][piece[1]+i]!='--':
                                not_viable=True
                                break
                            test_board[piece[0]][piece[1]+i]='bK'
                            test_board[piece[0]][piece[1]]='--'
                            if is_check(test_board,white_to_move)==True:
                                not_viable=True
                                break
                            else:
                                test_board=copy.deepcopy(board)
                        if not_viable==False:
                            this_tuple=(piece[0],piece[1],piece[0],piece[1]+2,'long castle')
                            all_moves.append(this_tuple)               
            if white_to_move==True:
                if piece[0]-1>=0 and piece[1]-1>=0:
                    if is_white(board,piece[0]-1,piece[1]-1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-1,piece[1]-1)
                        all_moves.append(this_tuple)
                if piece[0]-1>=0 and piece[1]<8:
                    if is_white(board,piece[0]-1,piece[1])==False:
                        this_tuple=(piece[0],piece[1],piece[0]-1,piece[1])
                        all_moves.append(this_tuple)
                if piece[0]-1>=0 and piece[1]+1<8:
                    if is_white(board,piece[0]-1,piece[1]+1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-1,piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]<8 and piece[1]+1<8:
                    if is_white(board,piece[0],piece[1]+1)==False:
                        this_tuple=(piece[0],piece[1],piece[0],piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]+1<8:
                    if is_white(board,piece[0]+1,piece[1]+1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]<8:
                    if is_white(board,piece[0]+1,piece[1])==False:
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1])
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]-1>=0:
                    if is_white(board,piece[0]+1,piece[1]-1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]-1)
                        all_moves.append(this_tuple)
                if piece[0]<8 and piece[1]-1>=0:
                    if is_white(board,piece[0],piece[1]-1)==False:
                        this_tuple=(piece[0],piece[1],piece[0],piece[1]-1)
                        all_moves.append(this_tuple)
            else:
                if piece[0]-1>=0 and piece[1]-1>=0:
                    if is_black(board,piece[0]-1,piece[1]-1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-1,piece[1]-1)
                        all_moves.append(this_tuple)
                if piece[0]-1>=0 and piece[1]<8:
                    if is_black(board,piece[0]-1,piece[1])==False:
                        this_tuple=(piece[0],piece[1],piece[0]-1,piece[1])
                        all_moves.append(this_tuple)
                if piece[0]-1>=0 and piece[1]+1<8:
                    if is_black(board,piece[0]-1,piece[1]+1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]-1,piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]<8 and piece[1]+1<8:
                    if is_black(board,piece[0],piece[1]+1)==False:
                        this_tuple=(piece[0],piece[1],piece[0],piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]+1<8:
                    if is_black(board,piece[0]+1,piece[1]+1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]+1)
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]<8:
                    if is_black(board,piece[0]+1,piece[1])==False:
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1])
                        all_moves.append(this_tuple)
                if piece[0]+1<8 and piece[1]-1>=0:
                    if is_black(board,piece[0]+1,piece[1]-1)==False:
                        this_tuple=(piece[0],piece[1],piece[0]+1,piece[1]-1)
                        all_moves.append(this_tuple)
                if piece[0]<8 and piece[1]-1>=0:
                    if is_black(board,piece[0],piece[1]-1)==False:
                        this_tuple=(piece[0],piece[1],piece[0],piece[1]-1)
                        all_moves.append(this_tuple) 
        if ((piece[2]=='wB' or piece[2]=='wQ') and white_to_move==True) or ((piece[2]=='bB' or piece[2]=='bQ') and white_to_move==False):
            for i in range(8):
                check_row=piece[0]-i-1
                check_col=piece[1]-i-1
                if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                    break
                if white_to_move==True:
                    if is_white(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_black(board,check_row,check_col)==True:
                        break
                else:
                    if is_black(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_white(board,check_row,check_col)==True:
                        break
            for i in range(8):
                check_row=piece[0]-i-1
                check_col=piece[1]+i+1
                if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                    break
                if white_to_move==True:
                    if is_white(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_black(board,check_row,check_col)==True:
                        break
                else:
                    if is_black(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_white(board,check_row,check_col)==True:
                        break
            for i in range(8):
                check_row=piece[0]+i+1
                check_col=piece[1]+i+1
                if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                    break
                if white_to_move==True:
                    if is_white(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_black(board,check_row,check_col)==True:
                        break
                else:
                    if is_black(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_white(board,check_row,check_col)==True:
                        break
            for i in range(8):
                check_row=piece[0]+i+1
                check_col=piece[1]-i-1
                if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                    break
                if white_to_move==True:
                    if is_white(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_black(board,check_row,check_col)==True:
                        break
                else:
                    if is_black(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_white(board,check_row,check_col)==True:
                        break
        if ((piece[2]=='wR' or piece[2]=='wQ') and white_to_move==True) or ((piece[2]=='bR' or piece[2]=='bQ') and white_to_move==False):
            for i in range(8):
                check_row=piece[0]
                check_col=piece[1]-i-1
                if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                    break
                if white_to_move==True:
                    if is_white(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_black(board,check_row,check_col)==True:
                        break
                else:
                    if is_black(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_white(board,check_row,check_col)==True:
                        break
            for i in range(8):
                check_row=piece[0]-i-1
                check_col=piece[1]
                if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                    break
                if white_to_move==True:
                    if is_white(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_black(board,check_row,check_col)==True:
                        break
                else:
                    if is_black(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_white(board,check_row,check_col)==True:
                        break
            for i in range(8):
                check_row=piece[0]
                check_col=piece[1]+i+1
                if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                    break
                if white_to_move==True:
                    if is_white(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_black(board,check_row,check_col)==True:
                        break
                else:
                    if is_black(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_white(board,check_row,check_col)==True:
                        break
            for i in range(8):
                check_row=piece[0]+i+1
                check_col=piece[1]
                if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                    break
                if white_to_move==True:
                    if is_white(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_black(board,check_row,check_col)==True:
                        break
                else:
                    if is_black(board,check_row,check_col)==True:
                        break
                    this_tuple=(piece[0],piece[1],check_row,check_col)
                    all_moves.append(this_tuple)
                    if is_white(board,check_row,check_col)==True:
                        break
    all_legal_moves=[]
    for move in all_moves:      
        if len(move)==5:
            continue
        test_board[move[2]][move[3]]=test_board[move[0]][move[1]]
        test_board[move[0]][move[1]]='--'
        if is_check(test_board,white_to_move)==False:
            all_legal_moves.append(copy.deepcopy(move))
        test_board=copy.deepcopy(board)
    return all_legal_moves
    
def move(board, prev_board, white_to_move, white_king_moved, black_king_moved, white_a_rook_moved, white_h_rook_moved, black_a_rook_moved, black_h_rook_moved, curr_row, curr_col, move_row, move_col):
    print(curr_row,curr_col,move_row,move_col)
    print(white_to_move)
    if(white_to_move):
        if(is_white(board,move_row,move_col)):
            return False
    else:
        if(is_black(board,move_row,move_col)):
            return False
    if ((board[curr_row][curr_col]=='wB' or board[curr_row][curr_col]=='wQ') and white_to_move==True) or ((board[curr_row][curr_col]=='bB' or board[curr_row][curr_col]=='bQ') and white_to_move==False):
        for i in range(8):
            check_row=curr_row-i-1
            check_col=curr_col-i-1
            if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                break
            if check_row==move_row and check_col==move_col:
                return True
            if(board[check_row][check_col]!='--'):
                break
        for i in range(8):
            check_row=curr_row-i-1
            check_col=curr_col+i+1
            if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                break
            if check_row==move_row and check_col==move_col:
                return True
            if(board[check_row][check_col]!='--'):
                break
        for i in range(8):
            check_row=curr_row+i+1
            check_col=curr_col+i+1
            if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                break            
            if check_row==move_row and check_col==move_col:
                return True
            if(board[check_row][check_col]!='--'):
                break
        for i in range(8):
            check_row=curr_row+i+1
            check_col=curr_col-i-1
            if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                break            
            if check_row==move_row and check_col==move_col:
                return True
            if(board[check_row][check_col]!='--'):
                break
    if ((board[curr_row][curr_col]=='wR' or board[curr_row][curr_col]=='wQ') and white_to_move==True) or ((board[curr_row][curr_col]=='bR' or board[curr_row][curr_col]=='bQ') and white_to_move==False):
        for i in range(8):
            check_row=curr_row
            check_col=curr_col-i-1
            if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                break            
            if check_row==move_row and check_col==move_col:
                return True
            if(board[check_row][check_col]!='--'):
                break
        for i in range(8):
            check_row=curr_row-i-1
            check_col=curr_col
            if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                break            
            if check_row==move_row and check_col==move_col:
                return True
            if(board[check_row][check_col]!='--'):
                break
        for i in range(8):
            check_row=curr_row
            check_col=curr_col+i+1
            if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                break            
            if check_row==move_row and check_col==move_col:
                return True
            if(board[check_row][check_col]!='--'):
                break
        for i in range(8):
            check_row=curr_row+i+1
            check_col=curr_col
            if check_row<0 or check_row>7 or check_col<0 or check_col>7:
                break            
            if check_row==move_row and check_col==move_col:
                return True
            if(board[check_row][check_col]!='--'):
                break
    if (board[curr_row][curr_col]=='wK' and white_to_move==True) or (board[curr_row][curr_col]=='bK' and white_to_move==False):
        if white_to_move==True:
            if curr_row==move_row and white_king_moved==False:
                if curr_col-move_col==-2 and white_h_rook_moved==False:
                    for i in range(1,3):
                        if board[curr_row][curr_col+i]!='--':
                            return False
                    return 'short castles'
                if curr_col-move_col==2 and white_a_rook_moved==False:
                    for i in range(1,3):
                        if board[curr_row][curr_col-i]!='--':
                            return False                    
                    return 'long castles'
        else:
            if curr_row==move_row and black_king_moved==False:
                if curr_col-move_col==-2 and black_h_rook_moved==False:
                    for i in range(1,3):
                        if board[curr_row][curr_col+i]!='--':
                            return False                    
                    return 'short castles'
                if curr_col-move_col==2 and black_a_rook_moved==False:
                    for i in range(1,3):
                        if board[curr_row][curr_col-i]!='--':
                            return False                    
                    return 'long castles'                
        if(abs(curr_row-move_row)<=1 and abs(curr_col-move_col)<=1):
            if(abs(curr_row-move_row)!=0 or abs(curr_col-move_col)!=0):
                return True
    if (board[curr_row][curr_col]=='wp' and white_to_move==True) or (board[curr_row][curr_col]=='bp' and white_to_move==False):
        if(curr_row==1 and board[curr_row][curr_col]=='bp'):
            if(move_row-curr_row==2 and board[curr_row+2][curr_col]=="--" and board[curr_row+1][curr_col]=="--"):
                return True
        if(curr_row==6 and board[curr_row][curr_col]=='wp'):
            if(curr_row-move_row==2 and board[curr_row-2][curr_col]=="--" and board[curr_row-1][curr_col]=="--"):
                return True                
        if(curr_row-move_row==1 and white_to_move==True) or (curr_row-move_row==-1 and white_to_move==False):
            if white_to_move==True:
                if curr_row==3 and abs(move_col-curr_col)==1:
                    if board[curr_row][move_col]=='bp' and prev_board[curr_row][move_col]=='--' and board[curr_row-2][move_col]=='--' and prev_board[curr_row-2][move_col]=='bp':
                        return 'En passant'
            else:
                if curr_row==4 and abs(move_col-curr_col)==1:
                    if board[curr_row][move_col]=='wp' and prev_board[curr_row][move_col]=='--' and board[curr_row+2][move_col]=='--' and prev_board[curr_row+2][move_col]=='wp':
                        return 'En passant'                                          
            if(move_col==curr_col and board[move_row][move_col]=='--'):
                return True
            if(abs(move_col-curr_col)==1 and (is_white(board,move_row,move_col) or is_black(board,move_row,move_col))):
                return True
    if (board[curr_row][curr_col]=='wN' and white_to_move==True) or (board[curr_row][curr_col]=='bN' and white_to_move==False):
        if(abs(move_row-curr_row)==1 and abs(move_col-curr_col)==2) or (abs(move_row-curr_row)==2 and abs(move_col-curr_col)==1):
            return True          
    return False

def is_game_over(gs):
    moves=find_legal_moves(gs.board[len(gs.board)-1],gs.board[len(gs.board)-2],gs.white_to_move,gs.white_king_moved,gs.black_king_moved,gs.white_a_rook_moved,gs.white_h_rook_moved,gs.black_a_rook_moved,gs.black_h_rook_moved)
    if is_check(gs.board[len(gs.board)-1],gs.white_to_move)==True and len(moves)==0:
        if gs.white_to_move==True:
            print('Checkmate! black wins!')
            return True
        else:
            print('Checkmate! white wins!')
            return True
    return False

def evaluate_pos(gs):
    pos_value=0
    legal_move=find_legal_moves(gs.board[len(gs.board)-1],gs.board[len(gs.board)-2],gs.white_to_move,gs.white_king_moved,gs.black_king_moved,gs.white_a_rook_moved,gs.white_h_rook_moved,gs.black_a_rook_moved,gs.black_h_rook_moved)
    if is_check(gs.board[len(gs.board)-1],gs.white_to_move)==True and len(legal_move)==0:
        return 1000
    for row in range(8):    
        for col in range(8):
            pos_value=pos_value+gs.piece_value[gs.board[len(gs.board)-1][row][col]]
    return pos_value                                               