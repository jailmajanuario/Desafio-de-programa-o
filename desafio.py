#função para calcular a mediana
def mediana(lista):
    n = len(lista)
    lista.sort()
    if n % 2 == 0:
        mediana1 = lista[n//2]
        
        mediana2 = lista[n//2 - 1]
        mediana = (mediana1 + mediana2)/2
    else:
        mediana = lista[n//2]
    return mediana

#print(mediana([9,2,1,4,6]))



#questão2
#n=[1,5,3,4,2]
def elemetPares(n):
    y=2
    q=0
    n.sort(reverse = True)#função para ordenar a lista do maior para o menor
    for i in n:
        for x in n:
            nm= i-x
            if(nm == y ):
                 q= q+1
    return (q)
#print(elemetPares([1,5,3,4,2]))

s= "olá mundo"
s1= s.replace(" ", "")
tam= len(s1)
raiz= round(float(tam) ** 0.5)
list=[]
for k in s1:
    if( len(list) < raiz):
        #print(raiz)
        temp=[s1[:raiz]]
        #temp.append(k)
        list.append(temp)
        s1= s1[raiz:]  
for f in list:
    print(', '.join(f))
