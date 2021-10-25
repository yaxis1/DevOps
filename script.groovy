def run_app(){
    //sh cat 'Running Application' 
    bat 'python3 ./app/run.py'
}

def run_tests(){
    //sh cat'Running Tests' 
    bat 'python3 ./app/test.py'
}

def run_dockers(){
    //sh cat'Running Dockers' 
    bat 'docker-compose up -d'
}
 
return this