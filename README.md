# Deep Autocomplete
A Deep learning based autocomplete using character RNNs
Associated blog: https://medium.com/p/1eb7ae19bfd8 

### Clone the repository
clone this repository:
```
git clone https://github.com/wingedrasengan927/deep-autocomplete.git
cd deep-autocomplete
```

## Running Locally

It is recommended to use a python virtual environment either with `conda` or `venv` for the backend.

### launching backend server
```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host localhost --port 8000
```

You should see the server up and running:

### launching frontend server
```
cd frontend
npm install
npm run serve
```

You should see the server up and running:

## Deployment in Kubernetes
Assuming you have Kubernetes installed, run the following commands in the order
```
kubectl apply -f ./backend/backend-deployment.yaml
kubectl apply -f ./backend/backend-service.yaml
kubectl apply -f ./frontend/frontend-deployment.yaml
kubectl apply -f ./frontend/frontend-service.yaml
```

You should see the application running at `localhost:8080`
