import matplotlib.pyplot as plt

def plot_multiple(x, y1, y2, y3, y4):
    plt.figure(figsize=(8, 8))

    plt.plot(x, y1, label="lr = 0.9e-4")
    plt.xlabel('time step (s)')
    plt.ylabel('Best Mean Reward')

    plt.plot(x, y2, label="lr = 1.0e-4")
    plt.xlabel('time step (s)')

    plt.plot(x, y3, label="lr = 1.1e-4")
    plt.xlabel('time step')

    plt.plot(x, y4, label="lr = 1.5e-4")
    plt.xlabel('time step')

    plt.legend()

    filename = "multiple_plot" + str(max(x)) + ".png"

    plt.savefig(filename)
    plt.show()

