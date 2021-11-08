# Sensors
The code for Instruments.
## How to build new code for new Instrument
### Create Package
When you add a new sensor, you need to create these file and package and put two file:
* `__init__.py`
* `lib.py`
```
.
└── sensors
    └── {model number}
        ├── init.py
        └── lib.py

```
### Context Manager
The lib.py example need to use 'context manager' to write, like this code:

```python
import pyvisa as visa
from Config.colorbar import vmin


class device:
    def __init__(self):
        self.rm = visa.ResourceManager()
        self.VISA_ADDRESS = self.rm.list_resources()[0]
        self.session = self.rm.open_resource(self.VISA_ADDRESS)

    def open(self):
        """
                # sensor pre set visa command
        """
        del self.session.timeout
        for _ in range(3):
            self.read_power()
        return self

    def read_power(self):
        try:
            """
                sensor read signal visa command
            """
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

```

