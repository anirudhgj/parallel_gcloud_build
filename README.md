# github_actions_parallel_gcloud_build


### HOW TO USE THIS GITHUB ACTIONS 


NOTE :- This github Actions uses GCP cloud build function

Setup Github Secrets for the following :-

GKE_KEY - GCP service account credentials in base64 encoded format 

example:- copy the output of 
``` bash
cat path-to-key.json | base64
```
\

GKE_PROJECT - Google Project where the Kubernetes Cluster is defined(can be located on GCP dashboard inside "Project Info" --> "Project Name" should be used) \
ENCODED_GOOGLE_APPLICATION_CREDENTIALS : Base64 encoded Google Application Credentials
GOOGLE_APPLICATION_CREDENTIALS : Path to store the decoded Google Application Credentials


### Example for parallel building and publishing of containers onto Google Cloud Registry (Mainly used for kubeflow pipelines) :- 

```yaml

- name: Parallel Container Build
  uses: anirudhgj/parallel_gcloud_build@master
  with:
    ENCODED_GOOGLE_APPLICATION_CREDENTIALS: ${{ secrets.GKE_KEY }}
    GOOGLE_APPLICATION_CREDENTIALS: /tmp/gcloud-sa.json
    GKE_PROJECT: ${{ secrets.GKE_PROJECT }}
    GIT_SHA: ${{ github.sha }}
    IMAGE_AND_DOCKERFILE_PATH: <<image-name1>> <<path-to-docker-file1>> <<image-name2>> <<path-to-docker-file1>> <<image-name3>> <<path-to-docker-file3>>

 ```      


