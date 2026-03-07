import asyncio

# 普通函数
def hello(msg:str):
    print(f'hello {msg}')

# 定义一个异步函数
async def test():
    print('hello')
    # 挂起当前的协程，等待1秒。
    # 当该协程挂起的时候，可以去执行其他协程（异步任务）
    await asyncio.sleep(1)   # 目的：切换
    # time.sleep()  不会进行协程的切换，只会让当前进程挂起，并且等待1秒。
    print('world')

hello('上古')
# 创建了一个协程，协程还没有开始。
# coroutine = test()
# print(coroutine)

# 启动协程
asyncio.run(test())


