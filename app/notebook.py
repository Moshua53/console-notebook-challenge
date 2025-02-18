from datetime import datetime
class Note:
    HIGH:str="HIGH"
    MEDIUM:str="MEDIUM"
    LOW:str="LOW"
    def __init__(self,code:str,title:str,text:str,importance:str,):
        self.code:str=code
        self.title:str=title
        self.text:str=text
        self.importance:str=importance
        self.creation_date:datetime=datetime.now()
        self.tags:list[str]=[]
    #Metodos
    def add_tag(self,tag:str):
        if tag not in self.tags:
            self.tags.append(tag)

    def fecha_creacion(self):
        return f"{self.creation_date}-{self.title}"

    class Notebook:
        #Atributos
        def __init__(self):
            self.notes:list[Note]=[]
        #Metodos
        Numero_notas = int(len(self.notes))
        def add_note(self,title:str,text:str,importance:str)-> int:
            code=Numero_notas+
            






