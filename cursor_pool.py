from logger_base import log
from conexion import Conexion

class cursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
        
    def __enter__(self):
        log.debug('Inicio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traceback_excepcion):
        log.debug('Se ejecuta método exit.')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrió una excepcion: {valor_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion().liberarConexion(self._conexion)
