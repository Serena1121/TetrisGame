import pygame
from define import *
import random
from Score.score import draw_score, CaculateScore

def draw_block(screen, x, y, color):
    pygame.draw.rect(screen, color, (x * BOARD_ALL, y * BOARD_ALL, BOARD_ALL, BOARD_ALL), 0)
    pygame.draw.rect(screen, GREY, (x * BOARD_ALL, y * BOARD_ALL, BOARD_ALL, BOARD_ALL), 1)

def draw_shape(screen, shape, x, y, color):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == 1:
                draw_block(screen, x + col, y + row, color)

def generate_shape():
    shape_idx = random.randint(0, len(SHAPE) -1)
    shape = SHAPE[shape_idx]
    color = SHAPE_COLOR[shape_idx]
    return shape, color

def is_collision(board, shape, offest_x, offest_y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):         
            if shape[row][col] == 1:
                y_pos = row + offest_y
                x_pos = col + offest_x
                if x_pos < 0 or x_pos >= BOARD_WIDTH or y_pos >= BOARD_HEIGHT:
                    return True
                if y_pos >= 0 and board[y_pos][x_pos] != BLACK:
                    return True
    return False

def shape_fall(bgm, can_move, x, y, board, current_shape, current_color, score, bonus):
    if not is_collision(board, current_shape, x, y + 1):
        y += 1
    else:
        for row in range(len(current_shape)):
            for col in range(len(current_shape[row])):
                if current_shape[row][col] == 1:
                    board[y + row][x + col] = current_color
        score, bonus = remove_rows(board, bgm, score, bonus)
        x, y = 3, 0
        current_shape, current_color = generate_shape()
        if is_collision(board, current_shape, x, y):
            can_move = False
    return can_move, x, y, board, current_shape, current_color, score, bonus
        

def remove_rows(board, bgm, score, bonus):
    full_rows = []
    row = len(board) - 1
    isDelete = False
    while row >= 0:
        current_row = board[row]
        if all(cell != BLACK for cell in current_row):
            full_rows.append(row)
            isDelete = True
        row -= 1

    if isDelete:
        bgm.play(1)
        for delRow in full_rows:
            del board[delRow]
            score, bonus = CaculateScore(delRow, BOARD_HEIGHT, score, bonus)
            
    for _ in range(len(full_rows)):
        board.insert(0, [BLACK for _ in range(BOARD_WIDTH)])

    return score, bonus