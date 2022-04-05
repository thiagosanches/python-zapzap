from flask import Flask,request
import os
import uuid

app = Flask(__name__)

def read_template():
    file = open("C:\\Users\\thiago.DESKTOP-TT0ETA0\\Downloads\\my-sikulli-test.sikuli\\my-sikulli-test.py", mode='r')
    file_content = file.read()
    file.close()
    return file_content

def generate_file_name():
    file_name = uuid.uuid1().hex + ".py"
    return file_name

def prepare_sikulixide_execution(template_content, request_data, final_file):
    print("Writing new content to the file...")
    new_file_content = template_content.replace("@NAME", request_data['name']).replace("@BODY", request_data['body'])
    
    new_file = open(final_file, "a")
    new_file.write(new_file_content)
    new_file.close()

@app.route('/')
def index():
    name = "This is the route."
    return name

@app.route('/sendMessage',methods=['POST'])
def send_message():
    request_data = request.get_json()
    template_file = read_template()
    final_file = generate_file_name()
    prepare_sikulixide_execution(template_file, request_data, final_file)
    
    print("Going to execute sikulixide...")
    os.system("java -jar C:\\_tools\\sikulixide-2.0.5.jar -r ./"+ final_file)
    return "OK"

@app.route('/sendMessages',methods=['POST'])
def send_messages():
    request_data = request.get_json()
    template_file = read_template()
    final_file = generate_file_name()

    for data in request_data:
        prepare_sikulixide_execution(template_file, data, final_file)
    
    print("Going to execute sikulixide...")
    os.system("java -jar C:\\_tools\\sikulixide-2.0.5.jar -r ./"+ final_file)
    return "OK"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
