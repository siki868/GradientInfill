import re
import numpy as np
import matplotlib.pyplot as plt
import math
from shapely.geometry import LineString, MultiPoint

# Treba da se popravi
def get_block_between(start, end, data):
    if end == ';TIME_ELAPSED':
        ret = []
        data = data.split('\n')

        app = False
        for line in data:
            if line.startswith(start):
                app = True
                continue
        
            if line.startswith(end) or line.startswith(';MESH:NONMESH'):
                break

            if app:
                ret.append(line)
    else:
        ret = []
        data = data.split('\n')

        app = False
        for line in data:
            if line.startswith(start):
                app = True
                continue
        
            if line.startswith(end):
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

    return x, y
    
def get_e(line):
    return float(re.findall(r'[E](\d*\.\d*)', line)[0])



def interpolate(p1, p2, nb_steps, e):
    ret = []
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    plt.plot([x1, x2], [y1, y2])

    # Segmentacija linije (sve tacke osim prve)
    line = LineString([p1, p2])
    segment_length = line.length/nb_steps

    if segment_length > 5.0:
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
            ret.append(l)
    else:
        l = f'G1 F600 X{p2[0]} Y{p2[1]} E{round(e*3.5, 5)}'
        ret.append(l)

    return ret

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
    with open('in3.gcode', 'r') as f, open('out.gcode', 'w') as w_f:
        data = f.read()
        lines = data.split('\n')
        wall_block = get_block_between(';TYPE:WALL-OUTER', ';TYPE:FILL', data)
        infill_block = get_block_between(';TYPE:FILL', ';TIME_ELAPSED', data)

        pisi = True
        # print(wall_block[-1])
        prev_xy = get_xy(wall_block[-1])


        for line in lines:
            if pisi:
                w_f.write(line + '\n')
            if ';TYPE:FILL' in line:
                '''
                    Nove vrednosti za e
                '''
                for line in infill_block:
                    if 'E' in line and 'X' in line and 'Y' in line:
                        ls = interpolate(prev_xy, get_xy(line), 6, e=get_e(line))
                        for l in ls:
                            w_f.write(l + '\n')
                    elif 'X' in line or 'Y' in line:
                        prev_xy = get_xy(line)
                        w_f.write(line + '\n')
                    else:
                        w_f.write(line + '\n')

                pisi = False
            if ';MESH:NONMESH' in line or ';TIME_ELAPSED' in line:
                w_f.write(line + '\n')
                pisi = True
        


        # interpolate(p1, p2 , 6)
        # plt.show()


if __name__ == "__main__":

    test()