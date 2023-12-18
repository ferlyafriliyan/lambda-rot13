import sys, argparse, codecs, binascii, time
from os import system, remove

from sys import argv
from random import choice, shuffle

from rich import print

# Definisi warna teks ANSI
black = "\x1b[0;90m"  # Hitam
red = "\x1b[38;5;196m"  # Merah
green = "\x1b[38;5;46m"  # Hijau
yellow = "\x1b[38;5;226m"  # Kuning
blue = "\x1b[38;5;44m"  # Biru
purple = "\x1b[0;95m"  # Ungu
white = "\x1b[38;5;231m"  # Putih
orange = "\x1b[38;5;208m"  # Jingga
gray = "\x1b[38;5;248m"  # Abu-Abu

# Definisi warna teks Rich
black_rich = "[#000000]"  # Hitam
red_rich = "[#FF0000]"  # Merah
green_rich = "[#00FF00]"  # Hijau
yellow_rich = "[#FFFF00]"  # Kuning
blue_rich = "[#00C8FF]"  # Biru
purple_rich = "[#AF00FF]"  # Ungu
pink_rich = "[#FF00FF]"  # Pink
cyan_rich = "[#00FFFF]"  # Biru Muda
white_rich = "[#FFFFFF]"  # Putih
orange_rich = "[#FF8F00]"  # Jingga
gray_rich = "[#AAAAAA]"  # Abu-Abu

lambda_pyobf = f"""
{blue_rich}╦  ┌─┐┌┬┐┌┐ ┌┬┐┌─┐   ╔═╗┬ ┬┌─┐┌┐ ┌─┐
{orange_rich}║  ├─┤│││├┴┐ ││├─┤───╠═╝└┬┘│ │├┴┐├┤ 
{green_rich}╩═╝┴ ┴┴ ┴└─┘─┴┘┴ ┴   ╩   ┴ └─┘└─┘└  
"""


class DescendingName(object):
    def __init__(self, string):
        for i in string + "\n":
            sys.stdout.write(str(i))
            sys.stdout.flush()
            time.sleep(5e-05)


class LambdaEncode:
    def __init__(self):
        self.encode_template = "# Developed_By : Ferly Afriliyan\nexec((lambda __, _, : _(%s,__))(\"%s\",__import__('codecs').decode))"
        self.execute()

    def execute(self):
        system("clear")
        print(lambda_pyobf)
        try:
            print(
                f"\n{green_rich}[{orange_rich}01{green_rich}] {white_rich}Encode Lambda python3 Rot 13\n{blue_rich}[{orange_rich}00{blue_rich}] {white_rich}Keluar\n"
            )
            user_input = int(
                input(
                    f"{blue}[{gray}•{blue}] {white}Pilih : {white}"
                )
            )
            if user_input == 1:
                layers = 0
                input_file = input(
                    f"\n{green}[{gray}•{green}] {white}Input File : {white}"
                )
                total_layers = int(
                    input(
                        f"\n{green}[{gray}•{green}] {white} Berapa Lapis Compile.? Max 10\n : {white}"
                    )
                )
                if total_layers < 11:
                    output_file = input(
                        f"\n{green}[{gray}•{green}] {white}Output : {white}"
                    )
                    content = open(input_file).read()
                    encoded_content = repr(codecs.encode(content, "rot_13"))
                    file = open(output_file, "w")
                    file.write(self.encode_template % (encoded_content, "rot_13"))
                    file.close()
                    while total_layers >= layers:
                        encoded_text = open(output_file).read()
                        new_encoded = repr(codecs.encode(encoded_text, "rot_13"))
                        file = open(output_file, "w")
                        file.write(self.encode_template % (new_encoded, "rot_13"))
                        file.close()
                        print(
                            f"{green_rich}[{orange_rich}•{green_rich}] {white_rich}Compile ke {orange_rich}: {cyan_rich}\r{layers}"
                        )
                        layers += 1
                    print(f"\nFile {input_file} Berhasil Di Compile")
                    print(f"\nNama File :  {output_file}")
            elif user_input == 0:
                exit(f"Good Bye")
            else:
                exit("\nEngkau Buta Kah Anjing")
        except (KeyboardInterrupt, EOFError):
            exit("\nSelamat Tinggal")
        except ValueError:
            exit("\nHarus Angka...")
        except FileNotFoundError:
            exit(f"\nNama File Dari > [ {input_file} ] Tidak Ada")


if __name__ == "__main__":
    try:
        LambdaEncode()
    except (KeyboardInterrupt, Exception) as e:
        exit(f"[Error] {str(e).capitalize()} !")
