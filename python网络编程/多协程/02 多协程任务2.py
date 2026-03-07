import asyncio
import time


async def eat():
    for i in range(6):
        print('正在吃饭！')
        await asyncio.sleep(0.5)

async def work():
    for i in range(6):
        print('正在作业！')
        await asyncio.sleep(0.5)

async def main():    # 其他协程的入口
    await asyncio.gather(eat(),work())    # 当第一个协程强制终止，会影响第二个协程的执行。

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'耗时为：{time.time() - start}')