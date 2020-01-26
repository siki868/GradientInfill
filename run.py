from funs import get_block_between, get_e, get_xy, interpolate
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory

master = Tk()



def choose_file(tf):
    global master
    master.filename = filedialog.askopenfilename(title="Biraj")
    tf.delete(0, END)
    tf.insert(0, master.filename)


def choose_folder(tf):
    global master
    master.directory = filedialog.askdirectory(title="Biraj")
    tf.delete(0, END)
    tf.insert(0, master.directory)

def make_gui():
    global master
    master.title("Infill")
    master.geometry("715x300")

    Label(master, text= "Ulazni gcd file:").grid(row= 0)
    tfInput = Entry(master, width= 60)
    tfInput.grid(row= 0, column= 1, pady= 4)

    Label(master, text= "Folder za izlazni file:").grid(row= 1)
    tfOutput = Entry(master, width= 60)
    tfOutput.grid(row= 1, column= 1, pady= 4)

    Label(master, text= "Naziv izlaznog file-a:").grid(row= 2)
    tfOutputName = Entry(master, width= 60)
    tfOutputName.grid(row= 2, column= 1, pady= 4)
    Label(master, text= "(npr izlaz.gcode)").grid(row= 2, column= 2)

    Button(master, text= "Otvori", command= lambda: choose_file(tfInput)).grid(row= 0, column= 2, sticky= W, pady= 4)
    Button(master, text= "Otvori", command= lambda: choose_folder(tfOutput)).grid(row= 1, column= 2, sticky= W, pady= 4)
    Button(master, text= "Napravi", command= lambda: main(tfInput.get(), tfOutput.get() + '/' + tfOutputName.get())).grid(row=3, column=0, sticky= W, pady=4)

def main(in_name, out_name):
    with open(in_name, 'r') as f, open(out_name, 'w') as w_f:
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
    make_gui()
    mainloop()
