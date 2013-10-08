import re
import os

with open("soundfiles.txt") as f:
  for line in f:
    filename = re.match(r".*ff.(\w*).aiff", line).group(1)
    os.system("sox ./piano_notes/" + filename + ".mp3 ./piano_notes/" + filename + "_trimmed.mp3 silence 1 0.1 0.1% reverse silence 1 0.1 0.1% reverse")
