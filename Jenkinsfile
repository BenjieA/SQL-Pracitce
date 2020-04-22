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
		    git clone https://github.com/spring-petclinic/spring-petclinic-angular
		    cd spring-petclinic-rest
                    docker start rest || docker run --name rest -p 9966:9966 springcommunity/spring-petclinic-rest
		    
		    npm uninstall -g angular-cli @angular/cli
                    npm cache clean
                    npm install -g @angular/cli@latest
		    cd ..
		    cd spring-petclinic-angular
		    
		    npm install --save-dev @angular/cli@latest
                    npm install
		   
		    ng serve
		    
		  
		   
		    
		    
		
		    '''
		}
	    }
	}
}
