# Neighbourhood Log

###  Author
Clinton Okerio

### Description
Neighbourhood log is a web appication that allows people living in a particular neighbourhood get news on what is happening 
in the neighbourhood and fast emergency services like hospital and police contacts.

### User Stories
1. Sign in with the application
2. Set up a profile, location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for health and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Only view details of a single neighborhood.

### Tech used
1. HTML and CSS
2. Visual Studio Code for code editing.
3. Python
4. Django
5. Postgres
6. Heroku for deployment
7. Git and github


## Set up and Installation

### Prerequisites
You will need to install git, django, postgres and python3.6+  in your device.
To install these packages, you can use the following commands

```
#python3.6
$ sudo apt-get install python3.6.

#django
$ pip install django==1.11.5

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev

#locust
$ pip install locustio
```

### Installation
1. To access this application on your command line, you need to clone it: 
`git clone https://github.com/ClintonClin/neighbourhood.git`

2. Create a requirements.txt in the root folder and copy the requirements above.

3. Install the required technologies with: 
`pip install -r requirements.txt`

4. Create a .env file and copy the .env code above

5. You can then run the server with:
`python3.6 manage.py runserver`

6. You can make changes to the db with: 
`python3.6 manage.py makemigrations clone`
`python3.6 manage.py migrate`

7. You can run tests:
`python3.6 manage.py test clone`

### Deployment
Follow the link for step-by-step guidance to heroku deployment : 
https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0


### License
Copyright (c) **Clinton Okerio**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 