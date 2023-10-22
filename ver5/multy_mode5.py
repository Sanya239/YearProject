import pygame
import os
import random
import ver5.buttons5.button_class as button_class
import ver5.disks5.disk_class5 as disk_class
import time
import ver5.elements.dialog_window_class as dialog_window_class
import ver5.elements.parameters_box_class5 as parameters_box_class
import ver5.server as Server


def copy1(L: list):
    a = []
    for i in L:
        a.append(i)
    return a


def copy2(L: list):
    a = []
    for i in L:
        a.append(copy1(i))
    return a


class multy_game():
    def __init__(self, parent):
        self.parent = parent
        self.screen = self.parent.screen
        self.turn_number = 1
        self.animation_mode_ON = False
        self.auto = False
        self.what_to_send = bytes('a!','UTF8')



        self.players = parameters_box_class.Parameters_box.players
        self.init_buttons()
        self.lists_generation()
        self.endgame_elements()
        self.connection_elements()
        self.update = self.update_game

        # self.disks = pygame.sprite.Group()
    def init_buttons(self):
        self.game_buttons = pygame.sprite.Group()
        self.time = 0
        #self.undo_button = button_class.button((150, 760),text='undo turn', func=self.undo)
        #self.redo_button = button_class.button((650, 760),text='redo turn', func=self.redo)
        self.menu_button = button_class.button((125,50),text= 'menu', func=self.return_to_menu)
        #self.game_buttons.add(self.undo_button)
        #self.game_buttons.add(self.redo_button)
        self.game_buttons.add(self.menu_button)
        self.count_black = pygame.font.Font(None, 60)
        self.count_gray = pygame.font.Font(None, 60)
        self.count_white = pygame.font.Font(None, 60)


    def lists_generation(self):
        self.disks = pygame.sprite.Group()
        self.desk = []
        self.colours = []
        self.possibilities = []
        self.history = [[0]] * 70
        for x in range(8):
            line = []
            line_of_colours = []
            for y in range(8):
                new_disk = disk_class.disk(0, (x, y))
                line.append(new_disk)
                self.disks.add(new_disk)
                line_of_colours.append(0)
            self.desk.append(line)
            self.colours.append(line_of_colours)

    def endgame_elements(self):
        self.shading = pygame.Surface((1000, 1000))
        self.shading.fill((0, 0, 0))
        self.shading.set_alpha(200)

        self.final_stats_surf = pygame.Surface((400,200))
        self.final_stats_surf.fill((128,128,128))

        self.final_buttons = pygame.sprite.Group()
        self.restart_button = button_class.button((600,400),text='restart',func=self.restart)
        self.final_buttons.add(self.restart_button)
        self.final_buttons.add(self.menu_button)

    def connection_elements(self):
        self.server_button = button_class.button((200,400), text= 'создать игру', func=self.server_start)
        self.connect_button = button_class.button((500,400),text= 'присоединиться', func= self.connect)
        self.ip_asker = dialog_window_class.Dialog_window(self,size=(600,60),position=(400,400),parameter=3,max_number=9999999999999999)
        self.connection_buttons = pygame.sprite.Group()
        self.connection_buttons.add(self.menu_button)
        self.connection_buttons.add(self.server_button)
        self.connection_buttons.add(self.connect_button)

    def connection_update(self,event):
        self.connection_buttons.draw(self.screen)
        if not event == None:
            self.connection_buttons.update(event)


    def server_start(self):
        self.connect_button.hide()
        self.draw_stage()
        self.disks.draw(self.screen)
        pygame.display.flip()
        self.players = ('me', 'stranger')
        print('server online')
        Server.server_online(self)


    def connect(self):
        self.players = ('stranger', 'me')
        self.server_button.hide()
        self.connect_button.hide()
        self.connection_buttons.add(self.ip_asker)
        self.draw_stage()
        self.screen.blit(self.shading,(0,0))

        return

    def return_to_menu(self):
        self.turn_number=-1
        self.parent.mode = 0
        self.buttons.draw(self.screen)
        self.buttons = pygame.sprite.Group()
        self.parent.menu.menu_draw()

    def currient_player(self):
        if self.turn_number % 2 == 1:
            return self.players[0]
        else:
            return self.players[1]

    def next_player(self):
        if self.turn_number % 2 == 1:
            return self.players[1]
        else:
            return self.players[0]

    def draw_stage(self):
        self.screen.fill(parameters_box_class.Parameters_box.background_colour)
        for i in range(0, 9):
            pygame.draw.line(self.screen, (0, 0, 0), [i * 80 + 80, 80], [i * 80 + 80, 720], 2)
            pygame.draw.line(self.screen, (0, 0, 0), [80, i * 80 + 80], [720, i * 80 + 80], 2)
        self.menu_button.rect.center = (125,50)
        #pygame.display.flip()

    def starting_position(self):
        self.draw_stage()
        self.turn_number = 1
        self.last_turn = None

        self.colours[3][3] = 2

        self.colours[3][4] = 1

        self.colours[4][3] = 1

        self.colours[4][4] = 2

        for x in range(8):
            for y in range(8):
                self.desk[x][y].flip(self.colours[x][y])
        #self.animation_mode_ON = True
        #self.auto = True
        #self.undo_button.hide()
        #self.redo_button.hide()
        self.disks.update()
        self.disks.draw(self.screen)
        self.connection_elements()
        self.buttons = self.connection_buttons
        self.screen.blit(self.shading, (0, 0))
        self.buttons.draw(self.screen)
        self.update = self.connection_update
        #self.possibilities = [[2, 3], [3, 2], [5, 4], [4, 5]]

        #self.history[1] = copy2(self.colours)
        #self.points_recount()


    def parcing(self, event):
        pos = event.pos
        if (pos[0] >= 80 and pos[0] <= 720) and (pos[1] >= 80 and pos[1] <= 720):
            pos_x = pos[0] // 80 - 1
            pos_y = pos[1] // 80 - 1
            return (pos_x, pos_y)
        else:
            return 'not desk'

    def animation(self):
        self.draw_stage()
        self.disks.update()
        self.game_buttons.draw(self.screen)
        self.points_recount()
        self.disks.draw(self.screen)
        self.animation_mode_ON = False

        for x in range(8):
            for y in range(8):
                self.animation_mode_ON = (self.animation_mode_ON or self.desk[x][y].animation_mode_ON)
        self.auto = self.animation_mode_ON

    '''def undo(self):
        if time.time() - self.time > 0.1:
            self.time = time.time()
            self.turn_number -= 1
            if self.currient_player() == 'bot':
                self.turn_number -= 1
            self.redo_button.show()
            self.undo_button.message = False
            if self.turn_number <= 1 or (self.turn_number == 2 and self.next_player() == 'bot'):
                self.undo_button.hide()
            self.load(self.history[self.turn_number])
            self.possibilities = copy2(self.possibilities_update(self.colours))'''

    '''def redo(self):
        if time.time() - self.time > 0.1:
            self.time = time.time()
            self.turn_number += 1
            if self.currient_player() == 'bot':
                self.turn_number+=1

            self.undo_button.show()

            if self.history[self.turn_number + 1] == 0:
                self.redo_button.hide()
            self.load(self.history[self.turn_number])
            self.possibilities = copy2(self.possibilities_update(self.colours))'''

    '''def bot_turn(self):
        if self.turn_number>=65:
            self.game_end()
        if self.possibilities == []:
            print('no poss')
            print(self.turn_number, self.currient_player())
            self.possibilities = copy2(self.possibilities_update(self.colours))
            if self.possibilities == 0:
                self.game_end()
            self.turn_number += 1
            self.history[self.turn_number] = copy2(self.colours)
            self.history[self.turn_number + 1] = 0
        else:
            if not self.turn_number == 1:
                self.undo_button.show()
            self.redo_button.hide()
            self.buttons.draw(self.screen)
            self.turn(self.best_move(self.colours))'''

    def update_game(self, event: pygame.event):
        self.what_to_send = bytes('a!')
        if self.auto == True:
            if self.animation_mode_ON == True:
                self.animation()
            elif self.currient_player() == 'bot':
                self.bot_turn()
            else:
                self.auto = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = self.parcing(event)
            if position == 'not desk':
                self.buttons.update(event)


            else:
                if self.turn_number>=65:
                    self.game_end()
                if self.possibilities == []:
                    print('no poss')
                    print(self.turn_number, self.currient_player())
                    self.turn_number += 1
                    self.possibilities = copy2(self.possibilities_update(self.colours))
                    if self.possibilities == 0:
                        self.game_end()
                    '''self.history[self.turn_number] = copy2(self.colours)
                    self.history[self.turn_number + 1] = 0'''


                elif self.currient_player() == 'human':
                    cell_x, cell_y = position
                    position = list(position)
                    if position in self.possibilities:
                        self.turn((cell_x, cell_y))
                        '''self.undo_button.show()
                        self.redo_button.hide()'''
                        self.buttons.draw(self.screen)
                        self.disks.draw(self.screen)



        elif event.type == pygame.MOUSEMOTION:
            self.game_buttons.update(event)
            self.game_buttons.draw(self.screen)
        if self.currient_player() == 'bot':
            self.auto = True

    def final_update(self,event: pygame.event):
        if not event == None:
            self.buttons.update(event)
            self.buttons.draw(self.screen)

    def load(self, colours):
        self.draw_stage()
        for x in range(8):
            for y in range(8):
                if self.colours[x][y] != colours[x][y]:
                    self.desk[x][y].flip(colours[x][y])
                    self.colours[x][y] = colours[x][y]
                    self.animation_mode_ON = (self.animation_mode_ON or self.desk[x][y].animation_mode_ON)
                    self.auto = self.animation_mode_ON
        self.disks.update()
        self.disks.draw(self.screen)
        self.game_buttons.draw(self.screen)
        self.points_recount()

    def turn(self, position):
        self.what_to_send = bytes(position)
        cell_x, cell_y = position
        self.colours[cell_x][cell_y] = self.turn_number % 2
        if self.colours[cell_x][cell_y] == 0:
            self.colours[cell_x][cell_y] = 2
        self.desk[cell_x][cell_y].flip(self.colours[cell_x][cell_y])
        col = copy2(self.colours)
        new_colours = self.all_directions(position, col)[0].copy()
        # print(new_colours)
        self.load(new_colours)
        self.turn_number += 1
        self.history[self.turn_number] = copy2(self.colours)
        self.history[self.turn_number + 1] = 0

        self.possibilities = copy2(self.possibilities_update(self.colours))

    def all_directions(self, position, colours):
        new_colours = colours.copy()
        changes = 0
        for direction_x in range(-1, 2):
            for direction_y in range(-1, 2):
                if (direction_x, direction_y) == (0, 0):
                    continue
                one_direction = self.one_direction(new_colours, position, direction_x, direction_y)
                new_colours = one_direction[0]
                changes += one_direction[1]
        return (new_colours, changes)

    def one_direction(self, colours, position, direction_x, direction_y):
        # desk = self.desk.copy()
        new_colours = []
        for x in range(8):
            a = []
            for y in range(8):
                a.append(colours[x][y])
            new_colours.append(a)
        coord_x, coord_y = position
        line = []
        changes = 0
        while 0 <= coord_x + direction_x <= 7 and 0 <= coord_y + direction_y <= 7:
            coord_x += direction_x
            coord_y += direction_y
            if colours[coord_x][coord_y] == 0:
                break
            elif colours[coord_x][coord_y] % 2 == self.turn_number % 2:
                for disk_position in line:
                    # desk[disk_position[0]][disk_position[1]].colour = self.turn_number%2
                    new_colours[disk_position[0]][disk_position[1]] = self.turn_number % 2
                    if new_colours[disk_position[0]][disk_position[1]] == 0:
                        new_colours[disk_position[0]][disk_position[1]] = 2
                    changes = len(line)
                break
            else:
                line.append((coord_x, coord_y))
        return (new_colours, changes)

    def possibilities_update(self, colours):
        possibilities = []
        for x in range(8):
            for y in range(8):
                if self.colours[x][y] == 0:
                    if self.all_directions((x, y), colours)[0] != colours:
                        possibilities.append((x, y))
        return possibilities

    def best_move(self, colours):
        possibilities = copy2(self.possibilities)
        best_move = possibilities[0]
        for cell in possibilities:
            if self.all_directions(cell, colours)[1] > self.all_directions(best_move, colours)[1]:
                best_move = cell
        return best_move

    def points_recount(self):
        whites = 0
        blacks = 0
        for x in self.colours:
            for y in x:
                if y == 1:
                    whites += 1
                if y == 2:
                    blacks += 1
        white_points = self.count_white.render('{} '.format(whites), True, (255, 255, 255))
        gray_points = self.count_gray.render(':', True, (128, 128, 128))
        black_points = self.count_black.render(' {}'.format(blacks), True, (0, 0, 0))
        white_place = white_points.get_rect(center=(360, 30))
        gray_place = gray_points.get_rect(center=(400, 30))
        black_place = white_points.get_rect(center=(420, 30))
        self.screen.blit(white_points, white_place)
        self.screen.blit(gray_points, gray_place)
        self.screen.blit(black_points, black_place)

    def game_end(self):
        self.screen.blit(self.shading,(0,0))
        self.screen.blit(self.final_stats_surf,(200,300))
        self.menu_button.rect.center = (500, 500)
        self.buttons = self.final_buttons
        self.buttons.draw(self.screen)
        self.update = self.final_update


    def restart(self):
        print('restarted')
        self.turn_number = 1
        self.lists_generation()
        self.starting_position()
        self.draw_stage()
        self.update = self.update_game

        self.restart_button.image = self.restart_button.button_unclicked




