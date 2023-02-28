# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def insertionSort(nlist):
  for index in range(1,len(nlist)):
    currentvalue = nlist[index]
    position = index
    while position > 0 and nlist[position-1] > currentvalue:
      nlist[position] = nlist[position-1]
      position = position-1
    nlist[position] = currentvalue




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    insertionSort(nlist)
    print(nlist)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
