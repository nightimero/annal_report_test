# -*- coding: utf-8 -*-
# 通过win32api获取系统屏幕的分辨率
def get_system_metrics():
    from win32api import GetSystemMetrics
    return GetSystemMetrics(0), GetSystemMetrics(1)

# 传入窗口大小(分辨率)计算出窗口居中的位置
def get_window_positons(width , height):
    system_metrics =get_system_metrics()
    window_x_position = (system_metrics[0] - width)//2
    window_y_position = (system_metrics[1] - height) // 2
    return window_x_position, window_y_position


# 测试窗口
def my_window():
    import Tkinter as tk

    root = tk.Tk()
    root_width = 300
    root_height = 150
    pos = get_window_positons(root_width, root_height)
    # root.geometry({root_width}x{root_height}+pos[0]+pos[1])  # 这里估计是python3的写法。需要看看python2怎么写。
    tk.mainloop()

if __name__ == '__main__':
    my_window()
