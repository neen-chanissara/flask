# flask Restful API 

#Flask is a web framework written for Python to be used together with a webserver such as Apache and accepted by leading community we #pages such as Pinterest, LinkedIn etc. Flask is called a micro framework because it doesn't need any tools or libraries. It does not #need a database. However, Flask will still be able to add special extensions if it supports Flask.

## Setup
### step 1 Python install virtual environments lib
pip install virtualenvwrapper-win
### step 2 Python create virtual environments
mkvirtualenv _{Name virtual environments}_
### step 3 Python virtual environments workon
workon _{Name virtual environments}_
### step 4 Python lib install to virtual environments 
pip install -r requirements.txt
> if don't want virtual environments, can pass step 2-3


## Start project flask

first Python Flask API

pip install -r requirements.txt

### step 1 Python virtual environments workon 
workon {Name virtual environments}
> if haven't virtual environments, can pass step 1
### step 2 Run Python
python app.py

## docker build and complie 
### step 1 
docker build -t flask_api:latest .
### step 2
docker run --name flask -i -d -p 5000:5000 flask_api:latest
<!-- docker run --name flask --restart=always -i -d -p 5001:5000 flask_api:latest -->


<!-- Quick Start -->
<!-- If you are not already logged in, you need to authenticate to the Container Registry by using your GitLab username and password. If you have Two-Factor Authentication enabled, use a Personal Access Token instead of a password. -->
