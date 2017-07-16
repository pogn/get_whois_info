import whois
import json
import argparse
import pythonwhois
import datetime
import sys

#adding argument parser
parser = argparse.ArgumentParser(description="args parser")
parser.add_argument("-f","--file",action="store")
args = parser.parse_args()

#open file and read domains 
f=open(args.file, "r")
out=open('result.txt','w')

line=f.readline()
print "line:",line

while line:
    #find whois informatino
    domain = whois.query(line)
    parsed = domain.__dict__
    
    #change unparseble data
    if 'last_updated' in parsed: 
        parsed["last_updated"] = parsed["last_updated"].isoformat()
    if 'expiration_date' in parsed:
        parsed["expiration_date"] = parsed["expiration_date"].isoformat()
    if 'creation_date' in parsed:
        parsed["creation_date"] = parsed["creation_date"].isoformat()

    if 'name_servers' in parsed:
        parsed["name_servers"]=list(parsed["name_servers"])
    
    result=json.dumps(parsed, indent=4,sort_keys=True)
    out.write(result)
    out.write("\n")
    line=f.readline()

f.close()
out.close()
