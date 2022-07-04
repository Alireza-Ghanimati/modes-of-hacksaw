import pygame
import math
from pygame.locals import *

window_height = 800
window_width = 800
circle_radious = 10
circle_border_thickness = 1
rope_length = 30
rope_width = 1
speed = 3

center = (window_width / 2, window_height / 2)
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Modes of hack saw')
white = (255, 255, 255)
black = (0, 0, 0)
window.fill(white)
pygame.display.flip()

h = [1, 1/2, -1/2, -1, -1/2, 1/2]
t = 0
j = 1
d = [0, 0, 0, 0, 0, 0]
amp = math.pi / 24
omega = .5
dt = speed / 100
em = 20
bm = 9
cm = -1
dm = 1

font = pygame.font.Font('freesansbold.ttf', 20)
text1 = font.render(" mode 1 ", True, "black")
text2 = font.render(" mode 2 ", True, "black")
text3 = font.render(" mode 3 ", True, "black")
text4 = font.render(" mode 4 ", True, "black")
text5 = font.render(" mode 5 ", True, "black")
text6 = font.render(" mode 6 ", True, "black")
mode_text = font.render(" mode 1 ", True, "black")
text_width = 80
text_height = 22


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if text1_pos[0] <= mouse[0] <= text1_pos[0] + text_width and text1_pos[1] <= mouse[1] <= text1_pos[
                1] + text_height:
                h = [1, 1 / 2, -1 / 2, -1, -1 / 2, 1 / 2]
                t = 0
                j = 1
                mode_text = font.render(" mode 1 ", True, "black")

            if text2_pos[0] <= mouse[0] <= text2_pos[0] + text_width and text2_pos[1] <= mouse[1] <= text2_pos[
                1] + text_height:
                h = [-1, 1 / 2, 1 / 2, -1, 1 / 2, 1 / 2]
                t = 0
                j = 3
                mode_text = font.render(" mode 2 ", True, "black")

            if text3_pos[0] <= mouse[0] <= text3_pos[0] + text_width and text3_pos[1] <= mouse[1] <= text3_pos[
                1] + text_height:
                h = [1, -1, 1, -1, 1, -1]
                t = 0
                j = 3
                mode_text = font.render(" mode 3 ", True, "black")

            if text4_pos[0] <= mouse[0] <= text4_pos[0] + text_width and text4_pos[1] <= mouse[1] <= text4_pos[
                1] + text_height:
                h = [0, 1, 1, 0, -1, -1]
                t = 0
                j = 1
                mode_text = font.render(" mode 4 ", True, "black")

            if text5_pos[0] <= mouse[0] <= text5_pos[0] + text_width and text5_pos[1] <= mouse[1] <= text5_pos[
                1] + text_height:
                h = [0, -1, 1, 0, -1, 1]
                t = 0
                j = 3
                mode_text = font.render(" mode 5 ", True, "black")

            if text6_pos[0] <= mouse[0] <= text6_pos[0] + text_width and text6_pos[1] <= mouse[1] <= text6_pos[
                1] + text_height:
                h = [1, 1, 1, 1, 1, 1]
                t = 0
                j = 0
                mode_text = font.render(" mode 6 ", True, "black")

    o = math.sqrt(em - 2 * bm * math.cos(j * math.pi / 3) - 2 * cm * math.cos(2 * j * math.pi / 3) - dm * math.cos(
        j * math.pi))
    window.fill(white)
    theta = 0

    for i in range(6):
        d[i] = h[i] * math.sin(omega * o * t) * amp
        last_position = center
        new_x = rope_length * math.cos(theta) + center[0]
        new_y = rope_length * math.sin(theta) + center[1]
        pygame.draw.line(window, black, last_position, (new_x, new_y), width=rope_width)
        last_position = (new_x, new_y)
        new_x = rope_length * math.cos(theta) + rope_length * math.cos(theta + (d[i] / 2)) + center[0]
        new_y = rope_length * math.sin(theta) + rope_length * math.sin(theta + (d[i] / 2)) + center[1]
        pygame.draw.line(window, black, last_position, (new_x, new_y), width=rope_width)
        last_position = (new_x, new_y)
        new_x = rope_length * math.cos(theta) + rope_length * math.cos(theta + (d[i] / 2)) + rope_length * math.cos(
            theta + d[i]) + center[0]
        new_y = rope_length * math.sin(theta) + rope_length * math.sin(theta + (d[i] / 2)) + rope_length * math.sin(
            theta + d[i]) + center[1]
        pygame.draw.line(window, black, last_position, (new_x, new_y), width=rope_width)
        last_position = (new_x, new_y)
        pygame.draw.circle(window, white, last_position, circle_radious, width=0)
        pygame.draw.circle(window, black, last_position, circle_radious, width=circle_border_thickness)
        theta += (math.pi / 3)

    text1_pos = (window_width / 7 - text_width / 2, window_height / 7)
    text2_pos = (2 * window_width / 7 - text_width / 2, window_height / 7)
    text3_pos = (3 * window_width / 7 - text_width / 2, window_height / 7)
    text4_pos = (4 * window_width / 7 - text_width / 2, window_height / 7)
    text5_pos = (5 * window_width / 7 - text_width / 2, window_height / 7)
    text6_pos = (6 * window_width / 7 - text_width / 2, window_height / 7)
    mode_text_pos = (window_width/2-text_width/2,window_height/2 + 3*rope_length + circle_radious + 20)

    text1_Rect = pygame.draw.rect(window, "gray", [text1_pos[0], text1_pos[1], text_width, text_height])
    text2_Rect = pygame.draw.rect(window, "gray", [text2_pos[0], text2_pos[1], text_width, text_height])
    text3_Rect = pygame.draw.rect(window, "gray", [text3_pos[0], text3_pos[1], text_width, text_height])
    text4_Rect = pygame.draw.rect(window, "gray", [text4_pos[0], text4_pos[1], text_width, text_height])
    text5_Rect = pygame.draw.rect(window, "gray", [text5_pos[0], text5_pos[1], text_width, text_height])
    text6_Rect = pygame.draw.rect(window, "gray", [text6_pos[0], text6_pos[1], text_width, text_height])

    window.blit(text1, text1_pos)
    window.blit(text2, text2_pos)
    window.blit(text3, text3_pos)
    window.blit(text4, text4_pos)
    window.blit(text5, text5_pos)
    window.blit(text6, text6_pos)
    window.blit(mode_text,mode_text_pos)

    pygame.display.flip()

    t += dt
    clock.tick(60)
