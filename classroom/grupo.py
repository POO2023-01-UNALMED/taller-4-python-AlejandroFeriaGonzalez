from classroom.asignatura import Asignatura


class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes:list="predeterminado"):
        if asignaturas == None:
            self._asignaturas = []
        else:
            self._asignaturas = asignaturas

        self._grupo = grupo
        self.listadoAlumnos = estudiantes
        # self.grado = "Grupo 12"

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista:list=None):
        if lista==None:
            lista = []
        lista.append(alumno)

        if self.listadoAlumnos == "predeterminado":
            self.listadoAlumnos = lista
        else:
            self.listadoAlumnos = self.listadoAlumnos + lista


    @classmethod
    def asignarNombre(cls, nombre = "Grupo 6"):
        cls.grado = nombre
    

    def __str__(self):

        return f"Grupo de estudiantes: {self.listadoAlumnos}"

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 6"):
    #     cls.grado = nombre

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 4"):
    #     cls.grado = nombre
