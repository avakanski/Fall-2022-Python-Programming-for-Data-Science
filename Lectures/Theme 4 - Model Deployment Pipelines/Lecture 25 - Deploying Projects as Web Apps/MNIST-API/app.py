from flask import Flask, render_template,request
from PIL import Image
import numpy as np
import tensorflow.keras.models
import re
import sys 
import os
import base64
sys.path.append(os.path.abspath("./model"))
from load import * 

global model

model = init()

app = Flask(__name__)

@app.route('/')
def index_view():
    return render_template('index.html')

def convertImage(imgData1):
	imgstr = re.search(b'base64,(.*)',imgData1).group(1)
	with open('output.png','wb') as output:
	    output.write(base64.b64decode(imgstr))

@app.route('/predict/',methods=['GET','POST'])
def predict():
	imgData = request.get_data()
	convertImage(imgData)

	x = Image.open('output.png')

	x = x.resize((28,28))

	x = np.invert(x)

	x = x[:,:,0].reshape(1,28,28,1)
    
	x = x/255
    
	out = model.predict(x)
	print(out)
	print(np.argmax(out,axis=1))

	response = np.array_str(np.argmax(out,axis=1))
	return response	

if __name__ == '__main__':
    app.run(debug=True, port=8000)
