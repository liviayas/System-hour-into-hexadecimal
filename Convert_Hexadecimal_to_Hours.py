# Code developed by Livia Amaral in august 2022
# The porpouse is to recieve an hexadecimal iput and return the Hour, minute and second associated to it

import tkinter
import customtkinter

window = tkinter.Tk()  # creates the window
window.geometry("400x240") # set window's dimensions
window.title("Conversão hexadecimal") # set window's title

# input box to receive the hexa code
input_box = customtkinter.CTkEntry(master=window,
                               width=120,
                               height=25,
                               corner_radius=10)
input_box.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER) # positioning the input box

# label to show the result
label = customtkinter.CTkLabel(master=window,
                               text="the result will appear here: ",
                               width=200,
                               height=25,
                               corner_radius=8,
                               text_color="grey")
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def button_calculate():
    try:
        input_value = input_box.get() # get the input value
        
        hexa_hora_inserida = input_value[:1] # get only the value which represents the hour

        # array of hour's hexadecimal values
        hour_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

        # for to find the hour of the hexa code inserted
        indice = 0 
        for hora in hour_array:
            hora = hour_array[indice]
            if(hexa_hora_inserida.upper() == hora):
                hora_inserida = indice
                print(hora_inserida)
            indice = indice + 1

        # gets the total second's hexadecimal value
        hexa_total_sec = input_value[1:]

        # transform the hexa in decimal
        decimal_total_sec = int(hexa_total_sec, 16)

        # get the minutes
        decimal_min = int(decimal_total_sec / 60)
        # the rest represents the seconds
        decimal_sec = decimal_total_sec % 60

        # fomates the variable (H:M:S)
        final_string = str(hora_inserida)+ ":" + str(decimal_min) + ":" + str(decimal_sec)

        # shows it
        label.set_text(final_string)
    
    except:
        label.set_text("Código inválido")

# creates the button to calculate
button = customtkinter.CTkButton(master=window, corner_radius=10, command=button_calculate, text="Calculate")
button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER) # posicioning the button

window.mainloop() # keeps the window in loop