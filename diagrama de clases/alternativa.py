class Alternativa:
    """
    Clase que representa una alternativa dentro de una pregunta.
    
    Attributes:
        contenido (str): El contenido de la alternativa.
        ayuda (str, opcional): La ayuda adicional para la alternativa.
    """
    
    def __init__(self, contenido, ayuda=None):
        """
        Inicializa una instancia de Alternativa.

        Args:
            contenido (str): El contenido de la alternativa.
            ayuda (str, opcional): La ayuda adicional para la alternativa.
        """
        self.contenido = contenido
        self.ayuda = ayuda
    
    def get_contenido(self):
        """Devuelve el contenido de la alternativa."""
        return self.contenido
    
    def get_ayuda(self):
        """Devuelve la ayuda de la alternativa."""
        return self.ayuda
    
    def set_contenido(self, contenido):
        """Establece el contenido de la alternativa."""
        self.contenido = contenido
    
    def set_ayuda(self, ayuda):
        """Establece la ayuda de la alternativa."""
        self.ayuda = ayuda
    
    def mostrar(self):
        """Muestra la alternativa con su contenido y ayuda."""
        if self.ayuda:
            return f"Contenido: {self.contenido}, Ayuda: {self.ayuda}"
        return f"Contenido: {self.contenido}"
