fileoutput = False #Set this to true if you want the JSON file to be auto-generated. Does not work in online compilers/intrepreters.
linecolor = "#ffff0000" #Select the line color in hex
linewidth = 1 #Set the line 
#-------------------------------------------------
import json
class conversion:
    def userinput(): 
        global name_general
        input("Make sure there's no unnecessary text or line breaks in the coordinates (use a website to remove if unsure) \n Press enter to continue ")
        name_general = input("Name your drawing: ")
        separator = input("Are the coordinate pairs separated by spaces or dashes? \n |-- XXXXXN 0XXXXXE XXXXXN 0XXXXXE --| OR |-- XXXXXN 0XXXXXE - XXXXXN 0XXXXXE --|? ")
        n = int(input("How many layers? "))
        return(conversion.letters(separator, n))
    
    def letters(separator, n): #Removes letters and unnecessary spaces, formats it so there is one space between every coordinate.
        global names
        global sphere
        sphere = [0, 0] #N/S and W/E
        a=[]
        names=[]
        for i in range(n):
            b = input("Enter coordinates for layer " + str(i+1) + " :")
            name_layer = input("Enter name for layer " + str(i+1) + " :")
            names.append(name_layer)
            if "S" in b: #Checks if "S" is in the inputted coordinates. 
                sphere[0]=1
            if "W" in b:
                sphere[1]=1
            if separator=="spaces" or separator==" ":
                b=b.replace(" ","")
                b=b.replace("-", " ")
                b=b.replace("N", " ")
                b=b.replace("S", " ")
                b=b.replace("E", " ")
                b=b.replace("W", " ")
                koord=b.split()
                a.append(koord)
            elif separator=="dashes" or separator=="-":
                b=b.replace(" ","")
                b=b.replace("-", " ")
                b=b.replace("N", " ")
                b=b.replace("S", " ")
                b=b.replace("E", "")
                b=b.replace("W", "")
                koord=b.split()
                a.append(koord)
            else:
                print("Unknown separator!")
        return(a)
    
    def makefloat(a): #Makes every coordinate into float 
        n=0
        n1=0
        for el in a:
            for el1 in a[n1]:
                a[n1][n]=float(el1)
                n=n+1
            n=0
            n1=n1+1
        return(a)
    
    def dd(x): #DDMMSS -> DD(Decimal Degrees)
        n=0
        n1=0
        for el in x:
            for b in range(len(x[n1])):
                x[n1][n] = ((x[n1][n]/100 - x[n1][n]//100))*(5/3) + x[n1][n]//100 #DDM
                x[n1][n] = ((x[n1][n]/100 - x[n1][n]//100))*(5/3) + x[n1][n]//100 #DD
                n=n+1
            n=0
            n1=n1+1
        print(x) #debug
        return(x)
    
    def latlong(x): #lat long pairs separation
        pairs={}
        points=[]
        points1=[]
        for i in range(len(x)):
            cnt=0
            points=[]
            for y in range(int(len(x[i])/2)):
                pairs={}
                if sphere[0]==1: #checks if coordinates were in the S or W hemispheres, multiplies coordinate with -1 where needed.
                    pairs["latitude"]=-1*(x[i][cnt]) #southern hemisphere
                else:
                    pairs["latitude"]=x[i][cnt] #North
                if sphere[1]==1:
                    pairs["longitude"]=-1*(x[i][cnt+1]) #West
                else:
                    pairs["longitude"]=x[i][cnt+1] #East
                points.append(pairs)
                cnt=cnt+2
            points1.append(points)
        return(points1)
    
def fileoutput(content):
    if fileoutput:
        f = open(name_general+".json", "w")
        f.write(json.dumps(content, indent=4))
        f.close()
    return

def datatodrawing(content):
    drawings=[]
    for i in range(len(content)): #add layer data to every layer
        drawing = {
        "author": "",
        "brushStyle": 1,
        "color": linecolor,
        "colorBg": "#33ff0000",
        "lineWidth": linewidth,
        "name": names[i],
        "shared": False,
        "timestamp": "",
        "type": "line"
        }
        drawing["points"] = content[i]
        drawings.append(drawing)
    return drawings

def mainfile(drawings):
    main_data={ 
    "author": "me",
    "drawings": [],
    "enable": "true",
    "id": "",
    "name": name_general,
    "shared": False,
    "timestamp": "",
    "type": "layer",
    "version": "2.2.3.301"
    }
    main_data["drawings"]=drawings
    return main_data
#----------------------------------------
main_drawing=mainfile(datatodrawing(conversion.latlong(conversion.dd(conversion.makefloat(conversion.userinput())))))
fileoutput(main_drawing)
print(json.dumps(main_drawing, indent=4))
input("Save the text above as a .json file and open it as a drawing in lotatc") 
