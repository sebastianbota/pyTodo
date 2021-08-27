from flask import Blueprint
from flask.templating import render_template

# Define the blueprint: 'todo', set its url prefix: app.url/todo
mod_todo = Blueprint('todo', __name__, url_prefix='/todo')

#Define the default route for this module
@mod_todo.route('/', methods=['GET'])
def index():
    return render_template('todo/index.html')
