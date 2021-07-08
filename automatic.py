import os
import time
from subprocess import Popen

a = open("C:/Server/train.txt", "w")

for path, subdirs, files in os.walk(r'C:\Server\Image\train'):
    for filename in files:
        if filename.endswith(".jpg"):
            f = os.path.join(path, filename)
            a.write(str(f) + "\n")

a = open("C:/Server/test.txt", "w")

for path, subdirs, files in os.walk(r'C:\Server\Image\test'):
    for filename in files:
        if filename.endswith(".jpg"):
            f = os.path.join(path, filename)
            a.write(str(f) + "\n")

exec(open("C:/Server/convert/train_txt2xml.py").read())
exec(open("C:/Server/convert/test_txt2xml.py").read())
exec(open("C:/Server/convert/train_xml2csv.py").read())
exec(open("C:/Server/convert/test_xml2csv.py").read())
Popen(['python', 'C:/Server/convert/csv2tfrecord.py', '--csv_input=C:/server/train.csv', '--output_path=C:/server/train.record'])
Popen(['python', 'C:/Server/convert/csv2tfrecord.py', '--csv_input=C:/server/test.csv', '--output_path=C:/server/test.record'])

print('[', time.ctime(), ']', 'Successfully created the TFRecords: {}'.format("C:/Server/Train.record"))
print('[', time.ctime(), ']', 'Successfully created the TFRecords: {}'.format("C:/Server/Test.record"))
