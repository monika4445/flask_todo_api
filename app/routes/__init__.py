from flask import Blueprint
from .task_routes import *

task_bp = Blueprint('tasks', __name__)
