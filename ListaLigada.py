class Nodo:#clase que contiene los elementos de la lista
    def __init__(self, dIni):#constructor
        self.dato = dIni #se requiere de un valor para que funcione la clase listaPalabras
        self.sig = None #siguiente de un nodo por defecto es None

    def getDato(self):#metodo obtiene el dato del nodo
        return self.dato

    def getSiguiente(self):#metodo obtiene el siguiente del nodo
        return self.sig

    def setDato(self,nuevodato):#metodo para ingresar el dato del nodo
        self.dato = nuevodato

    def setSiguiente(self, nuevosiguiente):#metodo para ingresar el siguiente del nodo
        self.sig = nuevosiguiente


class ListaOrdenada:
    def __init__(self):#constructor de la clase
        self.cabeza = None

    def buscar(self, valor):#metodo buscar en la lista
        actual = self.cabeza #inicializar la primera posicion para trabajar sobre esta
        encontrado = False #bandera por si es encontrado
        detenerse = False #bandera por si se detiene al ya no haber mas datos
        while actual != None and not encontrado and not detenerse: #mientras el elemento no se haya encontrado y la busqueda 
            if actual.getDato() == valor:#no se haya detenido y el elemento actual contenga algun valor, realizar busqueda
                encontrado = True #si el dato actual es igual al buscado se marca la bandera encontrado como True
            else:
                if actual.getDato() > valor:#si el dato actual es mas grande que el valor buscado, detiene la busqueda, 
                    detenerse = True#debido a que es una lista odenada
                else:
                    actual = actual.getSiguiente()#actual cambia al siguiente valor
        return encontrado #retorna el estado encontrado como True o False 

    def agregar(self, valor):#metodo para agregar valores
        actual = self.cabeza#empezar por la cabeza de la lista
        anterior = None #anterior del valor actual
        detenerse = False #bandera detenerse
        while actual != None and not detenerse:#iniciar ciclo mientras actual tenga valor y no se haya detenido
            if actual.getDato() > valor:#si el valor actual es mas grande que el valor inicial, detenerse
                detenerse = True#debido a que la lista esta ordenada
            else:
                anterior = actual#avanzar uno en conjunto
                actual = actual.getSiguiente()
        temp = Nodo(valor)#nodo que guardara el valor temporalmente
        if anterior == None:#si no tiene valor detras, se agrega unicamente nodo temp apuntando a None
            temp.setSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.setSiguiente(actual)#se agrega antes de actual y despues de anterior
            anterior.setSiguiente(temp)

    def quitar(self):#metodo para eliminar elemento mas grande
        actual = self.cabeza#cabeza de la lista
        while actual != None:#mientras actual tenga valor
            if(actual.getSiguiente().getSiguiente() == None):#cuando el siguiente del actual sea el ultimo
                print("Valor eliminado: "+str(actual.getSiguiente().getDato()))#imprimir su valor
                actual.setSiguiente(None)#desvincular ultimo nodo y vincularlo a None
            actual = actual.getSiguiente()#iterar sobre la lista

    def len(self):#metodo para obtener longitud de la lista
        actual = self.cabeza#Se inicia por la cabeza de la lista
        c = 0#Contador
        while actual != None:#Mientras el nodo actual tenga un valor
            c = c + 1 #Aumento de contador
            actual = actual.getSiguiente() #Avanzar al siguiente nodo
        return c #Retornar el contador que es el número de elementos
    
    def __str__(self):# Método para imprimir la lista
        s = '' #inicio de la cadena
        actual = self.cabeza #Se inicia por la cabeza de la lista
        if actual == None: #Si el nodo actual no tiene ningún valor es lista vacia
            print("Lista vacia") #imprime lista vacía
        while actual != None: # Mientras el nodo actual tenga algún valor
            s = s+str(actual.dato)+"\n" #agrega valores a la cadena a retornar
            actual = actual.getSiguiente() #Avanza al siguiente nodo
        return s # Retorna la cadena con las palabras

