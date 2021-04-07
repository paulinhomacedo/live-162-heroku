# live-162-heroku
*heroku login

mkdir live_162_heroku
cd live_162_heroku

poetry init -n
poetry shell

--cria repo local git (ls -a) (cat .git/config)
git init

poetry add gunicorn(sincrono)

heroku create live-162-macedo
https://live-162-macedo.herokuapp.com/

*nao esquecer de add python-dotenv
 export FLASK_APP=app:create_app
 export FLASK_ENV=development

git add .
git commit -m "first commit."
git push heroku master

heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
git push heroku master

git push heroku main:main

alterar versao do python no pyproject.toml python = "3.9.2"

poetry update

git add .
git commit -m "versao do python fixa 3.9.2"

https://dbdiagram.io/home





