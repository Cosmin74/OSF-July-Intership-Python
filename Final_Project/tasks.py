from flask import Blueprint, jsonify, request, render_template
from model import Task
from peewee import JOIN

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_users():
    tasks = list(Task.select())
    return render_template('tasks.html', tasks=tasks)

