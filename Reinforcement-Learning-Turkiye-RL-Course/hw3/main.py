from backup import *
from plot_multiple import *

def main():
    lr0_9 = Backup()
    lr0_9.read_log_file("log0_9.txt")

    lr1_0 = Backup()
    lr1_0.read_log_file("log1_0.txt")

    lr1_1 = Backup()
    lr1_1.read_log_file("log1_1.txt")

    lr1_5 = Backup()
    lr1_5.read_log_file("log1_5.txt")

    steps = [i for i in range(5, 247)]
    best_mean_rew0_9 = lr0_9.dict_filter("Best Mean Reward")
    best_mean_rew0_9 = best_mean_rew0_9[5:247]
    best_mean_rew1_0 = lr1_0.dict_filter("Best Mean Reward")
    best_mean_rew1_0 = best_mean_rew1_0[5:247]
    best_mean_rew1_1 = lr1_1.dict_filter("Best Mean Reward")
    best_mean_rew1_1 = best_mean_rew1_1[5:247]
    best_mean_rew1_5 = lr1_5.dict_filter("Best Mean Reward")
    best_mean_rew1_5 = best_mean_rew1_5[5:247]

    plot_multiple(steps, best_mean_rew0_9, best_mean_rew1_0, best_mean_rew1_1, best_mean_rew1_5)

if __name__ == "__main__":
    main()

