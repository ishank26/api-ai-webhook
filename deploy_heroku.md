## Steps to deploy python app using Git and Heroku

* Generate **requirements.txt** containing a list of required packages for app. If you're using virtualenv execute - `$ pip freeze > requirements.txt`

* Add **Procfile** lisitng the command to run app. For python - `web: python app_name.py`

* Push changes to git 

* Install Heroku CLI

* Add heroku to remote-`$ heroku git:remote -a heroku_app_name`. Check if heroku added to remote- `$ git remote -v`

* Execute `$ heroku create --buildpack heroku/python` for python build. 

* Check error logs if deployment unsuccessful- `$ heroku logs -n 50`