'''import pygame
import os
import random
import ver4.buttons5.button_class
import ver4.disks5.disk_class4 as disk_class


class multy_game():
    def __init__(self, screen):
        self.screen = screen

        self.desk = []
        self.possibilities = []
        self.history = []
        for i in range(8):
            self.desk.append([0] * 8)
        self.disks = pygame.sprite.Group()
        self.player = 1

    def start_a_game(self):
        self.screen.fill((0, 255, 0))
        for i in range(0, 9):
            pygame.draw.line(self.screen, (0, 0, 0), [i * 80 + 80, 80], [i * 80 + 80, 720], 2)
            pygame.draw.line(self.screen, (0, 0, 0), [80, i * 80 + 80], [720, i * 80 + 80], 2)
        disk1 = disk_class.disk(1, (3, 3))
        self.disks.add(disk1)
        self.desk[3][3] = disk1

        disk2 = disk_class.disk(2, (4, 3))
        self.disks.add(disk2)
        self.desk[4][3] = disk2

        disk3 = disk_class.disk(2, (3, 4))
        self.disks.add(disk3)
        self.desk[3][4] = disk3

        disk4 = disk_class.disk(1, (4, 4))
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
        new_disk = disk_class.disk(self.player, position)
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
                #if not (curr_x - dir[0] == start_cell[0] and curr_y - dir[1] == start_cell[1]):
                   # print('aaaa')
                break
        return 0

        # self.disks5.draw(self.screen)'''
