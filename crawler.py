import urllib
from urllib2 import urlopen
import re

# Sources: https://www.chessgames.com

PLAYER = 'alexander-baburin'
COLLECTION = 'alekhine-defense'
URL_COLLECTION = 'https://www.chessgames.com/perl/chess.pl?page=4&pid=14466&playercomp=black&eco=B02-B05&title=Alexander%20Baburin%20playing%20the%20Alekhine%27s%20Defense%20as%20Black'

# --------------------------------------------------------

filename = PLAYER + '__' + COLLECTION

regex = r"gid=([0-9]*)\""
webUrl  = urllib.urlopen(URL_COLLECTION)
# webUrl.getcode()
test_str  = webUrl.read()
matches = re.finditer(regex, test_str, re.MULTILINE)

ids = []

for matchNum, match in enumerate(matches, start=1):
  # matchNum
  # match.start(),
  # match.end(),
  # match.group()
    
  for groupNum in range(0, len(match.groups())):
    groupNum = groupNum + 1
    # groupNum
    # match.start(groupNum)
    # match.group(groupNum)
    ids.append(match.group(groupNum))


fullPathFileName = "./output/{id}.pgn".format(id=filename) 

for id in ids:
  pgnWebUrl  = 'https://www.chessgames.com/pgn/?gid={id}'.format(id=id)
  response = urlopen(pgnWebUrl)
  data = response.read()
  file_ = open(fullPathFileName, 'a+')
  file_.write(data)
  file_.write("\n\n\n")
  file_.close()
