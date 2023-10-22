import pygame
import os
import random
import buttons.button_class
import disks.disk_class


class multy_game():
    def __init__(self, screen):
        self.screen = screen

        self.desk = []
        self.possibilities = []
        for i in range(8):
            self.desk.append([0] * 8)
        self.disks = pygame.sprite.Group()
        self.player = 1

    def start_a_game(self):
        self.screen.fill((0, 255, 0))
        for i in range(0, 9):
            pygame.draw.line(self.screen, (0, 0, 0), [i * 80 + 80, 80], [i * 80 + 80, 720], 2)
            pygame.draw.line(self.screen, (0, 0, 0), [80, i * 80 + 80], [720, i * 80 + 80], 2)
        disk1 = disks.disk_class.disk(1, (3,3))
        self.disks.add(disk1)
        self.desk[3][3] = disk1

        disk2 = disks.disk_class.disk(2, (4, 3))
        self.disks.add(disk2)
        self.desk[4][3] = disk2

        disk3 = disks.disk_class.disk(2, (3, 4))
        self.disks.add(disk3)
        self.desk[3][4] = disk3

        disk4 = disks.disk_class.disk(1, (4, 4))
        self.disks.add(disk4)
        self.desk[4][4] = disk4
        self.disks.draw(self.screen)
        self.possibilities = [(2, 4), (3, 5), (4, 2), (5, 3)]


    def parcing(self, event):
        pos = event.pos
        if (pos[0] >= 80 and pos[0] <= 720) and (pos[1] >= 80 and pos[1] <= 720):
            pos_x = pos[0] // 80 - 1
            pos_y = pos[1] // 80 - 1
            return (pos_x, pos_y)
        else:
            return 'not desk'

    def update(self, event: pygame.MOUSEBUTTONDOWN):
        if self.parcing(event) != 'not desk':
            cell_X, cell_Y = self.parcing(event)
            if self.possibilities == []:
                self.player = 3 - self.player
                self.possibilities_update()
            if (cell_X,cell_Y) in self.possibilities:
                self.turn((cell_X, cell_Y))
                self.possibilities_update()
                self.player = 3 - self.player

                self.disks.draw(self.screen)

    def possibilities_update(self):
        self.possibilities = []
        for x in range(8):
            for y in range(8):
                if self.desk[x][y] == 0:
                    if self.all_directions((x,y),True,3-self.player) !=0:
                        self.possibilities.append((x,y))
        print(self.possibilities)



    def all_directions(self, position, checking,player):
        summ = 0
        for dir_x in range(-1, 2):
            for dir_y in range(-1, 2):
                if (dir_x, dir_y) == (0, 0):
                    continue
                if checking == False:
                    self.chain(position, (dir_x, dir_y), checking,player)
                else:
                    summ+=self.chain(position, (dir_x, dir_y), checking,player)
        return summ

    def turn(self, position):
        new_disk = disks.disk_class.disk(self.player, position)
        self.disks.add(new_disk)
        self.desk[position[0]][position[1]] = new_disk
        self.all_directions(position,False,self.player)

    def chain(self, start_cell, dir, checking,player):
        curr_x = start_cell[0]
        curr_y = start_cell[1]
        sttrclr = player
        line = []
        while ((0 <= curr_x + dir[0] <= 7) and (0 <= curr_y + dir[1] <= 7)):
            curr_x += dir[0]
            curr_y += dir[1]
            if self.desk[curr_x][curr_y] != 0:
                if self.desk[curr_x][curr_y].colour == sttrclr:
                    if checking == False:
                        for disk in line:
                            disk.flip()
                    if checking == True:
                        return len(line)
                    break
                else:
                    line.append(self.desk[curr_x][curr_y])
            else:
                '''if not (curr_x - dir[0] == start_cell[0] and curr_y - dir[1] == start_cell[1]):
                    print('aaaa')'''
                break
        return 0

        # self.disks5.draw(self.screen)
