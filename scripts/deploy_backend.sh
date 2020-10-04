
#!/bin/sh
# Deploy backend to HyperOne Website
WEBSITE_ID="${BACKEND:-5ed804ed8073de470f2984e2}"
set -eux
GIT_COMMIT=$(git rev-parse HEAD)
H1=$(which h1)
export HYPERONE_EARLY_ADOPTERS='true'
${H1} website ssh --website ${WEBSITE_ID} --command "rm -r /data/env"
${H1} website ssh --website ${WEBSITE_ID} --command "git --git-dir=small_eod/.git --work-tree=small_eod fetch origin"
${H1} website ssh --website ${WEBSITE_ID} --command "git --git-dir=small_eod/.git --work-tree=small_eod checkout -f ${GIT_COMMIT}"
${H1} website ssh --website ${WEBSITE_ID} --command "virtualenv /data/env";
${H1} website ssh --website ${WEBSITE_ID} --command "/data/env/bin/python -m pip install -r small_eod/backend-project/requirements/production.txt"
${H1} website ssh --website ${WEBSITE_ID} --command "/data/env/bin/python small_eod/backend-project/manage.py migrate --noinput"
${H1} website restart --query '[].{id:id,state:state}' --website ${WEBSITE_ID}
