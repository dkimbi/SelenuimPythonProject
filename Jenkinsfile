pipeline{
  agent any
  stages{
    stage("build"){
      steps{
       echo 'building the application v1.0.' 
      }
    }
    stage("test"){
      steps{
        echo 'testing the application.'
      }
    }
    stage("deploy"){
      steps{
        echo 'deploying the application.'
      }
    }
    stage("cleanUp"){
      steps{
        echo 'clean up of the application build.'
      }
    }
  }
}
