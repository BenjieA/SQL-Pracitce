//jenins for angualr
//clone angular repo
//cd into repo
//run built-in tests ng test, e2e
//run backend (rest server)
//deploy actual frontend 
pipeline{
	agent any
	stages{
		stage('Deploy Application'){
			steps{
				sh """
				ssh groupproject@ << EOF
				rm -rf spring-petclinic-angular
				git clone https://github.com/spring-petclinic/spring-petclinic-angular.git
				cd spring-petclinic-angular
				"""
			}
		}
	}
}
