def main():
    lista = ["Rojo","Amarillo","Verde","Naranja","Azul"]
    print("lista:", lista)

    lista.pop(1)
    print("con pop(1):", lista)

    lista.remove("Rojo")
    print("con remove(´Rojo´):", lista)

    #max sum min
    numbers = [1,2,3,4,5,6,7,8,9,10,11]
    resultmax = max(numbers)
    print(resultmax)
    resultmin = min(numbers)
    print(resultmin)
    resultsum = sum(numbers)
    print(resultsum)



if __name__ == "__main__":
    main()
