import sys
import raspi_accel_lib

YANGTZE = raspi_accel_lib.ADXL345(0, 0, 0, 0x53)
INDUS = raspi_accel_lib.ADXL345(0, 0, 0, 0x1D)

YANGTZE.accel_startup(False)
INDUS.accel_startup(False)

while True:
    print('{},{},{},{}'.format(INDUS.string_output(False), INDUS.accel_magnitude(False), YANGTZE.string_output(False), YANGTZE.accel_magnitude(False)))
    sys.stdout.flush()
