from conexion import Conexion
from persona import Persona
from logger_base import log
from cursor_pool import cursorDelPool

class PersonaDAO:
    '''
    DAO (Data Access Object)
    '''
    
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):    
        with cursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()        
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
        
    @classmethod
    def insertar(cls, persona):
        with cursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona a insertar {persona}')
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, persona):
        with cursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount
            
    @classmethod
    def eliminar(cls, persona):
        with cursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Se ha eliminado: {persona}')
            return cursor.rowcount
            

if __name__ == '__main__':
    persona1 = Persona(nombre = 'Eli', apellido = 'Gas', email = 'elig@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas {persona1}')
    
    """persona1 = Persona(id_persona= 3, nombre='Bruno', apellido='Juarez', email='nosehabladebruno@mail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas {personas_actualizadas}')"""
    
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
