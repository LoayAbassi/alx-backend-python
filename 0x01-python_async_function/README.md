# some asynchronus coding

# syntax 

    import asyncio
    # called coroutine too :) 
    async def afunction(): 
        # do something

asyncio.gather(...) // waits for all awaited tasks to finish 
asyncio.create_task(...) // creates a task from a coroutine
coruntime might cause problems when they are awaited out and inside , 2
        