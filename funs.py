import re
import math
from shapely.geometry import LineString, MultiPoint



def get_block_between(start, end, data):
    '''
    Vraca block texta izmedju start i enda (sad ga samo koristimo za WALL-OUTER da bi znali poslednje xy)
    '''
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
    '''
    Vraca X, Y iz linije
    '''
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
    '''
    Vraca E iz linije
    '''
    return float(re.findall(r'[E](\d*\.\d*)', line)[0])



def interpolate(p1, p2, nb_steps, e):
    '''
    p1, p2 - tacke u obliku (x, y) gde masina crtna liniju od p1 do p2
    nb_steps - na koliko delova se deli linija
    e - kolicina filamenta na toj liniji

    Vraca listu linija oblika ['G1 F600 Xnesto Ynesto Enesto', 'G1 F600 Xnesto2 Ynesto2 Enesto2'] - ret 
        koje se upisuju umesto trenutne linije

    Prvo pravimo liniju od tacaka, nalazimo njenu duzinum, ako je dobra duzina delimo je na tacke. 
        (pointi u Splitteru)
    
    Onda racunamo E u odnosu na staro tako da imamo njegove segmente -> 
        ako je br segmenata 6 a E je 3 -> znaci da ce segmenat od e biti 3 / (6/2) tj 1
    
    Po ovome ce es da bude [3, 2, 1], sto je polovina linije, i za drugu polovinu ocemo obrnuto tj 
        1 2 3 tako da es postaje [3, 2, 1, 1, 2 ,3]   
    '''
    ret = []

    # Segmentacija linije (sve tacke osim prve)
    line = LineString([p1, p2])
    segment_length = line.length/nb_steps

    if segment_length > 5.0:
        splitter = MultiPoint([line.interpolate((i/nb_steps), normalized=True) for i in range(1, nb_steps+1)])

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
