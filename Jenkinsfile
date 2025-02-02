pipeline{
  agent any
  stages{
    stages("build"){
      steps{
       echo 'building the application.' 
      }
    }
    stages("test"){
      steps{
        echo 'testing the application.'
      }
    }
    stages("deploy"){
      steps{
        echo 'deploying the application.'
      }
    }
    stages("cleanUp"){
      steps{
        echo 'clean up of the application build.'
      }
    }
  }
}
