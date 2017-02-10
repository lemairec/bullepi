#!/usr/bin/env python

import sys, optparse, subprocess, urllib2, os, os.path, errno, zipfile, string, json, platform, shutil, tarfile, urlparse, tempfile, multiprocessing
from subprocess import Popen, PIPE
import argparse
import sys

def callWithoutPrint(cmdline):
    ret = subprocess.call(cmdline, shell=True)
    if ret != 0:
        print >> sys.stderr, 'Running: ' + cmdline + ' failed with exit code ' + str(ret) + '!'
    return ret

def call(cmdline):
    print 'Running: ' + cmdline
    callWithoutPrint(cmdline)


class VimExec(object):

    def __init__(self):
        parser = argparse.ArgumentParser( description='WeedVision');
        parser.add_argument('command', help='Subcommand to run'
                , choices=['vim_f5', 'vim_f6', 'vim_f7', 'vim_f8']);
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)
        getattr(self, args.command)()



    def vim_f5(self):
        call('python bulle_server.py');

    def vim_f6(self):
        call('python test.py');


if __name__ == '__main__':
    VimExec()
