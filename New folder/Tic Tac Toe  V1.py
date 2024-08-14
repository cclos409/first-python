#tic tac toe V1
#IMPORTANT when inputting moves into the console you MUST hit enter instead of pressing run in the top right, if you hit run instead it will list file location and the variables wont change
# eligible input commands are "x" to enter x into the current space "o" to enter o into the current space and "0" to not go on the selected space
tr=input("input top right ")
tm=input("input top middle ")
tl=input("input top left ")
mr=input("input middle right ")
mm=input("input center ")
ml=input("input middle left ")
br=input("input bottom right ")
bm=input("input bottom middle ")
bl=input("input bottom left ")

c='''
     1 | 2 | 3  
   ____|___|____
     4 | 5 | 6  
   ____|___|____
     7 | 8 | 9  
       |   |'''

if tr=="x":
    xctr=c
    c=xctr.replace("3","X")
if tm=="x":
    xctm=c
    c=xctm.replace("2","X")

if tl=="x":
    xctl=c
    c=xctl.replace("1","X")

if mr=="x":
    xcmr=c
    c=xcmr.replace("6","X")

if mm=="x":
    xcmm=c
    c=xcmm.replace("5","X")

if ml=="x":
    xcml=c
    c=xcml.replace("4","X")

if br=="x":
    xcbr=c
    c=xcbr.replace("9","X")
if bm=="x":
    xcbm=c
    c=xcbm.replace("8","X")

if bl=="x":
    xcbl=c
    c=xcbl.replace("7","X")

if tr=="o":
    octr=c
    c=octr.replace("3","O")
if tm=="o":
    octm=c
    c=octm.replace("2","O")

if tl=="o":
    octl=c
    c=octl.replace("1","O")

if mr=="o":
    ocmr=c
    c=ocmr.replace("6","O")

if mm=="o":
    ocmm=c
    c=ocmm.replace("5","O")

if ml=="o":
    ocml=c
    c=ocml.replace("4","O")

if br=="o":
    ocbr=c
    c=ocbr.replace("9","O")
if bm=="o":
    ocbm=c
    c=ocbm.replace("8","O")

if bl=="o":
    ocbl=c
    c=ocbl.replace("7","O")
print(c)

x= c.count("X")
print(x)
o= c.count("O")
print(o)

bottom=(c[74:83])
print(bottom,"bottom")
middle=(c[40:49])
print(middle,"mid")
top =(c[6:15])
print(top,"top")


topright =(c[14])
print(topright,"topright")

middleright =(c[48])
print(middleright,"middleright")

bottomright= (c[82])
print(bottomright,"bottomright")

topmiddle = (c[10])
print(topmiddle,"topmiddle")

middlemiddle = (c[44])
print (middlemiddle,"middlemiddle")

bottommiddle= (c[78])
print(bottommiddle,"bottommiddle")

topleft=(c[6])
print(topleft,"topleft")

middleleft=(c[40])
print(middleleft,"middleleft")

bottomleft=(c[74])
print(bottomleft,"bottomleft")

if bottomright is topright is middleright:
    print(bottomright,"'s WIN right column")
    print("do you want to play more? If so then set 'replay' to 'True'")
if middlemiddle is bottommiddle is topmiddle:
    print(middlemiddle,"'s WIN middle column")
    print("do you want to play more? If so then set 'replay' to 'True'")
if topleft is middleleft is bottomleft:
    print(topleft,"'s WIN left column")
    print("do you want to play more? If so then set 'replay' to 'True'")
if topleft is topmiddle is topright:
    print(topleft,"'s WIN top row")
    print("do you want to play more? If so then set 'replay' to 'True'")
if middleleft is middlemiddle is middleright:
    print (middleleft,"'s WIN middle row")
    print("do you want to play more? If so then set 'replay' to 'True'")
if bottomleft is bottommiddle is bottomright:
    print(bottomleft,"'s WIN bottom row")
    print("do you want to play more? If so then set 'replay' to 'True'")
if bottomright is middlemiddle is topleft:
    print(bottomright,"'s WIN top left diagonal")
    print("do you want to play more? If so then set 'replay' to 'True'")
if bottomleft is middlemiddle is topright:
    print(bottomleft,"'s WIN top right diagonal")
    print("do you want to play more? If so then set 'replay' to 'True'")
print (c)
