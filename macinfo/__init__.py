import os
import argparse
from macinfo.api_client import APIClient

API_KEY = os.environ.get('MACADDRESS_API_KEY')

def _set_cli_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mac_address")
    return parser.parse_args()


def _proceed_request(args):
    if args.mac_address:
        get_vendor(args.mac_address)
        
# Endpoint(s)
def get_vendor(mac_address):
    client = APIClient(API_KEY)
    return client.get_vendor(mac_address)


# To use from lookup.sh
if __name__ == "__main__":
    args = _set_cli_options()
    _proceed_request(args)


