def primo_o_Noprimo():
    cont=0
    num=int(input("Digite un número: "))
    for i in range(1,num+1):
        if(num % i==0):
            cont=cont+1
    if(cont!=2):
        print(f"El número {num} no es primo")
    else:
        print(f"El número {num} es primo")

def main():
    primo_o_Noprimo()

if __name__ == "__main__":
    main()        