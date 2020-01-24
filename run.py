from funs import *

# def main():
#     with open('in3.gcode', 'r') as f, open('out.gcode', 'w') as w_f:
#         data = f.read()
#         lines = data.split('\n')
#         wall_block = get_block_between(';TYPE:WALL-OUTER', ';TYPE:FILL', data)
#         infill_block = get_block_between(';TYPE:FILL', ';TIME_ELAPSED', data)

#         pisi = True
#         # print(wall_block[-1])
#         prev_xy = get_xy(wall_block[-1])


#         for line in lines:
#             if pisi:
#                 w_f.write(line + '\n')
#             if ';TYPE:FILL' in line:
#                 '''
#                     Nove vrednosti za e
#                 '''
#                 for line in infill_block:
#                     if 'E' in line and 'X' in line and 'Y' in line:
#                         ls = interpolate(prev_xy, get_xy(line), 6, e=get_e(line))
#                         for l in ls:
#                             w_f.write(l + '\n')
#                     elif 'X' in line or 'Y' in line:
#                         prev_xy = get_xy(line)
#                         w_f.write(line + '\n')
#                     else:
#                         w_f.write(line + '\n')

#                 pisi = False
#             if ';MESH:NONMESH' in line or ';TIME_ELAPSED' in line:
#                 w_f.write(line + '\n')
#                 pisi = True

def main():
    with open(input('Puno ime ulaznog: '), 'r') as f, open(input('Puno ime izlaznog: '), 'w') as w_f:
        data = f.read()
        lines = data.split('\n')
        wall_block = get_block_between(';TYPE:WALL-OUTER', ';TYPE:FILL', data)

        prev_xy = get_xy(wall_block[-1])


        '''
        Za svaku liniju u gcode ide, ako nije u fillu prepisuje je u novi file,
        ako jeste prvo proverava dal ima E, ako ima, racuna novo i vraca listu novih linija, namesta novo xy
        inace ako ima samo x y namest novo xy
        inace samo prepisuje liniju
        ako naidje na mesh:nonmesh ili time_elapsed znaci da nije vise u fillu
        '''
        fill = False
        for line in lines:
            if not fill:
                w_f.write(line + '\n')
            else :
                if 'E' in line and 'X' in line and 'Y' in line:
                    ls = interpolate(prev_xy, get_xy(line), 6, e=get_e(line))
                    for l in ls:
                        w_f.write(l + '\n')
                    prev_xy = get_xy(line)
                elif 'X' in line and 'Y' in line:
                    prev_xy = get_xy(line)
                    w_f.write(line + '\n')
                else:
                    w_f.write(line + '\n')
            if ';TYPE:FILL' in line:
                fill = True
            elif ';MESH:NONMESH' in line or ';TIME_ELAPSED' in line:
                fill = False


if __name__ == "__main__":
    main()
