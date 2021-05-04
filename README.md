# MTDGUI
WEB GUI for the MTD Experiment at CMS,  with the support of ECAL DAQ Team https://gitlab.cern.ch/ecal-daq-upgrade

# Software
This GUI has been developed with Vue-CLI for the frontend and Flask with python3 for the backend. Web sockects exploited  through zqm and Flask-socket.io service

# Setup
Tested for MacOS (BigSur, should work with previous OS) and Linux based OS such as Debian and Ubuntu.
All the needed setup is automatic. The only requirement at the moment is  to have a python3 on your OS.

```
git clone git@github.com:GiacomoBoldrini/MTDGUI.git
cd MTDGUI
source setup.sh
```

This will install node, npm, nvm mongodb, vue-cli and all python libraries:
- Node dependencies for vue can be found under `Client/packages.json`
- Python dependencies for backend can be found  under `Server/requirements.txt`

# Start

Open two separate shells. In the first one run the frontend in development mode
```
cd Client
npm run dev
```

From the other shell, activate the environment and run the server side

```
source env/bin/activate
cd Server
python3 app.py
```

To connect to the gui, open a browser (try to stick to usual ones, firefox, chrome, safari, ...  didnot test on others) and connect to `https://localhost:8080/` for the homepage and start play.
