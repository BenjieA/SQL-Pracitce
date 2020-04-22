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
		    ssh -i ~/id_rsa app-dev@51.140.60.183 << EOF
		    rm -rf spring-petclinic-rest
		    git clone https://github.com/spring-petclinic/spring-petclinic-rest 
		    cd spring-petclinic-rest
		   
		    if [docker inspect -f '{{.State.Running}}' rest == "true"];
		    then
		       docker start rest
		   
		    else
		       docker run -p 9966:9966 --name rest springcommunity/spring-petclinic-rest	
		    fi
		   
		    
		    
		
		    '''
		}
	    }
	}
}
