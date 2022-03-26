
import argparse
import logging
logger = logging.getLogger(__name__)

# PROJECT IMPORTS
from tttbot import Client 

# TYPE CHECKING
from typing import *

def arg_parser() -> argparse.Namespace:

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--config', type=str, help='Path to config file.', default="config.yml")
    return parser.parse_args()

def main():

    logging.basicConfig(level=logging.INFO)

    args: argparse.Namespace = arg_parser()

    client: Client = Client(args.config)
    client.run()

if __name__ == "__main__":
    main()