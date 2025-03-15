import time

def memory_intensive_task():
    large_list = [0] * 10**7
    time.sleep(30)
    
if __name__ == "__main__":
    while True:
        memory_intensive_task()