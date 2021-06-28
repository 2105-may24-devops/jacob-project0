pipeline {
    agent any
    stages {
        stage('setup node'){
            steps{
                sh '''
                sudo apt-get install python3-venv -y
                python3 -m venv venv
                . venv/bin/activate
                python3 -m pip install -r requirements.txt
                '''
            }
        }
        stage('test') {
            steps {
                sh '''
                bash ./copy_test.sh
                bash ./append_test.sh
                bash ./write_test.sh
                '''
            }
        }
        stage('deploy') {
            steps {
                ansiblePlaybook(
                    inventory: './inventory.yml',
                    playbook: './deployP0.yml',
                    disableHostKeyChecking: true)
            }
        }
    }
}