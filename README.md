Full-Stack Docker Compose Project

This project demonstrates my practical experience with Docker and containerized applications by building a simple full-stack system using multiple services.

Overview

The application consists of several containers working together:

 • Frontend — served with Nginx
 
 • Backend — Python (Flask)
 
 • Database — PostgreSQL 16
 
 • Search engine — Meilisearch
 

All services are managed using Docker Compose and communicate within a shared network.

⸻

Tech Stack
 • Docker
 
 • Docker Compose
 
 • Nginx
 
 • Python (Flask)
 
 • PostgreSQL 16
 
 • Meilisearch
 

⸻

Architecture

 • Each service runs in its own container
 
 • Containers communicate through a Docker network
 
 • PostgreSQL uses a volume for persistent data
 
 • Backend connects to both database and search service
 

⸻

Features

 • Multi-container setup using Docker Compose
 
 • Service isolation
 
 • Internal networking between services
 
 • Persistent database storage
 
 • Integrated search functionality
 
 • Easy local deployment
 

⸻

Getting Started

git clone <your-repo-url>

cd <project-folder>

docker compose up --build


After starting the project:

 • Frontend: http://localhost
 
 • Backend API: http://localhost:5000
 
 • Meilisearch: http://localhost:7700
 

⸻

What I Learned

 • Building and managing multi-container applications
 
 • Docker networking basics
 
 • Working with volumes and persistent storage
 
 • Connecting backend services with databases
 
 • Structuring a simple microservice-based project
 

⸻

Author

Mykhailo Hudz

Aspiring System Administrator / DevOps Engineer

##SCREENSHOOTS

## SERVICE SCHEME

<img width="1152" height="648" alt="service scheme" src="https://github.com/user-attachments/assets/3ed80aab-697f-4f1b-bdb5-8c39377a7cf0" />


## Running Containers
![photo_5384129328657929930_y](https://github.com/user-attachments/assets/f39d66fc-004a-4827-b260-9d87aed53546)

## Meilisearch test
![photo_5384129328657929936_y](https://github.com/user-attachments/assets/12182750-418b-48a2-bdde-dc453dfb4193)

## Frontend TEST
![photo_5384129328657929937_y](https://github.com/user-attachments/assets/7c7de756-1de3-452c-8a14-37b26128c677)

## Backend test
![photo_5384129328657929941_y](https://github.com/user-attachments/assets/68e55aa9-9d81-41d4-a3ad-086f403c56e5)





