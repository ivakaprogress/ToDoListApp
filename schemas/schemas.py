from pydantic import BaseModel


class SchemaCreateTask(BaseModel):
    id: int
    description: str


class SchemaUpdateTask(BaseModel):
    tasks: list


class SchemaRemoveTasks(BaseModel):
    tasks: list
