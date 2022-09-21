from flask_crud.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojos_id = data['dojos_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
       

    @classmethod
    def get_all(cls):
        query ="SELECT * FROM ninjas;"
        results = connectToMySQL('ninjas_dojo').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return  ninjas    

    @classmethod
    def add_ninja(cls, data ):
        query = f"INSERT INTO ninjas ( first_name ,last_name , age ,dojos_id, created_at, updated_at  ) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s,NOW(),NOW());"
        resultado = connectToMySQL('ninjas_dojo').query_db( query, data ) 
        print("|||||||||data|||||||||||", data)
        print("|||||||||||resultado|||||||||", resultado)
        return  resultado  

