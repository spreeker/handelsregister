#!/bin/sh

set -e
set -u

DIR="$(dirname $0)"

dc() {
	docker-compose -f ${DIR}/docker-compose.yml $*;
}

trap 'dc kill ; dc rm -f' EXIT

rm -rf ${DIR}/backups
mkdir -p ${DIR}/backups

dc build --pull
# import new mks dump data in database
dc run --rm importer_mks
# create the hr_data
dc up importer_1  importer_2 importer_3
# wait until all building is done
docker wait jenkins_importer_1_1 jenkins_importer_2_1 jenkins_importer_3_1

err=`docker-compose ps -q | xargs docker inspect -f '{{ .State.ExitCode }}' | grep -v 0 | wc -l | tr -d ' '`
if [ "$code" == "1" ]; then
    exit -1
fi

# run the backup shizzle
dc run --rm db-backup
#dc run --rm el-backup

# You are awesome and done! <3
