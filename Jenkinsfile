def gv

pipeline {
    agent any

    stages {
        
        stage ('Loading groovy script and installing requirements'){
            steps{
                echo "Loading groovy script and installing requirements"
                script{
                    gv = load "script.groovy"
                    gv.installRequirements()
                }
            }
        }

        stage ("Building Application"){
            steps{
                echo'Building app'
                script{
                    gv.runApp()
                }
                }
            }
        }

        stage ("Testing Application"){
            steps{
                echo 'Testing app'
                script{
                    gv.runTest()
                }
                }
            }
        }

        stage ("Deploying Docker"){
            steps{
                echo 'Deploying Dockers'
                script{
                    gv.deployDocker()
                }
            }
        }
    }

    post{
        always{
            echo 'End of Pipeline'
        }
    }
}
