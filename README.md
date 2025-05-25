# 🚀 Three-Tier Web Application on GCP & Firebase

## 📖 Description

This project demonstrates a **full-stack 3-tier web application** deployed on **Google Cloud Platform (GCP)** and **Firebase Hosting**.  
The application features:

- A **React frontend** hosted on Firebase
- A **Flask backend API** deployed on Cloud Run
- A **PostgreSQL database** managed by Cloud SQL

This architecture reflects the classic three-tier model (presentation, logic, and data), separated into independent, scalable services.

---

## 🗺️ Architecture 

**Flow Summary:**
- Frontend (React) → Sends HTTP requests to Backend (Flask via Cloud Run)
- Backend → Connects securely to Cloud SQL via VPC connector and Private IP

---

## 🧰 Technologies Used

### Frontend:
- React.js
- HTML, CSS, JavaScript
- npm
- Firebase Hosting

### Backend:
- Flask (Python)
- Docker
- Google Cloud Run
- VPC Access Connector

### Database:
- PostgreSQL
- Google Cloud SQL

### Infrastructure & Tools:
- Google Cloud Platform (GCP): Compute, VPC, IAM, Cloud Build, Artifact Registry
- Firebase CLI
- Google Cloud SDK
- Git & GitHub
- Visual Studio Code

---

## ✨ Features

- Interactive UI built with React
- REST API to serve frontend requests
- Cloud-native deployment (Cloud Run, Cloud SQL)
- Firebase Authentication integration (optional)
- Scalable and modular architecture
- Secure VPC communication

---

## 🌐 Live Demo

[🔗 Click here to see the live application in action!](https://three-tier-app-project.web.app/)

---

## 🛠️ Getting Started (Local Development)

### 🔗 Prerequisites

Make sure the following are installed:

- Node.js and npm
- Python and pip
- Docker
- Google Cloud SDK (`gcloud`)
- Firebase CLI (`npm install -g firebase-tools`)

### 🔃 Clone the Repository

```bash
git clone https://github.com/Shervin29/three-tier-web-app-gcp-firebase.git
cd your-project-name
```

---

### ⚙️ Frontend Setup

```bash
cd frontend
npm install
npm start
```

To build:

```bash
npm run build
```

---

### 🧱 Backend Setup

For **Python/Flask**:
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

For **Node.js**:
```bash
cd backend
npm install
npm start
```

---

### 🗃️ Database Setup (Local Mock/Remote)

This project connects directly to **Cloud SQL (PostgreSQL)** over Private IP.  
For local development, configure a `.env` or connection string to use a remote Cloud SQL instance (no local DB setup required).

---

## 🚀 Deployment Information

- **Frontend**: Deployed on Firebase Hosting
- **Backend**: Containerized with Docker and deployed to Google Cloud Run
- **Database**: PostgreSQL on Cloud SQL with Private IP
- **Networking**: Connected via VPC and VPC Access Connector

👉 Detailed steps are documented in [`docs/deployment_notes.md`](docs/deployment_notes.md)

---

## 📁 Folder Structure

```
your-project-root/
├── frontend/          # React.js frontend code
├── backend/           # Flask or Node.js backend code
├── docs/
│   ├── architecture.png
│   └── deployment_notes.md
└── README.md
```

---

## 🙏 Credits / Acknowledgments

- GCP and Firebase Docs
- Open-source Flask & React starter templates

---

## 📜 License

Distributed under the MIT License.  
See `LICENSE` for more information.
