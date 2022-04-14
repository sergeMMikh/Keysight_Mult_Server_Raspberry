import pyvisa as visa
import time
import os


class DeviceM:

    def __init__(self, cfg_file: str):
        with open(cfg_file) as f:
            self.instrument_idn = f.read().strip()

        rm = visa.ResourceManager("@py")
        rm.list_resources()
        self.instrument = rm.open_resource(self.instrument_idn)

        try:
            self.idn = self.instrument.query("*IDN?")

            print(self.idn)

        except:
            print('Error open_resource!')