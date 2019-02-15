class Empleado():
    def __init__(self,experiencia,cualificación):
        self.experiencia=experiencia
        self.cualificacion=cualificacion
    def tiene_cualificacion(self):
        input=input("Tiene estudios superiores, responder con sí o no:")
        if input=="sí":
            set.cualificacion="sí"
        else:
            set.cualificacion="no"
        return
    def tiene_experiencia(self):
        input=input("Tiene experiencia, responder con si o no")
        if input=="sí":
            set.experiencia="sí"
        else:
            set.experiencia="no"
        return
    def contrato(self):
        if experiencia=="sí" and cualificacion=="sí":
            print("Está contratado")
        else:
            print("Lo sentimos, no cumple con los requerimientos")
        return
