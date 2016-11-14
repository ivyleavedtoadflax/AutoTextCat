import os, pickle
from flask import Flask, request, redirect, url_for, make_response
#from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from classify import classify

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
         filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):

            # Do note save the file to ensure no persistence on the server
            # Operate directly on the bytestream in 'file'
            
            #filename = secure_filename(file.filename)
            #content = pd.read_csv(file)
            intent = classify.survey()
            intent.load(file)
            intent.clean_raw()
            intent.clean_urls()
            intent.api_lookup()

            no_comments = (intent.data['comment_further_comments'] == 'none') & (intent.data['comment_where_for_help'] == 'none') & (intent.data['comment_other_where_for_help'] == 'none') & (intent.data['comment_why_you_came'] == 'none')
            easy_nones = intent.data.loc[no_comments,'respondent_ID'].astype(int)

            intent.data = intent.data.loc[~no_comments]
            #download_file = Response(intent.data.to_csv(),mimetype='text/csv')
            output = make_response(intent.data.to_csv())
            output.headers["Content-Disposition"] = "attachment; filename=export.csv"
            output.headers["Content-type"] = "text/csv"
            return(output)
#            
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',filename=filename))

    return '''
<!doctype html>
<h1>Automate classification of GOV.UK intents survey</h1>
<h3>Instructions</h3>
<p>Select a survey file downloaded as CSV file from survey monkey, and click upload. The app will then:</p>
<ul>
<li>Clean the data</li>
<li>Look up org and section data using the content API</li>
<li>Automatically classify both <code>ok</code> and <code>none</code> cases </li>
<li>Incorporate predictions, org, and section to the the original dataset, and download as a CSV file.</li>
</ul>
<p><em>Ensure that no personal identifying information is uploaded to this service.</em></p>
<p>Note that no physical copy of the uploaded file is retained on the server.</p>
<form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file>
       <input type=submit value=Upload>
</form>
<h3>Documentation</h3>
<ul>
<li><a href="https://github.com/ivyleavedtoadflax/classify">classify module</a>: responsible for data cleansing.</li>
</ul>
<h3>Classify version: 0.4.0</h3>
<h3>Model: adaboost classifier</h3>
'''
