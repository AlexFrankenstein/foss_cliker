import tkinter as tk
import pyautogui as pag
import time

def main():
    info_label = tk.Label(text="Running...", fg='#00FF00').place(relx=0.05, rely=0, width=50, height=30)
    pag.press('ctrlleft')
    root.after(100000, main)

def stop():
    # info_label_stop = tk.Label(text="Stopped...", fg='#FF0000').place(relx=0.05, rely=0, width=50, height=30)
    # time.sleep(1)
    tk._exit()

root = tk.Tk()
root.title("OS-Clicker")
root.geometry("250x70")
root.resizable(0, 0)
startBtn = tk.Button(text='Start', command=main).place(relx=0.05, rely=0.51, width=100, height=30)
stopBtn = tk.Button(text='Stop', command=stop).place(relx=0.55, rely=0.51, width=100, height=30)

root.mainloop()