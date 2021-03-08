class Backup:
    def __init__(self):
        self.logfile_name = 'log.txt'
        self.dict_data = dict()
      #  self.file = open(self.logfile_name,"w+")
      #  self.file.write("Timestep	MeanReward100Episodes	BestMeanReward	Episodes	Exploration	LearningRate	RunningTime\n")
      #  self.file.close()

    def read_log_file(self, filename):
        with open(filename,"r+") as fp:
            i = 0
            while True:
                line = fp.readline().strip() # delete \n
                if line == "":
                    break
                else:
                    if i == 0:  # if line is including titles
                        print(line)
                    else:
                        try:
                            # parsing row
                            splitted = line.split("\t")
                            self.dict_append(splitted)

                            print(str(self.dict_data['d' + str(i)]['Time step']) + " " +
                                  str(self.dict_data['d' + str(i)]['Mean Reward 100 Episodes']) + " " +
                                  str(self.dict_data['d' + str(i)]['Best Mean Reward']) + " " +
                                  str(self.dict_data['d' + str(i)]['Episodes']) + " " +
                                  str(self.dict_data['d' + str(i)]['Exploration']) + " " +
                                  str(self.dict_data['d' + str(i)]['Learning Rate']) + " " +
                                  str(self.dict_data['d' + str(i)]['Running Time']))
                        except ValueError: #ignore ValueError: could not convert string to float
                            pass
                    i += 1
        fp.close()
        return 0

    def dict_append(self, dict_data_row):
        row = dict()
        row['Time step'] = int(float(dict_data_row[0]))
        row['Mean Reward 100 Episodes'] = float(dict_data_row[1])
        row['Best Mean Reward'] = 0 if (dict_data_row[2] == '-inf') else float(dict_data_row[2])
        row['Episodes'] = int(float(dict_data_row[3]))
        row['Exploration'] = float(dict_data_row[4])
        row['Learning Rate'] = float(dict_data_row[5])
        row['Running Time'] = float(dict_data_row[6])

        i = len(self.dict_data)
        self.dict_data['d' + str(i + 1)] = row

        return 0

    def dict_filter(self, key):
        col = []
        i = 0
        while i < len(self.dict_data):
            col.append(float(self.dict_data['d' + str(i + 1)][key]))
            i += 1
        return col

    def write_log_file(self, dict_data_row):
        with open(self.logfile_name,"a+") as fp:
            fp.write(str(dict_data_row[0]) + "\t" +
                      str(dict_data_row[1]) + "\t" +
                      str(0 if (dict_data_row[2] == '-inf') else float(dict_data_row[2])) + "\t" +
                      str(dict_data_row[3]) + "\t" +
                      str(dict_data_row[4]) + "\t" +
                      str(dict_data_row[5]) + "\t" +
                      str(dict_data_row[6]) + "\n")
        fp.close()
        print("Your current work saved!")
        return 0
