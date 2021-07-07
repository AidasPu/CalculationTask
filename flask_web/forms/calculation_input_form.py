from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField
from wtforms.validators import DataRequired, NumberRange


class PlantCalculationForm(FlaskForm):
    client = StringField('Client', validators=[DataRequired()])
    power_plant_name = StringField('Plant name', validators=[DataRequired()])
    initial_cell_power = FloatField("Initial power of cells", validators=[DataRequired(), NumberRange()])
    args = TextAreaField("Input plant information", validators=[DataRequired()])
