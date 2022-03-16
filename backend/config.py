import json
import torch

# load vocabulary
with open("./saved_models/vocab/char2int.json", "r") as f:
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
PATH = "./saved_models/charRNN_questions_epoch_60.pt"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")