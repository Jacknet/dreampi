#!/usr/bin/env python
import os
import sys
from subprocess import Popen, PIPE
import fcntl
driver = sys.argv[-1]
print "resetting driver:", driver
USBDEVFS_RESET= 21780

try:
    lsusb_out = Popen("lsusb -t | grep -i %s"%driver, shell=True, bufsize=64, stdin=PIPE, stdout=PIPE, close_fds=True).stdout.read().strip().split()
    #bus = lsusb_out[1]
    #device = lsusb_out[3][:-1]
    bus = "001"
    device = "005"
    f = open("/dev/bus/usb/%s/%s"%(bus, device), 'w', os.O_WRONLY)
    fcntl.ioctl(f, USBDEVFS_RESET, 0)
    print lsusb_out
except Exception, msg:
    print "failed to reset device:", msg