import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import random
def arraygenerate():
    chooselist = [1, 0]
    longlist = []
    for _ in range(200):
        templist = []
        for _ in range(200):
          templist.append((random.choice(chooselist)))
        longlist.append(templist)
    array = np.array(longlist)
    return array
def update(framenum, arrayimage, coordinatearray, birthlist, survivelist):
    newarray = coordinatearray.copy()
    for i in range(200):
        for j in range(200):
            xmore = (i + 1)%200
            xless = (i - 1)%200
            ymore = (j + 1)%200
            yless = (j - 1)%200
            touchnum = (coordinatearray[xmore, j] + coordinatearray[xmore, ymore] + coordinatearray[xmore, yless]
            + coordinatearray[xless, j] + coordinatearray[xless, ymore] + coordinatearray[xless, yless]
            + coordinatearray[i, ymore] + coordinatearray[i, yless])
            if coordinatearray[i, j] == 1:
                if touchnum in survivelist:
                    newarray[i, j] = 1
                else:
                    newarray[i, j] = 0
            elif coordinatearray[i, j] == 0:
                if touchnum in birthlist:
                    newarray[i, j] = 1
                else:
                    newarray[i, j] = 0
    arrayimage.set_data(newarray)
    coordinatearray[:]=newarray[:]
    return arrayimage
def main():
    print('Press 1 for Conway\'s Game of Life, 2 for Day and Night, 3 for Highlife, 4 for Diamoeba, 5 for Anneal, 6 for Seeds')
    cellchoice = input('> ')
    if cellchoice == '1':
        birthlist = [3]
        survivelist = [2, 3]
        title = 'Conway\'s Game of Life'
    elif cellchoice == '2':
        birthlist =  [3, 6, 7, 8]
        survivelist = [3, 4, 6, 7, 8]
        title = 'Day and Night'
    elif cellchoice == '3':
        birthlist =  [3, 6]
        survivelist = [2, 3]
        title = 'Highlife'
    elif cellchoice == '4':
        birthlist = [3, 5, 6, 7, 8]
        survivelist = [5, 6, 7, 8]
        title = 'Diamoeba'
    elif cellchoice == '5':
        birthlist = [4, 6, 7, 8]
        survivelist = [3, 5, 6, 7, 8]
        title = 'Anneal'
    elif cellchoice == '6':
        birthlist = [2]
        survivelist = []
        title = 'Seeds'
    else:
        print('That is not a valid choice.')
        main()
    # Code for displaying the arrays inspired by Mahesh Venkitachalam
    array = arraygenerate()
    fig, ax = plt.subplots()
    arrayimage = ax.imshow(array, interpolation='nearest')
    arrayanimate = animation.FuncAnimation(fig, update, fargs=(arrayimage, array, birthlist, survivelist))
    plt.title(title)
    plt.show()
    # Inspired code over
if __name__ == '__main__':
    main()