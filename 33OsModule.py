import os
curDir =os.getcwd()
print(curDir)
os.mkdir('PMandAM')
import time
time.sleep(5)
os.rename('PMandAM','AMandPM')
time.sleep(2)
os.rmdir('AMandPM')
