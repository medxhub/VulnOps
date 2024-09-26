from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class VulnerabilityForm(FlaskForm):
    cve_id = StringField('CVE ID', validators=[DataRequired()])
    severity = SelectField('Severity', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('critical', 'Critical')])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

