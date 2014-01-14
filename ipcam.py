#!/usr/bin/python -tt
# This is a test module class, for learning pycurl
import pycurl

# Set you camera ip.
global ip
ip = "192.168.123.142:99"
#In case you have no ipcamera connected, comment above and un-comment below. Also the preform action of pycurl at the end.
#ip = "127.0.0.1"

class ipcam_class:
    def move(self,direction):
        if direction == "stop":
            print "Stop",
            cmd = "user=robot&pwd=robot&command=1"
        if direction == "up":
            print "UP",
            cmd = "command=0&user=robot&pwd=robot"
        if direction == "down":
            print "DOWN",
            cmd = "command=2&user=robot&pwd=robot"
        if direction == "left":
            print "left",
            cmd = "command=6&user=robot&pwd=robot"
        if direction == "right":
            print "right",
            cmd = "command=4&user=robot&pwd=robot"
        if direction == "upright":
            print "Move Diagonally Up Right" 
            cmd = "command=91&user=robot&pwd=robot"
        if direction == "home":
            cmd = "command=31&user=robot&pwd=robot"
        write(cmd)

def write(cmd):
    ipcam = "http://%s/decoder_control.cgi?%s" % (ip,cmd)
    c = pycurl.Curl()
    c.setopt(c.URL, ipcam )
    # To verify if the command line if given correctly
    #print "%s%s" % (ipcam,cmd)
    c.setopt(c.POSTFIELDS, cmd )
    #c.setopt(c.VERBOSE, True)
    c.perform()

if __name__ == '__main__':
    print "This module has n main, it is used to control ipcamera."
