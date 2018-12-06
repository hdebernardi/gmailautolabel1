# mailautolabel

## Quick start

### Requirements

In order to use this project, you should already have installed :
  - python3
    - https://www.python.org/
  - virtualenv
    - https://virtualenv.pypa.io/en/latest/
  - make
    - https://www.gnu.org/software/make/

### Libraries installation
Then, just navigate at the root of this project and run :
  - virtualenv -p python3 env
  - source env/bin/activate
  - make

### Connection to Gmail API

To connect to gmail, you should follow these instructions :
  - https://developers.google.com/gmail/api/quickstart/python
  - although the whole page is interesting, you could only follow step 1 to have a working project

### Running mailautolabel

- cd mailautolabel
- python3 main.py

The first connection will open a logging page in your web browser. Connect to your gmail account and autorize the application.

### Running tests

- cd mailautolabel
- python3 -m unittest -v tests.nom_du_test
