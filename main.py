import random
import tkinter

userwidth =15
rows = []
brows = []
flag = False

window = tkinter.Tk()
window.geometry("800x775")
window.maxsize(800, 775)
window.title("Minesweeper")
class Cell():
    value = 0
    visible = False
    flagged = False

    def __str__(self): 
        return str(self.value)

    def __repr__(self):
        return str(self.value)

def CheckCell(x, y):
    if(rows[x][y].value == 0):
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                print("About to check: " + str(i) + ", " + str(j))
                if(((0<=i<userwidth) and (0<=j<userwidth) and rows[i][j].visible!=True)):
                    print(str(i) + ", " + str(j) + ":" + str(rows[i][j]))
                    brows[x][y].config(text="   "+str(rows[x][y].value)+"   ")
                    rows[x][y].visible=True
                    CheckCell(i,j)
    else:
        brows[x][y].config(text="   "+str(rows[x][y].value)+"   ")
        rows[x][y].visible=True
    
    

def GameStart(window, userwidth):
    global rows
    global brows
    global flag

    brows= []
    flag = False
    
    MapInit(userwidth)

    print(userwidth)
    for brow in range(userwidth):
        bcols = []
        for bcol in range(userwidth):

            #bcols.append(tkinter.Button(window,text=str(gameRows[brow][bcol].value), command=lambda xy=[brow, bcol]: CellClicked(xy)))
            bcols.append(tkinter.Button(window,text= "       ", bg = "white", command=lambda xy=[brow, bcol]: ClickSwitch(xy)))
            #bcols.append(tkinter.Frame(window,width=30, height=25, background="gray"))
            
        brows.append(bcols)

        for bcol in range(userwidth):  
            brows[brow][bcol].place(x=(100-(userwidth/2))+(brow*30), y=(200-(userwidth/2))+(bcol*25))
            # xy=[brow, bcol]
            # brows[brow][bcol].bind("<Button-1>", CellLeftClicked(xy))
            # brows[brow][bcol].bind("<Button-2>", CellFlagClicked(xy))
            # brows[brow][bcol].bind("<Button-2>", CellFlagClicked(xy))


def CellLeftClicked(xy):
    
    print(str(xy[0]) + ", " + str(xy[1]) + ": " + str(rows[xy[0]][xy[1]]))
    #HERE!!
    
    if rows[xy[0]][xy[1]].flagged:
        return 0

    if rows[xy[0]][xy[1]].value == 'B':
        for r in range(userwidth):
            for c in range(userwidth):
                if rows[r][c].value == 'B':
                    if rows[r][c].flagged:
                        brows[r][c].config(text="  ! B  ", bg= "red")
                        rows[r][c].visible=True
                    else:
                        brows[r][c].config(text="   B   ", bg= "red")
                        rows[r][c].visible=True
                else:
                    brows[r][c].config(text="   " + str(rows[r][c].value) + "   ", bg = "white")
                    rows[r][c].visible=True
    elif rows[xy[0]][xy[1]].value == 0:
        CheckCell(xy[0], xy[1])
    else:
        brows[xy[0]][xy[1]].config(text= "   " + str(rows[xy[0]][xy[1]].value) + "   ")
        rows[xy[0]][xy[1]].visible=True

        
def CellFlagClicked(xy):
    if not rows[xy[0]][xy[1]].visible :
        if rows[xy[0]][xy[1]].flagged == False:
            brows[xy[0]][xy[1]].config(text= "   !   ", bg= "red")
            rows[xy[0]][xy[1]].flagged = True

        else:
            brows[xy[0]][xy[1]].config(text= "       ", bg = "white")
            rows[xy[0]][xy[1]].flagged = False

def ClickSwitch(xy):
    if flag:
        CellFlagClicked(xy)
    else:
        CellLeftClicked(xy)

def Fswitch(fbutton):
    global flag
    flag = not flag
    if flag:
        fbutton.config(bg = "red")
    else:
        fbutton.config(bg = "white")    

def ResetGame(window,userwidth):
    global brows
    global rows
    MapInit(userwidth)
    for brow in range(userwidth):
        for bcol in range(userwidth):
            brows[brow][bcol].config(text = '       ', bg= "white")

def MapInit(userwidth):
    global rows
    rows = []

    cell = Cell()
    for row in range(userwidth):
        col = []
        for c in range(userwidth):
            col.append(Cell())
        rows.append(col)        
    print(userwidth)
    n = random.randint((userwidth**2)//10,(userwidth**2)//7)
    print("Bombs: " + str(n))
    for b in range(n):
        flag = True
        while(flag):
            l = random.randint(0,userwidth-1)
            c = random.randint(0,userwidth-1)
            if rows[l][c].value != 'B':
                rows[l][c].value = 'B'
                for lm in range(-1,2):
                    for cm in range(-1,2):
                        if ((l + lm) in range(userwidth)) and ((c +cm) in range(userwidth)):
                            if rows[l + lm][c + cm].value != 'B':
                                rows[l + lm][c + cm].value += 1

                flag = False
    for r in rows:
        print(str(r))

def Window(userwidth):
    global window

    # Code to add widgets will go here...
    fbutton = tkinter.Button(window,text= "Flag", bg = "white", command=lambda :Fswitch(fbutton))
    rbutton = tkinter.Button(window,text= "Reset", bg = "white", command=lambda :ResetGame(window,userwidth))
    GameStart(window, userwidth)
    fbutton.place(x=90,y=150)
    rbutton.place(x=650,y=150)
    # for brow in range(userwidth):
    #     print(brows[brow])
    #     for bcol in range(userwidth):
    window.mainloop()

Window(userwidth)