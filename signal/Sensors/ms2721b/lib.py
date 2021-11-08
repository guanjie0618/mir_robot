import pyvisa as visa
from Config.colorbar import vmin


class device:
    def __init__(self):
        self.rm = visa.ResourceManager()
        self.VISA_ADDRESS = self.rm.list_resources()[0]
        self.session = self.rm.open_resource(self.VISA_ADDRESS)

    def open(self):
        print('Setting ms2721b...')
        self.session.write(':SENSe:BANDwidth:RESolution 100')
        self.session.write(':SENSe:FREQuency:CENTer 3500000001')
        self.session.write(':SENSe:FREQuency:SPAN 50000')
        del self.session.timeout
        for _ in range(2):
            self.read_power()
        print('OK!!')
        return self

    def read_power(self):
        try:
            self.session.write(':CALCulate:MARKer1:MAXimum')
            self.session.write(':CALCulate:MARKer1:Y?')
            result = float(self.session.read())
            return result
        except visa.Error or ValueError:
            return vmin

    def close(self):
        self.session.close()
        self.rm.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == '__main__':
    from Utils import timeit

    with device() as s:
        for i, _ in enumerate(range(500000)):
            with timeit(title='time= '):
                print(f'power= {s.read_power():.3f}, ', end='')
