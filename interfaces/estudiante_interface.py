from abc import ABCMeta,abstractmethod

class IEstudiante(metaclass=ABCMeta):
    @abstractmethod
    def listarTodos(self):
        pass
    @abstractmethod
    def grabarRegistro(self):
        pass
    @abstractmethod
    def obtenerRegistro(self):
        pass
    @abstractmethod
    def actualizarRegistro(self):
        pass
    @abstractmethod
    def eliminarRegistro(self):
        pass