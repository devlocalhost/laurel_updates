#!/usr/bin/env python3

import os
import sys
import pprint

import dns.resolver

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=["1.1.1.1"]

# setup database
client = MongoClient(os.getenv("DBURL"))
db = client["laurel_updates"]
collection = db["reviews"]

def get(build_name):
    return collection.find_one({"build_name": build_name}, {"_id": 0})

def put(data):
    return collection.insert_one(data)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("  usage: ./review_system ARG1 ARG2         ARG3\nexample: ./review_system put  LineageOS_15 TEXTTEXT\n         ./review_system get  LineageOS_15")

    if sys.argv[1].lower() == "get":
        response = get(sys.argv[2])

        print(f"database: {response}")

    if sys.argv[1].lower() == "put":
        data = {
            "build_name": sys.argv[2],
            "build_version": sys.argv[3],
            "build_release_date": sys.argv[4],
            "build_review": sys.argv[5],
        }

        pprint.pprint(data)

        confirm = input("approve?\n -> ")

        if confirm in ("", "y"):
            response = put(data)
            print(f"database: {response}")

        else:
            sys.exit(f"got {confirm}, denying")
