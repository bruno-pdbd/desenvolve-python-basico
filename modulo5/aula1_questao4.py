from datetime import datetime
atual = datetime.now()
data = atual.strftime("%d/%m/%Y")
hora = atual.strftime("%H:%M")
print(f"Data: {data}")
print(f"Hora: {hora}")