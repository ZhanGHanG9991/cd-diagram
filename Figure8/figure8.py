import sys
sys.path.append('/home/zh/opt/project/pycharmproject/cd-diagram')
from main import draw

draw("minirocket_bias_sampled.csv", "/home/zh/opt/project/pycharmproject/cd-diagram/Figure8/", "figure8.png", 0.7)