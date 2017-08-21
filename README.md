bower: [![Dependency Status](https://www.versioneye.com/user/projects/551d7c9c971f7847ca000010/badge.svg?style=flat)](https://www.versioneye.com/user/projects/551d7c9c971f7847ca000010)
python: [![Dependency Status](https://www.versioneye.com/user/projects/551d7ca6971f78433900000e/badge.svg?style=flat)](https://www.versioneye.com/user/projects/551d7ca6971f78433900000e)
node: [![Dependency Status](https://www.versioneye.com/user/projects/551d7ca0971f781c48000005/badge.svg?style=flat)](https://www.versioneye.com/user/projects/551d7ca0971f781c48000005)


OnBill Platform Backend
======================

Setup
-----

### Build the docker images and start the containers
```bash
./bin/develop.sh
```

### Check that the connection django <-> mongdb works properly

Connect to the running django container via exec and start an ```ipython``` shell and enter the following commands:
```python
In [1]: from pymongo import MongoClient
In [2]: import pprint
In [3]: client = MongoClient('mongodb', 27017)
In [4]: db = client.common
In [5]: db.collection_names()
Out[6]:
['Document',
 'Item',
 'Business',
 'File',
 'Trace',
 'Customer',
 'AccessToken',
 'FrontUser']
In [7]: documents = db.Document
In [8]: pprint.pprint(documents.find_one())
{'_id': ObjectId('58225a5cedf9313facf95ea1'),
 'businessId': ObjectId('582257d5edf9313facf95e9e'),
 'created': datetime.datetime(2016, 11, 8, 23, 6, 4, 519000),
 'date': datetime.datetime(2016, 11, 10, 0, 0),
 'fileId': ObjectId('592905f2210e537ba759a7f3'),
 'issuer': {'addressOffice': {'addition': 'HH',
                              'country': 'de',
                              'houseNumber': '7',
                              'locality': 'Berlin',
                              'postcode': '12459',
                              'street': 'Reinbeckstraße'},
            'bank': {'bank': 'Deutsche Kredit Bank',
                     'bic': 'BYLADEM100',
                     'holder': 'Thomas Rega',
                     'iban': 'DE66120300001001908635'},
            'created': '2016-11-08T22:55:17.712Z',
            'director': 'Thomas Rega',
            'email': 'thoreg@gmail.com',
            'familyName': 'Rega',
            'firm': 'thoreg',
            'forename': 'Thomas',
            'id': '582257d5edf9313facf95e9e',
            'legalForm': 'de-einzel',
            'paymentTarget': 14,
            'sequences': {'credit': 1,
                          'customer': 3,
                          'invoice': 1026,
                          'item': 4,
                          'offer': 5,
                          'reminder': 1},
            'smallScaleEnterprise': False,
            'taxNumber': '111/1111/111',
            'updated': '2017-01-02T20:40:57.734Z',
            'userIds': ['582257d5edf9313facf95e9d'],
            'vatClasses': {'c0': {'percent': 190000},
                           'c1': {'percent': 70000},
                           'c2': {'percent': 0}},
            'vatNumber': '22/222/222/22',
            'website': 'http://thoreg.com'},
 'items': [{'description': 'Tiere ausstopfen',
            'number': '1',
            'priceGross': 220000,
            'priceNet': 220000,
            'quantity': 20000,
            'quantityStr': '2',
            'sumGross': 440000,
            'sumNet': 440000,
            'vatAmount': 0,
            'vatPercent': 0},
           {'created': '2016-11-08T23:02:59.681Z',
            'description': 'Poolhasen bumsen',
            'id': '582259a3edf9313facf95e9f',
            'number': '1',
            'price': 600000,
            'priceGross': 600000,
            'priceNet': 600000,
            'quantity': 10000,
            'quantityStr': '1',
            'sumGross': 600000,
            'sumNet': 600000,
            'unit': 'hour',
            'updated': '2016-11-08T23:03:24.584Z',
            'vatAmount': 0,
            'vatClass': 'c0',
            'vatPercent': 0}],
 'number': '1002',
 'overdue': None,
 'paymentTargetDate': datetime.datetime(2016, 11, 24, 0, 0),
 'periodText': 'Leistungsdatum entspricht dem Rechnungsdatum',
 'recipient': {'addressOffice': {'country': 'de',
                                 'houseNumber': '17b',
                                 'locality': 'Berlin',
                                 'postcode': '10317',
                                 'street': 'Sophienstrasse'},
               'businessId': '582257d5edf9313facf95e9e',
               'contactIndex': '0',
               'created': '2016-11-08T23:05:41.014Z',
               'email': 'toni@onbill.com',
               'familyName': 'Klätke',
               'firm': 'Toni Klätke',
               'forename': 'Toni',
               'gender': 'male',
               'id': '58225a45edf9313facf95ea0',
               'number': '1',
               'updated': '2016-11-14T20:33:00.053Z'},
 'status': 'outstanding',
 'statusDyn': 'draft',
 'sumGross': 1040000,
 'sumNet': 1040000,
 'text': 'Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.',
 'type': 'invoice',
 'updated': datetime.datetime(2017, 5, 27, 4, 52, 2, 345000),
 'vats': [{'amount': 0, 'percent': 0, 'sumNet': 1040000}]}
In [9]: users = db.FrontUser
In [10]: pprint.pprint(users.find_one())
{'_id': ObjectId('582257d5edf9313facf95e9d'),
 'email': 'thoreg@gmail.com',
 'emailVerified': True,
 'password': '$2a$10$/YHlVpfcbs1clOmKK6ARx.C3SnRGWKXoUVaH7BUGUVZxEzSiU8DQG',
 'termsVersion': 1,
 'userIds': []}
```




OnBill Platform Frontend
========================






Django + Angular seed project w. Docker
=====================================================
This is a seed repo intended to bootstrap django + angular project development. It uses docker for dev environment and contains a small sample application.

Requirements
=============
Docker 1.6  
Docker-compose 1.2

Stack
=============
* Python 3.4.3
* PostgreSQL
* Django
* Jade template engine
* Stylus css preprocessor
* AngularJS frontend framework
* Bootstrap3  css framework
* Gulp based frontend build system
* Gunicorn app server
* Nginx web server


Installation
=============

Docker dev environent requires latest docker, see https://docs.docker.com/installation/

#### Mac
1. Install boot2docker and Docker Compose
```
brew install boot2docker docker-compose
```
2. Initialize and start up boot2docker
```
boot2docker init
```
```
boot2docker start
```
3. Configure your Docker host to point to your boot2docker image.
```
$(boot2docker shellinit)
```
You’ll need to run this for every terminal session that invokes the docker or docker-compose command – better export this line into your `.zshrc` or `.bashrc`.

#### Windows
[http://www.ubuntu.com/download/desktop/](http://www.ubuntu.com/download/desktop/)

Run development server
=============

```sh
# build images
# init database
# start django dev server & frontend builder
./bin/develop.sh
```

App should be up on [http://localhost:8000](http://localhost:8000/), running django development server.  You're good to go!

Run production server
==============

```sh
# stop containers,
# create database backup
# build docker images,
# build frontend,
# collect django static files,
# run migrations,
# start development stack
./bin/deploy.sh

#stop production server
./bin/stop_production.sh

#start production server
./bin/start_production.sh
```
App should be up on [http://localhost](http://localhost/)  
  
TODO:  
add log rotation  

Configure SSL
==============

### Configure SSL on included nginx server

1. Add your SSL key and certificat to conf/ssl
2. Rename ssl key/cert includes in conf/nginx_ssl.conf
3. Uncomment lines as specified by comments in docker-compose-prod.yml, conf/gunicorn.py, backend/conf/settings_prod.py

### Allready running behind a SSL-enabled proxy
1. Uncomment lines as speicifed by comments in conf/gunicorn.py, conf/nginx.conf,  backend/conf/settings_prod.py

Run django management commands
==============
```
# create migrations
./bin/django_admin.sh makemigrations sampleapp 

#apply migrations
./bin/django_admin.sh migrate 

#access django shell
./bin/django_admin.sh shell 

#create new admin user
./bin/django_admin.sh createsuperuser 
# etc
```

for production use /bin/django_admin_prod.sh

Build frontend
==============
In case you want to build forntend separately, to host it on cdn or whatevs:   
```
./bin/build_frontend.sh
```
This will build frontend & collect static files to frontend/dist  

Database
===============
```sh
# access postgress shell
./bin/psql.sh

# create a backup to backups/
./bin/db_backup.sh

# restore from backup
./bin/db_restore.sh [filename that exists in backups/]
```

Project layout
===============

```sh
#the important stuff: 

bin/                     # various scripts to deploy, run, manage app
frontend/src/app         # angular application
frontend/src/stylesheets # stylus stylesheets
frontend/bower.json      # frontend dependency bower config
backend/apps             # custom backend django apps
backend/conf             # django config files
requirements.txt         # python dependencies
e2e-tests/specs          # e2e tests
logs/                    # nginx, gunicorn, app logs for production
conf/gunicorn.conf.py         # gunicorn config for production
conf/nginx.conf               # nginx config for production
backups/                      # database backups 
```


Unit tests
=================
See [https://docs.djangoproject.com/en/1.ū/topics/testing/overview/](https://docs.djangoproject.com/en/1.7/topics/testing/overview/)  
Sample app includes sample tests at backend/apps/sampleapp/tests.py

```sh
# run django unit tests
./bin/run_unit_tests.sh
```

End to end tests
=================

Angular's default e2e test framework [protractor](https://github.com/angular/protractor) is used in conjunction with django test server.  
Test specs are located at e2e-tests/specs/  
Django e2e test config at backend/conf/settings_e2e.py  

Requires java, node > 10.0 and chrome browser  

To setup & run e2e tests, run:  
```
./bin/run_e2e_tests.sh
```

