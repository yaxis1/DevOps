def installRequirements(){
    //sh cat 'Installing requirements' 
    bat 'pip install -r requirements.txt'
}

def runApp(){
    //sh cat 'Running Application' 
    bat 'python3 ./app/run.py'
}

def runTest(){
    //sh cat'Running Tests' 
    bat 'python3 ./app/test.py'
}

def deployDocker(){
    //sh cat'Running Dockers' 
    bat 'docker-compose up -d'
}
 
return this