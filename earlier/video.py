#!/usr/bin/python

def func():
	frameSize = 200 / 30.0
	duration = 180
	fileSize = 1024  # MB
	averageSize = fileSize / duration

	print 'frameSize:', frameSize
	print 'averageSize:', averageSize


func()
