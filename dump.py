import os
import sys
import json

from pprint import pprint

data = {
    "name": sys.argv[1],
    "version": sys.argv[2],
    "maintainer": sys.argv[3],
    "date_release": sys.argv[4],
    "changelog": sys.argv[5],
    "status": sys.argv[6],
    "support": sys.argv[7],
    "rdp": sys.argv[8],
    "downloads":
    {
        "editions":
        {
            "vanilla": sys.argv[9] if sys.argv[9] != "null" else None,
            "gapps": sys.argv[10]
        }
    }
}

json_data = json.dumps(data, indent=4)

confirm = input(json_data + "\n\nOK? y/n\n -> ")

if confirm == "y":
    with open(f"roms/{sys.argv[11]}/{sys.argv[12]}.json", "w+") as json_file:
        json_file.write(json_data)

    with open(f"roms/{sys.argv[11]}/{sys.argv[12]}.json") as json_file:
        sys.exit(json.loads(json_file.read()))

else:
    sys.exit(f"Got {confirm}, exit")
