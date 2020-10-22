from flask import Flask, render_template, session, redirect, url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import SubmitField,FileField
from flask_wtf.file import FileField, FileRequired, FileAllowed 
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from flask_caching import Cache
from strip import stripping
from time import sleep
import os
import json


app = Flask(__name__)
csrf = CSRFProtect()
app.config['SECRET_KEY'] = '325245hkhf486axcv5719bf9397cbn69xv'
UPLOAD_FOLDER=os.path.join('static','uploads' )
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20MB max-limit.
csrf.init_app(app)


bootstrap = Bootstrap(app)
moment = Moment(app)

class PhotoForm(FlaskForm):
    photo = FileField('Pic',validators=[FileRequired(), FileAllowed(['jpg', 'png','gif','nii','mnc'], 'Images only!')])
    
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.template_filter('wait')
def wai():
    sleep(3)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PhotoForm()
    file_name=None
    img_path=None
    skull =None
    segment=None
    uploads1_dir='static/uploads1'
   
    if form.validate_on_submit():
        uploads1_dir = os.path.join( 'static','uploads1')
        file_name=secure_filename(form.photo.data.filename)
       
        if file_name is not "":
            #file_name=os.path.join(app.config['UPLOAD_FOLDER'],file_name)

            photo=form.photo.data
            photo.save(os.path.join(uploads1_dir, file_name))
            path=os.path.join(uploads1_dir,file_name)
            stripping(path)
            sleep(3)
            flash('Image uploaded successfully.')
    return render_template('index.html', form=form,file_name=file_name,uploads1_dir=uploads1_dir,img_path=img_path,skull=json.dumps(skull),segment=json.dumps(segment))

if __name__ == "__main__":
    app.run(debug=True)