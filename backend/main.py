from fastapi import FastAPI, WebSocket

from model import charRNN, GenerateText
from config import *

app = FastAPI()

# load model
model = charRNN(VOCAB_SIZE, HIDDEN_SIZE, N_LAYERS, P_DROPOUT, BATCH_FIRST)
model.load_state_dict(torch.load(PATH, map_location=device))
model.eval()

text_gen = GenerateText(model, int2char, char2int, device)

@app.websocket("/predict")
async def predict_question(websocket: WebSocket):
    await websocket.accept()
    while True:
        input_text = await websocket.receive_text()
        autocomplete_text = text_gen.generate_text(input_text)
        await websocket.send_text(autocomplete_text)