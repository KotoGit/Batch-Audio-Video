
import subprocess

class timestamp:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

testing = []
testing.append(timestamp("00:00:00", "00:00:27"))

start = input("Do you want the ouput to be audio (a) or video (v)? ")
loop = 0
cmdlist = []
while loop == 0:
    if start == 'a':
        filename = input("Print the video filename with extension: ")
        outname = input("Print the output file name with mp3 extension: ")
        program = "ffmpeg"
        for time in testing:
            start = time.begin
            fin = time.end
            arg = ["-i", filename, "-ss", start, "-to", fin, "-f", "mp3", "-ab", "320000", "-vn", outname]
            cmdlist.append(arg)
        for idx, command in enumerate(cmdlist):
            temp = subprocess.Popen([program] + cmdlist[idx], stdout=subprocess.PIPE)
            temp.wait()
        loop = 1
    elif start == 'v':
        filename = input("Print the video filename with extension: ")
        outname = input("Print the output file name with extension: ")
        program = "ffmpeg"
        for time in testing:
            start = time.begin
            fin = time.end
            arg = ["-i", filename, "-ss", start, "-strict", "-2", "-to", fin, outname]
            cmdlist.append(arg)
        for idx, command in enumerate(cmdlist):
            temp = subprocess.Popen([program] + cmdlist[idx], stdout=subprocess.PIPE)
            temp.wait()
        loop = 1
    else:
        print("Please enter either a or v: ")