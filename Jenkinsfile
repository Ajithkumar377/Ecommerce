pipeline {
  agent any
  environment {
    IMAGE_BACKEND = 'ajithkumar377/ecom-backend'
    IMAGE_FRONTEND = 'ajithkumar377/ecom-frontend'
  }
  stages {
    stage('Clone Repo') {
      steps {
        git url: 'https://github.com/Ajithkumar377/Ecommerce.git', branch: 'main'
      }
    }
    stage('Build Images') {
      steps {
        sh 'docker build -t $IMAGE_BACKEND -f Dockerfile.backend .'
        sh 'docker build -t $IMAGE_FRONTEND -f Dockerfile.frontend .'
      }
    }
    stage('Push Images') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
          sh 'docker push $IMAGE_BACKEND'
          sh 'docker push $IMAGE_FRONTEND'
        }
      }
    }
    stage('Deploy to K8s') {
      steps {
        sh 'kubectl apply -f k8s/'
      }
    }
  }
}

