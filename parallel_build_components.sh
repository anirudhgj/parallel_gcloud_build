#!/bin/bash

printenv


gcloud config set project $GKE_PROJECT
gcloud auth activate-service-account $GKE_EMAIL --key-file=/tmp/gcloud-sa.json --project=$GKE_PROJECT

IFS=' ' read -ra args <<< "$INPUT_IMAGE_AND_DOCKERFILE_PATH"
echo ${args[@]}

len=${#args[@]}
echo $len

build_and_pub_func(){
    echo "gcr.io/$GKE_PROJECT/$1:$GITHUB_SHA $2"
    gcloud builds submit --tag gcr.io/$GKE_PROJECT/$1:$GITHUB_SHA $2
    sleep 1
}

# For loop till file arguments end
for i in $( seq 1 2 $len )
do
	build_and_pub_func ${args[i-1]} ${args[i]} & # Put a function in the background
done
 
wait 
echo "All done"
