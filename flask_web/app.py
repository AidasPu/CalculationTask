import random
import time

from flask import Flask, session, request, render_template
from numpy import sum as npsum

from core_calculations.calculations import cell_power_calculations
from flask_web.forms.calculation_input_form import PlantCalculationForm

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.template_folder = "Templates"


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if session.get('user_identifier') is None:
            user_indetification = ""
            for _ in range(random.randint(10, 20)):
                number = random.randint(10, 1000)
                user_indetification = + number
            session['user_identifier'] = user_indetification
        form = PlantCalculationForm()
        context = {"form": form}
        return render_template("index.html", **context)
    else:
        form = PlantCalculationForm()
        args = eval(form.args.data)

        start = time.time()
        result = npsum(cell_power_calculations(form.initial_cell_power.data, *args))
        end = time.time() - start

        power_plant_info = [result, form.initial_cell_power.data, form.power_plant_name.data, form.client.data, end]

        context = {"power_plant": power_plant_info}
        if session.get('power_plants'):
            session['power_plants'] += [power_plant_info]
        else:
            session['power_plants'] = [power_plant_info]

        return render_template("power_plant_page.html", **context)


@app.route("/session_history", methods=['GET'])
def history():
    if session.get('power_plants'):
        power_plants = session.get('power_plants')
        context = {'power_plants': power_plants}
        return render_template("power_plant_history.html", **context)

    return render_template("power_plant_history.html")


if __name__ == "__main__":
    app.run()
