class Lecotres:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
    
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    
    def getAddress(self):
        return self.address
    def setName(self, address):
        self.name = address
    
    def getPhone(self):
        return self.phone
    def setName(self, phone):
        self.name = phone
      
    def reservar(self):
        print(f"{self.getName()} ha reservado un libro y su telefono es: {self.getPhone()}")
    def entregar(self):
        print(f"{self.getName()} ha entregado un libro")

class Estudiantes(Lecotres):
    def __init__(self, name, address, phone, carrera, matricula):
        super().__init__(name, address, phone)
        self._carrera = carrera
        self._matricula = matricula

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    
    def getAddress(self):
        return self.address
    def setName(self, address):
        self.name = address
    
    def getPhone(self):
        return self.phone
    def setName(self, phone):
        self.name = phone

    def getCarrera(self):
        return self._carrera
    def setCarrera(self, carrera):
        self._carrera = carrera

    def getMatricula(self):
        return self._matricula
    def setMatricula(self, matricula):
        self._matricula = matricula
    

    def reservar(self):
        print(f"El estudiante {self.getName()} de datos \nMatricula: {self.getMatricula()} \nCarrera: {self.getCarrera()} \nNumero: {self.getPhone()} \nDireccion: {self.getAddress()} \nHA RESERVADO UN LIBRO")
    def entregar(self):
        print(f"El estudiante {self.getName()} de datos \nMatricula: {self.getMatricula()} \nCarrera: {self.getCarrera()}\n Numero: {self.getPhone()} \nDireccion: {self.getAddress()} \nHA ENTREGADO UN LIBRO")

class Docentes(Lecotres):
    def __init__(self, name, address, phone, modalidad, num_empleado):
        super().__init__(name, address, phone)
        self.__modalidad = modalidad
        self.__num_empleado = num_empleado

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    
    def getAddress(self):
        return self.address
    def setName(self, address):
        self.name = address
    
    def getPhone(self):
        return self.phone
    def setName(self, phone):
        self.name = phone

    def getModalidad(self):
        return self.__modalidad
    def setModalidad(self, modalidad):
        self.__modalidad = modalidad

    def getNumeroEmpleado(self):
        return self.__num_empleado
    def setNumeroEmpleado(self, num_empleado):
        self.__num_empleado = num_empleado
    
    def reservar(self):
        print(f"El docente {self.getName()} de datos \nNumero de empelado: {self.getNumeroEmpleado()} \nModalidad: {self.getModalidad()} \nNumero: {self.getPhone()} \nDireccion: {self.getAddress()} \nHA RESERVADO UN LIBRO")
    def entregar(self):
        print(f"El docente {self.getName()} de datos \nNumero de empelado: {self.getNumeroEmpleado()} \nModalidad: {self.getModalidad()} \nNumero: {self.getPhone()} \nDireccion: {self.getAddress()} \nHA ENTREGADO UN LIBRO")
