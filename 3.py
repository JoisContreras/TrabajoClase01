def numeroperfecto_o_Noperfecto(num):
    suma = 0
    for i in range(1,num):
        if (num % i == 0):
            suma += i
    if num == suma:
        return True
    else:
        return False       
    
num = int(input("Digite un número: "))
 
if numeroperfecto_o_Noperfecto(num):
    print(f"El número {num} es perfecto")
else:
    print(f"El número {num} no es perfecto")