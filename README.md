# mailautolabel

## Quick start

In order to use this project, you should already have installed :
  - python3
    - https://www.python.org/
  - virtualenv
    - https://virtualenv.pypa.io/en/latest/
  - make
    - https://www.gnu.org/software/make/

Then just navigate at the root of this project and run :
  - virtualenv env
  - source env/bin/activate
  - make

Configure the connection editing :
  - mailautolabel/data/config.ini
    - for example
      - hostname: imap-mail.outlook.com
      - username: firstname.lastname@etu.univ-amu.fr
      - password: bonnenuitlespetits

At this point you should be able to run the script :
  - python mailautolabel/launcher.py
