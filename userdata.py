class userdata():
    def __init__(self,name,lastname,bornDate,genre,username,password,phoneNumber):
        self.name = name
        self.lastname = lastname
        self.bornDate = bornDate
        self.genre = genre
        self.username = username
        self.password = password
        self.phoneNumber = phoneNumber

    def get_json(self):
        return{
            "nombre" : self.name,
            "apellido" : self.lastname,
            "fecha_nacimiento" : self.bornDate,
            "sexo" : self.genre,
            "nombre_usuario" : self.username,
            "contrasena" : self.password,
            "telefono" : self.phoneNumber
        }