from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import re





master = Tk()
master.title("Infill")
master.geometry("800x350")

def dist(x1, y1, x2, y2, x3, y3): # calculate the diestance of a point to line with non-infinite length
    px = x2-x1
    py = y2-y1
    norm = px*px + py*py
    u =  ((x3 - x1) * px + (y3 - y1) * py) / float(norm)
    if u > 1:
        u = 1
    elif u < 0:
        u = 0
    x = x1 + u * px
    y = y1 + u * py
    dx = x - x3
    dy = y - y3
    dist = (dx*dx + dy*dy)**.5
    return dist

def getXY(currentLine): #Returns the X and Y value of the current line
    elementX = re.findall("[X]\d*\.*\d*",currentLine)[0][1:]
    elementY = re.findall("[Y]\d*\.*\d*",currentLine)[0][1:]
    return [float(elementX),float(elementY)]

def mapRange( a, b, s):
	(a1, a2), (b1, b2) = a, b
	return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

def promeni(gcodeFile='', outputFile='', maxFlow=350, minFlow=50, gradientDiscretization=4, gradientThickness=6, infillType=2):
    gcodeFile = open(gcodeFile, 'r')
    outputFile = open(outputFile, 'w+')
    currentSection = 0 # 0 = nothing, 1 = inner wall, 2 = infill
    lastPosition = [[-10000,-10000]]
    gradientDiscretizationLength = gradientThickness/gradientDiscretization
    for currentLine in gcodeFile:
        writtenToFile = 0
        if ";LAYER:" in currentLine:
            perimeterSegments = []
        #Look for the definition of the inner contour
        if ";TYPE:WALL-INNER" in currentLine:
            currentSection = 1
            #perimeterSegments = []
        #line with extrusion 
        if currentSection == 1 and "G1" in currentLine and " X" in currentLine and "Y" in currentLine and "E" in currentLine:
                perimeterSegments.append([getXY(currentLine), lastPosition[0]])
        #Inner wall definition end?
        if ";TYPE:WALL-OUTER" in currentLine:
            currentSection = 0
        #Infill segment
        if ";TYPE:FILL" in currentLine:
            currentSection = 2
            outputFile.write(currentLine)
            continue
        if currentSection == 2:
            if "F" in currentLine and "G1" in currentLine:
                outputFile.write("G1 F" + re.findall("[F]\d*\.*\d*",currentLine)[0][1:] + "\n")
            if "E" in currentLine and "G1" in currentLine and " X" in currentLine and "Y" in currentLine:
                currentPosition = getXY(currentLine)
                #linear infill
                if infillType == 2:
                    #find extrusion length
                    splitLine = currentLine.split(" ")
                    for element in splitLine:
                        if "E" in element:
                            extrusionLength = float(element[1:len(element)])
                    segmentLength = ((lastPosition[0][0]-currentPosition[0])**2+(lastPosition[0][1]-currentPosition[1])**2)**.5
                    segmentSteps = segmentLength / gradientDiscretizationLength
                    extrusionLengthPerSegment = extrusionLength / segmentSteps
                    segementDirection = [(currentPosition[0]-lastPosition[0][0])/segmentLength*gradientDiscretizationLength,(currentPosition[1]-lastPosition[0][1])/segmentLength*gradientDiscretizationLength]
                    if segmentSteps >= 2:
                        for step in range(int(segmentSteps)):
                            segmentEnd = [lastPosition[0][0] + segementDirection[0], lastPosition[0][1] + segementDirection[1]]
                            inbetweenPoint = [lastPosition[0][0] + (segmentEnd[0] - lastPosition[0][0])/2, lastPosition[0][1] + (segmentEnd[1] - lastPosition[0][1])/2]
                            #shortest distance from any inner perimeter
                            shortestDistance = 10000
                            for perimeterSegment in perimeterSegments:
                                distance = dist(perimeterSegment[0][0],perimeterSegment[0][1],perimeterSegment[1][0],perimeterSegment[1][1],inbetweenPoint[0], inbetweenPoint[1])
                                if distance < shortestDistance:
                                    shortestDistance = distance
                            if shortestDistance < gradientThickness:
                                outputFile.write("G1 X" + str(round(segmentEnd[0],3)) + " Y" + str(round(segmentEnd[1],3)) + " E" + str(round(extrusionLengthPerSegment * mapRange((0, gradientThickness), (maxFlow/100, minFlow/100), shortestDistance),5)) + "\n")
                            else:
                                outputFile.write("G1 X" + str(round(segmentEnd[0],3)) + " Y" + str(round(segmentEnd[1],3)) + " E" + str(round(extrusionLengthPerSegment * minFlow/100,5)) + "\n" )
                            lastPosition[0] = [segmentEnd[0],segmentEnd[1]]
                        #MissingSegment
                        segmentLengthRatio = ((lastPosition[0][0]-currentPosition[0])**2+(lastPosition[0][1]-currentPosition[1])**2)**.5 / segmentLength
                        # inbetweenPoint = [lastPosition[0][0] + (currentPosition[0] - lastPosition[0][0])/2, lastPosition[0][1] + (currentPosition[1] - lastPosition[0][1])/2]
                        outputFile.write("G1 X" + str(round(currentPosition[0],3)) + " Y" + str(round(currentPosition[1],3)) + " E" + str(round(segmentLengthRatio * extrusionLength * maxFlow/100,5)) + "\n")
                    else:
                        splitLine = currentLine.split(" ")
                        outPutLine = ""
                        for element in splitLine:
                            if "E" in element:
                                outPutLine = outPutLine + "E" + str(round(extrusionLength * maxFlow/100,5))
                            else:
                                outPutLine = outPutLine + element + " "
                        outPutLine = outPutLine + "\n"
                        outputFile.write(outPutLine)
                    writtenToFile = 1                    
                    
                #gyroid or honeycomb
                if infillType == 1:
                    inbetweenPoint = [lastPosition[0][0] + (currentPosition[0] - lastPosition[0][0])/2, lastPosition[0][1] + (currentPosition[1] - lastPosition[0][1])/2]
                    #shortest distance from any inner perimeter
                    shortestDistance = 10000
                    for perimeterSegment in perimeterSegments:
                        distance = dist(perimeterSegment[0][0],perimeterSegment[0][1],perimeterSegment[1][0],perimeterSegment[1][1],inbetweenPoint[0], inbetweenPoint[1])
                        if distance < shortestDistance:
                            shortestDistance = distance
                    newE = 0
                    outPutLine = ""
                    if shortestDistance < gradientThickness:
                        splitLine = currentLine.split(" ")
                        for element in splitLine:
                            if "E" in element:
                                newE = float(element[1:len(element)]) * mapRange((0, gradientThickness), (maxFlow/100, minFlow/100), shortestDistance)
                                outPutLine = outPutLine + "E" + str(round(newE,5))
                            else:
                                outPutLine = outPutLine + element + " "
                        outPutLine = outPutLine + "\n"
                        outputFile.write(outPutLine)
                        writtenToFile = 1
            if ";" in currentLine:
                currentSection = 0
                    
                
        #line with move
        if " X" in currentLine and " Y" in currentLine and ("G1" in currentLine or "G0" in currentLine):
            lastPosition[0] = getXY(currentLine)
        
        #write uneditedLine
        if writtenToFile == 0:
            outputFile.write(currentLine)
    gcodeFile.close()
    outputFile.close()

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

