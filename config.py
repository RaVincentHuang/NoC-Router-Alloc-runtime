import configparser
from argparse import ArgumentParser


class Config:
    def __init__(self):
        configs = configparser.ConfigParser()
        configs.read("configure", encoding='utf-8')
        self.nirgam_dir = configs.get("Nirgam", "nirgam_dir")
        self.router_dir = configs.get("Router", "router_dir")
        self.input_file = configs.get("Router", "input_file")
        self.exe_name = configs.get("Router", "exe_name")


if __name__ == "__main__":
    my_parser = ArgumentParser(description='config')
    my_parser.add_argument('-n', '--nirgam_dir', required=True, type=str,
                           help='The nirgam_dir.')
    my_parser.add_argument('-r', '--router_dir', required=True, type=str,
                           help='The router_dir.')
    my_parser.add_argument('-o', '--output', required=True, type=str, default="out.txt",
                           help='The router_dir.')
    my_parser.add_argument('-e', '--exe_name', required=True, type=str,
                           help='The router_dir.')
    args = my_parser.parse_args()
    config = configparser.ConfigParser()
    config.read("configure", encoding='utf-8')
    config.set("Nirgam", "nirgam_dir", args.nirgam_dir)
    config.set("Router", "router_dir", args.router_dir)
    config.set("Router", "input_file", args.output)
    config.set("Router", "exe_name", args.exe_name)
