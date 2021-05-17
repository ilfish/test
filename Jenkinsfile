pipeline {
  agent {
    node {
      label '111'
    }

  }
  stages {
    stage('clone') {
      steps {
        git(url: 'git@github.com:ilfish/testgit.git', branch: 'master')
      }
    }

  }
}