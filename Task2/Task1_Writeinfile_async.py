import aiohttp
import asyncio
import time

record=open("Task2_AsyncTime.txt","a")
filename = "Task2_Async.txt"     # create a file with a unique name
f=open(filename,'a')        #APPENDING A SINGLE FILE SINCE I'M NOT SURE IF CREATING 200 FILES WOULD BE A GOOD IDEA

async def getOnePage(session,comic_id: int):
    url = f"https://xkcd.com/{comic_id}/info.0.json/"
    async with session.get(url) as sesh:
        content=await sesh.read()
        print(content,file=f)               #writing contents into the file one by one here
        print(f"Begin downloading {url}")
        result=await sesh.text()
        print(f"Finished downloading {url}")
        return result

async def getAllPages(session):
    tasks=[]        #creating a dynamic array to store all the tasks we want to rin parallely
    for i in range(1,201):         #will take values 1-200 in loop
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



    