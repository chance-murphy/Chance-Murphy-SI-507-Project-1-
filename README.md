<h1>Chance Murphy 507 Project 1</h1>

<p>
This project imports code for the file lab3_code.py to the SI507_project_1.py
and uses that code to create a flask app. This flask app can be ran downloading
the required files and installing the requirments.txt file.
<br>
To run the flask app and install the requirments.txt file, you'll need to create
a virtual enviornment. In order to do this type in the following commands into
your command promot/terminal window.
<br>
1: python3 -m venv project1-env
<br>
source project1-env/bin/activate for Mac/Linux OR source project1-env/Scripts/activate for Windows
<br>
pip install -r requirements.txt
<br>
Once you have installed the requirments you can then run your flask app by typing in...
<br>
python SI507_project_1.py runserver
<br>
From here you'll be prompted and given a local host address. Copy this into a web
and you can then freely run the flask app. Addresses you can enter into the local
host url are as follows.
<br>
<h3>Home Page:</h3> http://localhost:5000/
<br>
<h3>Bank Name Page:</h3> http://localhost:5000/bank/<name>
<br>
<h3>Currency Page:</h3> http://localhost:5000/(pound/yuan/dollar)/<amount>
<br>
<h3>Account Holdings Page:</h3> http://localhost:5000//bank/<name>/(Pound/Yuan/Dollar)/<amount>
<br>
Once you are done you can quit the flask app by hitting Control+C.
<br>
<h2>Overall Grade</h2> 1000/1000
</p>
