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


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help=".elf file", required=True)
    parser.add_argument("--commands", help="commands file", required=True)
    return parser.parse_args()


def find(name, path):
    for root, _, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def main_run(args):
    define_tests = DefineTests()
    binary = find(args.file, "/")
    gdb = find(args.commands, "/")

    simavr_command = f"simavr -g -m atmega328p {binary}"
    simavr_call = subprocess.Popen(  # Starts simavr
        simavr_command,
        shell=True,
        stdout=subprocess.PIPE,
        preexec_fn=os.setsid,
    )
    command = f"avr-gdb --batch -x {gdb} {binary}"
    command_process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
    )
    process_stdout = command_process.stdout
    return_value = define_tests.run_tests(process_stdout)

    os.killpg(os.getpgid(simavr_call.pid), signal.SIGTERM)  # Kills simavr
    sys.exit(return_value)  # if !=0 will fail


if __name__ == "__main__":
    args = parse_args()
    main_run(args)
