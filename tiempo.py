from datetime import datetime

hora_actual = "18:31:00"
hora_salida = "19:00:00"

format_hora = "%H:%M:%S"

ha = datetime.strptime(hora_actual, format_hora)
hs = datetime.strptime(hora_salida, format_hora)

totalhoras = hs - ha

if hora_actual>hora_salida:
    print("ya puedes ir a tu casa")
else:
    print("Te hacen falta ", str(totalhoras), "para poder salir")
