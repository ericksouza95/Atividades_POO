a = int(input())
b = int(input())
c = int(input())
if (a < b):
    if (c > b or c < a):
        if (c > b):
            print(" parte superior do intervalo")
        elif (c < a):
            print ("parte inferior do intervalo")
    else:
        print (" dentro do intervalo")
else:
    print ("intervalo malfeito, reinicia ai fazendo o a sendo menor que o b")