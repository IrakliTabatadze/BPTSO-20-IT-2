import time
from datetime import datetime
import asyncio


async def drink_coffee():
    print('Start Drinking Coffee')
    await asyncio.sleep(2)
    print('Finished Drinking')
    return 'Coffee Drinking'


async def eat_breakfast():
    print('Start Eating Breakfast')
    await asyncio.sleep(5)
    print('Finished Eating')
    return 'Eating Breakfast'


async def main():
    start_time = datetime.now()

    # drink_coffee()
    # eat_breakfast()

    # coffee = asyncio.create_task(drink_coffee())
    # breakfast = asyncio.create_task(eat_breakfast())
    #
    # await coffee
    # await breakfast

    # print(coffee)
    # print(breakfast)

    lst = [drink_coffee(), eat_breakfast()]

    all_tasks = asyncio.gather(*lst)

    # await all_tasks

    coffee, breakfast = await all_tasks

    print(coffee)
    print(breakfast)

    end_time = datetime.now()

    print('Elapsed time: {}'.format(end_time - start_time))


if __name__ == '__main__':
    asyncio.run(main())

def test(*args):
    print(args)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a, b, *numbers = lst

test(*numbers)
test(3, 4, 5, 6, 7, 8, 9)

