import sys
sys.stderr.write('This is stderr text')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')
print(sys.argv)