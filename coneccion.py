# problema 3 hewe.ochoa@utp.ac.pa
import psycopg2
import configparser
import sys, os
import pandas as pd

def connect(comando):

    # Obteniendo archivo ini
    config = configparser.ConfigParser()
    config.read('config_bd.ini')

    # Variables globales
    PG_HOST = config['DEFAULT']['DB_HOST']
    PG_DATABASE = config['DEFAULT']['DB_NAME']
    PG_PORT = config['DEFAULT']['DB_PORT']
    PG_USER = config['DEFAULT']['DB_USER']
    PG_PASSWORD = config['DEFAULT']['DB_PASSWORD']
    conn = None

    try:
        # Conectandonos al server de postgresSql.
        conn_string = """
            host=%s port=%s user=%s password=%s dbname=%s
            """ % (PG_HOST, PG_PORT, PG_USER, PG_PASSWORD, PG_DATABASE)
        conn = psycopg2.connect(conn_string)
        print('\n Conectado a la Base de datos <{}>. \n'.format(str(PG_DATABASE)))

        # Creando un objeto
        cursor = conn.cursor()
        cursor.execute(comando)
        print('Comandos Ingresado Exitosamente...')
        cursor.close()
        conn.commit()
    except psycopg2.Error as e:
        print('{}'.format(e))
    finally:
        if conn is not None:
            conn.close()
            print('\n Conexion a la Base datos <{}> cerrada.'.format(str(PG_DATABASE)))