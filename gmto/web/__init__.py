import json
import os.path
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import SubmitField

from ..backend import get_proba
from ..helpers import read_falcon_data


class UploadForm(FlaskForm):
    file = FileField(
        "Upload .json file", validators=[FileRequired(), FileAllowed((["json"]))]
    )
    submit = SubmitField("Upload")


app = Flask(__name__)
app.config["SECRET_KEY"] = "5791666bb0b13ce0c676dfde282ba245"
app.config["FALCON_DATA_PATH"] = os.path.join(
    os.path.dirname(__file__), "data/millennium-falcon.json"
)

@app.route("/", methods=["GET", "POST"])
def upload():
    """_summary_

    Returns
    -------
    _type_
        _description_
    """
    form = UploadForm()
    probas = None

    if form.validate_on_submit():
        empire_data = json.load(form.file.data)
        falcon_data = read_falcon_data(app.config["FALCON_DATA_PATH"])

        # compute probability of success
        probas = get_proba(empire_data, falcon_data)

    return render_template("home.html", form=form, probas=str(probas))
