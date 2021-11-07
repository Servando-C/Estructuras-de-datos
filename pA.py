class Nodo:#clase que contiene los elementos de la lista
    def __init__(self, dIni):#constructor
        self.dato = dIni
        self.sig = None

    def getDato(self):
        return self.dato

    def getSiguiente(self):
        return self.sig

    def setDato(self,nuevodato):
        self.dato = nuevodato

    def setSiguiente(self, nuevosiguiente):
        self.sig = nuevosiguiente


class ListaOrdenada:
    def __init__(self):
        self.cabeza = None

    def buscar(self, valor):
        actual = self.cabeza
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.getDato() == valor:
                encontrado = True
            else:
                if actual.getDato() > valor:
                    detenerse = True
                else:
                    actual = actual.getSiguiente()
        return encontrado

    def agregar(self, valor):
        actual = self.cabeza
        anterior = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.getDato() > valor:
                detenerse = True
            else:
                anterior = actual
                actual = actual.getSiguiente()
        temp = Nodo(valor)
        if anterior == None:
            temp.setSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.setSiguiente(actual)
            anterior.setSiguiente(temp)

    def quitar(self):
        actual = self.cabeza
        a = actual.sig
        while actual != None:
            if(actual.sig.sig == None):
                actual.sig = None     
            actual = actual.getSiguiente()

    def estaVacia(self):
        return self.cabeza == None

    def len(self):
        actual = self.cabeza
        c = 0
        while actual != None:
            c = c + 1
            actual = actual.getSiguiente()
        return c
    def __str__(self):
        s = ''
        actual = self.cabeza
        while actual != None:
            s = s+str(actual.dato)+"\n"
            actual = actual.getSiguiente()
        return s

class ListaPalabras:
    def __init__(self, cadena):
        if cadena == None:
            print("Valor necesario para inicializar la lista")
        else:
            self.cabeza = cadena

    def agregar(self, cadena):
        temp = Nodo(cadena)
        actual = self.cabeza
        if self.buscar(cadena) == True:
            print("Error: palabra repetida")
        elif cadena == '':
            print("Error: cadena vacia")
        elif self.cabeza == None:
            temp.setSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.setSiguiente(actual)

    def buscar(self, valor):
        actual = self.cabeza
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.getDato() == valor:
                encontrado = True
            else:
                if actual.getDato() > valor:
                    detenerse = True
                else:
                    actual = actual.getSiguiente()
        return encontrado

    def __str__(self):
        s = ''
        c = 0
        actual = self.cabeza
        while actual != None:
            if actual.sig == None:
                s = s+str(actual.getDato())
            else:
                s = s+str(actual.dato)+", "
                actual = actual.getSiguiente()
            
            c += 1
        return s



milista = ListaOrdenada()

print(milista.len())

milista.agregar(5)
milista.agregar(10)
milista.agregar(3)
milista.agregar(1)
milista.agregar(20)
milista.agregar(7)
milista.agregar(100)
milista.agregar(2)

milista.quitar()

print(milista.len())
print(milista.buscar(93))
print(milista.buscar(100))

print(milista)

listaCadena = ListaPalabras("Hola")

listaCadena.agregar("EDA")

print(listaCadena)