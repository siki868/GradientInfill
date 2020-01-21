import re
import numpy as np
import matplotlib.pyplot as plt
import math

# Treba da se popravi
def get_block_between(start, end, data):
    ret = []
    data = data.split('\n')

    app = False
    for line in data:
        if line.startswith(start):
            app = True
            print('Cont')
            continue
    
        if line.startswith(end):
            print('Izasao')
            break

        if app:
            ret.append(line)


    return ret
    # return (data[data.find(start) + len(start):data.rfind(end)][1:-1]).split('\n')


def get_xy(line):
    try:
        x = float(re.findall(r'[X](\d*\.*\d*)', line)[0])
    except:
        x = float(re.findall(r'[X](\d*\)', line)[0])
    try:
        y = float(re.findall(r'[Y](\d*\.*\d*)', line)[0])
    except:
        y = float(re.findall(r'[Y](\d*\)', line)[0])

    print(x, y)
    return x, y
    
def get_e(line):
    return float(re.findall(r'[E](\d*\.\d*)', line)[0])



def interpolate(p1, p2, nb_steps, e=1.04099):
    print(p1, p2)
    plt.plot(p1, p2, 'og-')
    x1, x2, y1, y2 = p1[0], p2[0], p1[1], p2[1]

    length = math.hypot(x2 - x1, y2 - y1)
    print(f'Len {length}')
    step_length = length / (nb_steps*2)
    print(f'Step len {step_length}')
    step_size = (x2-x1) / (nb_steps*2)
    print(f'Step size {step_size}')

    e_step_size = e / nb_steps

    # Svi preseci prave izmedju p1 i p2 (za svaki treba da se izr E)\

    # prva polovina
    for i in range(1, nb_steps + 1):
        new_x = x1 + i * step_size
        new_y = np.interp(new_x, p1, p2)
        plt.plot(new_x, new_y, 'or')

    for i in range(nb_steps + 1, nb_steps*2):
        new_x = x1 + i * step_size
        new_y = np.interp(new_x, p1, p2)
        plt.plot(new_x, new_y, 'or')



    plt.show()

def main():
    with open('in1.gcode', 'r') as f:
        data = f.read()
        wall_block = get_block_between(';TYPE:WALL-OUTER', ';TYPE:FILL', data)
        infill_block = get_block_between(';TYPE:FILL', ';TIME_ELAPSED', data)

        last_xy = get_xy(wall_block[-1])

        for line in infill_block:
            if 'E' in line:
                print(f'Treba idem od {last_xy} do {get_xy(line)} sa E = {get_e(line)}')
            else:
                last_xy = get_xy(line)


def test():
    with open('in2.gcode', 'r') as f:
        data = f.read()
        wall_block = get_block_between(';TYPE:WALL-OUTER', ';TYPE:FILL', data)
        infill_block = get_block_between(';TYPE:FILL', ';', data)

        print(len(wall_block), len(infill_block))

        # p1, p2 = get_xy(wall_block[-1]), get_xy(infill_block[0])
        # interpolate(p1, p2 , 3)
if __name__ == "__main__":

    test()