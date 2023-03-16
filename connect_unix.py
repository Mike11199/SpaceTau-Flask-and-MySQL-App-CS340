import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine

load_dotenv(find_dotenv())


def get_connect_url():
    
    
    
    db_user = os.getenv("DB_USER")  # e.g. 'my-database-user'
    db_pass = os.getenv("PASSWORD")  # e.g. 'my-database-password'
    db_name = os.getenv("DBNAME")  # e.g. 'my-database'
    INSTANCE_UNIX_SOCKET = os.getenv("INSTANCE_UNIX_SOCKET","NO_INSTANCE_UNIX_SOCKET")  # e.g. 'my-database'
    
    
    if 1==1:
        unix_socket_path = os.getenv("INSTANCE_UNIX_SOCKET")  # e.g. '/cloudsql/project:region:instance'
        print('test')
        return f"postgresql+pg8000://{db_user}:{db_pass}@/{db_name}?unix_sock={unix_socket_path}/.s.PGSQL.5432"
        
    else:
        # Local test
        print('testlocal')
        db_host=os.getenv("DB_HOST")
        db_port=5432
        return f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        # postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}
        

load_dotenv(find_dotenv())

def get_engine():
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("PASSWORD")
    db_name = os.getenv("DBNAME")
    INSTANCE_UNIX_SOCKET = os.getenv("INSTANCE_UNIX_SOCKET","NO_INSTANCE_UNIX_SOCKET")
    
    if 1==1:
        unix_socket_path = os.getenv("INSTANCE_UNIX_SOCKET")
        print(f"postgresql+pg8000://{db_user}:{db_pass}@/{db_name}?unix_sock={unix_socket_path}/.s.PGSQL.5432")
        return create_engine(f"postgresql+pg8000://{db_user}:{db_pass}@/{db_name}?unix_sock={unix_socket_path}/.s.PGSQL.5432")
    else:
        db_host=os.getenv("DB_HOST")
        db_port=5432
        return create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")
