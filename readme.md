you can run python app.py to create the flask environment locally

or
__Step 2: Building and Testing the Docker Image__

Once you have a Dockerfile, you can build an image and then test it:
Bash Command <br>
# Build the Docker image <br>
docker build -t my_flask_app . <br><br>

# Run the Docker container <br>
docker run -p 8080:8080 my_flask_app<br>

__2) Deploy Steps__
-------------

gcloud auth configure-docker

a)
# Tag the Docker image
docker tag my_flask_app gcr.io/[YOUR-PROJECT-ID]/my_flask_app

b)
# Push the Docker image
docker push gcr.io/[YOUR-PROJECT-ID]/my_flask_app

c)
Here's a basic example of how to deploy a Docker image to Google Cloud Run:
gcloud run deploy SERVICE_NAME --image gcr.io/PROJECT_ID/IMAGE_NAME --platform managed --region REGION_NAME
You need to replace:

SERVICE_NAME: the name you want to give your service.
PROJECT_ID: your Google Cloud project ID.
IMAGE_NAME: the name of the Docker image you pushed to the Google Container Registry.
REGION_NAME: the Google Cloud region where you want to deploy your service.

e.x)
gcloud run deploy flask-app --image gcr.io/flask-app-2023-387823/my_flask_app --platform managed --region us-central1

__3) Implement CI/CD__
a) Create a build trigger
url : https://cloud.google.com/build/docs/automating-builds/create-manage-triggers

b) add yaml
This cloudbuild.yaml does three things:

It builds a Docker image from your Dockerfile.
It pushes the Docker image to the Google Container Registry.
It deploys the Docker image to Google Cloud Run.
Replace my-service (args: line 8) with your actual service name and us-central1 with your desired region. Also, the $PROJECT_ID will be automatically replaced by your GCP project ID.