import os
import uuid
from flask import Flask,render_template, request, Response,send_from_directory, jsonify
import pandas as pd 

app = Flask(__name__,template_folder='templates')

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'user' and password == 'password':
            return 'Success'
        else:
            return 'Fail'
        
@app.route('/file_upload',methods = ['POST'])
def file_upload():
    file = request.files['file']

    if file.filename.endswith('.txt'):
        return file.read().decode()
    elif file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
        return df.to_html()

@app.route('/convert_to_csv',methods = ['POST'])
def convert_to_csv():
    file = request.files['file']
    df = pd.read_excel(file)
    response = Response(
        df,
         mimetype="text/csv",
        headers={
                "Content-Disposition": "attachment; filename=result.csv"
        }
    )
    return response
@app.route('/convert_to_csv2',methods = ['POST'])
def convert_to_csv2():
    file = request.files['file']
    df = pd.read_excel(file)
    if not os.path.exists('downloads'):
        os.mkdir('downloads')

    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads',filename))
    
    return render_template(template_name_or_list='download.html', filename= filename) 
    
@app.route('/downloads/<filename>')
def download(filename):
    return send_from_directory('downloads',filename , download_name = 'result.csv')

@app.route('/handle_post',methods = ['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']
    
    with open('file.txt','w') as f:
        f.write(f'{greeting}, {name}')
        
    return jsonify({'message': "Successfully written"})
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)