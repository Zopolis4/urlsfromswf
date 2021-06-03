#!/usr/bin/env python3

import sys
import zlib
import pylzma
from urlextract import URLExtract

def main(filename):
    with open(filename, 'r+b') as fh:
        c = fh.read()
    ver = c[3]
    raw_header = c[:8]
    test = c[5:]
    header = (repr(raw_header)[2:-1])

    if header.startswith('CWS'):
        decompressed = zlib.decompress(c[8:])
    elif header.startswith('ZWS'):
        decompressed = pylzma.decompress(c[12:])
    elif header.startswith('FWS'):
        decompressed = c[8:]
    decompressed2 = str(decompressed)
    extractor = URLExtract()
    urls = extractor.find_urls(decompressed2, check_dns=True)
    print(*urls,sep='\n')


if __name__ == '__main__':
    main(sys.argv[1])