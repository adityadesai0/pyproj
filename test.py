from tkinter import *
import os



version = "0.0.1"
print("VERSION: ",version)
os_name = os.name
print("OS NAME: ",os_name)
curr_working_dir = os.getcwd()
print("CURRENT WORKING DIRECTORY: ",curr_working_dir)


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

def mov1_call():
    sec_main_screen.destroy()
    mov_1()


def mov2_call():
    sec_main_screen.destroy()
    mov_2()


def mov3_call():
    sec_main_screen.destroy()
    mov_3()


def mov4_call():
    sec_main_screen.destroy()
    mov_4()


def mov5_call():
    sec_main_screen.destroy()
    mov_5()



def seat_a1():
    global seatNo
    seatNo = "a1"

def seat_a2():
    global seatNo
    seatNo = "a2"

def seat_a3():
    global seatNo
    seatNo = "a3"

def seat_a4():
    global seatNo
    seatNo = "a4"

def seat_a5():
    global seatNo
    seatNo = "a5"

def seat_b1():
    global seatNo
    seatNo = "b1"

def seat_b2():
    global seatNo
    seatNo = "b2"

def seat_b3():
    global seatNo
    seatNo = "b3"

def seat_b4():
    global seatNo
    seatNo = "b4"

def seat_b5():
    global seatNo
    seatNo = "b5"


def date_save():
    global date_info
    date_info = Date.get()

def date_select():
    dSel = Tk()
    dSel.title("Select Date")
    dSel.geometry("500x200")
    Label(dSel, text = "Date Select", bg = "#e63232", width = "100", height = "2", font = ("Calibri", 13)).pack()
    Label(dSel, text = "").pack()
    Label(dSel, text = "Type Date (MMDDYYYY) :", width = "100", height = "1", font = ("Calibri", 13)).pack()

    Label(dSel, text = "").pack()
    global Date
    Date = StringVar()
    global date_entry
    date_entry = Entry(dSel, textvariable = Date).pack()

    Label(dSel, text = "").pack()
    
    Button(dSel, text = "Submit", width = 10, height = 1, bg = "white", command = date_save).pack()

    

