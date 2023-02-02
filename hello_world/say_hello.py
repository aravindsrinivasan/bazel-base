"""
bazel run //hello_world:say_hello -- \
    --name Aravind
"""

import argparse
import glog

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
args = parser.parse_args()


def main():
    glog.info(f'Hello, {args.name}!')


if __name__ == "__main__":
    main()
