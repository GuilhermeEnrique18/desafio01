#entradas
horaInformado1 = int(input("Informe a primeira hora"))
minutoInformado1 = int(input("Informe o primeiro minuto"))
horaInformado2 = int(input("Informe a segunda hora"))
minutoInformado2 = int(input("Informe o segundo minuto"))

horaTotal = horaInformado1 + horaInformado2
minutoTotal = (minutoInformado1 + minutoInformado2)

if minutoTotal >= 60:
    horaTotal += 1
    minutoTotal -= 60
#minutoTotal = 0

#if horaTotal > 24:

if horaInformado1 > 24 or horaInformado2 > 24:
    print("horário inválido, digite até 24 horas")
elif minutoInformado1 > 60 or minutoInformado2 > 60:
    print("minuto inválido, 1 hora vai até 60 minutos, digite até 60")
elif horaTotal >12:
    horaTotal = horaTotal - 12
#    print(f"são {horaTotal}:{minutoTotal}")

if horaTotal >12:
    horaTotal = horaTotal - 12
    print(f"são {horaTotal}:{minutoTotal}")