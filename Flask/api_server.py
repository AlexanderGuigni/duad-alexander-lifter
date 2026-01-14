from flask import Flask, request
from data import Data
from task import Task, Fields, TaskStatus

app = Flask(__name__)

tasks_data = Data()

@app.route("/tasks", methods=["GET"])
def getAllTasks():
    task_status = request.args.get("status")
    
    try:
        if (task_status is not None):
            if task_status not in [status.value for status in TaskStatus]:
                raise ValueError("Invalid status value.")
            tasks = tasks_data.get_tasks_by_status(task_status)
            return tasks
        else:
            tasks = tasks_data.read_json()
            return tasks
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500

@app.route("/tasks", methods=["POST"])
def create():
    try:
        new_task = Task.from_dict(request.json)
        tasks_data.add_task(new_task.get_task_as_dict())
        return {"message": "Task created successfully.", "task": tasks_data.get_last_task()}, 201
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500


@app.route("/tasks/id/<id>", methods=["PUT"])
def edit(id):
    try:
        updated_task = Task.from_dict(request.json).get_task_as_dict()
        task = tasks_data.update_task(int(id), updated_task)
        if task is None:
            return {"error": "Task not found."}, 404
        return {"message": "Task updated successfully.", "task": task}, 200
    except ValueError as ex:
        return {"error": str(ex)}, 400
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500


@app.route("/tasks/id/<id>", methods=["DELETE"])
def delete(id):
    try:
        task = tasks_data.delete_task(int(id))
        if task is None:
            return {"error": "Task not found."}, 404
        return {"message": "Task deleted successfully.", "task": task}, 200
    except Exception as ex:
        return {"error": "An unexpected error occurred.", "details": str(ex)}, 500

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)