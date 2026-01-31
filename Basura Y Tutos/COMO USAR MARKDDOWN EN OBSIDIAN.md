sss
# Header
asdasdasd
asdasdasdasd
#####
###### lol

#tag
*italics*
_italics_
**bold**
__bold__
normal

==highlight
asdasd==
==highlight==

Lists
"-"
- ## Uno
- 2
1. lol
	- sadasd
		- asd
			- da
			- asdad
			1. a
	1. si
	2. 
- 3
- 4
- 5 asdddddddddddddddddddddddddddddddddddddddddd asdasdasdsd
"+"
+ 1
+ 2
+ 2
+ 2
+ 2

"1. "
1. # loco ^c9ad1d
2. asd
3. asd

crtl+L:
- [ ] asdasdas
- [x] asdasdas
- [ ] asdasdasd
- [ ] dasdad


link: [[Antes/2024-2025/Cuatrimestre 2/Diseño y Análisis de Algoritmos/Índice DAA| Asi se le pone nombre al link]]

links en la misma pagina: [[COMO USAR MARKDDOWN EN OBSIDIAN#Header]]

# header 1.2
holaaa
## header2
hola 
### header3
- asd
- sad
- asd
asdasd


# 
sssss
# d
sss

links en la misma pagina: [[COMO USAR MARKDDOWN EN OBSIDIAN#^c9ad1d | : [COMO USAR MARKDDOWN EN OBSIDIAN > List > Loco]]

[youtuve](https://www.youtube.com/)

links embebidos:

![[COMO USAR MARKDDOWN EN OBSIDIAN#^c9ad1d ]]

anotaciones^[esto son anotaciones]

https://www.youtube.com/
otra^[esto tambien, se numeran solas]

holaa
<iframe src="https://pomofocus.io/"></iframe>

silencio



```python
def getBestItem(data, candidates):
    bestRatio = 0 #porque la voy a poder mejorar
    bestItem = 0 #tambien la vamos a optimizar
    for c in candidates:
        r = data["profit"][c] / data["weight"][c] #calculo el ratio
        if r > bestRatio:
            bestRatio = r
            bestItem = c
    return bestItem
def isFeashible(data, bestItem, freeWeight):
    return freeWeight - data["weight"][bestItem] > 0 #devuelve booleano es estrictamente mayor que cero, para que cuando llegue justo a 0, entre por el else  de if isFeashible
def greedyKnapSack(data):
    n = len(data["profit"]) #tamaño
    candidates = set()
    for i in range(n):
        candidates.add(i) #añade todos los candidatos
    sol = [0] * n #crea una solucion y la llena de ceros de momento
    freeWeight = data["maxWeight"] #peso maximo = peso libre, antes de meter ningun objeto
    isSol = False #esta la solucion completa?
    while not isSol and candidates: #mientras no tenga solucion, y haya candidatos
        bestItem = getBestItem(data,candidates) #funcion para conseguir el mejor de todos los candidatos (cogemos el mejor)
        candidates.remove(bestItem)
        if isFeashible(data,bestItem,freeWeight): #factible? me cabe el objeto entero?
            sol[bestItem] = 1.0 #meto el objeto entero 1.0 partes de 1 del objeto
            freeWeight -= data["weight"][bestItem]
        else: #si he llegado aqui es que el item perfecto no cabe en la mochila por lo que ya está llena y solo le cabe una fraccion del objeto perfecto, o puede ser que ya no te quede espacio y ningun item sea el perfecto
            sol[bestItem] = freeWeight/data["weight"][bestItem] #calcular cuantas partes de uno del objeto te caben, porque se puede partir
            isSol = True
    return sol
n = 5
data = {} #diccionario vacio que trataremos como un array pero en vez de un indice numerico, se usa un nombre.
data["profit"] = [20,30,66,40,60] #primer vector del array
data["weight"] = [10,20,30,40,50] #segundo
data["maxWeight"] = 100 #tercero
sol = greedyKnapSack(data)
print(sol)
#conjunto de candidatos: los n objetos
#funcion solucion: cuando no pueda añadirse más fracciones de objetos en la mochila(el objeto se puede partir)
#funcion de factibilidad:sumatorio de numero de objetos por su peso tiene que ser inferior al peso maximosoportado
#funcion solucion: optimizar el numero de objetos segun su valor
#como los objetos se pueden partir, el algoritmo voráz garantiza el recorrido optimo.
```

## Ejemplo de código con desplazamiento horizontal


<iframe src="https://onthegomap.com/#/create" style="border:0px #ffffff none;" name="myiFrame" scrolling="no" frameborder="1" marginheight="0px" marginwidth="0px" height="400px" width="600px" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/cUzklzVXJwo?si=Qov9QOk_7MA6K1m4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

![[Untitled Diagram 1.svg]]
<pre>
como los objetos se pueden partir, el algoritmo voráz garantiza el recorrido optimo que locura.
</pre>
```plantuml 
Bob -> Alice : hello
Alice -> Wonderland: hello
Wonderland -> next: hello
next -> Last: hello
Last -> next: hello
next -> Wonderland : hello
Wonderland -> Alice : hello
Alice -> Bob: hello
```

# 
![[VisualOrdenacióntopológicaDFS.html]]

[[MP_Tema_5_Patrones_de_diseño.pdf]]

![[COMO USAR MARKDDOWN EN OBSIDIAN 2025-09-18 15.31.25.excalidraw]]