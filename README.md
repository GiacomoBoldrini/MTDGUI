# MTDGUI
WEB GUI for the MTD Experiment at CMS,  with the support of ECAL DAQ Team https://gitlab.cern.ch/ecal-daq-upgrade

# Requirements

## Python:
```
Package          Version
---------------- -------
aniso8601        9.0.1
beautifulsoup4   4.9.3
bidict           0.21.2
click            7.1.2
dnspython        1.16.0
eventlet         0.30.2
Flask            1.1.2
Flask-RESTful    0.3.8
Flask-SocketIO   5.0.1
gevent           21.1.2
gevent-websocket 0.10.1
greenlet         1.0.0
itsdangerous     1.1.0
Jinja2           2.11.3
MarkupSafe       1.1.1
pymongo          3.11.3
python-engineio  4.0.1
python-socketio  5.1.0
pytz             2021.1
setuptools       47.1.0
six              1.15.0
soupsieve        2.2.1
Werkzeug         1.0.1
zope.event       4.5.0
zope.interface   5.3.0
```
Essentials are `pymongo`, `flask`, `Flask-SocketIO`, `gevent`, `python-engineio`, `python-socketio`, `gevent-websocket`others should be dependencies.


## Node:
`npm install` under the Client folder will install all the dependencies. In case of error try with `nvm install 10` after removing the node_packages folder and install them again.

# Start

```
cd Client
npm run dev
```

From another folder

```
cd Server
python3 app.py
```

To connect to the gui, open a browser (try to stick to usual ones, firefox, chrome, safari, ...  didnot test on others) and connect to `https://localhost:8080/` for the homepage and start play.
