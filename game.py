"""This is like a small app that the users can use it to draw by pressing the
   directional button."""
import tkinter as tk

class Screen(tk.Canvas):
    size=250
    radius=5
    path=10

    def __init__(self,parent):
        super().__init__(parent,bg="light blue",width=self.size,height=self.size)
        self._x,self._y=(self.size/2,self.size/2)
        self._path=[(self._x,self._y)]
        self._redraw()

    def _redraw(self):
        self.delete(tk.ALL)
        coords=(self._x-self.radius,
                self._y-self.radius,
                self._x+self.radius,
                self._y+self.radius)
        self.create_rectangle(coords,fill="black",width=0)
        if len(self._path)>1:
          self.create_line(self._path)
          
    def _move(self,dx,dy):
        self._x +=dx
        self._y +=dy
        self._path.append((self._x,self._y))
        self._redraw()

    def moveup(self):
        self._move(0,-self.path)

    def movedown(self):
        self._move(0,self.path)

    def moveright(self):
        self._move(self.path,0)

    def moveleft(self):
        self._move(-self.path,0)
    
class Controls(tk.Frame):
    BT_wildth=10
    def __init__(self,parent,screen):
      super().__init__(parent)
      up=tk.Button(self,text="up",width=self.BT_wildth,command=screen.moveup)
      up.pack(side=tk.TOP)
      left=tk.Button(self,text="left",width=self.BT_wildth,command=screen.moveleft)
      left.pack(side=tk.LEFT)
      down=tk.Button(self,text="down",width=self.BT_wildth,command=screen.movedown)
      down.pack(side=tk.LEFT)
      right=tk.Button(self,text="right",width=self.BT_wildth,command=screen.moveright)
      right.pack(side=tk.LEFT)
    
class game1(object):
    def __init__(self,master):
      master.title("Game")
      screen=Screen(master)
      con=Controls(master,screen)
      con.pack(side=tk.BOTTOM)
      screen.pack(side=tk.BOTTOM,expand=True,fill=tk.BOTH)


root=tk.Tk()
g=game1(root)
root.mainloop()


