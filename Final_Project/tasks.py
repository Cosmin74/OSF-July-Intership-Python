from flask import Blueprint, jsonify, app, request, render_template
from model import Task
from peewee import JOIN

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_users():
    tasks = list(Task.select())
    return render_template('tasks.html', tasks=tasks)

@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    task = Task.get_or_none(Task.task_id == task_id)
    if task:
        return render_template('task.html', task=task)
    else:
        return jsonify({"error": "Task not found."}), 404

@task_bp.route('/submit_task', methods=['POST'])
def submit_task():
    task_title = request.form.get('task_title')
    task_description = request.form.get('task_description')  
    task = Task(task_title=task_title, task_description=task_description)
    task.save()
    return """
    <script>
        alert('Task submitted successfully!');
        window.location.href = '/tasks'; 
    </script>
    """