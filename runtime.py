from task_mgr import TaskMgr
from result_parser import parser_latency, parser_power

task_mgr = TaskMgr("test/a5.txt")
task_mgr.task_run()
edp = parser_latency() * parser_power()
print("edp is", edp)