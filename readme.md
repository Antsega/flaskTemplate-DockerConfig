# Flask Application Deployment Guide

This guide walks through the steps to run and deploy a Flask application locally and on Google Cloud Run.

## Table of Contents

1. [Running the Application Locally](#running-the-application-locally)
2. [Building and Testing the Docker Image](#building-and-testing-the-docker-image)
3. [Deployment Steps](#deployment-steps)
4. [Implementing CI/CD](#implementing-ci-cd)

---

## 1. Running the Application Locally

To run the application in your local environment, you need to start the Flask server using the following command:

\`\`\`bash
python app.py
\`\`\`

---

## 2. Building and Testing the Docker Image

Once you have a Dockerfile, you can build an image and then test it:

**Step 2.1: Building the Docker Image**

\`\`\`bash
# Build the Docker image
docker build -t my_flask_app .
\`\`\`

**Step 2.2: Running the Docker Container**

\`\`\`bash
# Run the Docker container
docker run -p 8080:8080 my_flask_app
\`\`\`

---

## 3. Deployment Steps

To deploy the Docker image to Google Cloud Run, follow these steps:

**Step 3.1: Configuring Docker with GCloud**

\`\`\`bash
gcloud auth configure-docker
\`\`\`

**Step 3.2: Tagging the Docker Image**

Replace `[YOUR-PROJECT-ID]` with your Google Cloud project ID.

\`\`\`bash
# Tag the Docker image
docker tag my_flask_app gcr.io/[YOUR-PROJECT-ID]/my_flask_app
\`\`\`

**Step 3.3: Pushing the Docker Image**

\`\`\`bash
# Push the Docker image
docker push gcr.io/[YOUR-PROJECT-ID]/my_flask_app
\`\`\`

**Step 3.4: Deploying to Google Cloud Run**

Replace `SERVICE_NAME`, `PROJECT_ID`, `IMAGE_NAME`, and `REGION_NAME` with your service name, project ID, image name, and region respectively. For example:

\`\`\`bash
gcloud run deploy flask-app --image gcr.io/flask-app-2023-387823/my_flask_app --platform managed --region us-central1
\`\`\`

---

## 4. Implementing CI/CD

You can automate the build and deployment process with Google Cloud Build.

**Step 4.1: Creating a Build Trigger**

Create a build trigger as per the instructions provided [here](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers).

**Step 4.2: Adding a cloudbuild.yaml File**

Add a `cloudbuild.yaml` file to your GitHub repository, which specifies the build steps. This file automates the following:

- Building a Docker image from your Dockerfile.
- Pushing the Docker image to the Google Container Registry.
- Deploying the Docker image to Google Cloud Run.

Replace `my-service` with your actual service name and `us-central1` with your desired region. The `$PROJECT_ID` will be automatically replaced by your GCP project ID.

---

Please refer to the relevant documentation for more detailed steps and troubleshooting. If you encounter issues or have further questions, feel free to raise an issue in this repository.
