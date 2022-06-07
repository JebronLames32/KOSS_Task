import threading
import time
import requests

record=open("threadingDloadTime.txt","a")


def download(el: int):

    url = f"https://reqres.in/api/users?page{el}"
    print(f"Begin downloading {url}")
    response = requests.get(url)
    print(f"Finished downloading {url}")
    return response.content

if __name__ == "__main__":
    
    t1 = threading.Thread(target=download, args=(1,))
    t2 = threading.Thread(target=download, args=(2,))
    t3 = threading.Thread(target=download, args=(3,))

    
   
    
    start = time.time()
    t1.start()
    t2.start()
    t3.start()

    t1.join()       #making sure all three have returned before finding time
    t2.join()
    t3.join()

    timeTaken = time.time() - start
    print(f"Time Taken {timeTaken:0.2f} seconds")
    record.writelines(str(timeTaken)+"\n")
    record.close