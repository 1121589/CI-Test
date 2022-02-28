"""
avr-gcc -Os -g -o push.elf push.c -mmcu=atmega328p
simavr -g -m atmega328p water_level.elf
"""
import argparse
import subprocess
import os
import signal

from testing_sim import DefineTests


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help=".elf file", required=True)
    parser.add_argument("--commands", help="commands file", required=True)
    return parser.parse_args()

def main_run(args):
    define_tests = DefineTests()
    simavr_call = subprocess.Popen("simavr -g -m atmega328p water_level.elf", shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)

    command_process = subprocess.Popen(f"avr-gdb --quiet --batch -x {args.commands} {args.file}", shell=True, stdout=subprocess.PIPE)
    process_stdout = command_process.stdout
    define_tests.first_test(process_stdout)
        
    os.killpg(os.getpgid(simavr_call.pid), signal.SIGTERM)


if __name__ == "__main__":
    args = parse_args()
    main_run(args)
