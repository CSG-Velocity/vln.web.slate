pipeline {
    agent any
    environment {
        ORG_NAME = "velocityln"
        DEPLOYMENT_ENVIRONMENT = getEnvName(env.BRANCH_NAME)
        SERVICE_NAME = getservicename(env.GIT_URL.replaceFirst(/^.*\/([^\/]+?).git$/, '$1'))
        GITLEAKS='/var/lib/jenkins/external_tools/gitleaks/8.18.0'
        // SONAR=credentials("sonar-token")
        // scannerHome = tool 'SonarScanner-msbuild'
        // DOTNET7LOCATION = '/var/lib/jenkins/external_tools/dotnet-sdk/dotnet-sdk-7.0'
        BASTIONIP = '172.174.239.212'
        BASTIONUSER = 'velocityln'
        GIT_COMMIT_SHORT = sh(
                script: "printf \$(git rev-parse --short ${GIT_COMMIT})",
                returnStdout: true
        )
    }
    options {
		buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5', daysToKeepStr: '15'))
	}
    stages {
        stage('VERSION'){
            steps{
                buildDescription "$BUILD_NUMBER - $GIT_COMMIT_SHORT"
            }
        }
         stage('GitLeaks'){
             steps{
                 sh '''
                     $GITLEAKS/gitleaks detect -v --no-git
                 '''
             }
         }
        // stage('SonarAnalysis'){
        //     steps{
        //         withSonarQubeEnv('sonarqube-server'){
        //             sh '''
        //                 $DOTNET7LOCATION/dotnet ${scannerHome}/SonarScanner.MSBuild.dll begin /k:"${ORG_NAME}-${SERVICE_NAME}-${DEPLOYMENT_ENVIRONMENT}" /d:sonar.host.url="https://cd-builds.compunnel.com/sonar" /d:sonar.login="${SONAR}"  /d:sonar.cs.opencover.reportsPaths="**/*opencover.xml" /d:sonar.coverage.exclusions="**TestCases*.cs" /v:$GIT_COMMIT_SHORT
        //                 $DOTNET7LOCATION/dotnet build -c Release Vfx.Services.SysAdmin.sln
        //                 $DOTNET7LOCATION/dotnet test tests/Vfx.Services.SysAdmin.API.Tests.Unit/Vfx.Services.SysAdmin.API.Tests.Unit.csproj /p:CollectCoverage=true /p:CoverletOutputFormat=opencover
        //                 $DOTNET7LOCATION/dotnet ${scannerHome}/SonarScanner.MSBuild.dll end /d:sonar.login=$SONAR
        //             '''
        //         }
        //     }
        // }
        // stage('Quality Gate') {
        //     steps {
        //         timeout(time: 1, unit: 'HOURS') {
        //             waitForQualityGate abortPipeline: true
        //         }
        //     }
        // }
        stage('Copying code to bastion server'){
            steps{
                withCredentials([sshUserPrivateKey(credentialsId: "velocitylndevvm", keyFileVariable: 'keyfile')]){
                    sh """
                    echo ${SERVICE_NAME}
                    ssh -i ${keyfile} ${BASTIONUSER}'@'${BASTIONIP} "cd ${SERVICE_NAME}/${env.BRANCH_NAME}; \
                    rm -rf ${SERVICE_NAME}/${env.BRANCH_NAME}/"
                    scp -i ${keyfile} -r * ${BASTIONUSER}'@'${BASTIONIP}:/home/${BASTIONUSER}/${SERVICE_NAME}/${env.BRANCH_NAME}/
                    """
                }
            }
        }
        // stage('Docker Build & Push using Bastion') {
        //     steps {
        //         withCredentials([sshUserPrivateKey(credentialsId: "velocitydevvm", keyFileVariable: 'keyfile')]) {
        //             sh """
        //                 ssh -i ${keyfile} ${BASTIONUSER}'@'${BASTIONIP} "cd ${SERVICE_NAME}/${env.BRANCH_NAME}; \
        //                 sudo docker build -t ${ORG_NAME}-${SERVICE_NAME}-${DEPLOYMENT_ENVIRONMENT} .; \
        //                 sudo docker tag ${ORG_NAME}-${SERVICE_NAME}-${DEPLOYMENT_ENVIRONMENT}:latest velocfxdevityacr.azurecr.io/${ORG_NAME}-${SERVICE_NAME}-${DEPLOYMENT_ENVIRONMENT}-images:${GIT_COMMIT_SHORT}; \
        //                 sudo docker push velocfxdevityacr.azurecr.io/${ORG_NAME}-${SERVICE_NAME}-${DEPLOYMENT_ENVIRONMENT}-images:${GIT_COMMIT_SHORT};
        //                 "
        //             """
        //         }
        //     }
        // }
        // stage('Deploying to AKS using Bastion') {
        //     when {
        //         allOf {
        //             expression { environment name: 'DEPLOYMENT_ENVIRONMENT', value: 'dev'}
        //             expression { environment name: 'DEPLOYMENT_ENVIRONMENT', value: 'qa'}
        //         }
        //     }
        //     steps {
        //         withCredentials([sshUserPrivateKey(credentialsId: "velocitydevvm", keyFileVariable: 'keyfile')]) {
        //             sh """
        //                 ssh -i ${keyfile} ${BASTIONUSER}'@'${BASTIONIP} "cd k8/${SERVICE_NAME}/${env.BRANCH_NAME}; \
        //                 sed 's/_IMAGE_/${ORG_NAME}-${SERVICE_NAME}-${DEPLOYMENT_ENVIRONMENT}-images/g' deployment-template.yml > ${SERVICE_NAME}-deployment.yml; \
        //                 sed -i 's/_VERSION_/${GIT_COMMIT_SHORT}/g' ${SERVICE_NAME}-deployment.yml; \
        //                 sudo kubectl apply -f ${SERVICE_NAME}-deployment.yml
        //                 "
        //             """
        //         }
        //     }
        // }
        // stage("RELEASE_TAG"){
        //     when { 
        //         environment name: 'DEPLOYMENT_ENVIRONMENT', value: 'uat' 
        //     }
        //     steps{
        //         sh """
        //             git tag -a $GIT_COMMIT_SHORT -m 'Release version - $GIT_COMMIT_SHORT'
        //             git push git@github.com:CSG-Velocity/Vfx.Services.SysAdmin.git $GIT_COMMIT_SHORT
        //         """
        //     }
        // }
        // stage('CleanUP') {
        //     steps {
        //        withCredentials([sshUserPrivateKey(credentialsId: "velocitydevvm", keyFileVariable: 'keyfile')]) {
        //             sh """
        //                 ssh -i ${keyfile} ${BASTIONUSER}'@'${BASTIONIP} "sudo docker rmi -f ${ORG_NAME}-${SERVICE_NAME}-${DEPLOYMENT_ENVIRONMENT}:latest; \
        //                 sudo docker rmi -f velocfxdevityacr.azurecr.io/${ORG_NAME}-${SERVICE_NAME}-${DEPLOYMENT_ENVIRONMENT}-images:${GIT_COMMIT_SHORT};
        //                 "
        //             """
        //         }
        //     }
        // }
    }
}


def getEnvName(branchName) {
    if("main".equals(branchName)) {
        return "uat";
    } else if ("pre-production".equals(branchName)) {
        return "qa";
    }else if ("development".equals(branchName)){
        return "dev";
    }
}

def getservicename(serviceName){
    return serviceName.toLowerCase(); 
}