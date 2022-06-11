import pygame as pg
from PIL import Image
import sys
import random
import chess_engine
import copy
import random
import math

width=800 
height=800
row=col=8
sq_size=width//row
font_size=sq_size
Images={}
max_depth=2
counting=0


def loadimages():
    pieces=["wp","wN","wB","wR","wQ","wK","bp","bN","bB","bR","bQ","bK"]
    for piece in pieces:
        Images[piece]=pg.transform.scale(pg.image.load("images/"+piece+".png"),(sq_size,sq_size))

def draw_board(screen):
    colors=[pg.Color((235, 235, 208)),pg.Color(119, 148, 85)]
    for i in range(row):
        for j in range(col):
            color=colors[(i+j)%2]
            pg.draw.rect(screen,color,pg.Rect(j*sq_size,i*sq_size,sq_size,sq_size))
        
def draw_pieces(screen,gs):
    colors=["black","white"]    
    for i in range(row):
        for j in range(col):       
            text_rect= pg.Rect(j*sq_size,i*sq_size,sq_size,sq_size)
            curr_piece=gs.board[len(gs.board)-1][i][j]
            if curr_piece!="--":
                screen.blit(Images[curr_piece],text_rect)

def run_ai(gs,depth,white_to_move):
    global counting
    counting=counting+1
    print(counting)
    all_moves=copy.deepcopy(chess_engine.find_legal_moves(gs.board[len(gs.board)-1],gs.board[len(gs.board)-2],white_to_move,gs.white_king_moved,gs.black_king_moved,gs.white_a_rook_moved,gs.white_h_rook_moved,gs.black_a_rook_moved,gs.black_h_rook_moved))
    if len(all_moves)==0:
        return False
    gs.board.append(copy.deepcopy(gs.board[len(gs.board)-1]))
    if white_to_move==False:
        best_move=(0,0,0,0,1000)
    else:
        best_move=(0,0,0,0,-1000)
    equal_eval=[]

    for move in all_moves:
        gs.board[len(gs.board)-1][move[2]][move[3]]=gs.board[len(gs.board)-1][move[0]][move[1]]
        gs.board[len(gs.board)-1][move[0]][move[1]]='--'
        if len(move)==5:
            if move[4]=='En passant':
                gs.board[len(gs.board)-1][move[0]][move[3]]='--'
            if move[4]=='short castles':
                gs.board[len(gs.board)-1][move[2]][move[3]-1]=gs.board[len(gs.board)-1][move[2]][7]
                gs.board[len(gs.board)-1][move[2]][7]='--'
            if move[4]=='long castles':
                gs.board[len(gs.board)-1][move[2]][move[3]+1]=gs.board[len(gs.board)-1][move[2]][0]
                gs.board[len(gs.board)-1][move[2]][0]='--'
        if depth==max_depth:
            value=chess_engine.evaluate_pos(gs)
            evaluation=(move[0],move[1],move[2],move[3],value)
        else:
            evaluation=run_ai(gs,depth+1,not(white_to_move))
        if evaluation==False:
            continue
        if best_move[4]==evaluation[4]:
            testtuple=(move[0],move[1],move[2],move[3],evaluation[4])
            equal_eval.append(testtuple)
        if white_to_move==False:            
            if best_move[4]>evaluation[4]:
                equal_eval.clear()
                best_move=(move[0],move[1],move[2],move[3],evaluation[4])
                equal_eval.append(best_move)
        else:
            if best_move[4]<evaluation[4]:
                equal_eval.clear()
                best_move=(move[0],move[1],move[2],move[3],evaluation[4])
                equal_eval.append(best_move)
        if 
        gs.board[len(gs.board)-1]=copy.deepcopy(gs.board[len(gs.board)-2])
    gs.board.pop(len(gs.board)-1)
    num=random.random()*len(equal_eval)
    #print(len(equal_eval),math.floor(num))
    return equal_eval[math.floor(num)]
