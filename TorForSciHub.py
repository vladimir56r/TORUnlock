# -*- coding: utf-8 -*-
import sys, traceback
import requests
import os
from datetime import datetime
import time
import json
import collections
from bs4 import BeautifulSoup
#
import argparse
import progressbar as pb
#
from torrequest import TorRequest


_HOST = "http://sci-hub.tw/"
_DOI = "10.1080/13658816.2017.1410549"


# CONSOLE LOG
cfromat = "[{0}] {1}{2}"
def print_message(message, level=0):
    level_indent = " " * level
    print(cfromat.format(datetime.now(), level_indent, message))
#


def main():
    start_time = datetime.now()
    try:
        print_message("Connection to TOR...")
        with TorRequest(tor_app=r".\Tor\tor.exe") as tr:
            print_message("Get page. URL = {}".format("{}{}".format(_HOST, _DOI)))
            resp = tr.get("{}{}".format(_HOST, _DOI))
            if resp is not None:
                print_message("Save page to 'example.html'")
                with open("example.html", "w") as f:
                    f.write(resp.text)
    except:
        print_message(traceback.format_exc())
    end_time = datetime.now()
    print_message("Run began on {0}".format(start_time))
    print_message("Run ended on {0}".format(end_time))
    print_message("Elapsed time was: {0}".format(end_time - start_time))


if __name__ == "__main__":
    main()