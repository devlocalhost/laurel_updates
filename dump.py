import os
import sys
import json

from pprint import pprint

if len(sys.argv) != 15:
    sys.exit(f"Incorrect argument count, got {len(sys.argv)}, need 14")

data = {
    "name": sys.argv[1],
    "version": sys.argv[2],
    "maintainer": sys.argv[3],
    "date_release": sys.argv[4],
    "changelog": "$LS" + sys.argv[5].replace(", ", "$LE$LS"),
    "status": sys.argv[6],
    "support": sys.argv[7],
    "rdp": sys.argv[8],
    "notes": sys.argv[9] if sys.argv[9] != "none" else None,
    "banner": sys.argv[10],
    "downloads":
    {
        "editions":
        {
            "vanilla": sys.argv[11] if sys.argv[11] != "none" else None,
            "gapps": sys.argv[12]
        }
    }
}

json_data = json.dumps(data, indent=4)

confirm = input(json_data + "\n\nOK? y/n\n -> ")

if confirm in ("y", ""):
    with open(f"roms/{sys.argv[13]}/{sys.argv[14]}.json", "w+") as json_file:
        json_file.write(json_data)

    sys.exit(f"Data dumped to roms/{sys.argv[13]} as {sys.argv[14]}.json")

else:
    sys.exit(f"Got {confirm}, exit")
