import threading
import time
import tkinter
import pyautogui
import sys

is_on = False
stop = False


def switch():
    global is_on

    if is_on:
        on_button.config(image=off)
        label.config(text="AutoLoL is disabled!", fg="red")
        is_on = False
        return

    on_button.config(image=on)
    label.config(text="AutoLoL is on", fg="green")
    is_on = True
    return


def waiting():
    while True:
        if not stop:
            if is_on:
                try:
                    time.sleep(0.5)

                    accept_button = pyautogui.locateOnScreen("img/accept.png", confidence=0.6)
                    emotes_button = pyautogui.locateOnScreen("img/emotes.png", confidence=0.8)
                    emotes_button1 = pyautogui.locateOnScreen("img/emote.png", confidence=0.8)

                    if emotes_button is not None:
                        print("emotes.png")
                        continue

                    if emotes_button1 is not None:
                        print("emote.png")
                        continue

                    if accept_button is not None:
                        print("accept.png")
                        pyautogui.click(pyautogui.center(accept_button))

                except:
                    pass

        else:
            sys.exit()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("AutoLoL")
    root.geometry("450x300")
    root.iconbitmap("img/lol_icon.ico")
    root.resizable(False, False)
    label = tkinter.Label(root, text="AutoLoL is disabled!", fg="red", font=("Courier", 20))
    label.pack(pady=20)
    on = tkinter.PhotoImage(file="img/on.png")
    off = tkinter.PhotoImage(file="img/off.png")
    on_button = tkinter.Button(root, image=off, bd=0, command=switch)
    on_button.pack(pady=50)

    t_waiting = threading.Thread(target=waiting)
    t_waiting.start()

    root.mainloop()
    stop = True
