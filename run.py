from funs import *


def main():
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

def test():
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



if __name__ == "__main__":
    main()