class ListaPalabras:
    def __init__(self, cadena=None): #Constructor necesita de una palabra para inicializarse
        if cadena == None:# Si no hay ninguna palabra imprime error
            print("Valor necesario para inicializar la lista")
        else:
            temp = Nodo(cadena)# Se agrega el primer nodo
            temp.setSiguiente(None)
            self.cabeza = temp


    def agregar(self, cadena=None):#Método para agregar palabras a la lista 
        temp = Nodo(cadena) #nodo temporal para guardar el valor
        if cadena == None:#Si no hay ningún elemento en la cadena la cadena está vacía
            print("Error: cadena vacia")#Mensaje de error
        elif self.buscar(cadena):#Busca en la lista la cadena recibida, evita repeticiones
            print("Error: palabra repetida") #Mensaje de error
        else:
            temp.setSiguiente(self.cabeza)#Se agrega el nuevo nodo primero en la lista
            self.cabeza = temp 

    def len(self):#metodo para obtener longitud de la lista
        actual = self.cabeza#Se inicia por la cabeza de la lista
        c = 0#Contador
        while actual != None:#Mientras el nodo actual tenga un valor
            c = c + 1 #Aumento de contador
            actual = actual.getSiguiente() #Avanzar al siguiente nodo
        return c #Retornar el contador que es el número de elementos
    
    def buscar(self, valor):#metodo buscar en la lista
        actual = self.cabeza #inicializar la primera posicion para trabajar sobre esta
        encontrado = False #bandera por si es encontrado
        detenerse = False #bandera por si se detiene al ya no haber mas datos
        while actual != None and not encontrado and not detenerse: #mientras el elemento no se haya encontrado y la busqueda 
            if actual.getDato() == valor:#no se haya detenido y el elemento actual contenga algun valor, realizar busqueda
                encontrado = True #si el dato actual es igual al buscado se marca la bandera encontrado como True
            else:
                if actual.getDato() > valor:#si el dato actual es mas grande que el valor buscado, detiene la busqueda, 
                    detenerse = True#debido a que es una lista odenada
                else:
                    actual = actual.getSiguiente()#actual cambia al siguiente valor
        return encontrado #retorna el estado encontrado como True o False 

    def pop(self):#Método para quitar el último elemento ingresado
        print ("pop: "+str(self.cabeza.getDato()))#imprime el valor a eliminar
        self.cabeza = self.cabeza.getSiguiente() #Cambia el nodo cabeza por el siguiente en la lista

    def __str__(self):#Método para imprimir la lista
        s = ''#inicializar cadena
        c = 0#contador
        actual = self.cabeza #iniciar con nodo cabeza
        while actual != None: #Mientras el logo actual tenga un valor
            if actual.getSiguiente() == None: #Cuando sea el último valor
                s = s+actual.getDato()+"\n" #imprimir sin coma
                return s# retornar la cadena
            else:
                s = s+actual.getDato()+", "#imprimir con coma al final
                actual = actual.getSiguiente()#Continuar al siguiente nodo
            c += 1


print("--LISTA ORDENADA--\n")
milista = ListaOrdenada()#Inicializar una lista ordenada

print(milista)#Imprimir elementos de la lista
print("Longitud : "+str(milista.len())+"\n")#Imprimir longitud de la lista

milista.agregar(5)#Agregar elementos a la lista
milista.agregar(10)
milista.agregar(3)
milista.agregar(1)
milista.agregar(20)
milista.agregar(7)
milista.agregar(100)
milista.agregar(2)

print("Lista:")
print(milista)#Imprimir elementos de la lista
print("Longitud : "+str(milista.len()))#Imprimir longitud de la lista

milista.quitar()#quitar elementos mas grandes de la lista
milista.quitar()

print("\nLista:")
print(milista)#Imprimir elementos de la lista
print("Longitud : "+str(milista.len()))#Imprimir longitud de la lista

print("\n--LISTA CADENAS--\n")

listaCadena = ListaPalabras("Hola")#inicializar lista con una palabra
listaCadena.agregar("Mundo")#Agregar palabras a la lista
listaCadena.agregar("Ingenieria")
listaCadena.agregar("EDA")
listaCadena.agregar("2")
listaCadena.agregar()#pruebas de error con palabra vacía
listaCadena.agregar("Mundo")#Prueba de error con palabra repetida

print("\nLista: ")
print(listaCadena)#Imprimir elementos de la lista

print("¿La palabra Ingenieria esta?: "+str(listaCadena.buscar("Ingenieria")))#Comprobar si palabras existen en la lista
print("¿La palabra UNAM esta?: "+str(listaCadena.buscar("UNAM")))

listaCadena.pop()#Quitar últimos elementos agregados a la lista
listaCadena.pop()
listaCadena.pop()

print("\nLista: ")
print(listaCadena)#Imprimir elementos de la lista
