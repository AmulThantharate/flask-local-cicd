pipeline {
    agent any

    parameters {
       booleanParam(
          name: 'RUN_TESTS',
          defaultValue: true,
          description: 'Run Flask application tests'
       )
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

  }
}

