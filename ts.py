import sys
import json
from datetime import datetime

def timestampToDate(ts): 
    timestamp = int(ts)
    tt = str(datetime.fromtimestamp(timestamp))
    sys.stdout.write(json.dumps({
        "items": [
            {
                "title": tt,
                "arg": tt,
                "subtitle": "Press Enter to paste, or Cmd+C to copy"
            }
        ]
    }))

def outputNow():
    now = datetime.now()
    res = str(now) + "   " + str(int(now.timestamp()))
    sys.stdout.write(json.dumps({
        "items": [
            {
                "title": res,
                "arg": res,
                "subtitle": "Press Enter to paste, or Cmd+C to copy"
            }
        ]
    }))


argv = sys.argv[1]
if argv.isdigit():
    timestampToDate(argv)
elif argv == "now":
    outputNow()
    
