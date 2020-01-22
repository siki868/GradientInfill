import re
import numpy as np
import matplotlib.pyplot as plt
import math
from shapely.geometry import LineString, MultiPoint

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
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    plt.plot([x1, x2], [y1, y2])

    # Segmentacija linije (sve tacke osim prve)
    line = LineString([p1, p2])
    splitter = MultiPoint([line.interpolate((i/nb_steps), normalized=True) for i in range(1, nb_steps+1)])

    xs = [point.x for point in splitter]
    ys = [point.y for point in splitter]

    # Izbacivanje srednje tacke jer je e isto 
    xs.pop((len(xs)-1)//2)
    ys.pop((len(ys)-1)//2)


    plt.scatter(xs, ys)

    # racunanje svih e-ova
    e_step = e / (nb_steps//2)
    es = []
    for i in range(nb_steps//2):
        es.append(e - i*e_step)
    es.extend(es[::-1])

    # G1 F600 X93.508 Y90.68 E1.516
    for ex, point in zip(es, splitter):
        l = f'G1 F600 X{round(point.x, 3)} Y{round(point.y, 3)} E{round(ex, 5)}'
        # print(l)



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
        infill_block = get_block_between(';TYPE:FILL', ';TIME_ELAPSED', data)


        # print(wall_block[-1])
        prev_xy = get_xy(wall_block[-1])

        for line in infill_block:
            if 'E' in line and 'X' in line and 'Y' in line:
                interpolate(prev_xy, get_xy(line), 6, e=get_e(line))
            elif 'X' in line or 'Y' in line:
                prev_xy = get_xy(line)


        # interpolate(p1, p2 , 6)
        plt.show()


if __name__ == "__main__":

    test()