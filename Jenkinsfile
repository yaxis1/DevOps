def gv

pipeline {
    agent any

    stages {
        stage ('Load env script'){
            steps{
                echo "Loading groovy script"
                script{
                    gv = load "script.groovy"
                }
            }
        }

        stage ("Build Stage"){
            steps{
                echo'Building app'
                script{
                    gv.run_app()
                }
            }
        }

        stage ("Test Stage"){
            steps{
                echo 'Testing app'
                script{
                    gv.run_tests()
                }
            }
        }

        stage ("Deploy Stage"){
            steps{
                echo 'Deploying Dockers'
                script{
                    gv.run_dockers()
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
