from task_mgr import TaskMgr
from result_parser import parser_latency, parser_power
from task_chain import get_delays
from argparse import ArgumentParser

my_parser = ArgumentParser(description='runtime')

my_parser.add_argument('-t', '--task', required=True, type=int,
                           help='the number of the task.')

my_parser.add_argument('-o', '--opt', help='Use the list algorithm.', action="store_true")

args = my_parser.parse_args()
task_mgr = TaskMgr("test/a5.txt")
task_mgr.task_run()
edp = parser_latency() * parser_power()
print("Time cost is", get_delays(args.task, args.opt))
