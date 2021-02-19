# tribe-stats

Set up virtual environment to recreate
```
pip install virtualenv
virtualenv tribe
source tribe/bin/activate
...
deactivate
```

Install modules
```
pip install -r requirements.txt
pip install -r requirements.in
```

Set up Heroku
```
brew install heroku/brew/heroku
heroku login
heroku create
git push heroku main
heroku open
```