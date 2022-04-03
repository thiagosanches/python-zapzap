from flask import Flask,request
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    name = "This is the route."
    return name

@app.route('/sendMessage',methods=['POST'])
def hello():
    request_data = request.get_json()
    file = open("C:\\Users\\thiago.DESKTOP-TT0ETA0\\Downloads\\my-sikulli-test.sikuli\\my-sikulli-test.py", mode='r')
    fileContent = file.read()
    file.close()

    print("Writing new content to the file...")
    newFileContent = fileContent.replace("@NAME", request_data['name']).replace("@BODY", request_data['body'])
    fileName = uuid.uuid1().hex + ".py"
    print(fileName)
    
    newFile = open(fileName, "a")
    newFile.write(newFileContent)
    newFile.close()
    
    print("Going to execute sikulixide...")
    os.system("java -jar C:\\_tools\\sikulixide-2.0.5.jar -r ./"+ fileName)
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')