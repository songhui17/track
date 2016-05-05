#!/usr/bin/env python

import re

def create():
    test_str = '''
    AvarageFPS:


    SampleID: ScriptDeltaTime
    Count: 1024
    FrameCount: 128
    TotalTime: 120
    AverageTime: 2.02
    AverageFPS: 222
    '''

    with open('temp', 'w') as f:
        f.write(test_str)


def load():
    test_str = ''
    with open('temp') as f:
       test_str = f.read()
    return test_str


def test_readline():
    with open('temp') as f:
        for l in f:
            print l

# test_readline()
test_str = load()

tag_pattern = 'SampleID: ScriptDeltaTime'
time_pattern = re.compile('^AverageTime: ([\d.]+)')

time_match = time_pattern.search(test_str)
if time_match is not None:
    print time_match.group(1)
else:
    print 'no match'
