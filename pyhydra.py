#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import argparse
import os
import sys
import time

dict_dir = '/usr/share'

def cmdLineParser():
    parser = argparse.ArgumentParser(add_help=False)
    usage = parser.add_argument_group('Usage')
    usage.add_argument('-l', metavar='user', dest="l", type=str, default='',help='user input')
    usage.add_argument('-p', metavar='pass', dest="p", type=str, default='',help='pass input')
    usage.add_argument('-ip', metavar='ip', dest="ip", type=str, default='',help='ip input')
    usage.add_argument('-M', metavar='file', dest="file", type=str, default='',help='file input')
    usage.add_argument('-m', metavar='module', dest="m", type=str, default='',help='designated module')
    usage.add_argument('-s', metavar='port', dest="s", type=str, default='', help='designated port')
    syst = parser.add_argument_group('sys')
    syst.add_argument('-v',action='version', version='v1.0',help="")
    syst.add_argument('-h',action='help',help='')
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    return parser.parse_args()


if __name__ == '__main__':
    if not os.path.exists("hyresult"):
        os.mkdir("hyresult")
    only_pass_module = ['redis','adam6500','cisco','oracle-listener','s7-300','snmp','vnc']
    args = cmdLineParser()
    cmds = []
    module = args.m.lower()
    cmds.append("hydra")
    if not module in only_pass_module:
        if args.l:
            cmds.append('-l {}'.format(args.l))
        else:
            cmds.append('-L {}'.format(os.path.join(dict_dir,'hydict/{}_username.txt'.format(module))))
    if args.p:
        cmds.append('-p {}'.format(args.p))
    else:
        cmds.append('-P {}'.format(os.path.join(dict_dir,'hydict/{}_password.txt'.format(module))))
    if args.ip:
        cmds.append('{}'.format(args.ip))
    elif args.file:
        cmds.append('-M {}'.format(args.file))
    else:
        sys.exit(-1)
    if args.s:
        cmds.append('-s {}'.format(args.s))
    cmds.append('-vV')
    cmds.append('-o hyresult/{}_{}.txt'.format(module,time.strftime("%m%d_%H%M%S", time.localtime())))
    cmds.append('-e nsr')
    cmds.append('-q')
    cmds.append('-I')
    cmds.append('-K')
    cmds.append('-f')
    cmds.append(module)
    RUN_CMD = ' '.join(cmds)
    print(RUN_CMD)
    os.system(RUN_CMD)




