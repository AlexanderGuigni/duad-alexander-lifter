from flask import Flask, request
from data import Data
from task import Task, Fields

app = Flask(__name__)

@app.route("/getAllTasks", methods=["GET"])
def getAllTasks():
    tasks_data = Data()
    tasks = tasks_data.read_json()
    return tasks

@app.route("/getTaskByStatus/<task_status>", methods=["GET"])
def getTaskByStatus(task_status):
    tasks_data = Data()
    tasks = tasks_data.get_tasks_by_status(task_status)
    return tasks

@app.route("/getTaskById/<task_id>", methods=["GET"])
def getTaskById(task_id):
    tasks_data = Data()
    task = tasks_data.get_task_by_id(int(task_id))
    return task

@app.route("/create", methods=["POST"])
def create():
    try:
        if Fields.TITLE.value not in request.json or Fields.DESCRIPTION.value not in request.json or Fields.STATUS.value not in request.json:
            raise ValueError("Missing required fields.")
        new_task = Task.from_dict(request.json)
        tasks_data = Data()
        tasks_data.add_task(new_task.get_task_as_dict())
        return {"message": "Task created successfully.", "task": tasks_data.get_last_task()}, 201
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred."}, 500


@app.route("/edit/<id>", methods=["PUT"])
def edit(id):
    try:
        if Fields.TITLE.value not in request.json or Fields.DESCRIPTION.value not in request.json or Fields.STATUS.value not in request.json:
                raise ValueError("Missing required fields.")
        task_data = Data()
        updated_task = Task.from_dict(request.json).get_task_as_dict()
        task = task_data.update_task(int(id), updated_task)
        if task is None:
            return {"error": "Task not found."}, 404
        return {"message": "Task updated successfully.", "task": task}, 200
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred."}, 500


@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    try:
        task_data = Data()
        task = task_data.delete_task(int(id))
        if task is None:
            return {"error": "Task not found."}, 404
        return {"message": "Task deleted successfully.", "task": task}, 200
    except Exception as ex:
        return {"error": "An unexpected error occurred."}, 500

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)