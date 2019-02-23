import subprocess

class timestamp:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

class commands:
    def __init__(self, name, argu):
        self.name = name
        self.arg = argu

testing = [timestamp("00:00:00", "00:00:27")]

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
            temp = commands(program, arg)
            cmdlist.append(temp)
        for idx, command in enumerate(cmdlist):
            temp = subprocess.Popen([cmdlist[idx].name].extend(cmdlist[idx].arg), stdout=subprocess.PIPE)
            temp.wait()
        loop = 1
    elif start == 'v':
        filename = input("Print the video filename with extension: ")
        outname = input("Print the output file name with extension: ")
        program = "ffmpeg"
        for time in testing:
            start = time.begin
            fin = time.end
            arg = ["-i", filename, "-ss", start, "-to", fin, "-acodec copy", "-vcodec copy", outname]
            temp = commands(program, arg)
            cmdlist.append(temp)
        for idx, command in enumerate(cmdlist):
            temp = subprocess.Popen([cmdlist[idx].name].extend(cmdlist[idx].arg), stdout=subprocess.PIPE)
            temp.wait()
        loop = 1
    else:
        print("Please enter either a or v: ")