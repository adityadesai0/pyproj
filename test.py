from tkinter import *
import os



version = "0.0.1"
print("VERSION: ",version)
os_name = os.name
print("OS NAME: ",os_name)
curr_working_dir = os.getcwd()
print("CURRENT WORKING DIRECTORY: ",curr_working_dir)

infoFile_create = open("info", "w+")
infoFile_create.close()
infoFile_a = open("info", "a")
infoFile_a.write(version)
infoFile_a.write(os_name)
infoFile_a.write(curr_working_dir)


a = "a"
b = "b"
c = "c"
d = "d"
e = "e"

def date_selector():
    return 0


def movie_write(x):
    #sec_main_screen.destroy()
    ticketWrite = open("ticket.txt", "w+")
    ticketWrite.close()
    ticketWrite_2 = open("ticket.txt", "w")
    if x == "a":
        ticketWrite_2.write("Movie1\n")
        mov()
    elif x == "b":
        ticketWrite_2.write("Movie2\n")
        mov()
    elif x == "c":
        ticketWrite_2.write("Movie3\n")
        mov()
    elif x == "d":
        ticketWrite_2.write("Movie4\n")
        mov()
    elif x == "e":
        ticketWrite_2.write("Movie5\n")
        mov()

    ticketWrite_2.close()




def seatWrite(w):
    ticketWrite = open("ticket.txt", "a")
    if w == "a1":
        ticketWrite.write("Seat: A1\n")
    elif w == "a2":
        ticketWrite.write("Seat: A1\n")
    elif w == "a3":
        ticketWrite.write("Seat: A1\n")
    elif w == "a4":
        ticketWrite.write("Seat: A1\n")
    elif w == "a5":
        ticketWrite.write("Seat: A1\n")
    elif w == "b1":
        ticketWrite.write("Seat: A1\n")
    elif w == "b2":
        ticketWrite.write("Seat: A1\n")
    elif w == "b3":
        ticketWrite.write("Seat: A1\n")
    elif w == "b4":
        ticketWrite.write("Seat: A1\n")
    elif w == "b5":
        ticketWrite.write("Seat: A1\n")
    ticketWrite.close()
    date_selector()


a1 = "a1"
a2 = "a2"
a3 = "a3"
a4 = "a4"
a5 = "a5"
b1 = "b1"
b2 = "b2"
b3 = "b3"
b4 = "b4"
b5 = "b5"

def mov():
    mov_1 = Tk()
    mov_1.title("Seat Selector - Movie Booking")
    mov_1.geometry("500x450")
    Label(mov_1, text = "Movie 1", bg = "#e63232", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(mov_1, text = "").pack()
    Label(mov_1, text = "Select your seat:", width = "300", height="2", font = ("Calibri", 13)).pack()
    
    button_frame = Frame()
    button_frame.pack(fill=X, side=LEFT)

    button_frame_2 = Frame()
    button_frame_2.pack(fill=X, side=RIGHT)

    Button(button_frame, text="A1", height="2", width="10", command = seatWrite(a1)).pack()
    button_frame.columnconfigure(0, weight=1)
    Button(button_frame, text="A2", height="2", width="10", command = seatWrite(a2)).pack()
    button_frame.columnconfigure(1, weight=1)
    Button(button_frame, text="A3", height="2", width="10", command = seatWrite(a3)).pack()
    button_frame.columnconfigure(2, weight=1)
    Button(button_frame, text="A4", height="2", width="10", command = seatWrite(a4)).pack()
    button_frame.columnconfigure(3, weight=1)
    Button(button_frame, text="A5", height="2", width="10", command = seatWrite(a5)).pack()
    button_frame.columnconfigure(4, weight=1)

    Button(button_frame_2, text="B1", height="2", width="10", command = seatWrite(b1)).pack()
    button_frame.columnconfigure(0, weight=1)
    Button(button_frame_2, text="B2", height="2", width="10", command = seatWrite(b2)).pack()
    button_frame.columnconfigure(1, weight=1)
    Button(button_frame_2, text="B3", height="2", width="10", command = seatWrite(b3)).pack()
    button_frame.columnconfigure(2, weight=1)
    Button(button_frame_2, text="B4", height="2", width="10", command = seatWrite(b4)).pack()
    button_frame.columnconfigure(3, weight=1)
    Button(button_frame_2, text="B5", height="2", width="10", command = seatWrite(b5)).pack()
    button_frame.columnconfigure(4, weight=1)

    mov_1.mainloop()




def second_main_screen():
    #global sec_main_screen
    sec_main_screen = Tk()
    sec_main_screen.title("Home - Movie Booking")
    sec_main_screen.geometry("500x450")
    Label(sec_main_screen, text="Welcome!", bg="#e63232", width="300", height="2", font=("Calibri", 13)).pack()
    Label(sec_main_screen, text="").pack()
    Label(sec_main_screen, text="Select a Movie to continue:", width="300", height="2", font=("Calibri", 13)).pack()
    
    Button(text="Movie 1", height="2", width="20").pack()
    Label(sec_main_screen, text="").pack()
    
    Button(text="Movie 2", height="2", width="20").pack()
    Label(sec_main_screen, text="").pack()
    
    Button(text="Movie 3", height="2", width="20").pack()
    Label(sec_main_screen, text="").pack()
    
    Button(text="Movie 4", height="2", width="20").pack()
    Label(sec_main_screen, text="").pack()
    
    Button(text="Movie 5", height="2", width="20").pack()

    sec_main_screen.mainloop()


    
#second_main_screen()
mov()
