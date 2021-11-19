import random
import tkinter

userwidth = 20
rows = []
brows = []

class Cell():
    value = 0
    visible = False

    def __str__(self): 
        return str(self.value)

    def __repr__(self):
        return str(self.value)

def CheckCell(x, y):
    if(rows[x][y].value == 0):
        for i in range(-1,2):
            for j in range(-1,2):
                if((rows[i][j].visible!=True) and (rows[i][j].value==0)):
                    CheckCell(i,j)
    else:
        brows[x][y].config(text="   "+str(rows[x][y].value)+"   ")
        rows[x][y].visible=True
    
    

def GameStart(userwidth):
    
    cell = Cell()
    for row in range(userwidth):
        col = []
        for c in range(userwidth):
            col.append(Cell())
        rows.append(col)        
    print(userwidth)
    n = random.randint(userwidth^2//5,userwidth^2//3)

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

def CellClicked(xy,userwidth):
    
    print(str(rows[xy[0]][xy[1]]))
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
        


def Window(userwidth):
    gameRows = GameStart(userwidth)
    window = tkinter.Tk()
    window.geometry("800x775")
    window.maxsize(800, 775)
    # Code to add widgets will go here...
    
    for brow in range(userwidth):
        bcols = []
        for bcol in range(userwidth):
            bcols.append(tkinter.Button(window,text=str(gameRows[brow][bcol].value), command=lambda xy=[brow, bcol]: CellClicked(xy)))
            #bcols.append(tkinter.Button(window,text= "       ", command=lambda xy=[brow, bcol]: CellClicked(xy, userwidth)))

        brows.append(bcols)
        for bcol in range(userwidth):   
            brows[brow][bcol].place(x=(100-(userwidth/2))+(brow*30), y=(200-(userwidth/2))+(bcol*25))

    # for brow in range(userwidth):
    #     print(brows[brow])
    #     for bcol in range(userwidth):
    window.mainloop()

Window(userwidth)