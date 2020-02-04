pipeline {
    agent none
    stages {
        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python3'
                }
            }
            steps {
                sh 'pyinstaller --onefile scrape_rpa.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/dl_ma'
                            }
        }
    }
}
