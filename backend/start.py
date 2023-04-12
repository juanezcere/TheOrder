import os
import logging
from datetime import date

def initialize():
    """
    Función para crear la carpeta de logs y luego inicializar el registro de eventos sobre un archivo cuyo nombre cambia a diario
    """
    try:
        os.mkdir(os.path.join(os.path.dirname(__file__), 'data', 'logs'))
    except:
        pass
    filename = os.path.join(os.path.dirname(__file__), 'data', 'logs', 'TheOrder_log_' + str(date.today()))
    logging.basicConfig(filename=filename, filemode='w', format='%(name)s - %(levelname)s - %(asctime)s - %(message)s')
    logging.info('Logging file started')


if __name__ == '__main__':
    initialize()
    while True:
        try:
            from src import server
            server.initialize(os.path.dirname(__file__))
            server.app.run(host='0.0.0.0', port=3000)
        except Exception as err:
            print(err)
            logging.critical('A critical error happend. ' + str(err))
