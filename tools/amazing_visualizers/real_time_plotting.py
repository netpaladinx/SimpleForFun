import matplotlib.pyplot as plt

if __name__ == '__main__':
    fig = plt.gcf()
    fig.show()
    fig.canvas.draw()

    while True:
        # compute something
        plt.plot([1], [2]) # plot something

        # update canvas immediately
        plt.xlim([0, 100])
        plt.ylim([0, 100])
        plt.pause(0.01)  # I ain't needed!!!
        fig.canvas.draw()