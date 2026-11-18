import asyncio
async def main():
  task=asyncio.cr_task(fn2())
  print(1)
  print(4)
  await asyncio.sleep(3)
  print(5)
  await asyncio.sleep(1)

async def fn2():
  await asyncio.sleep(1)
  print(2)
  await asyncio.sleep(3)
  print(3)