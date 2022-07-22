# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

import requests as requests

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pageSize = 100
    totalSize = 311
    numPages = int(totalSize / pageSize) + 1
    print(numPages)
    successCount = 0
    failureCount = 0
    failureList = []
    for pageNumber in range(1, numPages + 1):
        url = 'https://api.staging.jupiter.money/lobby/v1/migrate?pageSize=' \
              + str(pageSize) + '&pageNumber=' + str(pageNumber)
        response = requests.post(url)
        print("pageNumber: " + str(pageNumber))
        if response.status_code != 200:
            failureList.append(pageNumber)

        time.sleep(10 / 1000)

    print(failureList)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
