import os

folder = os.path.dirname(__file__)

class Parameters_box():
    file = open(os.path.join(folder, 'parameters.txt'), 'r+')
    background_colour = list(map(int,file.readline().split(' ')))
    font_colour = list(map(int,file.readline().split(' ')))
    players = list(file.readline().split(' '))
    file.close()

    @staticmethod
    def file_rewrite():
        file = open(os.path.join(folder, 'parameters.txt'), 'w')
        a = Parameters_box.background_colour
        file.write(str(a[0])+' '+str(a[1])+' '+str(a[2]))
        file.write('\n')
        a = Parameters_box.font_colour
        file.write(str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]))
        file.write('\n')
        a = Parameters_box.players
        file.write(str(a[0]) + ' ' + str(a[1]))
        file.close()
