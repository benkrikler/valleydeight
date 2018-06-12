"""
Demo of validating the dictionary contained in a yaml file.
"""
from __future__ import print_function
import yaml
import argparse
import glob
import os
import valleydeight as vd


def run(config):
    # Set up the schema
    stage_description = vd.Dict(glob=vd.Str(), recursive=vd.Bool(), print_dirs=vd.Bool())
    all_stage_description = vd.List(vd.Object(StudyDirectory, args=stage_description))

    # Process the provided config
    stages = all_stage_description(config)

    # Execute things
    for stage in stages:
        stage.execute()


def prepare_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("in_file", help='The name of the input file')
    args = parser.parse_args()
    return args


def read_config(filename):
    with open(filename, "r") as infile:
        cfg = yaml.load(infile)
    return cfg


class StudyDirectory():
    def __init__(self, glob, recursive=True, print_dirs=True):
        self.glob = glob
        self.recursive = recursive
        self.print_dirs = print_dirs

    def execute(self):
        files = glob.glob(self.glob)
        self.files = [f for f in files if os.path.exists(f)]
        self.dirs = [f for f in files if os.path.isdir(f)]

        if self.recursive:
            for directory in self.dirs:
                for root, dirs, files in os.walk(directory):
                    self.files += files
                    self.dirs += dirs

        print("The glob:", self.glob, "(recursive =", self.recursive, ")")
        print("   points to", len(self.files), "files:", self.files)
        if self.print_dirs:
            print("   and", len(self.dirs), "directories")


if __name__ == "__main__":
    args = prepare_args()
    config = read_config(args.in_file)
    run(config)
