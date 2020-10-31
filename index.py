def validaAlfabeto(alfabeto):
    for letra in alfabeto:
        if (letra != "A" and letra!="B" and letra!="C" ):
            return "Os caracteres informados não são permitidos, check o alfabeto!"
    return "Processando"

def CriaLSystem(numIteracoes, axiom,regras):
    inicioString = axiom[0]
    finalString = ""
    for i in range(numIteracoes):
        finalString = procString(inicioString,regras)
        inicioString = finalString
    return finalString

def procString(oldStr,regras):
    novaString = ""
    for ch in oldStr:
        novaString = novaString + AplicaRegra(ch,regras)

    return novaString

def montaRegras(regras):
    reg = []
    for i in regras:
        reg.append(i.split("=")[1])
    return reg

def AplicaRegra(caracter, regras):
    novaString = ""

    if caracter == 'A':
        novaString = regras[0]   # Regra 1
    elif caracter == 'B':
        novaString = regras[1]
    elif caracter == 'C':
        novaString = regras[2]   # Regra 2
    else:
        novaString = caracter   
    return novaString

def desenhaLsystem(painel, desenhar, stringInstr, angulo, comprimento):
    svg = '<svg height="1600" width="1600">'
    coordX = 600
    coordY = 1200
    dirVetorial = 'R' # Right (R) / Left (L) / Up (U) / Down (D)

    for cmd in stringInstr:
        if cmd == 'F':
            svg = svg + "\n" + createLineSVG(coordX, coordY, dirVetorial, comprimento)
            coordX = updateCoord(coordX, dirVetorial, True, comprimento)
            coordY = updateCoord(coordY, dirVetorial, False, comprimento)    
        elif cmd == '+':
            dirVetorial = anguloVetorial(dirVetorial, 'R')
        elif cmd == '-':
            dirVetorial = anguloVetorial(dirVetorial, 'L')
        elif cmd == 'A':
            svg = svg + "\n" + createLineSVG(coordX, coordY, dirVetorial, comprimento)
            coordX = updateCoord(coordX, dirVetorial, True, comprimento)
            coordY = updateCoord(coordY, dirVetorial, True, comprimento)    
        elif cmd == 'B':
            svg = svg + "\n" + createLineSVG(coordX, coordY, dirVetorial, comprimento)
            coordX = updateCoord(coordX, dirVetorial, False, comprimento)
            coordY = updateCoord(coordY, dirVetorial, False, comprimento)    
        elif cmd == 'C':
            svg = svg + "\n" + createLineSVG(coordX, coordY, dirVetorial, comprimento)
            coordX = updateCoord(coordX, dirVetorial, False, comprimento)
            coordY = updateCoord(coordY, dirVetorial, True, comprimento)    

    svg = svg + '</svg>'
    return svg

def updateCoord(coord, char, x, comp):
    if x:
        if char == 'R':
            return (coord + comp)        
        elif char == 'L':
            return (coord - comp)    
        else:
            return coord    
    else:
        if char == 'U':
            return (coord - comp)     
        elif char == 'D':
            return (coord + comp)
        else:
            return coord

def anguloVetorial(char, sentido):
    if sentido == 'R':
        if char == 'R':
            return 'D'
        elif char == 'D':
            return 'L'
        elif char == 'L':
            return 'U'
        elif char == 'U':
            return 'R'
    else:
        if char == 'R':
            return 'U'
        elif char == 'U':
            return 'L'
        elif char == 'L':
            return 'D'
        elif char == 'D':
            return 'R'

def createLineSVG(x: int, y: int, dir, compr: int):
    if dir == 'R':
       return ('<line x1="{}" y1="{}" x2="{}" y2="{}"; style="stroke:rgb(0,0,0);stroke-width:2"/>').format(x, y, (x + compr), y)
    elif dir == 'L':
       return ('<line x1="{}" y1="{}" x2="{}" y2="{}"; style="stroke:rgb(0,0,0);stroke-width:2"/>').format(x, y, (x - compr), y)
    elif dir == 'U':
       return ('<line x1="{}" y1="{}" x2="{}" y2="{}"; style="stroke:rgb(0,0,0);stroke-width:2"/>').format(x, y, x, (y - compr))
    elif dir == 'D':
       return ('<line x1="{}" y1="{}" x2="{}" y2="{}"; style="stroke:rgb(0,0,0);stroke-width:2"/>').format(x, y, x, (y + compr))

def main():

    gramatica = open('gramatica.txt','r')
    cont = 1
    axioma = ""
    regras = ""
    alfabeto = ""
    angulo = 90

    for line in gramatica:
        if cont == 1:
            axioma = (line.split(":")[1]).lstrip().rsplit()
        if cont == 2:
            regras = ((line.split(":")[1]).split(","))
        if cont == 3:
            alfabeto =((line.split(":")[1]).split(","))
        if cont == 4:
            angulo = line.lstrip().rsplit()
        cont+=1
    #Valida se os caracteres pertence ao alfabeto
    print(validaAlfabeto(alfabeto))


    finalString = CriaLSystem(100, axioma,montaRegras(regras)) #cria a string para desenho
    
    print(finalString)
    t = 0
    svgArq = desenhaLsystem(t, True, finalString, angulo, 100)     

    arquivo = open("L-System.html","w", encoding="utf-8")
    arquivo.write(svgArq)
    gramatica.close()
    arquivo.close()

    print('Arquivo Constriuido')
main()