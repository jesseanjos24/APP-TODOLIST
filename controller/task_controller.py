from model.task_model import TaskModel


class TaskController:
    def __init__(self):
        self.model = TaskModel()

    def load_tasks(self):
        return self.model.load_tasks()

    def get_tasks(self):
        return self.model.get_tasks()

    def add_task(self, title, date, tags):
        return self.model.add_task(title, date, tags)

    def toggle_task(self, task_id, state):
        self.model.toggle_task(task_id, state)

    def delete_task(self, task_id):
        self.model.delete_task(task_id)

    def sort_by_date(self):
        self.model.sort_by_date()

    def separate_tasks(self):
        return self.model.separate_tasks()

    def separate_task_tag(self):
        return self.model.separate_task_tag()
