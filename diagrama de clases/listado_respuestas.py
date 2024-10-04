class ListadoRespuestas:
    """
    Clase que representa un listado de respuestas.

    Attributes:
        usuario (Usuario): El usuario que responde la encuesta.
        respuestas (list[int]): Lista de respuestas (números enteros).
    """
    
    def __init__(self, usuario, respuestas):
        """
        Inicializa una instancia de ListadoRespuestas.

        Args:
            usuario (Usuario): El usuario que responde.
            respuestas (list[int]): Lista de respuestas.
        """
        self.usuario = usuario
        self.respuestas = respuestas
    
    def get_usuario(self):
        """Devuelve el usuario asociado al listado de respuestas."""
        return self.usuario
    
    def get_respuestas(self):
        """Devuelve la lista de respuestas."""
        return self.respuestas
    
    def mostrar(self):
        """Muestra el listado de respuestas."""
        return f"Usuario: {self.usuario.get_correo()}, Respuestas: {self.respuestas}"
