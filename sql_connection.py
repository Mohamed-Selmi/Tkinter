import mysql.connector

def get_config():
    config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'students'
    }
    return config


def start_connection(config):
    return mysql.connector.connect(**config)

def close_connection(cnx):
    if cnx.is_connected():
        cnx.close()