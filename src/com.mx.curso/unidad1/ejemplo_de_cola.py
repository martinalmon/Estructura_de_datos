#ejemplo de cola fifo(first in first out)
class Cola:
    def __init__(self):
        self.item=[]
    
    def esta_vacia(self):
        return len(self.items)
    
    def encolar(self,item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola esta vacia")
    
    def temano(self):
        return len(self.items)
    
#ejemplos de uso 
if __name__=="__main__":
    cola=Cola()
    cola.encolar(1)
    cola.encolar(1)
    cola.encolar(1)
    print(cola)