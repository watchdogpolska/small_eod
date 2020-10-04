#!/bin/sh
# Deploy frontend to HyperOne Website
set -eux
WEBSITE_ID="${FRONTEND:5ed7d87d8073de470f295685}"
export HYPERONE_EARLY_ADOPTERS='true'
H1=$(which h1)
FQDN=$(${H1} website show --website ${FRONTEND} --query '[].{fqdn:fqdn}' --output tsv)
docker-compose run -e REACT_APP_ENV=prod frontend bash -c 'yarn && yarn build'
rsync -av --delete frontend-project/dist/ ${FRONTEND}@${FQDN}:/data/public