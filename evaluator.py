#This is like an easy calculator 
import tkinter as tk

class cal(object):
    def __init__(self,master):
      self.master=master
      master.title("Easy Calculator")
      self.number=0

      lb=tk.Label(master,text="Please type what you want to calculate here:")
      lb.pack(side=tk.LEFT)

      self.entry=tk.Entry(master,width=30)
      self.entry.pack(side=tk.LEFT)

      but=tk.Button(master,text="Evaluate",command=self.eva)
      but.pack(side=tk.LEFT)

      self.result=tk.Label(master,text="",bg="grey")
      self.result.pack(side=tk.LEFT,padx=50)

    def eva(self):
       try:
             self.num=eval(self.entry.get())
             self.result.config(text="{0}={1}".format(self.entry.get(),self.num),bg="grey")
       except Exception as e:
             self.result.config(text="Something went wrong {0}".format(e),bg="red")
         

root=tk.Tk()
calculator=cal(root)
root.mainloop()

              
              
      



