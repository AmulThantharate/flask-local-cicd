pipeline {
    agent any

    parameters {
       booleanParam(
          name: 'RUN_TESTS',
          defaultValue: true,
          description: 'Run Flask application tests'
       )
    }
    
    environment {
      DOCKER_USE = secrets.DOCKER_USER
      DOCKER_PASSWORD = credentials('docker-cred')
    }

    stages {
        stage("Git Checkout") {
          steps {
            checkout scm
          }
        }

        stage("Install Dependencies") {
          steps {
            sh """
                  python3 -m venv venv
                  . venv/bin/activate
                  pip install -r requirements.txt
            """
          }
        }
        
        stage("Run tests"){
          when {
            expression { param.RUN_TESTS }
          }
          steps {
            script {
              echo "Build number: ${env.BUILD_NUMBER}"
              echo "Build ID: ${env.BUILD_ID}"
              
              sh """
                  . venv/bin/activate
                  python3 -m pytest -v test/
                """
            }
          }
        }
       
        stage("Build Summary"){
          steps {
            scripts {
              if (params.RUN_TESTS){
                echo "Python tests were enabled"
              } else {
                echo "Python tests were disabled"
              }
            }
          }
        }

        stage("Docker Push") {
           steps {
             withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_CRED', usernameVariable: 'DOCKER_USER')]) {
               sh """
                   docker build -t ${env.DOCKER_USERNAME}/flask-local-cicd:${env.BUILD_NUMBER} .
                   docker login -u ${env.DOCKER_USERNAME} -p ${env.DOCKER_PASSWORD}
                   docker push ${env.DOCKER_USERNAME}/flask-local-cicd:${env.BUILD_NUMBER}
               """
             }
           }
         }
        }

}

