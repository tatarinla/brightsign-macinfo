import os
import sys
import argparse
from macinfo.api_client import APIClient


def _set_cli_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mac_address")
    return parser.parse_args()


def _proceed_request(args):
    if args.mac_address:
        return get_vendor(args.mac_address)
        
# Endpoint(s)
def get_vendor(mac_address):
    client = APIClient()
    return client.get_vendor(mac_address)


# To use from lookup.sh
if __name__ == "__main__":
    args = _set_cli_options()
    sys.stdout.write(_proceed_request(args))

