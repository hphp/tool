'''/***************************************************************************
 * 
 * Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
 * 
 **************************************************************************/
 
 
 
/**
 * @file test_tool.py
 * @author hanjiatong(com@baidu.com)
 * @date 2014/09/19 12:43:21
 * @brief 
 *  
 **/
/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
'''
#encoding: utf-8
import argparse
import os
import time
parser = argparse.ArgumentParser(description='test command')

def test_roll():
    cmd = "python log_roll_4cgi.py"
    for count in range(30*10):
        os.system(cmd)
        time.sleep(2)

if(__name__ == '__main__'):
    parser.add_argument('cmd', metavar='S', type=str, nargs='+', help='test command')
    args = parser.parse_args()
    if args.cmd[0] == "roll":
        test_roll()
