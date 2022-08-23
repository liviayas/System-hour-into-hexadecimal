#Programa desenvolvido por Livia Amaral em 23/08/2022
#Projeto para converter código hexadecimal em hora, minuto e segundo

import tkinter
import customtkinter

window = tkinter.Tk()  # cria janela
window.geometry("400x240") # dimensiona altura e largura da janela
window.title("Conversão hexadecimal") # determina título da janela

# caixa de entrada de texto para  receber o código inserido pelo usuários
input_box = customtkinter.CTkEntry(master=window,
                               width=120,
                               height=25,
                               corner_radius=10)
input_box.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER) # posiciona a caixa na janela

#cria campo para mostrar o texto
label = customtkinter.CTkLabel(master=window,
                               text="O resultado vai aparecer aqui: ",
                               width=200,
                               height=25,
                               corner_radius=8,
                               text_color="grey")
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) # posiciona o campo na janela

# função executada no clique do botão
def button_calculate():
    try:
        input_value = input_box.get() # pega o valor inserido pelo usuário
        
        hexa_hora_inserida = input_value[:1] # pega apenas o valor referente a hora

        #matriz com os representantes em hexa das horas
        hour_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

        # for para encontrar o valor da hora em decimal
        indice = 0 
        for hora in hour_array:
            hora = hour_array[indice]
            if(hexa_hora_inserida.upper() == hora):
                hora_inserida = indice
                print(hora_inserida)
            indice = indice + 1

        #pega o valor em hexa dos minutos e segundos
        hexa_total_sec = input_value[1:]

        #tranforma hexadecimal em decimal
        decimal_total_sec = int(hexa_total_sec, 16)

        # divide o total de segundos por 60 para descobrir os minutos
        decimal_min = int(decimal_total_sec / 60)
        # pega o resto da divisão para ter os segundos
        decimal_sec = decimal_total_sec % 60

        # formata as variaveis (H:M:S)
        final_string = str(hora_inserida)+ ":" + str(decimal_min) + ":" + str(decimal_sec)

        # mostra o valor final na tela
        label.set_text(final_string)
    
    except:
        label.set_text("Código inválido")

# cria o botão para calcular
button = customtkinter.CTkButton(master=window, corner_radius=10, command=button_calculate, text="Calcular")
button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER) # posiciona o botão na janela

window.mainloop() # mantem a janela em execução