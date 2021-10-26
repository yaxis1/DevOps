def installRequirements(){
    // Installing requirements
    bat 'pip install -r ./app/requirements.txt'
}

def runApp(){
    // Running Application
    bat 'start python3 ./app/run.py'
}

def runTest(){
    // Running Tests
    bat 'start python3 ./app/test.py'
}

def runDocker(){
    // Running Dockers 
    bat 'docker-compose up -d'
}
 
return this