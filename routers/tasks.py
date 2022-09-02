from fastapi import APIRouter
from classes.tasks import Tasks
from schemas.schemas import SchemaCreateTask, SchemaUpdateTask, SchemaRemoveTasks

router = APIRouter()


@router.get('/tasks')
def get_all_tasks():
    result = Tasks().get_all_tasks()

    return result


@router.post("/tasks")
def insert_task(schema: SchemaCreateTask):
    task = Tasks().insert_task(schema)
    return task


@router.post("/tasks/delete") # да очаква лист с таскове, SchemaDeleteTask
def remove_task(schema: SchemaRemoveTasks):
    result = Tasks().remove_task(schema.tasks)

    return result


@router.patch("/tasks")  # да ъпдейтва повече от 1 таск едновременно
def update_task(schema: SchemaUpdateTask):
    result = Tasks().update_task(schema)

    return result


@router.get('/tasks/completed')
def completed_tasks():
    result = Tasks().completed_tasks()
    return result


@router.get('/tasks/pending')
def pending_tasks():
    result = Tasks().pending_tasks()
    return result
