# 📘 Deployment Notes: GCP-Based 3-Tier Web Application

This document explains the step-by-step deployment of a full-stack 3-tier web app using **Google Cloud Platform (GCP)**, React (frontend), Flask (backend), and PostgreSQL (database).

---

## 🧩 Part 1: Set Up GCP Account

### Step 1.1: Create a GCP Account
- Open your browser and visit: `https://cloud.google.com`
- Click **“Get started for free”**
- Sign in with a Google account
- Accept terms and conditions
- Set up billing (Free $300 credits included)
- Create a new project: **`three-tier-app-project`**

---

## 🛠 Part 2: Set Up the Environment

### Step 2.1: Enable Required APIs
1. Go to: `Navigation Menu (☰)` → **APIs & Services** → **Library**
2. Enable the following:
   - **Compute Engine API**
   - **Cloud SQL Admin API**
   - **Cloud Run API** (or App Engine if preferred)
   - **VPC Access Connector API**

### Step 2.2: Install Google Cloud SDK (on your local machine)
- Visit: `https://cloud.google.com/sdk/docs/install`
- Download and install the SDK
- Open a terminal and run:
  ```bash
  gcloud init
  ```
- Log in and select your project.

---

## ☁️ Part 3: VPC, Subnets & Security

### Step 3.1: Create VPC and Subnets
1. Go to **VPC Network** → **VPC Networks** → **Create VPC**
2. Configure:
   - Name: `three-tier-vpc`
   - Mode: **Custom**
3. Add Subnets:
   - `frontend-subnet`: `10.0.1.0/24`
   - `backend-subnet`: `10.0.2.0/24`
   - `db-subnet`: `10.0.3.0/24`

### Step 3.2: Firewall Rules
- Rule 1: `allow-http`
  - Source: `0.0.0.0/0`
  - TCP Ports: `80,443`
- Rule 2: `allow-ssh`
  - TCP Port: `22`

---

## 🧱 Part 4: Backend Setup (Flask)

### Step 4.1: Create Locally
1. In `VS Code` or terminal:
   ```bash
   mkdir backend && cd backend
   ```
2. Add code:
   ```python
   from flask import Flask
   app = Flask(__name__)
   @app.route('/')
   def hello(): return "Hello from Backend!"
   if __name__ == '__main__': app.run()
   ```
3. Run it locally:
   ```bash
   pip install flask
   python app.py
   ```

---

## 🗃 Part 5: Cloud SQL (PostgreSQL)

### Step 5.1: Create Instance
- Go to **SQL** → **Create instance**
- Choose **PostgreSQL**
- Instance ID: `three-tier-db`
- Set strong root password
- Enable **Private IP** and attach to `three-tier-vpc`

### Step 5.2: Create Database & User
- Create DB: `myappdb`
- Create User: `appuser`

---

## 🚀 Part 6: Deploy Backend to Cloud Run

### Step 6.1: Dockerize and Deploy
1. Create `Dockerfile` in `backend/`:
   ```dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY . /app
   RUN pip install flask
   CMD ["python", "app.py"]
   ```
2. Deploy:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/backend
   gcloud run deploy backend-service \
     --image gcr.io/YOUR_PROJECT_ID/backend \
     --platform managed \
     --allow-unauthenticated \
     --region us-central1 \
     --vpc-connector=YOUR_VPC_CONNECTOR
   ```

---

## 🎨 Part 7: Frontend Setup (React)

### Step 7.1: Create App
```bash
npx create-react-app frontend
cd frontend
npm start
```

### Step 7.2: Connect to Backend
- Edit `App.js` to call the **Cloud Run backend URL**

### Step 7.3: Deploy to Firebase
```bash
npm install -g firebase-tools
firebase login
firebase init hosting
npm run build
firebase deploy
```

---

## 🧪 Part 8: Test End-to-End

- Open your **Firebase Hosting URL**
- Test frontend → backend → database integration
- Check logs in:
  - **Cloud Run** → Logs
  - **SQL** → Query logs
  - **Operations Suite** for monitoring

---

✅ **Done!**  
Your GCP-based 3-tier app is deployed and live.