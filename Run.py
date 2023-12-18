from run import LambdaEncode as Kontol

import os, sys

if __name__ == '__main__':
  try:
    os.system('clear')
    Kontol()
  except (KeyboardInterrupt, Exception) as e:
    exit(f"[ Error ]: {str(e).capitalize()}!")