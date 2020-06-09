cookiecutter-template
=====================
[Cookiecutter](https://github.com/audreyr/cookiecutter) 

This is a template for creating a basic Command Line Python application.   

Requirements
------------
__If using Mac OS 10.15 and greater:__

*If you haven't installed `xcode`, `homebrew`, `pipenv`, or `cookiecutter` please follow steps 1-4.*

1. Install `xcode` command line tools<br/>
command line: `xcode-select --install`

2. Install `hombrew`<br/>
command line: ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

3. Clone this template from GitHub<br/>
In the directory of your choosing:<br/>
command line: `git clone https://github.com/bfulroth/cookiecutter-basic-python-app.git`

4. Install cookiecutter<br/>
command line: `brew install cookiecutter`

Usage
-----
Generate a new Python application:<br/>
command line: `cookiecutter path_to_this_template`<br/>

Follow the prompts to to create the skeleton your Python application.

Special Features
---------------- 


Contribute
----------
If you'd like to contribute, fork this [repository](https://github.com/eviweb/cookiecutter-template), and send a pull request.    
- To install dev requirements: `pipenv install --dev`     
- To run tests from the root of the project directory: `pytest`     

License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
