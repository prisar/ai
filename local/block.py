import torch
import torch.nn as nn
from resnet import ResNet

class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, in_planes, planes, stride = 1):
        super(BasicBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_planes, planes, kernel_size = 3, stride = stride, padding = 1, bias = False)

m = ResNet(BasicBlock, [2,2,2,2])
print(m)