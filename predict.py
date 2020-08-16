import torch
import numpy as np
from model import Net

MODEL_PATH = './trained_model.pth'

def main():
    # input = [month, day, hour, minute]
    input = np.array([12, 31, 12, 0])

    device = torch.device("cuda")

    model = Net()

    model = model.to(device)
    model.load_state_dict(torch.load(MODEL_PATH))
    model.eval()

    minute_log = np.ndarray((60,2))
    with torch.no_grad():
        for i in range(0, 60):
            input[-1] = i
            data = torch.from_numpy(input)
            data = data.float().cuda().to(device)
            prediction = model(data)
            minute_log[i] = prediction.cpu().numpy()
    minute_log[:, 0] += 47.6
    minute_log[:, 1] -= 122.3
    np.save('minute.npy', minute_log)
    # output should be similar to: 47.6, -122.3

if __name__ == '__main__':
    main()
