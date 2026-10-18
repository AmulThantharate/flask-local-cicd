// Jenkinsfile (Groovy Pipeline for Flask CI/CD)
// In Jenkins, pipelines are written using Groovy.

// Groovy helper function defined at top-level
def printBanner(String message) {
    echo "=========================================="
    echo ">>> ${message}"
    echo "=========================================="
}

pipeline {
    agent any

    // Pipeline environment variables
    environment {
        PYTHON_BIN = 'python3'
        VENV_DIR   = '.venv'
    }

    stages {
        stage('Groovy Demo & Info') {
            steps {
                // The 'script' block lets you execute imperative Groovy code
                script {
                    printBanner("Starting Build #${env.BUILD_NUMBER ?: 'LOCAL'}")

                    // 1. Groovy Variables (dynamic typing with 'def')
                    def appName = 'flask-local-cicd'
                    def devOpsStack = ['Flask', 'Pytest', 'Jenkins', 'Groovy']

                    // 2. Groovy String Interpolation (GString with double quotes)
                    echo "Project: ${appName}"

                    // 3. Groovy Closures & Collection iteration (.each)
                    echo "Pipeline components:"
                    devOpsStack.each { item ->
                        echo "  * ${item}"
                    }

                    // 4. Groovy Map (Key-Value)
                    def buildMetadata = [
                        jobName: env.JOB_NAME ?: 'flask-pipeline',
                        executor: env.NODE_NAME ?: 'master/built-in'
                    ]
                    echo "Running on node: ${buildMetadata.executor}"
                }
            }
        }

        stage('Prepare Virtualenv & Dependencies') {
            steps {
                script {
                    printBanner("Installing dependencies")
                }
                sh '''
                    # Ensure virtual environment exists
                    if [ ! -d "${VENV_DIR}" ]; then
                        ${PYTHON_BIN} -m venv ${VENV_DIR}
                    fi

                    # Activate venv and install packages
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Execute Pytest Suite') {
            steps {
                script {
                    printBanner("Executing tests")
                }
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest -v test/test_app.py
                '''
            }
        }
    }

    // Post-execution handlers (Groovy closures)
    post {
        always {
            script {
                echo "Pipeline finished with result: ${currentBuild.currentResult}"
            }
        }
        success {
            echo "Build #${env.BUILD_NUMBER} PASSED successfully!"
        }
        failure {
            echo "Build #${env.BUILD_NUMBER} FAILED. Check test logs above."
        }
    }
}
