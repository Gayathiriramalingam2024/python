# Streamlit Calculator App

Creating a simple task application in Streamlit involves setting up a basic interface where users can add tasks, mark them as completed, and view the list of tasks. Here's a step-by-step guide to creating such an application: built using Streamlit and containerized with Docker.

## Features

- Select from the task List
- Change the status of the task like completed or workin progress

## Requirements

- Python 3.10 or later
- Docker Desktop

## Getting Started

### Step 1: Clone the Repository

- Clone this repository to your local machine: git clone https://github.com/Gayathiriramalingam2024/python/VCC-Assignment-1.git

### Step 2: Enter into folder

- cd VCC-Assignment-1

### Step 3: Open Docker Desktop

- Open Docker Desktop application

### Step 4: Creating Docker Image by running the below command

- docker build -t streamlit-taskstatus .

### Step 5: Running the Docker image by running the below command

- docker run -p 8501:8501 streamlit-taskstatus

#### Authored by - Gayathiri Ramalingam - G23AI2012