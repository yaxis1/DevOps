def gv

pipeline {
    agent any

    stages {
        stage ('Load env script'){
            steps{
                echo "Loading groovy script"
                
            }
        }

        stage ("Build Stage"){
            steps{
                echo'Building app'
                
            }
        }

        stage ("Test Stage"){
            steps{
                echo 'Testing app'
               
            }
        }

        stage ("Deploy Stage"){
            steps{
                echo 'Deploying Dockers'
                
            }
        }
    }

    post{
        always{
            echo 'End of Pipeline'
        }
    }
}
