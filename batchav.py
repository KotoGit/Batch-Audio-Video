import sys
import subprocess

class timestamp:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

testing = []
with open(sys.argv[1], 'r') as file:
    contents = [line.rstrip('\n') for line in file]
    len_contents = len(contents)
    i = 0
    while i < len_contents:
        readtime = contents[i].split('-')
        testing.append(timestamp(readtime[0], readtime[1]))
        i += 1

filename = sys.argv[2]
cont = 0
while cont == 0:
    start = input("Please choose output format audio (a) or video (v): ")
    if start == 'a' or start == 'v':
        cont = 1
loop = 0
cmdlist = []
outname = []
while loop == 0:
    if start == 'a':
        len_test = len(testing)
        j = 0
        while j < len_test:
            temp = "out" + str(j) + ".mp3"
            outname.append(temp)
            j += 1
        program = "ffmpeg"
        for counter, time in enumerate(testing):
            start = time.begin
            fin = time.end
            arg = ["-i", filename, "-ss", start, "-to", fin, "-f", "mp3", "-ab", "320000", "-vn", outname[counter]]
            cmdlist.append(arg)
        for idx, command in enumerate(cmdlist):
            temp = subprocess.Popen([program] + cmdlist[idx], stdout=subprocess.PIPE)
            temp.wait()
        loop = 1
    elif start == 'v':
        len_test = len(testing)
        j = 0
        outext = input("Print the desired output extension: ")
        while j < len_test:
            temp = "out" + str(j) + outext
            outname.append(temp)
            j += 1
        program = "ffmpeg"
        for counter, time in enumerate(testing):
            start = time.begin
            fin = time.end
            arg = ["-i", filename, "-ss", start, "-strict", "-2", "-to", fin, outname[counter]]
            cmdlist.append(arg)
        for idx, command in enumerate(cmdlist):
            temp = subprocess.Popen([program] + cmdlist[idx], stdout=subprocess.PIPE)
            temp.wait()
        loop = 1
    else:
        print("Please enter either a or v: ")