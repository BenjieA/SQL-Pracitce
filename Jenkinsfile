//jenins for angualr
//clone angular repo
//cd into repo
//run built-in tests ng test, e2e
//run backend (rest server)
//deploy actual frontend 
pipeline{
	agent any
	//tools { 
        //	maven 'Maven 3.3.9' 
        //	jdk 'jdk8' 
    	//}
	stages{
	    stage('Deploy'){
		steps{
		    sh '''
		    pwd
		    ls -a ~/
		    cat ~/.ssh/id_rsa
		    ssh -i ~/.ssh/id_rsa groupproject@51.137.130.31 << EOF
		    rm -rf spring-petclinic-rest
		    git clone https://github.com/spring-petclinic/spring-petclinic-rest
		    cd spring-petclinic-rest
		    ./mvnw spring-boot:run
		//running back end maven (petclinic-rest)
		//cd ..
		//running frontend api (petclinic-angular)
		//rm -rf spring-petclinic-angular
		//git clone https://github.com/spring-petclinic/spring-petclinic-angular.git
		//cd spring-petclinic-angular
		    '''
		}
	    }
	}
}
