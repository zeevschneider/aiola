Table of Contents
=================

1. `General`_

2. `Specifications`_

3. `Installation and deployment`_

4. `Usage`_


General
========
This program is a home assignment of Aiola.
It demonstrates testing related abilities:
1. Create testing planning doc : please see Q1.docx document
2. Creation of frontend tests using Selenium - please see main.py and page_objects and support directory with support code

Specifications
===============
The assignment has it's own specification described in the "Home assignment.pdf" document

Installation and deployment
===========================

1. Open a command line on your machine (verify git installation) and run the following:
    git clone git@github.com:zeevschneider/aiola.git

2. Make sure that you have a machine with Python &gt;= 3.6 installed

3. Open a command line and cd to the /aiola folder in the downloaded package

4. The best way is to install requirements into a virtual environment in order not to soil
    your python with unnecessary packages:
    a. Install virtualenv package - pip install virtualenv
    b. Create virtual environment:
        1. Make sure that you are in the /aiola folder
        2. Run the following command – virtualenv {your_env_name}
        3. Activate your virtual environment – type {your_env_name}\Scripts\activate
        Your command line looks like the following:
        ({your_env_name}) {path}/aiola
    c. Run the following command to install packages that are listed in the requirements.txt file:
       pip install -r requirements.txt
       You should receive a “Successfully installed…” message


Usage
======
Run tests:
    CD to /aiola and type "python main.py"