def mov_1():
    mov_1 = Tk()
    mov_1.title("Movie 1 - Seat Selector - Movie Booking")
    mov_1.geometry("500x450")
    Label(mov_1, text = "Movie 1", bg = "#e63232", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(mov_1, text = "").pack()
    Label(mov_1, text = "Select your seat:", width = "300", height="2", font = ("Calibri", 13)).pack()
    
    button_frame = Frame()
    button_frame.pack(fill=X, side=LEFT)

    button_frame_2 = Frame()
    button_frame_2.pack(fill=X, side=RIGHT)

    Button(button_frame, text="A1", height="2", width="10", command = seat_a1).pack()
    #button_frame.columnconfigure(0, weight=1)
    Button(button_frame, text="A2", height="2", width="10", command = seat_a2).pack()
    #button_frame.columnconfigure(1, weight=1)
    Button(button_frame, text="A3", height="2", width="10", command = seat_a3).pack()
    #button_frame.columnconfigure(2, weight=1)
    Button(button_frame, text="A4", height="2", width="10", command = seat_a4).pack()
    #button_frame.columnconfigure(3, weight=1)
    Button(button_frame, text="A5", height="2", width="10", command = seat_a5).pack()
    #button_frame.columnconfigure(4, weight=1)

    Button(button_frame_2, text="B1", height="2", width="10", command = seat_b1).pack()
    #button_frame.columnconfigure(0, weight=1)
    Button(button_frame_2, text="B2", height="2", width="10", command = seat_b2).pack()
    #button_frame.columnconfigure(1, weight=1)
    Button(button_frame_2, text="B3", height="2", width="10", command = seat_b3).pack()
    #button_frame.columnconfigure(2, weight=1)
    Button(button_frame_2, text="B4", height="2", width="10", command = seat_b4).pack()
    #button_frame.columnconfigure(3, weight=1)
    Button(button_frame_2, text="B5", height="2", width="10", command = seat_b5).pack()
    #button_frame.columnconfigure(4, weight=1)




def mov_2():
    mov_2 = Tk()
    mov_2.title("Movie 2 - Seat Selector - Movie Booking")
    mov_2.geometry("500x450")
    Label(mov_2, text = "Movie 2", bg = "#e63232", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(mov_2, text = "").pack()
    Label(mov_2, text = "Select your seat:", width = "300", height="2", font = ("Calibri", 13)).pack()
    
    button_frame = Frame()
    button_frame.pack(fill=X, side=LEFT)

    button_frame_2 = Frame()
    button_frame_2.pack(fill=X, side=RIGHT)

    Button(button_frame, text="A1", height="2", width="10", command = seat_a1).pack()
    Button(button_frame, text="A2", height="2", width="10", command = seat_a2).pack()
    Button(button_frame, text="A3", height="2", width="10", command = seat_a3).pack()
    Button(button_frame, text="A4", height="2", width="10", command = seat_a4).pack()
    Button(button_frame, text="A5", height="2", width="10", command = seat_a5).pack()


    Button(button_frame_2, text="B1", height="2", width="10", command = seat_b1).pack()
    Button(button_frame_2, text="B2", height="2", width="10", command = seat_b2).pack()
    Button(button_frame_2, text="B3", height="2", width="10", command = seat_b3).pack()
    Button(button_frame_2, text="B4", height="2", width="10", command = seat_b4).pack()
    Button(button_frame_2, text="B5", height="2", width="10", command = seat_b5).pack()


def mov_3():
    mov_3 = Tk()
    mov_3.title("Movie 3 - Seat Selector - Movie Booking")
    mov_3.geometry("500x450")
    Label(mov_3, text = "Movie 3", bg = "#e63232", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(mov_3, text = "").pack()
    Label(mov_3, text = "Select your seat:", width = "300", height="2", font = ("Calibri", 13)).pack()
    
    button_frame = Frame()
    button_frame.pack(fill=X, side=LEFT)

    button_frame_2 = Frame()
    button_frame_2.pack(fill=X, side=RIGHT)

    Button(button_frame, text="A1", height="2", width="10", command = seat_a1).pack()
    Button(button_frame, text="A2", height="2", width="10", command = seat_a1).pack()
    Button(button_frame, text="A3", height="2", width="10", command = seat_a1).pack()
    Button(button_frame, text="A4", height="2", width="10", command = seat_a1).pack()
    Button(button_frame, text="A5", height="2", width="10", command = seat_a1).pack()


    Button(button_frame_2, text="B1", height="2", width="10", command = seat_b1).pack()
    Button(button_frame_2, text="B2", height="2", width="10", command = seat_b1).pack()
    Button(button_frame_2, text="B3", height="2", width="10", command = seat_b1).pack()
    Button(button_frame_2, text="B4", height="2", width="10", command = seat_b1).pack()
    Button(button_frame_2, text="B5", height="2", width="10", command = seat_b1).pack()




def mov_4():
    mov_4 = Tk()
    mov_4.title("Movie 4 - Seat Selector - Movie Booking")
    mov_4.geometry("500x450")
    Label(mov_4, text = "Movie 4", bg = "#e63232", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(mov_4, text = "").pack()
    Label(mov_4, text = "Select your seat:", width = "300", height="2", font = ("Calibri", 13)).pack()
    
    button_frame = Frame()
    button_frame.pack(fill=X, side=LEFT)

    button_frame_2 = Frame()
    button_frame_2.pack(fill=X, side=RIGHT)

    Button(button_frame, text="A1", height="2", width="10", command = seat_a1).pack()
    Button(button_frame, text="A2", height="2", width="10", command = seat_a1).pack()
    Button(button_frame, text="A3", height="2", width="10", command = seat_a1).pack()
    Button(button_frame, text="A4", height="2", width="10", command = seat_a1).pack()
    Button(button_frame, text="A5", height="2", width="10", command = seat_a1).pack()


    Button(button_frame_2, text="B1", height="2", width="10", command = seat_b1).pack()
    Button(button_frame_2, text="B2", height="2", width="10", command = seat_b1).pack()
    Button(button_frame_2, text="B3", height="2", width="10", command = seat_b1).pack()
    Button(button_frame_2, text="B4", height="2", width="10", command = seat_b1).pack()
    Button(button_frame_2, text="B5", height="2", width="10", command = seat_b1).pack()



def mov_5():
    mov_5 = Tk()
    mov_5.title("Movie 5 - Seat Selector - Movie Booking")
    mov_5.geometry("500x450")
    Label(mov_5, text = "Movie 5", bg = "#e63232", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(mov_5, text = "").pack()
    Label(mov_5, text = "Select your seat:", width = "300", height="2", font = ("Calibri", 13)).pack()
    
    button_frame = Frame()
    button_frame.pack(fill=X, side=LEFT)

    button_frame_2 = Frame()
    button_frame_2.pack(fill=X, side=RIGHT)

    Button(button_frame, text="A1", height="2", width="10", command = seat_a1).pack()
    Button(button_frame, text="A2", height="2", width="10", command = seat_a2).pack()
    Button(button_frame, text="A3", height="2", width="10", command = seat_a3).pack()
    Button(button_frame, text="A4", height="2", width="10", command = seat_a4).pack()
    Button(button_frame, text="A5", height="2", width="10", command = seat_a5).pack()


    Button(button_frame_2, text="B1", height="2", width="10", command = seat_b1).pack()
    Button(button_frame_2, text="B2", height="2", width="10", command = seat_b2).pack()
    Button(button_frame_2, text="B3", height="2", width="10", command = seat_b3).pack()
    Button(button_frame_2, text="B4", height="2", width="10", command = seat_b4).pack()
    Button(button_frame_2, text="B5", height="2", width="10", command = seat_b5).pack()



    
def second_main_screen():
    global sec_main_screen
    sec_main_screen = Tk()
    sec_main_screen.title("Home - Movie Booking")
    sec_main_screen.geometry("500x450")
    Label(sec_main_screen, text="Welcome!", bg="#e63232", width="300", height="2", font=("Calibri", 13)).pack()
    Label(sec_main_screen, text="").pack()
    Label(sec_main_screen, text="Select a Movie to continue:", width="300", height="2", font=("Calibri", 13)).pack()
    
    Button(text="Movie 1", height="2", width="20", command = mov1_call).pack()
    Label(sec_main_screen, text="").pack()
    
    Button(text="Movie 2", height="2", width="20", command = mov2_call).pack()
    Label(sec_main_screen, text="").pack()
    
    Button(text="Movie 3", height="2", width="20", command = mov3_call).pack()
    Label(sec_main_screen, text="").pack()
    
    Button(text="Movie 4", height="2", width="20", command = mov4_call).pack()
    Label(sec_main_screen, text="").pack()
    
    Button(text="Movie 5", height="2", width="20", command = mov5_call).pack()

    sec_main_screen.mainloop()


    
#second_main_screen()


date_select()
