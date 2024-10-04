class Pregunta:
    """
    Clase que representa una pregunta dentro de una encuesta.

    Attributes:
        enunciado (str): El enunciado de la pregunta.
        ayuda (str, opcional): La ayuda adicional para la pregunta.
        es_requerida (bool): Indica si la pregunta es obligatoria.
        alternativas (list[Alternativa]): Lista de alternativas para la pregunta.
    """
    
    def __init__(self, enunciado, es_requerida, alternativas, ayuda=None):
        """
        Inicializa una instancia de Pregunta.

        Args:
            enunciado (str): El enunciado de la pregunta.
            es_requerida (bool): Indica si la pregunta es obligatoria.
            alternativas (list[Alternativa]): Lista de alternativas de la pregunta.
            ayuda (str, opcional): La ayuda adicional para la pregunta.
        """
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.es_requerida = es_requerida
        self.alternativas = alternativas
    
    def get_enunciado(self):
        """Devuelve el enunciado de la pregunta."""
        return self.enunciado
    
    def get_ayuda(self):
        """Devuelve la ayuda de la pregunta."""
        return self.ayuda
    
    def get_es_requerida(self):
        """Devuelve si la pregunta es requerida."""
        return self.es_requerida
    
    def get_alternativas(self):
        """Devuelve la lista de alternativas de la pregunta."""
        return self.alternativas
    
    def set_enunciado(self, enunciado):
        """Establece el enunciado de la pregunta."""
        self.enunciado = enunciado
    
    def set_ayuda(self, ayuda):
        """Establece la ayuda de la pregunta."""
        self.ayuda = ayuda
    
    def set_es_requerida(self, es_requerida):
        """Establece si la pregunta es requerida."""
        self.es_requerida = es_requerida
    
    def mostrar(self):
        """Muestra la pregunta con su enunciado, ayuda y alternativas."""
        output = f"Enunciado: {self.enunciado}"
        if self.ayuda:
            output += f", Ayuda: {self.ayuda}"
        output += f"\nAlternativas:\n"
        for alt in self.alternativas:
            output += f"- {alt.mostrar()}\n"
        return output
