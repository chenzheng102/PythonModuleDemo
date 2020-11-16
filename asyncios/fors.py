import time

def hello():
    print('Hello World:%s' % time.time())  # 任何伟大的代码都是从Hello World 开始的！



def run():
    for i in range(1000000):
        hello()
if __name__ == '__main__':
    run()