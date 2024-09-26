from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms import LoginForm, VulnerabilityForm
from models import db, User, Vulnerability

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vulntrack.db'
app.config['SECRET_KEY'] = 'yoursecretkey'

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    vulnerabilities = Vulnerability.query.all()
    return render_template('dashboard.html', vulnerabilities=vulnerabilities)

@app.route('/add_vulnerability', methods=['GET', 'POST'])
@login_required
def add_vulnerability():
    form = VulnerabilityForm()
    if form.validate_on_submit():
        vuln = Vulnerability(
            cve_id=form.cve_id.data,
            severity=form.severity.data,
            description=form.description.data
        )
        db.session.add(vuln)
        db.session.commit()
        flash('Vulnerability added successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_vulnerability.html', form=form)

if __name__ == '__main__':
    app.run(host="10.0.2.6",debug=True)

