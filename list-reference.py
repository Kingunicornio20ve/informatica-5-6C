def main():
    lista = ["Rojo","Amarillo","Verde","Naranja","Azul"]
    print("lista:", lista)

    lista.pop(1)
    print("con pop(1):", lista)

    lista.remove("Rojo")
    print("con remove("Rojo"):", lista)

    #green team
    #max sum min
    numbers = [1,2,3,4,5,6,7,8,9,10,11]
    resultmax = max(numbers)
    print(resultmax)
    resultmin = min(numbers)
    print(resultmin)
    resultsum = sum(numbers)
    print(resultsum)

    #green team
    mylist = ["pencil","computer","shirt","phone","paper"]
    print(len(mylist))

    #blue team
    numbers = [1,4,5,7,9,3]
    numbers.sort()
    print(numbers)

    items = ["lettuce","tomato","bread","jam","mayonaise"]
    letters.sort(reserve=true)
    print(letters)

    words = ["banana","pie","apple"]
    sorted_words = sorted(words,key=len)
    print




if __name__ == "__main__":
    main()