def main():
    pg.init()
    loadimages()
    screen=pg.display.set_mode((width,height))
    fps=120
    clock=pg.time.Clock()
    screen.fill(pg.Color("white"))
    gs=chess_engine.game_state()
    move=chess_engine.move
    running=True
    piece_selected='--'
    piece_sel_col=0
    piece_sel_row=0
    move_to_col=0
    move_to_row=0
    is_over=False
    while running:
        if is_over==False:
            if gs.white_to_move==False:
                ai_move=run_ai(gs,1,False)
                gs.board.append(copy.deepcopy(gs.board[len(gs.board)-1]))
                if gs.board[len(gs.board)-1][ai_move[0]][ai_move[1]]=='wK':
                    gs.white_king_moved=True
                elif gs.board[len(gs.board)-1][ai_move[0]][ai_move[1]]=='bK':
                    gs.black_king_moved=True
                if gs.board[len(gs.board)-1][ai_move[0]][ai_move[1]]=='wR':
                    if ai_move[1]==7:
                        gs.white_h_moved=True
                    else:
                        gs.white_a_moved=True
                elif gs.board[len(gs.board)-1][ai_move[0]][ai_move[1]]=='bR':
                    if ai_move[1]==7:
                        gs.black_h_moved=True
                    else:
                        gs.black_a_moved=True
                    gs.black_king_moved=True                                 
                print(gs.board[len(gs.board)-1][ai_move[0]][ai_move[1]],ai_move)
                if (gs.board[len(gs.board)-1][ai_move[0]][ai_move[1]]=='wp' and ai_move[2]==0):
                    gs.board[len(gs.board)-1][ai_move[2]][ai_move[3]]='wQ'
                elif (gs.board[len(gs.board)-1][ai_move[0]][ai_move[1]]=='bp' and ai_move[2]==7):
                    gs.board[len(gs.board)-1][ai_move[2]][ai_move[3]]='bQ'
                else:
                    gs.board[len(gs.board)-1][ai_move[2]][ai_move[3]]=gs.board[len(gs.board)-1][ai_move[0]][ai_move[1]]
                gs.board[len(gs.board)-1][ai_move[0]][ai_move[1]]='--'
                if gs.white_to_move==True:
                    gs.white_to_move=False
                else:
                    gs.white_to_move=True
                if chess_engine.is_game_over(gs)==True:
                    running=False
                draw_curr_state(screen,gs)
                clock.tick(fps)
                pg.display.flip()                  
            for e in pg.event.get():
                if e.type==pg.QUIT:
                    running=False
                elif e.type==pg.MOUSEBUTTONDOWN:
                    mouse_pos=pg.mouse.get_pos()
                    if piece_selected!='--':
                        move_to_col=mouse_pos[0]//sq_size
                        move_to_row=mouse_pos[1]//sq_size
                        is_legal_move=move(gs.board[len(gs.board)-1],gs.board[len(gs.board)-2],gs.white_to_move,gs.white_king_moved,gs.black_king_moved,gs.white_a_rook_moved,gs.white_h_rook_moved,gs.black_a_rook_moved,gs.black_h_rook_moved,piece_sel_row, piece_sel_col, move_to_row, move_to_col)
                        if is_legal_move==True or is_legal_move=='En passant' or is_legal_move=='short castles' or is_legal_move=='long castles':
                            gs.board.append(copy.deepcopy(gs.board[len(gs.board)-1]))
                            print(gs.board[len(gs.board)-1])
                            if is_legal_move=='short castles':
                                is_legal=True
                                for i in range(3):
                                    if gs.white_to_move==True:
                                        gs.board[len(gs.board)-1][piece_sel_row][piece_sel_col]='--'
                                        gs.board[len(gs.board)-1][move_to_row][piece_sel_col+i]=piece_selected                                           
                                        if chess_engine.is_check(gs.board[len(gs.board)-1],True)==True:
                                            for row in range(8):
                                                for col in range(8):
                                                    gs.board[len(gs.board)-1][row][col]=copy.deepcopy(gs.board[len(gs.board)-2][row][col])
                                            is_legal=False
                                            break
                                    else:
                                        if chess_engine.is_check(gs.board[len(gs.board)-1],False)==True:
                                            for row in range(8):
                                                for col in range(8):
                                                    gs.board[len(gs.board)-1][row][col]=copy.deepcopy(gs.board[len(gs.board)-2][row][col])
                                            is_legal=False
                                            break
                                if is_legal==False:
                                    piece_selected='--'
                                    draw_curr_state(screen,gs)
                                    clock.tick(fps)
                                    pg.display.flip()                                    
                                    continue
                                else:
                                    #print(gs.board[len(gs.board)-1][move_to_row][7],move_to_col)
                                    #print(gs.board[len(gs.board)-1][move_to_row][4])
                                    gs.board[len(gs.board)-1][piece_sel_row][piece_sel_col]='--'
                                    gs.board[len(gs.board)-1][move_to_row][move_to_col]=piece_selected
                                    gs.board[len(gs.board)-1][move_to_row][7]='--'
                                    if piece_selected=='wK':
                                        gs.white_king_moved=True
                                    if piece_selected=='bK':
                                        gs.black_king_moved=True
                                    if piece_selected=='wR':
                                        gs.white_h_moved=True
                                    if piece_selected=='bR':
                                        gs.black_h_moved=True                                     
                                    if gs.white_to_move==True:
                                        print(gs.board[len(gs.board)-1][move_to_row][move_to_col-1])                                        
                                        gs.board[len(gs.board)-1][move_to_row][move_to_col-1]='wR'
                                        print(gs.board[len(gs.board)-1][move_to_row][move_to_col-1])
                                    else:
                                        gs.board[len(gs.board)-1][move_to_row][move_to_col-1]='bR'
                                    gs.white_to_move=not(gs.white_to_move)
                                    piece_selected='--'
                                    #print(gs.board[len(gs.board)-1][move_to_row][7])
                                    draw_curr_state(screen,gs)
                                    clock.tick(fps)
                                    pg.display.flip()  
                                    if chess_engine.is_game_over(gs)==True:
                                        running=False                                                                    
                                    continue
                            if is_legal_move=='long castles':
                                is_legal=True
                                for i in range(3):
                                    if gs.white_to_move==True:
                                        gs.board[len(gs.board)-1][piece_sel_row][piece_sel_col]='--'
                                        gs.board[len(gs.board)-1][move_to_row][piece_sel_col-i]=piece_selected
                                        if chess_engine.is_check(gs.board[len(gs.board)-1],True)==True:
                                            for row in range(8): 
                                                for col in range(8):
                                                    gs.board[len(gs.board)-1][row][col]=copy.deepcopy(gs.board[len(gs.board)-2][row][col])
                                            is_legal=False
                                            break
                                    else:
                                        if chess_engine.is_check(gs.board[len(gs.board)-1],False)==True:
                                            for row in range(8):
                                                for col in range(8):
                                                    gs.board[len(gs.board)-1][row][col]=copy.deepcopy(gs.board[len(gs.board)-2][row][col])
                                            is_legal=False
                                            break
                                if is_legal==False:
                                    piece_selected='--'
                                    draw_curr_state(screen,gs)
                                    clock.tick(fps)
                                    pg.display.flip()                                    
                                    continue
                                else:
                                    gs.board[len(gs.board)-1][piece_sel_row][piece_sel_col]='--'
                                    gs.board[len(gs.board)-1][move_to_row][move_to_col]=piece_selected
                                    if piece_selected=='wK':
                                        gs.white_king_moved=True
                                    if piece_selected=='bK':
                                        gs.black_king_moved=True
                                    if piece_selected=='wR':
                                        gs.white_a_moved=True
                                    if piece_selected=='bR':
                                        gs.black_a_moved=True                                     
                                    gs.board[len(gs.board)-1][move_to_row][0]='--'
                                    if gs.white_to_move==True:
                                        gs.board[len(gs.board)-1][move_to_row][move_to_col+1]='wR'
                                    else:
                                        gs.board[len(gs.board)-1][move_to_row][move_to_col+1]='bR'
                                    gs.white_to_move=not(gs.white_to_move)
                                    piece_selected='--'
                                    print(gs.board[len(gs.board)-1])
                                    print(gs.board[len(gs.board)-1][move_to_row][7])
                                    draw_curr_state(screen,gs)
                                    clock.tick(fps)
                                    pg.display.flip()
                                    if chess_engine.is_game_over(gs)==True:
                                        running=False                                    
                                    continue
                            if is_legal_move=='En passant':
                                if gs.white_to_move==True:
                                    gs.board[len(gs.board)-1][move_to_row+1][move_to_col]='--'
                                else:
                                    gs.board[len(gs.board)-1][move_to_row-1][move_to_col]='--'
                            gs.board[len(gs.board)-1][piece_sel_row][piece_sel_col]='--'
                            gs.board[len(gs.board)-1][move_to_row][move_to_col]=piece_selected
                            if (piece_selected=='wp' and move_to_row==0):
                                gs.board[len(gs.board)-1][move_to_row][move_to_col]='wQ'
                            if (piece_selected=='bp' and move_to_row==7):
                                gs.board[len(gs.board)-1][move_to_row][move_to_col]='bQ'  
                            if gs.white_to_move==True:
                                if chess_engine.is_check(gs.board[len(gs.board)-1],True)==True:
                                    for row in range(8):
                                        for col in range(8):
                                            gs.board[len(gs.board)-1][row][col]=gs.board[len(gs.board)-2][row][col]         
                                else:
                                    gs.white_to_move=False
                                    if piece_selected=='wK':
                                        gs.white_king_moved=True
                                    if piece_selected=='bK':
                                        gs.black_king_moved=True
                                    if piece_selected=='wR' and piece_sel_row==0:
                                        gs.white_a_moved=True
                                    if piece_selected=='bR' and piece_sel_row==0:
                                        gs.black_a_moved=True                                     
                                    if piece_selected=='wR' and piece_sel_row==7:
                                        gs.white_h_moved=True
                                    if piece_selected=='bR' and piece_sel_row==7:
                                        gs.black_h_moved=True                                                                            
                            else:
                                if chess_engine.is_check(gs.board[len(gs.board)-1],False)==True:
                                    for row in range(8):
                                        for col in range(8):
                                            gs.board[len(gs.board)-1][row][col]=gs.board[len(gs.board)-2][row][col]
                                else:                              
                                    gs.white_to_move=True
                                    if piece_selected=='wK':
                                        gs.white_king_moved=True
                                    if piece_selected=='bK':
                                        gs.black_king_moved=True
                                    if piece_selected=='wR' and piece_sel_row==0:
                                        gs.white_a_moved=True
                                    if piece_selected=='bR' and piece_sel_row==0:
                                        gs.black_a_moved=True                                     
                                    if piece_selected=='wR' and piece_sel_row==7:
                                        gs.white_h_moved=True
                                    if piece_selected=='bR' and piece_sel_row==7:
                                        gs.black_h_moved=True                                    

                        piece_selected='--'          
                        if chess_engine.is_game_over(gs)==True:
                                running=False                        
                    else:
                        piece_sel_col=mouse_pos[0]//sq_size
                        piece_sel_row=mouse_pos[1]//sq_size
                        piece_selected=gs.board[len(gs.board)-1][piece_sel_row][piece_sel_col]
                draw_curr_state(screen,gs)
                clock.tick(fps)
                pg.display.flip()
        else:
            draw_curr_state(screen,gs)
            clock.tick(fps)
            pg.display.flip()
          

def draw_curr_state(screen,gs):
    draw_board(screen)
    draw_pieces(screen,gs)

if __name__=="__main__":
    main()