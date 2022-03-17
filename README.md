# Deep Autocomplete
A Deep learning based autocomplete using character RNNs
Associated blog: https://medium.com/p/1eb7ae19bfd8 

## Running Locally
clone this repository:
```
git clone https://github.com/wingedrasengan927/deep-autocomplete.git
cd deep-autocomplete
```

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