import numpy as np
import matplotlib.pyplot as plt
import math
def phuong_trinh(h, t):
    #gia tốc trọng trường g=10m/s
    g=10 
    
    #Thời gian để vật B chạm đất
    t1=math.sqrt(2*h/g)               # y1 = h - (1/2)*g*(t1**2)
    y1 = h - (1/2)*g*(t1**2)
    
    #Thời gian để vật A chạm đất sau vật B t giây
    t2=t1+t
    
    #Vận tốc vo cần tìm
    v=(-h+(1/2)*g*(t2**2))/t2         #y2 = h + v*t - (1/2)*g*(t2**2)
    y2 = h + v*t - (1/2)*g*(t2**2)
    
    print(f"Vận tốc cần tìm: Vo = {v}m/s để vật A rơi xuống đất chậm hơn vật B {t} giây")

    #Biểu diễn bằng đồ thị
    x2points = np.linspace(0, t2, 10000)
    y2points = h + v*x2points - (1/2)*g*(x2points**2)
    
    x1points = np.linspace(0, t1, 10000)
    y1points = h - (1/2)*g*(x1points**2)


    plt.plot(x1points, y1points, label = "Vật B")
    plt.plot(x2points, y2points, label = "Vật A")
    
    plt.legend()
    plt.xlabel("Thời gian t (s)")
    plt.ylabel("Độ cao h (m)")
    
    plt.show()

a= int (input("Nhập vào độ cao ban đầu: "))
b= int (input("Nhập vào thời gian vật A chạm đất trễ hơn so với vật B: "))
phuong_trinh(a,b)
