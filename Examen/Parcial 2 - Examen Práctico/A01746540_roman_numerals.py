# Edgar Alexis González Amador - A1746540

def ConvertIntToRoman(num):
    dic = ['I','V','X','L','C','D','M']
    offset = 4-len(num)
    rom = ''
    for i in range(4-offset):
        dig = int(num[(-i)-1])
        if (dig < 4):
            rom = (dig * (dic[(i * 2)])) + rom
        elif(dig == 4):
            rom = (dic[(i * 2)]) + (dic[(i*2)+1]) + rom
        elif(dig == 5):
            rom = (dic[(i*2)+1]) + rom
        elif (dig > 5 and dig < 9):
            rom = (dic[(i * 2) + 1]) + ((dig-5) * (dic[(i * 2)])) + rom
        elif (dig == 9):
            rom = (dic[(i * 2)]) + (dic[(i*2)+2]) + rom
    return rom

while (True):
    print("Introduce el número que deseas convertir a número romano")
    num = input()
    if(int(num) < 4000):
        rom = ConvertIntToRoman(num)
        print("Conversión de Entero a Romano:")
        print("Num: " + num + " -> " + rom)
    else:
        print("- Para fines de este programa debes ingresar un numero menor a 4000\n- REINICIANDO ...\n")