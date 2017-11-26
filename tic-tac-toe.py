from tkinter import *

def checked(i) :
      global player
      button = list[i]
      
      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"
      

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"
      ifWin(i)
      
def ifWin(i):

      
      if (list[0]["text"]==list[1]["text"]==list[2]["text"]=="O"):
            msg=Message(window, text="winner: O")
            msg.grid(row=4,column=3)
            return
      if (list[3]["text"]==list[4]["text"]==list[5]["text"]=="O"):
            msg=Message(window, text="winner: O")
            msg.grid(row=4,column=3)
            return
      if (list[6]["text"]==list[7]["text"]==list[8]["text"]=="O"):
            msg=Message(window, text="winner: O")
            msg.grid(row=4,column=3)
            return
      if (list[0]["text"]==list[1]["text"]==list[2]["text"]=="X"):
            msg=Message(window, text="winner: X")
            msg.grid(row=4,column=3)
            return
      if (list[3]["text"]==list[4]["text"]==list[5]["text"]=="X"):
            msg=Message(window, text="winner: X")
            msg.grid(row=4,column=3)
            return
      if (list[6]["text"]==list[7]["text"]==list[8]["text"]=="X"):
            msg=Message(window, text="winner: X")
            msg.grid(row=4,column=3)
            return

window = Tk()
player = "X"

list= []
startmsg=Message(window, text="make horizon")
startmsg.grid(row=3,column=3)

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)


window.mainloop()
