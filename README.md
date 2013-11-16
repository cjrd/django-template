Django Project Template
==============

This template is my own personal (evolving) preference. You may do wahtever you wish with it (see the license) without mentioning that I even exist.

## Template includes

included django modules (see requirements.txt):
* south
* werkzeurg
* django-compressor
* django-appconf
* django-devserver
* guppy
* sqlparse
* wsgiref
* six

## How to use this template

### Preliminary requirements
* Install python 2.7X. NB: install `python-devel` if you're using a package manager such as apt-get. The following command should print a path (if this command raises an exception, make sure that you have the `python-devel` version installed):
* 
            python -c 'from distutils.sysconfig import get_makefile_filename as m; print m()'

* Install [gcc](http://gcc.gnu.org) (OSX users: installing the [OSX developer tools](https://developer.apple.com/technologies/tools/) is probably the easiest way to do this). The following command should not throw an error:
        
        gcc -v  

* Install [pip](http://www.pip-installer.org/en/latest/); here are [pip's installation instructions](http://www.pip-installer.org/en/latest/installing.html). The following command should not throw an error:

        pip -V

1. install virtualenv `pip install virtualenv` (you may need to instead run `sudo pip install virtualenv`)
1. create a top-level (container) project directory in a desired location, e.g. `mkdir -p ~/MyProjects/<project container name>`
1. go to the top-level directory `cd ~/MyProjects/<project container name>`
1. initialize a virtual environment in this directory 

        virtualenv --no-site-packages .

1. activate your virtual environment
    
        source bin/activate 

### creating your project with this template
1. From within the container directory run

        django-admin.py startproject --template=https://github.com/cjrd/django-template/archive/master.zip <project name>
        
1. install the dependencies

        pip install -r requirements.txt

1. copy the local settings file

        cd  <project name>/<project name>; cp settings_local_template.py settings_local.py; cd ..

1. add the project directory to your virtualenv PYTHONPATH

        echo "PYTHONPATH=.:$PWD:$PYTHONPATH" >> ../../bin/activate

1. reset your environment

        source ../../bin/activate

1. sync the databse 

       python manage.py syncdb

1. run the server

       python manage.py runserver

1. navigate to test page http://127.0.0.1:8000

