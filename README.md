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

## Todo, to improve

- comment the code !

- laucher.py
  - make it usable with args, for example :
    - --verbose(default)
    - --quiet
    - --from-remote(then ask for hostname, username, password in terminal)
    - --from-csv csv_filename
    - --ml-methode [supervised, unsupervised]
  - make it colorful !
  - indent the outputs

- data/
  - add a method to save the mails we download (which format should we use ?)
  - add a method to download from imap only the mails we don't have on a local file
  - remove the config.ini file when the arg --from-remote is done in the launcher
  - make two repositories, one to deal with local files, the other one to deal with imap connection
  - add a gmail module for imap

- ml/
  - add a method to determine if we can use supervised algorithm
  - add a supervised algorithm

- docs/
  - add documentation generated by Sphinx

- tests/
  - add tests ?
