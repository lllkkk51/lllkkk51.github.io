#!/usr/bin/python
# Copyright (c) Microsoft. All rights reserved.


# Note: This script targets Python 2

import argparse
from argparse import SUPPRESS
import sys
import os.path
import getpass
import subprocess
import mssqlconfhelper
import mssqlsettingsmanager
from ConfigParser import ConfigParser

def main():
    """Program main function
    """
    ret = sys.argv[1]
    ret = mssqlconfhelper.configureSqlservrWithArguments("--setup --reset-sa-password", MSSQL_SA_PASSWORD=ret)
    if(ret == 0):
#lllkkk        print(_("The system administrator password has been changed."))
        print(("The system administrator password has been changed."))

    exit(mssqlconfhelper.successExitCode)

if __name__ == "__main__":
    main()

