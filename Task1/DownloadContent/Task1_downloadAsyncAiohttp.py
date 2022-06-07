import aiohttp
import asyncio
import time

record=open("AsyncDloadTime.txt","a")

async def getOnePage(session,el: int):
    url = f"https://reqres.in/api/users?page{el}"
    async with session.get(url) as sesh:
        print(f"Begin downloading {url}")
        result=await sesh.text()
        print(f"Finished downloading {url}")
        return result

async def getAllPages(session):
    tasks=[]        #creating a dynamic array to store all the tasks we want to rin parallely
    for i in range(1,4):         #will take values 1,2,3 in loop
        task=asyncio.create_task(getOnePage(session,i))
        tasks.append(task)
    results= await asyncio.gather(*tasks)       #pointing to the list so that all the members are defined as async task
    return results

async def Main():
    async with aiohttp.ClientSession() as sesh:
        downloads = await getAllPages(sesh)
        return downloads

if __name__ == "__main__":
    start=time.time()
    finalresult=asyncio.run(Main())
    timeTaken=time.time()-start
    print(f"Time taken= {timeTaken:0.2f} seconds")
    record.writelines(str(timeTaken)+"\n")
    record.close



    
    