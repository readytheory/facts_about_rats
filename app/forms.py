from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class StorySpecForm(FlaskForm):
    search_string = StringField('Search Criteria')
    date_spec_start = StringField('Date Start')
    date_spec_end  = StringField('Date End')
    submit = SubmitField('News me')
        
    
