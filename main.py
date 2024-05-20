from hashlib import sha1
from math import lcm
import argparse
from os.path import exists
from string import printable
from time import time

VERSION = "0.2"

ALPHA = printable[0:94]+"´¨ÁÉÍÓÚÀÈÌÒÙÄËÏÖÜÑÇáéíóúàèìòùäëïöüñç¿¡"
LENGTH = len(ALPHA)

parser = argparse.ArgumentParser(prog="CaesarOnCoke",description= f"Encrypting program using a modified Caesar cypher algorithm. v{VERSION}", epilog="by unfuz3, 2024, MIT License")

parser.add_argument("--version", action="version", version=f"CaesarOnCoke v{VERSION}")
parser.add_argument("-e","--encrypt",action="store_true",help="Select encryption mode")
parser.add_argument("-d","--decrypt",action="store_true",help="Select decryption mode")
parser.add_argument("-i","--input",help="Select input file")
parser.add_argument("-o","--output",help="Select output file")
parser.add_argument("-k","--key",help="Select the key file")

argns = parser.parse_args() # Parse data and create the args namespace

def _get_keys(key:str) -> list[int]:
    hash = sha1(key.encode()).hexdigest()

    a = int(hash[0:4],base=16)
    b = int(hash[4:8], base=16)
    c = int(hash[8:16], base=16)
    d = int(hash[16:24], base=16)
    e = int(hash[24:32], base=16)
    f = int(hash[32:40], base=16)

    c,d = [c,d] if c == min(c,d) else [d,c] # c < d
    e == e if e else e+1 # e not null

    return [a,b,c,d,e,f]

def _update_offset(x:int, keys:list[int]) -> int:
    new = (int((keys[4]/keys[5])*(x + keys[0])*keys[1]))^int(2 + keys[2]/keys[3])
    new = int(str(new)[0:20])
    return new

def _process(inp:str,keys:list[int],mode:bool):
    # Mode: true = encrypt, false = decrypt
    offset = 1
    out = ""
    modeint = 1 if mode else -1

    for s in inp:
        if s == "\n" or s == " ":
            out += s
        else:
            s = ALPHA[(ALPHA.index(s)+(offset * modeint))%(LENGTH)]
            offset = _update_offset(offset,keys)
            out += s
    return out


def main() -> None:
    ti = time()

    # Misusage check
    if not argns.encrypt and not argns.decrypt:
        print("Error: A mode must be selected")
        return
    elif argns.encrypt and argns.decrypt:
        print("Error: A single mode must be selected")
        return
    elif not argns.input:
        print("Error: Input file must be selected")
        return
    elif not exists(argns.input):
        print("Error: Input file not found")
        return
    elif not argns.output:
        print("Error: Output file must be selected")
        return
    elif not argns.key:
        print("Error: Key file must be selected")
        return
    elif not exists(argns.key):
        print("Error: Key file not found")
        return
    
    # Retrieve keys
    with open(argns.key,"r") as f:
        keys = _get_keys(f.read())

    # Retrieve input
    with open(argns.input,"r") as f:
        textinput = f.read()

    # Process the input
    textoutput = _process(textinput,keys,argns.encrypt)

    # Write output
    with open(argns.output,"w") as f:
        f.write(textoutput)

    tf = time()

    print(f"Finish! Processed in {round(tf-ti,3)} seconds")

# Execute main
if __name__=="__main__":
    main()