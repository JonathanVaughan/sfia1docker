pipeline {
    agent any

    stages {
        stage('Enable all scripts to be executable') {
            steps {
                sh 'chmod +x ./script/*'
            }
        }
        stage('Get the envinronment ready') {
            steps {
                sh './script/install.sh'
            }
        }
            
        }
    }
