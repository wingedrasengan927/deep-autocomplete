import json
import torch
import os

# load vocabulary
vocab_path = os.path.join("app", "saved_models", "vocab", "char2int.json")
with open(vocab_path, "r") as f:
    char2int = json.load(f)
    # add additional key to account for "space" in unicode form
    char2int.update({"\xa0": char2int[" "]})

int2char = {v:k for k, v in char2int.items()}

# define parameters
VOCAB_SIZE=len(int2char)
HIDDEN_SIZE=512
N_LAYERS=3
P_DROPOUT = 0.4
BATCH_FIRST = True
PATH = os.path.join("app", "saved_models", "charRNN_questions_epoch_60.pt")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")