class Encuesta:
    """
    Clase que representa una encuesta.

    Attributes:
        nombre (str): El nombre de la encuesta.
        preguntas (list[Pregunta]): Lista de preguntas de la encuesta.
        listados_respuestas (list[ListadoRespuestas]): Lista de listados de respuestas asociados a la encuesta.
    """
    
    def __init__(self, nombre, preguntas):
        """
        Inicializa una instancia de Encuesta.

        Args:
            nombre (str): El nombre de la encuesta.
            preguntas (list[Pregunta]): Lista de preguntas de la encuesta.
        """
        self.nombre = nombre
        self.preguntas = preguntas
        self.listados_respuestas = []
    
    def get_nombre(self):
        """Devuelve el nombre de la encuesta."""
        return self.nombre
    
    def set_nombre(self, nombre):
        """Establece el nombre de la encuesta."""
        self.nombre = nombre
    
    def mostrar(self):
        """Muestra la encuesta con sus preguntas."""
        output = f"Encuesta: {self.nombre}\n"
        for pregunta in self.preguntas:
            output += pregunta.mostrar() + "\n"
        return output
    
    def agregar_listado_respuestas(self, listado):
        """Agrega un listado de respuestas a la encuesta."""
        self.listados_respuestas.append(listado)

class EncuestaLimitadaEdad(Encuesta):
    """
    Clase que representa una encuesta limitada por edad.
    
    Attributes:
        edad_minima (int): Edad mínima para responder la encuesta.
        edad_maxima (int): Edad máxima para responder la encuesta.
    """
    
    def __init__(self, nombre, preguntas, edad_minima, edad_maxima):
        """
        Inicializa una instancia de EncuestaLimitadaEdad.

        Args:
            nombre (str): El nombre de la encuesta.
            preguntas (list[Pregunta]): Lista de preguntas.
            edad_minima (int): Edad mínima para responder la encuesta.
            edad_maxima (int): Edad máxima para responder la encuesta.
        """
        super().__init__(nombre, preguntas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima
    
    def agregar_listado_respuestas(self, listado):
        """Agrega un listado de respuestas solo si el usuario tiene la edad adecuada."""
        if self.edad_minima <= listado.get_usuario().get_edad() <= self.edad_maxima:
            self.listados_respuestas.append(listado)

class EncuestaLimitadaRegion(Encuesta):
    """
    Clase que representa una encuesta limitada por región.
    
    Attributes:
        regiones (list[int]): Lista de regiones permitidas.
    """
    
    def __init__(self, nombre, preguntas, regiones):
        """
        Inicializa una instancia de EncuestaLimitadaRegion.

        Args:
            nombre (str): El nombre de la encuesta.
            preguntas (list[Pregunta]): Lista de preguntas.
            regiones (list[int]): Lista de regiones permitidas.
        """
        super().__init__(nombre, preguntas)
        self.regiones = regiones
    
    def agregar_listado_respuestas(self, listado):
        """Agrega un listado de respuestas solo si el usuario pertenece a una región permitida."""
        if listado.get_usuario().get_region() in self.regiones:
            self.listados_respuestas.append(listado)
