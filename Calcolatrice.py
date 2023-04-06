import math
import os

print("Calcolatrice\n")
operators = ("!","_", "v","^","%","/",":","*","x","-","+","<",">","=") #questo definisce le operazioni possibili e il loro ordine di esecuzione
previousResult = 0
precision = 2
verbose = False

def throwError(index, value = None):
    match index:
        case 0: print("Espressione non valida:", value, "non è un operatore valido\n")
        case 1: print("Espressione non valida: operatore", value, "necessita di 2 fattori\n")
        case 2: print("Espressione non valida: p può essere preceduto e seguito solo da operatori\n")
        case 3: print("Espressione non valida: l'operatore fattoriale (!) può essere usato solo con numeri interi positivi\n")
        case 4: print("Espressione non valida: il simbolo logico" + value + "non può stare all'interno di una parentesi\n")
        case 5: print("Espressione non valida: le parentesi non possono essere vuote\n")
        case 6: print("Espressione non valida: una parentesi è stata aperta ma non chiusa\n")
        case 7: print("Espressione non valida: una parentesi è stata chiusa ma non aperta\n")
        case 8: print("Espressione non valida: la sintassi per l'operatore fattoriale (!) è come segue: numero!\n")
        case 9: print("Comando errato: risoluzione - accettati solo interi positivi\n")
        case 10: print("Comando errato: help - l'argomento", value, "non esiste\n")
        case 11: print("Espressione non valida: l'operatore logico", value, "necessita di 2 numeri\n")
    return True

def help(topic):
    module = "%"
    match topic:
        case 0:
            print("\nOperatori aritmetici:\n +     addizione\n -     sottrazione\n * x   moltiplicazione\n / :   divisione")
            print(" " + module + "     resto della divisione\n ^     elevamento a potenza\n v _   radicale\n !     fattoriale")
            print("\nOperatori logici:\n ()    parentesi\n =     uguaglianza\n <     minore\n >     maggiore")
            print("\nParole chiave:\n help         visualizza una guida per l'uso, se viene seguito da uno degli elementi elencati sopra visualizzerà istruzioni specifiche su di esso")
            print(" p            richiama il risultato dell'operazione precendente (0 se non c'è stata alcuna operazione)")
            print(" passaggi     abilita e disabilita la visualizzazione delle operazioni intermedie oltre al risultato")
            print(" risoluzione   seguito da un numero intero positivo, serve per indicare il numero di cifre decimali da visualizzare (2 di default)")
            print(" cancella     cancella tutto ciò che è stato scritto in precedenza\n")
        case 1:
            print("\nAddizione:")
            print("Rappresentata dal simbolo +, necessita di 2 operandi detti addendi e il risultato è detto somma.\n")
            print(" addendo 1 + addendo 2 = somma\n")
        case 2:
            print("\nSottrazione:")
            print("Rappresentata dal simbolo -, necessita di 2 operandi detti rispettivamente minuendo e sottraendo, il risultato è detto differenza.\n")
            print(" minuendo - sottraendo = differenza\n")
        case 3:
            print("\nMoltiplicazione:")
            print("Rappresentata dal simbolo * o x, necessita di 2 fattori detti rispettivamente moltiplicando e moltiplicatore, il risultato è detto prodotto.\n")
            print(" moltiplicando * moltiplicatore = prodotto\n moltiplicando x moltiplicatore = prodotto\n")
        case 4:
            print("\nDivisione:")
            print("Rappresentata dal simbolo / o :, necessita di 2 fattori detti rispettivamente dividendo e divisore (o numeratore e denominatore, se viene rappresentata come frazione), il risultato è detto quoziente.\n")
            print(" dividendo / divisore = quoziente\n dividendo : divisore = quoziente\n")
        case 5:
            print("\nResto della divisione:")
            print("Rappresentato dal simbolo %, necessita di 2 fattori detti rispettivamente dividendo e divisore, il risultato è detto resto.\n")
            print(" dividendo", module, "divisore = resto\n")
        case 6:
            print("\nElevamento a potenza:")
            print("Rappresentato dal simbolo ^, necessita di 2 fattori detti rispettivamente base ed esponente, il risultato è detto potenza.\n")
            print(" base ^ esponente = potenza\n")
        case 7:
            print("\nRadicale:")
            print("Rappresentato dai simboli _ e v, necessita di 2 fattori detti rispettivamente radicando ed indice, il risultato è detto radice.\n")
            print(" indice _ radicando = radice\n indice v radicando = radice")
        case 8:
            print("\nFattoriale:")
            print("Rappresentato dal simbolo !, necessita solo di un fattore che deve essere un intero positivo, il risultato è detto fattoriale.\n")
            print(" numero! = fattoriale\n")
        case 9:
            print("\nParentesi:")
            print("Rappresentate dai simboli ( e ), servono a specificare l'ordine delle operazioni.")
            print("Racchiudi in una parentesi l'operazione che va eseguita prima del resto, può contenere altre parentesi.\n")
        case 10:
            print("\nUguaglianza:")
            print("Rappresentata dal simbolo =, compara il valore alla sua destra con quello alla sua sinistra, il risultato sarà Vero se sono uguali o Falso altrimenti.\n")
        case 11:
            print("\nMinore:")
            print("Rappresentato dal simbolo <, compara il numero alla sua destra con quello alla sua sinistra, il risultato sarà Vero se il numero a sinistra è minore di quello a destra o Falso altrimenti.\n")
        case 12:
            print("\nMaggiore:")
            print("Rappresentato dal simbolo >, compara il numero alla sua destra con quello alla sua sinistra, il risultato sarà Vero se il numero a sinistra è Maggiore di quello a destra o Falso altrimenti.\n")

