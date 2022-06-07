import re

def parser_latency():
    latency_dir = "results/fix_packet_a1/stats/sim_results"
    file = open(latency_dir, 'r')
    str = file.read()
    file.close()
    item = re.search("flit\\) = \d+\\.\d+", str).group()
    latency = float(item[7:])
    return latency

def parser_power():
    power_dir = "results/fix_packet_a1/stats/power_sim_results"
    file = open(power_dir, 'r')
    str = file.read()
    file.close()
    item = re.search(":\d+\\.\d+", str).group()
    power = float(item[1:])
    return power