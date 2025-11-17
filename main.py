from dataclasses import dataclass, field
from collections import deque

@dataclass
class Cola:
    tareas: deque = field(default_factory=deque)
    
    def añadir_tarea(self, tarea):
        self.tareas.append(tarea)
        
    def siguiente_tarea(self):
        return self.tareas.popleft()
    
    def tareas_pendientes(self):
        return len(self.tareas)
    

if __name__ == "__main__":
    cola = Cola()

    cola.añadir_tarea("procesar_imagen")
    cola.añadir_tarea("backup")
    cola.añadir_tarea("exportar_pdf")

    print(cola)  # Cola(pendientes=3)

    print(cola.siguiente_tarea())  # procesar_imagen
    print(cola.siguiente_tarea())  # backup
    
    print(cola.tareas_pendientes())

    print(cola)  # Cola(pendientes=1)
 