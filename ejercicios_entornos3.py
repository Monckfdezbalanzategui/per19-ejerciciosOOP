class Libros():
    def __init__(self,nombre_libro,fecha_recogida):
        nombre_libro=input("ELija el libro")
        fecha_recogida=input(int("Indique el número de día de hoy:"))
    def __init__(self, libro, fecha):
        self.__libro=str(nombre_libro)
        self.__fecha=int(fecha_recogida)
    def get_nombrelibro(self):
        return self.__libro
    def get_fecha (self):
        return self.__fecha
    def set_fechadevolucion(self):
        for get_fecha() in range(1,31):
            if 1<=get_fecha()<=15:
                self.fecha_devolucion=get_fecha()+=15
            elif 15<get_fecha()<=30:
                self.fecha_devolucion=get_fecha()+=15
                fecha_devolucion=int(self.fecha_devolucion)-30
                return fecha_devolucion
            return
    def prestamo(self, libro, fecha_devolucion):
        print("""Se le cede el libro""",get__nombrelibro(),"""hasta la fecha""",set_fechadevolucion())
        return
    def devolucion(self,fecha_hoy):
        self.fecha_hoy=fecha_recogida
        if self.fecha_hoy==get_fechadevolucon:
            print("Hoy expira el plazo para devolver su libro")

    def dame_info(self):
        self.dame_info="Préstamos de libro ",get_nombrelibro(),"expira en",get_fechadevolucion()
        print(self.dame_info)
        return
