#!groovy

node {

    String BRANCH = "${env.BRANCH_NAME}"
    String INVENTORY = (BRANCH == "master" ? "production" : "acceptance")

    try {

    stage "Checkout"
        checkout scm

    //stage "Test"

    //    try {
    //        sh "docker-compose build"
    //        sh "docker-compose up -d"
    //        sh "sleep 20"
    //        sh "docker-compose up -d"
    //        sh "docker-compose run -u root atlas python manage.py jenkins"

    //        step([$class: "JUnitResultArchiver", testResults: "reports/junit.xml"])

    //    }
    //    finally {
    //        sh "docker-compose stop"
    //        sh "docker-compose rm -f"
    //    }


    stage "Build"

        def image = docker.build("admin.datapunt.amsterdam.nl:5000/datapunt/handelsregister:${BRANCH}", "web" )
        image.push()

        if (BRANCH == "master") {
            image.push("latest")
        }

    stage "Deploy"

        build job: 'Subtask_Openstack_Playbook',
                parameters: [
                        [$class: 'StringParameterValue', name: 'INVENTORY', value: INVENTORY],
                        [$class: 'StringParameterValue', name: 'PLAYBOOK', value: 'deploy-handelsregister.yml'],
                        [$class: 'StringParameterValue', name: 'BRANCH', value: BRANCH],
                ]
}
    catch (err) {
        slackSend message: "Problem while building Handelsregister service: ${err}",
                channel: '#ci-channel'

        throw err
    }
}