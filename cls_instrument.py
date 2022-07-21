import pyvisa as visa


class DeviceM:

    def __init__(self, cfg_file: str):
        with open(cfg_file) as f:
            self.instrument_idn = f.read().strip()
            print(f'self.instrument_idn: {self.instrument_idn}')

        self.instrument = str()
        self.idn = str()

    def open_instrument(self):

        rm = visa.ResourceManager("@py")
        rm.list_resources()

        print('try to open resource')

        try:
            self.instrument = rm.open_resource(self.instrument_idn)
        except visa.VisaIOError as e:
            print(e.args)
            return 'Error'

        try:
            self.idn = self.instrument.query("*IDN?")
        except visa.VisaIOError as e:
            print(e.args)
            return 'Error'

        return self.idn

    def make_meas(self):
        try:
            instr_data = self.instrument.query("MEAS?")
            return instr_data
        except visa.VisaIOError as e:
            print(e.args)
            return 'Error'
