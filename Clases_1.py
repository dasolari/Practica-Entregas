class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    def muerte(self):
        p = 100 - self.edad
        print("A "+self.nombre+" le quedan "+str(p)+" años de vida")
    def check_sex(self):
        print(self.nombre+" es "+self.sexo)
    def __str__(self):
        e = str(self.edad)
        return ("Elle se llama "+self.nombre+" es "+self.sexo+" y tiene "+e+" años")


persona=Persona("Carlos",35,"hombre")
persona2=Persona("Valentina",29,"mujer")
print(persona)
print(" ")
print(persona2)

persona.muerte()
persona.check_sex()
print(" ")
persona2.muerte()
persona2.check_sex()