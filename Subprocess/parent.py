from subprocess import Popen, PIPE
from time import sleep
from nbstreamreader import NonBlockingStreamReader as NBSR

# run the shell as a subprocess:
p = Popen(['python', 'child_2.py'],
        stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = False)
# wrap p.stdout with a NonBlockingStreamReader object:
nbsr = NBSR(p.stdout)
# issue command:
p.stdin.write('sl\n')
# get the output
while True:
    output = nbsr.readline(10)
    # 0.1 secs to let the shell output the result
    if not output:
        print '[No more data]'
        p.stdin.write('ls\n')
#        break
    else:
    	print "From Subprocess: ",output
print "Waited too long for data, we are out now"
