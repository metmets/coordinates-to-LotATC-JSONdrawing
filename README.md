This code converts takes in coordinates of a drawing (in XXXXXXN/S XXXXXXXW/E etc) and converts it into a LotAtc drawing. This code supports multiple layers in one drawing - for drawing different sectors in an airspace.

Simply find the things you want to draw (usually from an AIP), example: 414217N 0450126E - 414340N 0450353E - 413901N 0452757E - 413756N 0452930E - 413701N 0453109E - 413622N 0453301E - 413535N 0454349E - 412122N 0454200E - then along the state border - 412804N 0451543E - 
413110N 0451526E - 414217N 0450126E.
Remove any text ("then along the state border") and any line breaks (there are websites that do that).
Run the code and follow the instructions from there. 

# Coordinates to LotATC drawing
This code takes in coordinates of a drawing (in DDMMSSN/S DDDMMSSW/E etc) and converts it into a LotAtc drawing. This code supports multiple layers in one drawing - useful for drawing different sectors in an airspace.

# How to run?
**If you are familiar with running python scripts then you can skip this part.** 
If you don't have python installed on your computer, you can use an online interpreter, [such as this one](https://www.online-python.com/). Simply copy the code from [Coordinates_to_JSON_for_LOTATC.py](https://github.com/metmets/coordinates-to-LotATC-JSONdrawing/blob/main/Coordinates_to_JSON_for_LOTATC.py), paste it into the interpreter and run it.
# How to use?
## Coordinate preparation

 Find the airspace you want to draw. In this example I will use Batumi TMA. ![enter image description here](https://raw.githubusercontent.com/metmets/coordinates-to-LotATC-JSONdrawing/main/img/Screenshot%202023-01-09%20221336.png)

The TMA is made up of three parts - the main part, and two sectors. So in total we have three layers to our drawing. First of all **remove all text  and line breaks from the coordinates**.
So now we have: 

**BATUMI TMA**:

420819N 0410250E - 415659N 0414755E - 413128N 0415756E - 413100N 0413255E - 413600N 0411655E - 414151N 0405843E - 420426N 0405703E - 420819N 0410250E
**BATUMI TMA SECTOR 1**:

414544N 0415223E-413128N 0415756E - 413100N 0413255E - 413240N 0414245E - 414544N 0415223E
**BATUMI TMA SECTOR 2**:

420819N 0410250E 415659N 0414755E 414544N 0415223E 413240N 0414245E 413100N 0413255E 413600N 0411655E 414151N 0405843E 420426N 0405703E 420819N 0410250E
## Running the code

