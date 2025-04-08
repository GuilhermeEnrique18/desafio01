horaInformado1 = int(input("Informe a primeira hora"))
minutoInformado1 = int(input("Informe o primeiro minuto"))
horaInformado2 = int(input("Informe a segunda hora"))
minutoInformado2 = int(input("Informe o segundo minuto"))
horaTotal = horaInformado1 + horaInformado2
minutoTotal = (minutoInformado1 + minutoInformado2)
#if minutoInformado1 > 59 or minutoInformado2 > 59:
#   print("minuto inválido, 1 hora vai até 60 minutos, digite até 60 seu imbecil")

if minutoTotal > 59:
    horaTotal += 1
    minutoTotal -= 60
if minutoTotal > 59:
    horaTotal += 1
    minutoTotal -= 60

if horaTotal > 12:
    horaTotal = horaTotal - 12

if horaTotal > 12:
    horaTotal = horaTotal - 12

print(f"são {horaTotal}:{minutoTotal}")