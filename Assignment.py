import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

def phuong_trinh(h, delta_t):
    #gia tốc trọng trường g=10m/s
    g=10 
    
    #Thời gian để vật B chạm đất
    tB=math.sqrt(2*h/g)               # yB = h - (1/2)*g*(tB**2)
    
    #Thời gian để vật A chạm đất sau vật B t giây
    tA=tB+delta_t
    
    #Vận tốc vo cần tìm
    vA=(-h+(1/2)*g*(tA**2))/tA         #yA = h + vA*tA- (1/2)*g*(tA**2)
    
    print(f"Vận tốc cần tìm: Vo = {vA:.2f}m/s để vật A rơi xuống đất chậm hơn vật B {delta_t} giây")

    #Biểu diễn bằng đồ thị
    #quy_dao(h, tA, tB, vA, g);
    quy_dao(h, tA, tB, vA, g);

def quy_dao(h, tA, tB, vA, g):    
    # Set num_frams dựa trên tA để đảm bảo animation sẽ kết thúc khi vật A chạm đất
    num_frames= 100

    # Tạo mảng giá trị đến tA
    t_points = np.linspace(0, tA, num_frames)

    # Phương trình toạ độ của vật B
    yBpoints = h - (1/2) * g * np.clip(t_points, 0, tB)**2 

    #Phương trình toạ độ của vật A
    yApoints = h + vA * t_points - (1/2) * g * t_points**2
    
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 1)  # Đặt giá trị nhỏ cho trục hoành bởi phương 
                        # trình toạ độ chỉ phụ thuộc vào trục tung
    ax.set_ylim(0, 2 * h)  # Đặt giá trị cho trục tung tối đa là 2h để đảm bảo
                            # có thể thấy được toàn bộ giá trị của vật A khi ném lên
    pointA, = ax.plot([], [], 'ro', label="Vật A", markersize=10)  # Vật A là red circle
    pointB, = ax.plot([], [], 'bo', label="Vật B", markersize=10)  # Vật B là blue circle
    
    def init():
        pointA.set_data([], [])
        pointB.set_data([], [])
        return pointA, pointB
    
    def update(frame):
        # Update giá trị của vật B
        pointB.set_data([0], [max(0, yBpoints[frame])])  # Đảm bảo vật B vẫn sẽ nằm trên mặt đất

        # Update giá trị của vật B (Đảm bảo vật B vẫn sẽ nằm trên mặt đất cho tới khi vật A chạm đất)
        pointA.set_data([0], [yApoints[frame]])

        return pointA, pointB   #Trả về giá trị update cho biến 
    
    # Điều chỉnh thời gian cho animation
    interval = (tA*520) / num_frames
    ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=interval)
    plt.legend()
    plt.xlabel("Tầm xa (Cố định)") # Ném vật thẳng đứng và rớt tại điểm đó 
    plt.ylabel("Độ cao (m)")
    plt.title("Quỹ đạo chuyển động của Vật A và Vật B")
    plt.show()


'''def quy_dao1(h, v, g):    
    x1points = 2
    y1points = np.linspace(h - (1/2)*g*(x1points**2), 0, 100)

    x2points = 2
    y2points = np.linspace(h + v*x2points - (1/2)*g*(x2points**2), 0, 100)
    
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2*h) 
    line1, = ax.plot([], [], 'r-', label="Vật A") 
    line2, = ax.plot([], [], 'b-', label="Vật B") 
    
    def init(): 
        line1.set_data([], []) 
        line2.set_data([], []) 
        return line1, line2 
    def update(frame): 
        line1.set_data(x2points[:frame], y2points[:frame]) 
        line2.set_data(x1points[:frame], y1points[:frame]) 
        return line1, line2 
    
    ani = FuncAnimation(fig, update, frames=len(y2points), init_func=init, blit=True, interval=20)    
    plt.legend()
    plt.xlabel("Thời gian t (s)")
    plt.ylabel("Độ cao h (m)")
    
    plt.show()
'''

def main():
    h = int (input("Nhập vào độ cao ban đầu (m): "))
    delta_t= int (input("Nhập vào thời gian vật A chạm đất trễ hơn so với vật B (s): "))
    phuong_trinh(h, delta_t)

if __name__ == "__main__":
    main()
