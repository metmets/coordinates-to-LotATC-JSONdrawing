import json
class teisendus:
    def dd(x):
        n=0
        n1=0
        for el in x:
            for b in range(len(x[n1])):
                x[n1][n] = ((x[n1][n]/100 - x[n1][n]//100))*(5/3) + x[n1][n]//100 #DDM
                x[n1][n] = ((x[n1][n]/100 - x[n1][n]//100))*(5/3) + x[n1][n]//100 #DD
                n=n+1
            n=0
            n1=n1+1
        return(x)
    def viimane(x):
        paarid={}
        points=[]
        points1=[]
        for i in range(len(x)):
            cnt=0
            for y in range(int(len(x[i])/2)):
                paarid={}
                paarid["latitude"]=x[i][cnt]
                paarid["longitude"]=x[i][cnt+1]
                points.append(paarid)
                cnt=cnt+2
            points1.append(points)
        return(points1)
        
a=[]
separator = input("Are the coordinate pairs separated by spaces or dashes? \n XXXXXN 0XXXXXE XXXXXN 0XXXXXE OR XXXXXN 0XXXXXE - XXXXXN 0XXXXXE? ")
n = int(input("How many layers? "))
names=[]
name_general=input("Name your drawing: ")
for i in range(n):
    b = input("Enter coordinates for layer " + str(i+1) + " :")
    name_layer = input("Enter name for layer " + str(i+1) + " :")
    names.append(name_layer)
    if separator=="spaces" or separator==" ":
        b=b.replace(" ","")
        b=b.replace("-", " ")
        b=b.replace("N", " ")
        b=b.replace("E", " ")
        koord=b.split()
        a.append(koord)
    elif separator=="dashes" or separator=="-":
        b=b.replace(" ","")
        b=b.replace("-", " ")
        b=b.replace("N", " ")
        b=b.replace("E", "")
        koord=b.split()
        a.append(koord)
    else:
        print("Unknown separator!")
        
n=0
n1=0
b=[]
for el in a:
    for el1 in a[n1]:
        a[n1][n]=float(el1)
        n=n+1
    n=0
    n1=n1+1
tase1=teisendus.viimane(teisendus.dd(a))
peamine={
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
drawings1=[]
for i in range(len(tase1)):
    drawing = {
    "author": "",
    "brushStyle": 1,
    "color": "#ffff0000", #EDIT THIS FOR LINE COLOUR
    "colorBg": "#33ff0000",
    "lineWidth": 1,
    "name": names[i],
    "shared": False,
    "timestamp": "",
    "type": "line"
    }
    drawing["points"] = tase1[i]
    drawings1.append(drawing)
peamine["drawings"]=drawings1
print(json.dumps(peamine, indent=4))
input("Save the text above as a .json file and open it as a drawing in lotatc")