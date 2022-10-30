import io
import os
import re
from mutagen.mp3 import MP3
import mutagen

text = """
[General]
AudioFilename: hello110.mp3
AudioLeadIn: 1500
PreviewTime: 49342
Countdown: 0
SampleSet: Soft
StackLeniency: 0.7
Mode: 0
LetterboxInBreaks: 0
WidescreenStoryboard: 1
"""

rootdir = r"D:\Program Files\osu!\Songs"
regex = "AudioFilename:\s*(.*)"

lengths = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if os.path.join(subdir, file).endswith('.osu'):
            fullpath = os.path.join(subdir, file)
            f = io.open(fullpath, mode="r", encoding="utf-8")
            text = f.read()

            matches = re.finditer(regex, text)

            for matchNum, match in enumerate(matches, start=1):
                
                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1
                    if match.group(groupNum).lower().endswith('.mp3'):
                        audiopath = os.path.dirname(fullpath) + "\\" + match.group(groupNum)
                        try:
                            audio = MP3(audiopath)
                            lengths.append(audio.info.length)
                            print(f"Processed audio file: '{audiopath}'")
                        except mutagen.MutagenError as e:
                            print(f"ERROR : Could not find file '{audiopath}' - This probably means the osu file is incorrect")
                            print(e)
                    else:
                        print(f"Skipped invalid file: '{match.group(groupNum)}'")


print(f"Processed {len(lengths)} songs")
seconds = sum(lengths)
print(f"Total length of all songs is {seconds}")
m, s = divmod(int(seconds), 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print(f'Which is equal to {d:d}d {h:d}h {m:02d}m {s:02d}s')