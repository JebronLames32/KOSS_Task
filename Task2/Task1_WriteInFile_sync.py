import time

import requests

record=open("Task2_SyncTime.txt","w")

filename = "Task2_sync.txt"     # create a file with a unique name
f=open(filename,'a')        #APPENDING A SINGLE FILE SINCE I'M NOT SURE IF CREATING 200 FILES WOULD BE A GOOD IDEA

def download(comic_id: int):

    url = f"https://xkcd.com/{comic_id}/info.0.json"
    print("In",url)
    response = requests.get(url)
    
    return response.content


def write_to_file(content: bytes):
    print(content,file=f)
    


if __name__ == "__main__":
    start = time.time()

    for i in range(1,201):      #will take values 1-200 in the loop
        content = download(i)     # download response
        write_to_file(content)   # paste the json contents in the file

    timeTaken = time.time() - start
    print(f"Execution time: {timeTaken:0.2f} seconds.")
    record.writelines(str(timeTaken)+"\n")
    record.close
