mkdir -p src
nano src/contador.py   

import time
import sys

def main():
    for i in range(1, 11):
        print(i, flush=True)
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrumpido", file=sys.stderr)

