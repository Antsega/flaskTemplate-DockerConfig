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

```bash
python app.py

# Build the Docker image
docker build -t my_flask_app .
