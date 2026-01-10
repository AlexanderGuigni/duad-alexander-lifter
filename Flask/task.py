from enum import Enum

class Task:

    def __init__(self, title, description, TaskStatus):
        self.title = self.validate_not_empty(Fields.TITLE.value, title)
        self.description = self.validate_not_empty(Fields.DESCRIPTION.value, description)
        self.status = TaskStatus

    def validate_not_empty(self, field_name, value):
        if not value.strip():
            raise ValueError(f"{field_name} cannot be empty.")
        return value
    
    def get_task_as_dict(self):
        return {
            Fields.TITLE.value: self.title,
            Fields.DESCRIPTION.value: self.description,
            Fields.STATUS.value: self.status.value
        }
    
    @classmethod
    def from_dict(cls, data):
        title = data.get(Fields.TITLE.value, "")
        description = data.get(Fields.DESCRIPTION.value, "")
        status_str = data.get(Fields.STATUS.value, "")
        status = TaskStatus(status_str)
        return cls(title, description, status)

class TaskStatus(Enum):
    POR_HACER = "Por Hacer"
    EN_PROGRESO = "En Progreso"
    COMPLETADA = "Completada"

class Fields(Enum):
    TITLE = "title"
    DESCRIPTION = "description"
    STATUS = "status" 
    ID = "id"   