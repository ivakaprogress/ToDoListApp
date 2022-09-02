from functions.file_manager import read_file, update_file


class Tasks(object):
    def __init__(self):
        self.tasks = read_file()

    def is_task_exist(self, task_id):
        if task_id in self.tasks:
            return True
        else:
            return False

    def get_all_tasks(self):

        return self.tasks

    def insert_task(self, data):

        if data.id not in self.tasks:
            if data.description != '':
                self.tasks[data.id] = {"status": False, "description": data.description}
                update_file(self.tasks)
                return {"status": "success", "message": "Item has been successfully added"}
            else:
                return {'Error': 'description is empty'}
        else:
            return {"Error": "There is already a task. "}

    def remove_task(self, tasks):
        non_existing_tasks = []
        deleted_tasks = []
        message = ''
        for task in tasks:
            if task in self.tasks:
                deleted_tasks.append(task)
                self.tasks.pop(task)
                update_file(self.tasks)
            else:
                non_existing_tasks.append(task)
        if deleted_tasks and non_existing_tasks:
            if len(deleted_tasks) > 1 and len(non_existing_tasks) > 1:
                message += f'Tasks {", ".join([str(x) for x in deleted_tasks])} were removed, tasks {", ".join([str(x) for x in non_existing_tasks])} do not exist'
            else:
                message += f'Task {", ".join([str(x) for x in deleted_tasks])} was removed, task {", ".join([str(x) for x in non_existing_tasks])} do not exist'
        elif deleted_tasks and not non_existing_tasks:
            if len(deleted_tasks) > 1:
                message += f'Tasks {", ".join([str(x) for x in deleted_tasks])} were removed'
            else:
                message += f'Task {", ".join([str(x) for x in deleted_tasks])} was removed'
        elif not deleted_tasks:
            message += f'Tasks do not exist'
        return {'status': 'success', 'message': f'{message}'}

    def update_task(self, data):

        for task in data.tasks:
            if task['id'] in self.tasks:
                if self.tasks[task['id']]['description'] != task['description'] and task['description'] != '':
                    self.tasks[task['id']] = {"status": task['status'], "description": task['description']}  # ?
                else:
                    self.tasks[task['id']]['status'] = task['status']
                update_file(self.tasks)
            else:
                print("Error: There is no task with that id.")

        return {"status": "success", "message": "Task has been successfully updated"}

    def completed_tasks(self):
        completed_tasks_list = []

        for task in self.tasks:
            if self.tasks[task]['status'] is True:
                self.tasks[task]['id'] = task  # ?
                completed_tasks_list.append(self.tasks[task])
        return {'status': 'success', 'data': completed_tasks_list}

    def pending_tasks(self):
        uncompleted_tasks = []
        for task in self.tasks:
            if self.tasks[task]['status'] is False:
                self.tasks[task]['id'] = task
                uncompleted_tasks.append(self.tasks[task])
        return {'status': 'success', 'data': uncompleted_tasks}
