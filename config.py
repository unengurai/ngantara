#!/usr/bin/env python


import os


_data_path = os.path.join(os.path.dirname(__file__), 'data')
_db_file = 'websearch.sqlite'
_db = os.path.join(_data_path, _db_file)


dbconfig = {
    'sqlite': {
        'db_path': _data_path,
        'db_name': _db_file,
        'db': _db,
    },
    'mysql': {
        'host': '127.0.0.1',
        'user': '',
        'password': '',
        'db_name': '',
    },
    'postgre': {
        'host': '127.0.0.1',
        'user': 'ton',
        'password': 'tono123',
        'db_name': 'ngantara',
    }
}
