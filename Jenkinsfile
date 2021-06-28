pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh '''
                apt-get install python3-venv
                python3 -m venv venv
                . venv/bin/activate
                python3 -m pip install -r requirements.txt
                bash ./copy_test.sh
                bash ./append_test.sh
                bash ./write_test.sh
                '''
            }
        }
        stage('deploy') {
            steps {
                ansiblePlaybook(
                    credentialsId: 'trainer_key',
                    inventory: './inventory.yaml',
                    playbook: './deployP0.yml',
                    disableHostKeyChecking: true)
            }
        }
    }
}