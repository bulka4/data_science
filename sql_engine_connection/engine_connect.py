# this file requires another file called config.py which contains object cfg of format:
# cfg = {
#   'host': 'host',
#   'user': 'user',
#   'password': 'password',
#   'port': 'port',
#   'db': 'db'
# }

from sqlalchemy import create_engine
import config

# def get_engine(user, password, host, port, db):
def get_engine():
    user = config.cfg['user']
    password = config.cfg['password']
    host = config.cfg['host']
    port = config.cfg['port']
    db = config.cfg['db']
    
    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    
    engine = create_engine(url, pool_size = 50, echo = False)
    
    return engine