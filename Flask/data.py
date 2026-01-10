import json
from task import Fields

class Data:

    __file_path = "Flask/Files/tasks.json"

    def read_json(self):
        data = []
        try:
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                return data
        except Exception as ex:
            print(f"Error reading JSON: {ex}")
            return data
        
    def get_tasks_by_status(self, status):
        all_tasks = self.read_json()
        filtered_tasks = [task for task in all_tasks if task[Fields.STATUS.value] == status]
        return filtered_tasks
    
    def get_task_by_id(self, task_id):
        all_tasks = self.read_json()
        for task in all_tasks:
            if task[Fields.ID.value] == task_id:
                return task
        return None
    
    def add_task(self, task):
        task[Fields.ID.value] = self.generate_id()
        all_tasks = self.read_json()
        all_tasks.append(task)
        self.save_json(all_tasks)

    def get_last_task(self):
        all_tasks = self.read_json()
        if all_tasks:
            return all_tasks[-1]
        return None
    
    def update_task(self, task_id, updated_task):
        all_tasks = self.read_json()
        for index, task in enumerate(all_tasks):
            if task[Fields.ID.value] == task_id:
                all_tasks[index][Fields.TITLE.value] = updated_task[Fields.TITLE.value]
                all_tasks[index][Fields.DESCRIPTION.value] = updated_task[Fields.DESCRIPTION.value]
                all_tasks[index][Fields.STATUS.value] = updated_task[Fields.STATUS.value]
                self.save_json(all_tasks)
                return all_tasks[index]
        return None

    def delete_task(self, task_id):
        all_tasks = self.read_json()
        for index, task in enumerate(all_tasks):
            if task[Fields.ID.value] == task_id:
                deleted_task = all_tasks.pop(index)
                self.save_json(all_tasks)
                return deleted_task
        return None

    def save_json(self, data):
        try:
            with open(self.__file_path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4)
        except Exception as ex:
            print(f"Error saving JSON: {ex}")

    def generate_id(self):
        all_tasks = self.read_json()
        if not all_tasks:
            return 1
        max_id = max(task[Fields.ID.value] for task in all_tasks)
        return max_id + 1