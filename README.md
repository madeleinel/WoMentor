# WoMentor / WomenToTech

## CONCEPT: a platform which helps you (a woman in tech) find a mentor!
* For self-identifying women!
* Prospective mentees and mentors can sign up on the platform to create a profile
* Using the twitter API these profiles will be tweeted with the hashtag #WomenToTech through our [Twitter account](https://twitter.com/WomenToTech), and they will also be displayed on the website
* Mentors and mentees can look through existing profiles on the site, and sort through and filter them based on the profile content

## File structure
* Main folder:
  * The main file, "app.py", which launches the page (Flask and all HTML/CSS files are linked/imported to this file)
  * Subfolders: Templates and Static
* Templates folder:
  * All HTML files (one for each URL extension)
* Static folder:
  * All CSS files (one for each URL extension)

## To run the app
* Clone the repo
* Run "python app.py" in the command line
* Go to http://127.0.0.1:5000/ or http://127.0.0.1:5000/mentee_signup or http://127.0.0.1:5000/mentor_signup to see the current content

## To create a virtual environment
* [Detailed documentation can be found on the Hitchhiker's guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)
* Alternatively just follow the instructions below!
  * If you don't already have virtualenv installed you should install it and navigate to your project folder
  * Create the environment using `virtualenv **environment-name**`
  * Enter the environment with `source **environment-name**/bin/activate`
  * You should then be inside the environment and can install the required packages from `requirements.txt` with `pip install -r requirements.txt`
  * When you're finished working in the environment you can `deactivate` it
```
$ pip install virtualenv
$ cd womentor_project_folder
$ virtualenv womentor_env
$ source womentor_env/bin/activate
(womentor_env) $ pip install -r requirements.txt
(womentor_env) $ deactivate
$
```
  * you should only need to do this step once, after that you can just run the environment, freezing your `requirements.txt` file as needed!
  * we can then be sure that we're running the same versions of whatever we packages we are using
  * it should also stop any interference between other packages you might have that are not used in the project

## To start the database and create the tables from scratch
(ensure you have a valid address for a db)
navigate to your project folder and open the python interpreter

```
yourMachine:projectFolder yourUser$ python
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from cordb import db
>>> from app import create_app
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
```

if you open the db you should now see that the empty tables have been created as specified in the `flask_data_models.py` file
