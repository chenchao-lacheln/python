import threading
import time

def task():
    time.sleep(5)
# Gil
# 在同一时刻，只能有一个线程在运行
def main():
    # 开始时间
    start_time = time.time()
    # threading.Thread 创建一个线程
    thread1 = threading.Thread(target=task)
    thread2 = threading.Thread(target=task)
    #让线程执行
    thread1.start()
    thread2.start()
    # 让其他线程等待自己执行完成
    # thread1.join()
    # thread2.join()
    end_time = time.time()
    print(end_time - start_time)

if __name__ == "__main__":
    main()