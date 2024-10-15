from flask import Flask,render_template, request
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
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)