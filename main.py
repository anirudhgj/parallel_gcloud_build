import os
import logging
import sys
import json 
from datetime import datetime

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main():

    logging.info("Started the process to build containers in parallel")
    logging.info("Authenticating") 
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ["INPUT_GOOGLE_APPLICATION_CREDENTIALS"]

    print (os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

    with open(os.environ["GOOGLE_APPLICATION_CREDENTIALS"]) as f:
        sa_details = json.load(f)

    os.system("gcloud auth activate-service-account {} --key-file={} --project={}".format(sa_details['client_email'],
                                                                                          os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
                                                                                          sa_details['project_id']))

    logging.info("The value of the VERSION_GITHUB_SHA is: {}".format(os.environ["INPUT_GIT_SHA"]))
    git_sha = os.environ['INPUT_GIT_SHA']
    project_name = os.environ['INPUT_GKE_PROJECT']
    build_input = os.environ['INPUT_IMAGE_AND_DOCKERFILE_PATH']

    build_arr = build_input.split(' ')
    image_names = build_arr[::2]
    dockerfile_paths = build_arr[1::2]

    logging.info("submitting the processes to the background")

    for i in range(len(build_arr)):
        image = image_names[i]
        dockerfile_path = dockerfile_paths[i]
        cmd = f"gcloud builds submit --tag gcr.io/{project_name}/{image}:${git_sha} {dockerfile_path} &"
        os.system(cmd)        
        os.system("sleep 1")
    
if __name__ == "__main__":
    main()



