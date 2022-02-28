"""
avr-gcc -Os -g -o push.elf push.c -mmcu=atmega328p
simavr -g -m atmega328p water_level.elf
"""
import argparse
import subprocess
import os
import signal
import sys

from testing_sim import DefineTests

SRC_PATH = "src/"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help=".elf file", required=True)
    parser.add_argument("--commands", help="commands file", required=True)
    return parser.parse_args()


def main_run(args):
    define_tests = DefineTests()

    simavr_call = subprocess.Popen(  # Starts simavr
        f"simavr -g -m atmega328p {SRC_PATH}water_level.elf",
        shell=True,
        stdout=subprocess.PIPE,
        preexec_fn=os.setsid,
    )

    command_process = subprocess.Popen(
        f"avr-gdb --quiet --batch -x {args.commands} {args.file}",
        shell=True,
        stdout=subprocess.PIPE,
    )
    process_stdout = command_process.stdout
    return_value = define_tests.first_test(process_stdout)

    print(return_value)

    os.killpg(os.getpgid(simavr_call.pid), signal.SIGTERM)  # Kills simavr
    sys.exit(return_value) # if !=0 will fail


if __name__ == "__main__":
    args = parse_args()
    main_run(args)
