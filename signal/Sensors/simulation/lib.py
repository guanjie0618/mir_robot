import time


class device:
    def __init__(self):
        self._start = time.time()

    def __enter__(self):
        """
        # sensor pre set command
        """
        return self

    def read_power(self):
        time.sleep(0.5)
        power = -20 - (time.time() - self._start) / 50
        if power < -110:
            self._start = time.time()
        return power
        
    def close(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == '__main__':
    from Utils import timeit

    with device() as s:
        for i, _ in enumerate(range(500000)):
            with timeit(title='time= '):
                print(f'power= {s.read_power():.3f}, ', end='')
