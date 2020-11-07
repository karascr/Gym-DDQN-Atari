import matplotlib.pyplot as plt

def plot(x, mean_rew, best_mean_rew):
    plt.figure(figsize=(8, 8))

    plt.plot(x, mean_rew, label="Mean Reward")
    plt.xlabel('time step (s)')
    plt.ylabel('Mean Rewad')

    plt.plot(x, best_mean_rew, label="Best Mean Reward")
    plt.xlabel('time step')
    plt.ylabel('Best Mean Reward')

    plt.legend()

    filename = "plot" + str(max(x)) + ".png"

    plt.savefig(filename)


