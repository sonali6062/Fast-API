import asyncio
from timeit import default_timer as timer

async def run_task(name, seconds):
    print(f'{name} starts at: {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} ends at: {timer()}')

async def main():
    start = timer()
    
    # Create tasks to run concurrently
    tasks = [
        run_task('Task 1', 2),
        run_task('Task 2', 1),
        run_task('Task 3', 3)
    ]
    
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    
    print(f'\nTotal time taken: {timer()-start:.2f}s')

# Run the async program
asyncio.run(main())
