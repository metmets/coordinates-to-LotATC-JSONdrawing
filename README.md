# Coordinates to LotATC drawing
This code takes in coordinates (in DDMMSSN/S DDDMMSSW/E etc) and converts it into a [LotAtc](https://www.lotatc.com/) drawing. This code supports multiple layers in one drawing - useful for drawing different sectors in an airspace.

Currently the code only creates lines (no polygons, circles etc).

Disclaimer: I'm very new to programming, so the fact that this code even runs is a feat itself.

# How to run?
**If you are familiar with running python scripts then you can skip this part.** 

If you don't have python installed on your computer, you can use an online interpreter, [such as this one](https://www.online-python.com/). Simply copy the code from [Coordinates_to_JSON_for_LOTATC.py](https://github.com/metmets/coordinates-to-LotATC-JSONdrawing/blob/main/Coordinates_to_JSON_for_LOTATC.py), paste it into the interpreter and run it.
# How to use?
tl;dr:
1.	Find the coordinates of the layers
2.	Remove any unnecessary text (keep N/S and W/E at the end of a coordinate) and line breaks
3.	Run the code and follow the instructions
4.	Save the output as a .json file and open it in LotATC
## Coordinate preparation
Currently the code works with coordinates in DDMMSS N/S DDDMMSS W/E format. Coordinate pairs can either be separated by spaces or dashes.

Find the airspace you want to draw. In this example I will use Batumi TMA. ![enter image description here](https://raw.githubusercontent.com/metmets/coordinates-to-LotATC-JSONdrawing/main/img/Screenshot%202023-01-09%20221336.png)

Note that in BATUMI TMA SEC2 the coordinate pairs are separated by spaces, so we'll need to add the dashes between the pairs.

The TMA is made up of three parts - the main part, and two sectors. So in total we have three layers to our drawing. First of all **remove all text  and line breaks from the coordinates**.
So now we have: 

**BATUMI TMA**:

420819N 0410250E - 415659N 0414755E - 413128N 0415756E - 413100N 0413255E - 413600N 0411655E - 414151N 0405843E - 420426N 0405703E - 420819N 0410250E

**BATUMI TMA SECTOR 1**:

414544N 0415223E-413128N 0415756E - 413100N 0413255E - 413240N 0414245E - 414544N 0415223E

**BATUMI TMA SECTOR 2**:

420819N 0410250E - 415659N 0414755E - 414544N 0415223E - 413240N 0414245E - 413100N 0413255E - 413600N 0411655E - 414151N 0405843E - 420426N 0405703E - 420819N 0410250E
## Running the code
Before running you can set the line color and width at the start of the code. Also if you are running this on your computer (not online) you can set *fileoutput = True*, that way the program will output the drawing JSON file. 

First of all enter the name for the whole drawing and enter whether the coordinate pairs are separated by spaces or dashes (entering either "-" or "dashes" works, same with spaces)

![enter image description here](https://raw.githubusercontent.com/metmets/coordinates-to-LotATC-JSONdrawing/main/img/1.gif)
 
 Now just follow the instructions. For every layer it will ask you it's coordinates and name. Do that with every layer and it should output the JSON data

![enter image description here](https://github.com/metmets/coordinates-to-LotATC-JSONdrawing/blob/main/img/2.gif)

Once you have the data, just open a notepad file, paste it there and save it as a .json file. 

Now just open the .json file in LotATC as a drawing.
![enter image description here](https://github.com/metmets/coordinates-to-LotATC-JSONdrawing/blob/main/img/3.gif?raw=true)

And that's it. 

# Limitations
Currently the coordinates in the drawing cannot cross the equator nor the prime meridian. As there aren't any dcs maps that cross them I don't see this as a big issue.
