import torch
import matplotlib.pyplot as plt

y = torch.distributions.normal.Normal(loc=0.0, scale=1.0)
print(y)
# plt.plot(y)
# plt.show()