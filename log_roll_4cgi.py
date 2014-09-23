
'''
/***************************************************************************
 * 
 * Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
 * 
 **************************************************************************/
 
 
 
/**
 * @file log_roll_4cgi.py
 * @author hanjiatong(com@baidu.com)
 * @date 2014/09/19 11:21:42
 * @brief 
 *  
 **/

/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
'''
import datetime
import os
import glob

def rolling():
    lastMinuteDateTime = datetime.datetime.now() - datetime.timedelta(minutes = 1)
    lastMin_time_format = lastMinuteDateTime.strftime('%Y-%m-%d_%H_%M')
    file = "out.log_roll_4cgi"
    if not glob.glob(lastMin_time_format):
        cmd = " ".join(("mv", file, lastMin_time_format))
        os.system(cmd)
    cmd = " ".join(("echo", datetime.datetime.now().strftime('%Y-%m-%d_%H_%M'), ">>", file))
    os.system(cmd)

if __name__ == "__main__":
    rolling()