Label(master, text= "Max flow:").grid(row= 3)
tfMax = Entry(master, width= 60)
tfMax.grid(row= 3, column= 1, pady= 4)
Label(master, text= "(350 default)").grid(row= 3, column= 2)


Label(master, text= "Min flow:").grid(row= 4)
tfMin = Entry(master, width= 60)
tfMin.grid(row= 4, column= 1, pady= 4)
Label(master, text= "(50 default)").grid(row= 4, column= 2)


Label(master, text= "Diskretizacija:").grid(row= 5)
tfDiscr = Entry(master, width= 60)
tfDiscr.grid(row= 5, column= 1, pady= 4)
Label(master, text= "(4 dafault)").grid(row= 5, column= 2)


Label(master, text= "Debljina:").grid(row= 6)
tfThick = Entry(master, width= 60)
tfThick.grid(row= 6, column= 1, pady= 4)
Label(master, text= "(6 default)").grid(row= 6, column= 2)


Label(master, text= "Infill type:").grid(row= 7)
tfInfill = Entry(master, width= 60)
tfInfill.grid(row= 7, column= 1, pady= 4)
Label(master, text= "1 - gyroid, 2 - lines").grid(row= 7, column= 2)




Button(master, text= "Otvori", command= lambda: choose_file(tfInput)).grid(row= 0, column= 2, sticky= W, pady= 4)
Button(master, text= "Otvori", command= lambda: choose_folder(tfOutput)).grid(row= 1, column= 2, sticky= W, pady= 4)
Button(master, text= "Promeni", command= lambda: promeni(gcodeFile= tfInput.get(), outputFile= tfOutput.get() + '/' + tfOutputName.get(), maxFlow= int(tfMax.get()), minFlow=int(tfMin.get()), gradientDiscretization=int(tfDiscr.get()), gradientThickness=int(tfThick.get()), infillType=int(tfInfill.get()))).grid(row= 9, column= 0, sticky= W, pady= 4)
# Button(master, text= "Konvertuj i skini", command= skiniSve).grid(row= 2, column= 1, sticky= W, pady= 4)
# Button(master, text= "Dwnld dest", command= noviFolder).grid(row= 3, column= 0, sticky= W, pady= 4)


mainloop()

