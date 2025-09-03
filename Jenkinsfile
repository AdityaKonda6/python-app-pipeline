pipeline {
    agent any // This means the pipeline can run on any available Jenkins agent.

    stages {
        stage('Build Docker Image') {
            steps {
                // We use 'sh' because our Jenkins server is running on Linux (Ubuntu).
                sh 'docker build -t adityakonda/python-app .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                // This block securely accesses the credentials we will create in Jenkins.
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                    sh 'docker push adityakonda/python-app'
                }
            }
        }
        stage('Deploy Application') {
            steps {
                // Stop and remove any old container to avoid conflicts.
                // The '|| true' part ensures the command doesn't fail if the container doesn't exist yet.
                sh 'docker stop python-app-container || true'
                sh 'docker rm python-app-container || true'

                // Run the new container from the fresh image we just pushed to Docker Hub.
                sh 'docker run -d --name python-app-container -p 80:80 adityakonda/python-app'
            }
        }
    }
}