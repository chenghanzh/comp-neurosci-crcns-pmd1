#!/bin/env python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" A very simple script """

import getpass
import argparse


if __name__=="__main__":

    p = argparse.ArgumentParser(description='prints hello')
    args = p.parse_args()

    print("Hello {}!".format(getpass.getuser()))
