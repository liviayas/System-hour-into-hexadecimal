# Código desenvolvido por Livia Amaral em 2022.
# Programa que gera um código hexadecimal com a Hora, minuto e segundo do sistem
# Exemplo de caso de uso: identificação de produto de acordo com a hora em que foi produzido

from datetime import date, datetime

now = datetime.now() #coleta a hora atual do sistema

hour = now.strftime("%H") # pega apenas o valor da hora
min = now.strftime("%M") # pega apenas o valor do minuto
sec = now.strftime("%S") # pega apenas o valor do segundo

print("hora: " , hour, "min: ",  min, "sec: ", sec) # imprime na tela a hora, o minuto e o segundo em ordem

# matriz para associar a hora com o seu valor em hexadecimal
hour_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

# atribui o valor hexa da hora em uma variavel
hexa_hour = hour_array[int(hour)]

print("hora em hexa: ", hexa_hour)  # imprime o valor hexadecimal da hora na tela

min_into_sec = int(min) * 60 # transforma minutos em segundos

total_sec = min_into_sec + int(sec) # soma os minutos transformados em segundos com os segundos

hexa_min_sec = hex(total_sec) # transforma o total de segundo em hexadecimal

print("min e sec em hexa: ", hexa_min_sec) # imprime o valor hexadecimal do total de segundos na tela

final_hexa = hexa_hour + hexa_min_sec # concatena os dois valores hexadecimal em uma variavel final

print("valor final: ", final_hexa) # imprime o valor final na tela

