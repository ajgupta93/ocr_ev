import subprocess
x = subprocess.Popen(['python','OCR segmentation 2.py'], stdout=subprocess.PIPE).stdout.read()
print x
x=x.split(' ')
a = x[-1]
x[-1] = a[:-1]
for i in range(len(x)):
    x[i] = float(x[i])
print x
