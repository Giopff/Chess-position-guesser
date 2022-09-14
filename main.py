import tkinter as tk
import random as r
class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=32, color1="white", color2="Black"):

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)


        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row=0, column=0):
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


global count
count=0
def main():
    import time
    start = time.time()

    while True:
        root = tk.Tk()
        board = GameBoard(root)
        board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        player1 = tk.PhotoImage(file="./pawn (2).png")
        ROWZ = r.randrange(0,8)
        COLUMNZ = r.randrange(0,8)
        CHARZ = 'ABCDEFGH'
        canvas1 = tk.Canvas(root, width = 200, height = 150)
        canvas1.pack()

        entry1 = tk.Entry (root) 
        canvas1.create_window(100, 70, window=entry1)
        # print(CHARZ[COLUMNZ])
        # print(8-ROWZ)
        def getAnswer ():  
            global count
            answer = entry1.get()
            try:
                if answer[0]==CHARZ[COLUMNZ] and int(answer[1])==(8-ROWZ):
                    label1 = tk.Label(root, text= str("sagol"))
                    count+=1

                    canvas1.update()
                    root.destroy()
                else:
                    label1 = tk.Label(root, text= str("arasworia"))
                    root.destroy()
            except:
                pass
                
            try:
                canvas1.create_window(100, 115, window=label1)
            except:
                pass

        button1 = tk.Button(text='Get the Square Root', command=getAnswer)
        canvas1.create_window(100, 90, window=button1)
        board.addpiece("player1", player1, ROWZ,COLUMNZ)
        root.mainloop()

        if time.time()-start>=10:
            break
    print(count)
    
    


if __name__ == "__main__":
    main()