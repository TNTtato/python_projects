import time
from datetime import time as t, datetime as d

current_hour = str(time.localtime().tm_hour)
current_minute = str(time.localtime().tm_min)
current_second = str(time.localtime().tm_sec)

format_h = "%H:%M:%S"
salida = d.strptime("19:00:00", format_h)
actual = d.strptime(f'{current_hour}:{current_minute}:{current_second}', format_h)
print("Time to go home!!") if actual >= salida else print(f'Aun queda {salida - actual} para salir')