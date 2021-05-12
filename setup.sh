echo "@INFO: Starting to setup the MTDGUI. Only use this script in a Linux-based or MacOS operating system"

# Installing brew if on mac
if [ $OSTYPE == "darwin*" ]
then 
    brew_=$(which brew)
    if [ -z "$brew_" ]
    then 
        echo "@INFO: Detected MacOS OS ..."
        xcode-select --install
        # Installing Homebrew
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        brew update 
    fi
fi 

# Installing root it not present 
root_=$(which root)
if [ -z "$root_" ]
then 
    cd
    echo "@INFO Installing ROOT v6.22.00 ... "
    if [ $OSTYPE == "linux-gnu" ]
    then 
        wget https://root.cern/download/root_v6.22.00.Linux-ubuntu19-x86_64-gcc9.2.tar.gz
        tar -xzvf root_v6.22.00.Linux-ubuntu19-x86_64-gcc9.2.tar.gz
        rm root_v6.22.00.Linux-ubuntu19-x86_64-gcc9.2.tar.gz
        source root/bin/thisroot.sh

    elif [ $OSTYPE == "darwin*" ]
    then 
        brew install root

    fi
    cd -
else
    echo "@INFO: Detected ROOT, continuing without installation ..."
fi

# Installing the MTD Analysis packages

mkdir -p MTDAnalysis && cd MTDAnalysis
git clone --recursive git@github.com:Lab5015/Lab5015Analysis.git
git clone git@github.com:Lab5015/sw_daq_tofhir2.git

cd Lab5015Analysis
source scripts/setup.sh
make
make exe 

cd ../..

# Now setup GUI specific

PY=$(which python3)

# Check if py3 is present. For now exit otherwise
if [ -z "$PY" ]
then 
   echo "No python detected"
   exit
else
   echo $PY
fi

if [ $OSTYPE == "linux-gnu" ]
then  
    echo "@INFO: Detected Linux-based OS ..."
    # Installing venv for virtual environments
    sudo apt-get install python3-venv
    python3 -m venv env

    # Installing node and package manager
    sudo apt install nodejs
    sudo apt install npm

    # Install node version manager
    wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

    # Setting up mongodb
    sudo apt-get install gnupg
    wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
    sudo apt-get update

    sudo apt-get install -y mongodb-org
    sudo systemctl daemon-reload

    sudo systemctl start mongod


elif [ $OSTYPE == "darwin*" ]
then 
    # Installing venv for virtual environments
    pip3 install virtualenv
    virtualenv -p python3 env 
    source ./env/bin/activate

    # Installing node, package manager and node version manager
    brew install node
    brew install nvm 

    # Installing mongo
    brew tap mongodb/brew
    brew install mongodb-community@4.4

else
    echo "ERROR: Unsupported operating system. Currently working with MacOS (darwin) or Linux-based (Ubuntu, Debian, ...). Exiting"
    exit 
fi 

# Install node v 10
nvm install 10

# Installing python dependencies in environment
source ./env/bin/activate
python3 -m pip install -r requirements.txt
deactivate


# Installing node dependencies
cd Client
# Install Vue globally on the machine
npm update
npm cache verify
npm install -g @vue/cli
npm install 

cd ..