from config import Config
import os
import subprocess


class TaskMgr:
    def __init__(self, dir=None, name="inorder"):
        config = Config()
        if dir:
            input_dir = dir
        else:
            self.task_get(name)
            input_dir = config.router_dir + "/" + config.input_file
        file = open(input_dir, 'r')
        self.size = int(file.readline())
        tmp = []
        for line in file.readlines():
            tasks = line.split()
            tmp.append(set(map(int, tasks)))
        self.tasks = tmp

    @staticmethod
    def task_get(name):
        config = Config()
        exe_dir = config.router_dir + "/" + name
        ret = subprocess.check_call(exe_dir)

    def get_target(self, idx):
        res = set()
        if idx in self.tasks[0]:
            res = res | self.tasks[0]
        if idx in self.tasks[1]:
            res = res | self.tasks[1]
        return res

    def task_run(self):
        config = Config()
        self.task_alloc()
        nirgam_exe = config.nirgam_dir + "/nirgam"
        pwd = os.getcwd()
        os.chdir(config.nirgam_dir)
        ret = subprocess.call(nirgam_exe)
        os.chdir(pwd)
        res = config.nirgam_dir + "/results"
        os.system("rm -rf %s" % (pwd + "/results"))
        os.system("cp -r %s %s" % (res, pwd + "/results"))

    def task_alloc(self):
        config = Config()
        nirgam_config = config.nirgam_dir + "/config/nirgam.config"
        nirgam = open(nirgam_config, 'w')
        nirgam.write("TOPOLOGY MESH\n")
        nirgam.write("NUM_ROWS %d\n" % self.size)
        nirgam.write("NUM_COLS %d\n" % self.size)
        nirgam.write("RT_ALGO xy\nDIRNAME fix_packet_a1\nWARMUP 5\nSIM_NUM 20000\nTG_NUM 10000\nCLK_FREQ 1")
        nirgam.close()

        application_config = config.nirgam_dir + "/config/application.config"
        application = open(application_config, 'w')
        out = set()
        for task in self.tasks:
            for item in task:
                out.add(item)
        for task in out:
            application.write("%d news_w.so\n" % task)
        application.close()

        traffic_dir = config.nirgam_dir + "/config/traffic"
        for idx in range(self.size ** 2):
            file = open("%s/tile-%d" % (traffic_dir, idx), 'w')
            file.write("PKT_SIZE 8\nLOAD 100\n")
            target = self.get_target(idx)
            file.write("DESTINATION RANDOM %d" % (0 if len(target) == 0 else len(target) - 1))
            for to in target:
                if to != idx:
                    file.write(" %d" % to)
            file.write("\n")
            file.write("WEIGHT %d" % (0 if len(target) == 0 else len(target) - 1))
            for to in target:
                if idx != to:
                    file.write(" 400")
            file.write("\n")
            file.write("FLIT_INTERVAL 2")
            file.close()
