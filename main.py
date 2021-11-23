import random
import tkinter

global userwidth
global rows
global brows
userwidth = 20
rows=[]
brows=[]

class Cell():
    value = 0
    visible = False

    def __str__(self): 
        return str(self.value)

    def __repr__(self):
        return str(self.value)

def CheckCell(x, y):
    if(rows[x][y].value == 0):
        for i in range(x-1,x+2):
            if userwidth>i>=0:
                for j in range(y-1,y+2):
                    if (userwidth>j>=0 and rows[i][j].visible!=True):
                        #print("About to check: " + str(i) + ", " + str(j))
                        #print(str(i) + ", " + str(j) + ":" + str(rows[i][j]))
                        brows[x][y].config(text="   "+str(rows[x][y].value)+"   ")
                        rows[x][y].visible=True
                        CheckCell(i,j)
    else:
        brows[x][y].config(text="   "+str(rows[x][y].value)+"   ")
        rows[x][y].visible=True
    
    

def GameStart():
    
    cell = Cell()
    for row in range(userwidth):
        col = []
        for c in range(userwidth):
            col.append(Cell())
        rows.append(col)        
    print(userwidth)
    n = random.randint(userwidth,userwidth*2)
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
    
    return rows

def CellLeftClicked(xy):
    
    print(str(xy[0]) + ", " + str(xy[1]) + ": " + str(rows[xy[0]][xy[1]]))
    #HERE!!
    
    if rows[xy[0]][xy[1]].value == 'B':
        for r in range(userwidth):
            for c in range(userwidth):
                if rows[r][c].value == 'B':
                    brows[r][c].config(text="   B   ")
                    rows[r][c].visible=True
                else:
                    brows[r][c].config(text="   " + str(rows[r][c].value) + "   ")
                    rows[r][c].visible=True 
                

    elif rows[xy[0]][xy[1]].value == 0:
        CheckCell(xy[0], xy[1])
    else:
        brows[xy[0]][xy[1]].config(text= "   " + str(rows[xy[0]][xy[1]].value) + "   ")
        rows[xy[0]][xy[1]].visible=True
        
def CellRightClicked(xy):
    if not rows[xy[0]][xy[1]].visible: 
        brows[xy[0]][xy[1]].config(text= "   !   ")

def GameReset(window):
    for row in range(userwidth):
        for col in range(userwidth):
            brows[row][col].destroy()
    GameStart()
    brows.clear()

    PlaceButtons(window)

def PlaceButtons(window):
    buttonsFrame=tkinter.Frame(window, width=(userwidth*30), height=(userwidth*30))
    buttonsFrame.pack(pady=5)
    for brow in range(userwidth):
        bcols = []
        for bcol in range(userwidth):
            #bcols.append(tkinter.Button(window,text=str(gameRows[brow][bcol].value), command=lambda xy=[brow, bcol]: CellClicked(xy)))
            #bcols.append(tkinter.Button(window,text= "       ", command=lambda xy=[brow, bcol]: CellLeftClicked(xy)))
            bcols.append(tkinter.Frame(buttonsFrame,background="red"))
            
            

        brows.append(bcols)
        for bcol in range(userwidth): 
            label = tkinter.Label(brows[brow][bcol], text= "   " + str(rows[brow][bcol]) + "   ")
            label.pack(padx=1, pady=1)
            brows[brow][bcol].grid(row=brow, column=bcol)
        #     brows[brow][bcol].grid(column=bcol, row= 0)

            #brows[brow][bcol].place(x=(100-(userwidth/2))+(brow*30), y=(200-(userwidth/2))+(bcol*25))
            # xy=[brow, bcol]
            # brows[brow][bcol].bind("<Button-1>", CellLeftClicked(xy))
            # brows[brow][bcol].bind("<Button-2>", CellRightClicked(xy))
            # brows[brow][bcol].bind("<Button-2>", CellRightClicked(xy))

def Window():
    GameStart()
    window = tkinter.Tk()
    window.geometry("800x775")
    window.maxsize(800, 775)
    # Code to add widgets will go here...
    
    resetb = tkinter.Button(window, text= "RESET", command=lambda : GameReset(window))
    resetb.pack()

    quitb = tkinter.Button(window, text= "QUIT", command=lambda : window.destroy())
    quitb.pack()
    
    #flagb = tkinter.Button(window, text= "FLAG", command=lambda : )

    PlaceButtons(window)

    # for brow in range(userwidth):
    #     print(brows[brow])
    #     for bcol in range(userwidth):
    window.mainloop()

Window()