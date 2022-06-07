import time
import requests

record=open("synchronousDloadTime.txt","a")


def download(el: int):

    url = f"https://reqres.in/api/users?page{el}"
    print(f"Begin downloading {url}")
    response = requests.get(url)
    print(f"Finished downloading {url}")
    return response.content





if __name__ == "__main__":
    start = time.time()

    for i in range(3):
        download(i+1)
        

    timeTaken = time.time() - start
    print(f"Execution time: {timeTaken:0.2f} seconds.")
    record.writelines(str(timeTaken)+"\n")
    record.close