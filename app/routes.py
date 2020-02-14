from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import StorySpecForm
from news_search import searching



@app.route('/', methods=['GET', 'POST'])
def index():
    
    form = StorySpecForm()

    if form.validate_on_submit() :
        results  = searching.search(form.search_string.data)
        session["prior_results"] = results
        redirect(url_for('.index'))

    try:
        results == ""
    except NameError:
        results = ""
         
    return render_template("StorySpecInput.html", title='Search news', form=form, prior_results=results)
