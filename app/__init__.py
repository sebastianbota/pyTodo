from flask import Flask, render_template

app = Flask(__name__)

#Configurations
app.config.from_object('config')

from app.mod_todo.controllers import mod_todo as todo_module
app.register_blueprint(todo_module)

#Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')