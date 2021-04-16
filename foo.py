import json
import time
from datetime import datetime
class demconstruct():
    def __init__(self, define, json, ascii_cache):
        self.json = json
        self.ascii_cache = ascii_cache
    def denote(self):
        efx = (self.json, self.ascii_cache)
        return efx

def run():
    foo = []
    amt = int(input("foo in amt: "))
    for x in range(amt):
        text = input("foo in: ")
        foo.append(text.lower())
    data = {"bar":foo}
    define = json.dumps(data)
    et = demconstruct(define, json=[], ascii_cache=[ord(char) for char in define]) 
    string_literal = u"define"
    data["bar"].append([(string_literal)])
    eft = "*".join(f"{data}")
    with open("printer-output.txt", "a") as f:
        print("INSIDE")
        f.write("\n")
        f.write(f"*/ AUTO GENERATED PRINTER OUTPUT - {datetime.today().strftime('%Y-%m-%d')} *\\")
        f.write("\n")
        f.write("\n")
        f.write(f"Denoted ascii chars from foo define data of type {type(et)}: {et.denote()}")
        f.write("\n")
        f.write(f"Translation of define : {[chr(ord(char)) for char in define]}")
        f.close()
    print("foo process ended..")
    time.sleep(3)
