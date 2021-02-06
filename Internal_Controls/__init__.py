from flask import Flask
app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'C:\\Users\\ThierryHaddad\\source\\repos\\Internal_Controls\\Internal_Controls\\static\\uploads'



import Internal_Controls.views
