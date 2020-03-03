#!usr/bin/python
import psutil
import sys
from subprocess import call
for process in psutil.process_iter():
    if process.cmdline() == ['python', 'flow', '--model', 'cfg/yolo-forms.cfg', '--train', '--annotation', 'data/annotation/train', '--dataset', 'data/image/train']:
        sys.exit('Process found, exiting run check')
        
print('Process was not found, restarting')
call(['python', 'flow', '--model', 'cfg/yolo-forms.cfg', '--train', '--annotation', 'data/annotation/train', '--dataset', 'data/image/train'])
