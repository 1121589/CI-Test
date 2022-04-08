# Python Script
"""
avr-gcc -g -mmcu=atmega128 -O2 -DTEST=1 -o water_level.elf water_level.c
PYTHONPATH=/Projects/simulavr/build/pysimulavr/ python3 test_water_level.py atmega128:water_level.elf
"""
from sys import argv
from os.path import splitext, basename

import pysimulavr
from ex_utils import SimulavrAdapter


class XPin(pysimulavr.Pin):
    def __init__(self, dev, name, state=None):
        pysimulavr.Pin.__init__(self)
        self.name = name
        if state is not None:
            self.SetPin(state)
        # hold the connecting net here, it have not be destroyed, if we leave this method
        self.__net = pysimulavr.Net()
        self.__net.Add(self)
        self.__net.Add(dev.GetPin(name))

    def SetInState(self, pin):
        pysimulavr.Pin.SetInState(self, pin)
        c = pin.toChar()
        t = sim.getCurrentTime()
        if verbose:
            print("%s='%s' (t=%dns)" % (self.name, c, t))
        if not self.name in changeMap:
            changeMap[self.name] = list()
        if len(changeMap[self.name]) > 0:
            if not changeMap[self.name][-1][0] == c:
                changeMap[self.name].append((c, t))
        else:
            changeMap[self.name].append((c, t))

    def __del__(self):
        del self.__net


def ns2us(t):
    return t / 1000.0


def printPin(pid, pin):

  print("  pin%d: (char)pin='%s', (bool)pin=%d, pin.GetAnalogValue(vcc)=%0.2fV" % (pid,
                                                                                   pin.toChar(),
                                                                                   ord(pin.toBool()),
                                                                                   pin.GetAnalogValue(5.0)))

if __name__ == "__main__":
    # proc = microcontrolador, exemplo atmega128
    # elffile ficheiro .elf
    proc, elffile = argv[1].split(":")

    verbose = False
    changeMap = dict()

    sim = SimulavrAdapter() 
    sim.dmanSingleDeviceApplication()
    dev = sim.loadDevice(proc, elffile) # Probably starts simulavr?

    b0 = XPin(dev, "B0", "L") # PB0 Button input
    b1 = XPin(dev, "B1") # PB1 led output


    sim.dmanStart()
    print("simulation start: (t=%)")# % ns2us(sim.getCurrentTime()))
    sim.doRun(sim.getCurrentTime() + 7000000)
    b0.SetPin("H")
    sim.doRun(sim.getCurrentTime() + 7000000)
    print("simulation end: (t=%)")# % ns2us(sim.getCurrentTime()))

    l = list(changeMap)
    l.sort()
    printPin(1,b0)
    printPin(2,b1)
    
    sim.dmanStop()
    del dev

# EOF
