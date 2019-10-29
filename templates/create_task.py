from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextField, SelectField
import wtforms.validators as Validators
from repositories.task_repository import TaskRepository

TASK_REPO = TaskRepository()

class CreateTaskForm(FlaskForm):
    title = StringField("Title", [Validators.input_required()], render_kw={"placeholder": "Ticket title"})
    description = TextField("Description", [Validators.input_required()], render_kw={"placeholder": "Ticket description"})
    completion_date = StringField("Expected completion", render_kw={"placeholder": "Expected completion date"})
    state = SelectField("Task state", choices=[(taskState.id, taskState.state) for taskState in TASK_REPO.get_task_states()], coerce=int)
    worker = StringField("Worker", [Validators.input_required()], render_kw={"placeholder": "Assign task to worker"})
    ticket = StringField("Ticket", render_kw={"readonly": True})
