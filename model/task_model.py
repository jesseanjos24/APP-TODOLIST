from datetime import datetime, timedelta

from utils.utilities import load_data, save_tasks


class TaskModel:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        self.tasks = load_data()
        return self.tasks

    def get_tasks(self):
        return self.tasks

    def add_task(self, title, date, tags):
        new_task = {
            "id": max([t["id"] for t in self.tasks], default=0) + 1,
            "title": title,
            "done": False,
            "date": date,
            "tags": tags,
        }
        self.tasks.append(new_task)
        save_tasks(self.tasks)
        return new_task

    def toggle_task(self, task_id, state):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = state == 2
                break
        save_tasks(self.tasks)

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        save_tasks(self.tasks)

    def sort_by_date(self):
        def parse_date(task):
            date = task.get("date")
            if date:
                try:
                    return datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    return datetime.max
            return datetime.max

        self.tasks.sort(key=parse_date)
        save_tasks(self.tasks)

    def separate_tasks(self):
        today_now = datetime.today().date()
        tomorrow_now = today_now + timedelta(days=1)

        today = []
        tomorrow = []
        upcoming = []
        completed = []

        for task in self.tasks:
            if task.get("done"):
                completed.append(task)
                continue

            data_str = task.get("date")
            if not data_str:
                continue

            try:
                data = datetime.strptime(data_str, "%Y-%m-%d").date()
            except ValueError:
                continue

            if data == today_now:
                today.append(task)
            elif data == tomorrow_now:
                tomorrow.append(task)
            elif data > tomorrow_now:
                upcoming.append(task)

        return today, tomorrow, upcoming, completed

    def separate_task_tag(self):
        work, personal, leisure, study, day_by_day = [], [], [], [], []

        for task in self.tasks:
            if task.get("done"):
                continue

            tags = task.get("tags", [])
            for tag in tags:
                if tag == "Trabalho":
                    work.append(task)
                elif tag == "Pessoal":
                    personal.append(task)
                elif tag == "Lazer":
                    leisure.append(task)
                elif tag == "Estudo":
                    study.append(task)
                elif tag == "Dia A Dia":
                    day_by_day.append(task)

        return work, personal, leisure, study, day_by_day
