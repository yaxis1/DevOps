def run_app(){
    sh cat'Running Application' 
    sh 'python3 run.py'
}

def run_tests(){
    sh cat'Running Tests' 
    sh 'python3 test.py'
}

def run_dockers(){
    sh cat'Running Dockers' 
    sh 'docker-compose up -d'
}
 
return this