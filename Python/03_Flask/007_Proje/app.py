from flask import Flask, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime as dt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veritabani.db'
db = SQLAlchemy(app)

class User(db.Model):
    """Data model for user accounts."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    bio = db.Column(db.Text, index=False, unique=False, nullable=True)
    admin = db.Column(db.Boolean, index=False, unique=False, nullable=False)


@app.route('/', methods=['GET'])
def create_user():
    """Create a user via query string parameters."""
    username = request.args.get('user')
    email = request.args.get('email')
    
    if username and email:
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        
        if existing_user:
            return make_response(f'{username} ({email}) already created!')
        
        new_user = User(username=username,
                        email=email,
                        created=dt.now(),
                        bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
                        admin=False)  # Create an instance of the User class
        
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    
    return render_template('users.jinja2',
                           users=User.query.all(),
                           title="Show Users")

if __name__ == "__main__":
    app.run(debug=True)