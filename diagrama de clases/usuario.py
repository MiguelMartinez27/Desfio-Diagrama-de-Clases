from listado_respuestas import ListadoRespuestas

class Usuario:
    """
    Clase que representa un usuario.

    Attributes:
        correo (str): Correo del usuario.
        edad (int): Edad del usuario.
        region (int): Región del usuario.
    """
    
    def __init__(self, correo, edad, region):
        """
        Inicializa una instancia de Usuario.

        Args:
            correo (str): Correo del usuario.
            edad (int): Edad del usuario.
            region (int): Región del usuario.
        """
        self.correo = correo
        self.edad = edad
        self.region = region
    
    def get_correo(self):
        """Devuelve el correo del usuario."""
        return self.correo
    
    def get_edad(self):
        """Devuelve la edad del usuario."""
        return self.edad
    
    def get_region(self):
        """Devuelve la región del usuario."""
        return self.region
    
    def set_correo(self, correo):
        """Establece el correo del usuario."""
        self.correo = correo
    
    def set_edad(self, edad):
        """Establece la edad del usuario."""
        self.edad = edad
    
    def set_region(self, region):
        """Establece la región del usuario."""
        self.region = region
    
    def contestar_encuesta(self, encuesta, respuestas):
        """Permite al usuario contestar una encuesta."""
        listado_respuestas = ListadoRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(listado_respuestas)
