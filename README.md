# SPEX Website
So the intention of this project is to be the webserver/website for the RIT Space Exploration group. We will be using [Flask](http://flask.pocoo.org/) as the webframework and [Bootstrap](http://getbootstrap.com/) for the styling of the website. This site is deployed using the Openshift Platform.

### Technologies used:
- [Flask](http://flask.pocoo.org/) - web framework
- [Bootstrap](http://getbootstrap.com/) - html,cs,js framework
- [Jinja2](http://jinja.pocoo.org/docs/dev/) - templating
- Python 3.4.3+

### Install and Run
For those  new to python, read up on virtual environments to create a clean slate to install on.
- [virtualenv](https://virtualenv.pypa.io/en/stable/)
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

```
$ pip install -r ./requirements.txt
$ export FLASK_APP=spex.py
$ flask run
```
