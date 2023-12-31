from dboard import DfResponseController, get_db_store

class BaseController(DfResponseController):

    def get_pagila_db_store(self):
        return get_db_store("pagila")
    
    def get_sakila_db_store(self):
        return get_db_store("sakila")