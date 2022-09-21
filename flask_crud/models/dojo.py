from flask_crud.config.mysqlconnection import connectToMySQL
from flask_crud.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']        
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas =[]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('ninjas_dojo').query_db(query)
        all_dojos = []
        if len(results) == 0:
            return None
        for data in results:
            all_dojos.append(cls(data))
        return all_dojos 

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        resultado = connectToMySQL('ninjas_dojo').query_db( query, data ) 
        print(resultado)
        return  resultado  
    
    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM dojos where id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL('ninjas_dojo').query_db(query, data)
        return cls(results[0]) if len(results) > 0 else None

    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(dojos_id)s"
        results = connectToMySQL('ninjas_dojo').query_db(query, data)
           
        if len(results) == 0:
            print(results)
            return None 
        dojo_data = {
            'id': results[0]['id'],
            'name': results[0]['name'],
            'created_at': results[0]['created_at'],
            'updated_at': results[0]['updated_at'],
        }
        dojo = Dojo(dojo_data)
        all_ninjas =[]
        for data in results:
            ninja_data = {
                'id':data['ninjas.id'],
                'first_name':data['first_name'],
                'last_name':data['last_name'],
                'age':data['age'],
                'dojos_id' : data['dojos_id'],
                'created_at':data['ninjas.created_at'],
                'updated_at':data['ninjas.updated_at'],
            }
            new_ninja = Ninja(ninja_data)
            all_ninjas.append(new_ninja)
        dojo.ninjas = all_ninjas
        return dojo


    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('ninjas_dojo').query_db(query,data)