while True:
    error = False
    string = input()
    string = string.strip()

    if string.lower() == "help":  #se viene digitato il comando help
        help(0)
        error = True
    elif string[0:string.find(" ")] == "help":  #se viene digitato il comando help con specifica dell'argomento
        string = string[string.find(" "):len(string)].strip().lower()
        match string:
            case "addizione" | "somma" | "+": help(1)
            case "sottrazione" | "differenza" | "-": help(2)
            case "moltiplicazione" | "prodotto" | "*" | "x": help(3)
            case "divisione" | "quoziente" | "/" | ":": help(4)
            case "resto della divisione" | "resto" | "%": help(5)
            case "elevamento a potenza" | "potenza" | "^": help(6)
            case "radicale" | "radice" | "_" | "v": help(7)
            case "fattoriale" | "!": help(8)
            case "parentesi" | "(" | ")" | "()": help(9)
            case "uguaglianza" | "uguale" | "=": help(10)
            case "minore" | "<": help(11)
            case "maggiore" | ">": help(12)
            case _: throwError(10, string)
        error = True
    elif string.lower() == "passaggi":  #se viene digitato il comando passaggi
        match verbose:
            case True:
                verbose = False
                print("\nVisualizzazione dei passaggi intermedi disattivata\n")
            case False:
                verbose = True
                print("\nVisualizzazione dei passaggi intermedi attivata\n")
        error = True
    elif string.lower() == "risoluzione":
        print("\nRisoluzione attuale:", precision, "cifre decimali\n")
        error = True
    elif string[0:string.find(" ")] == "risoluzione": #se viene digitato il comando precisione
        string = string[string.find(" "):len(string)].strip().lower()
        if string.isdigit() and float(string) % 1 == 0 and float(string) > 0:
            precision = int(string)
            print("\nRisoluzione modificata a", precision, "cifre decimali\n")
            print("\n%.*f" % (precision, previousResult), "\n")
            error = True
        else: error = throwError(9)
    elif string.lower() == "cancella":
        os.system('cls||clear')
        print("Calcolatrice\n")
        error = True

    brackets = True #se ci sono parentesi
    if error == False:
        while brackets: #ripete finche sono presenti parentesi
            tempString = string
            nOpenBrackets = 0
            nClosedBrackets = 0
            while True: #legge la stringa per isolare le parentesi
                start = tempString.find("(")
                end = tempString.find(")")
                if start > -1 and end > -1: #è presente una parentesi valida (aperta e chiusa)
                    tempString1 = tempString[start:end + 1]
                    while tempString1.find("(") > -1: #isola la parentesi più interna
                        bracketIndex = tempString1.find("(") + 1
                        tempString = tempString1[bracketIndex:len(tempString1) - 1]
                        tempString1 = tempString1[bracketIndex:len(tempString1)]
                        nOpenBrackets += 1
                    nClosedBrackets += 1
                    trueStart = [i for i, v in enumerate(string) if v == "("][nOpenBrackets - 1] #indice di posizione della apertura di parentesi nella stringa completa
                    trueEnd = [i for i, v in enumerate(string) if v == ")"][nClosedBrackets - 1] + 1 #indice di posizione della chiusura di parentesi nella stringa completa
                    if tempString.strip() == "": #controlla che le parentesi non siano vuote
                        error = throwError(5)
                        brackets = False
                    break
                elif start == -1 and end == -1: #non sono presenti parentesi
                    tempString = string
                    brackets = False
                    trueStart = 0
                    trueEnd = len(tempString)
                    break
                elif end == -1: #la parentesi è stata solo aperta
                    error = throwError(6)
                    brackets = False
                    break
                elif start == -1: #la parentesi è stata solo chiusa
                    error = throwError(7)
                    brackets = False
                    break
        
            if error == False: #salta se è stato riscontrato un errore
                nOperators = 0
                offset = 1
                for x in operators: #conta quanti operatori ci sono
                    count = tempString.count(x)
                    nOperators += count
                    if x == "!" and count > 0: offset = 0
                op = list(range(0, nOperators)) #lista degli operatori
                n = list(range(0, nOperators + offset)) #lista dei valori

            if error == False: #salta se è stato riscontrato un errore
                nIndex = 0 #indice di posizione dei numeri
                oIndex = 0 #indice di posizione degli operatori
                index = 0 #indice di posizione del carattere nella stringa
                previous = "value"
                lentgh = len(tempString)
                for x in tempString: #legge l'espressione
                    if (x.isnumeric() and index == 0) or x.isdecimal() or tempString.startswith("."): #legge i numeri e li salva nella lista n
                        if type(n[nIndex]) != str:
                            n[nIndex] = ""
                        n[nIndex] += x
                        tempString = tempString[1:lentgh]
                        previous = "value"
                    elif tempString.startswith(" "): #elimina eventuali spazi
                        tempString = tempString.lstrip()
                    elif tempString.startswith("p"): #se viene inserito p, lo sostituisce con il risultato della precedente operazione
                        if type(n[nIndex]) == str or previous == "operator": #espressione invalida se p è vicino ad un numero
                            error = throwError(2)
                            break
                        n[nIndex] = previousResult
                        tempString = tempString[1:lentgh]
                        previous = "value"
                    else: #legge gli operatori e li salva nella lista op
                        n[nIndex] = float(n[nIndex])
                        if n[nIndex] % 1 == 0: n[nIndex] = int(n[nIndex])
                        if nOperators > 0 and x != "!" and index < lentgh - 1: nIndex += 1
                        if x == "!": #da errore se il simbolo fattoriale viene prima del numero
                            if previous == "value" and index != 0: n[nIndex - 1] = int(n[nIndex - 1])
                            else:
                                error = throwError(8)
                                break
                        if nOperators == 0: #da errore se ci sono simboli ma nessuno è valido
                            error = throwError(0, x)
                            break
                        else:
                            valid = False
                            if index != 0 or x == "+" or x == "-": #se è il primo carattere della stringa, è valido solo + e -
                                for x in operators: #controlla che il simbolo inserito sia un operatore valido
                                    if tempString.startswith(x):
                                        op[oIndex] = x
                                        oIndex += 1
                                        valid = True
                                        break
                            else: #da errore se il primo carattere della stringa è un simbolo diverso da + e -
                                error = throwError(1, x)
                                break
                            if valid == False: #da errore se viene inserito un simbolo non valido
                                error = throwError(0, x)
                                break
                            if previous == "value": #controlla che prima del simbolo ci sia un numero
                                if op[oIndex - 1] != "!": previous = "operator"
                                tempString = tempString[1:len(tempString)]
                            else: #da errore se ci sono 2 o più simboli non separati da numeri
                                error = throwError(1, x)
                                break
                    index += 1

            def calc(x, index, n): #esegue le singole operazioni
                result = 0
                match x:
                    case "=" | "<" | ">":
                        if type(n[index]) == type(n[index + 1]): #controlla che i due fattori del simbolo logico siano due numeri
                            match x:
                                case "=":
                                    if type(n[index]) == str: n[index] = n[index].lower()
                                    if type(n[index + 1]) == str: n[index + 1] = n[index + 1].lower()
                                    result = n[index] == n[index + 1]
                                case "<": result = n[index] < n[index + 1]
                                case ">": result = n[index] > n[index + 1]
                        elif x == "=": result = 0 #se i due fattori non sono entrambi numeri ma il simbolo è uguale, restituisce falso come risultato
                        else: return throwError(11, x) #da errore se il simbolo è maggiore o minore e i due fattori non sono entrambi numeri
                        if result == 0: result = "Falso"
                        else: result = "Vero"
                    case "+": result = n[index] + n[index + 1]
                    case "-": result = n[index] - n[index + 1]
                    case "*" | "x": result = n[index] * n[index + 1]
                    case "/" | ":": result = n[index] / n[index + 1]
                    case "%": result = n[index] % n[index + 1]
                    case "^": result = n[index] ** n[index + 1]
                    case "_" | "v": result =  n[index + 1] ** (1 / n[index])
                    case "!":
                        if n[index] > 0 and type(n[index]) == int: result = math.factorial(n[index]) #controlla che che il fattoriale venga fatto su un intero positivo
                        else: return throwError(3)

                if type(result) != str:
                    if result % 1 == 0: result = int(result)
                    else: format = "%.*f" % (precision, result)
                format = str(result)

                if verbose: #solo se la visualizzazione dei passaggi è attiva
                    if type(n[index]) != str:
                        if n[index] % 1 == 0: n1 = str(int(n[index]))
                        else: n1 = "%.*f" % (precision, n[index])
                    else: n1 = n[index]
                    if x == "!": print(n1+x,"→",format,"\n")
                    else:
                        if type(n[index + 1]) != str:
                            if n[index + 1] % 1 == 0: n2 = int(n[index + 1])
                            else: n2 = "%.*f" % (precision, n[index + 1])
                        else: n2 = n[index + 1]
                        print(n1,x,n2,"→",format,"\n")
                
                op.pop(index)
                if x != "!": n.pop(index + 1)
                return result
            
            if error == False: #salta se è stato riscontrato un errore
                n[nIndex] = float(n[nIndex])
                if n[nIndex] % 1 == 0: n[nIndex] = int(n[nIndex])
                for x in operators: #gestisce l'ordine delle operazioni
                    for y in range(len(op)):
                        index = min(y, len(op) - 1)
                        if x == op[index]:
                            n[index] = calc(x, index, n)
                            if type(n[index]) == bool: error = True

            if error == False: #salta se è stato riscontrato un errore
                if type(n[0]) == float: format = "%.*f" % (precision, n[0])
                else: format = str(n[0])
                string = string.replace(string[trueStart:trueEnd], format, 1)
                if verbose:  #solo se la visualizzazione dei passaggi è attiva
                    if string.isnumeric(): print(string + "\n\n")
                    else: print(string)

    if error == False: #salta se è stato riscontrato un errore
        previousResult = n[0] #salva il risultato per eventuale uso in operazioni successive
        if type(previousResult) != str and previousResult % 1 == 0: previousResult = int(previousResult) #se il risultato è un intero elimina il .0

        if verbose == False: #solo se la visualizzazione dei passaggi è disattivata
            if type(previousResult) != float: print(previousResult,"\n\n") #stampa a video il risultato
            else: print("%.*f" % (precision, previousResult) + "\n\n")