#This program handles reading the output of the various sensor and writing the output
#to a file

dataFile = open('data.csv', 'w')
dataFile.write("Acceleration,Pressure,Temperature,Altitude\n")
rawXAccelFile = open('~/sys/bus/iio/devices/iio\:device0/in_accel_x_raw')
accelScaleFile = open('~/sys/bus/iio/devices/iio\:device0/in_accel_scale')
rawPressureFile = open('~/sys/bus/iio/devices/iio\:device1/in_pressure_raw')
pressureScaleFile = open('~/sys/bus/iio/devices/iio\:device1/in_pressure_scale')
tempOffsetFile = open('~/sys/bus/iio/devices/iio\:device1/in_temp_offset')
rawTempFile = open('~/sys/bus/iio/devices/iio\:device1/in_temp_raw')
tempScaleFile = open('~/sys/bus/iio/devices/iio\:device1/in_temp_scale')
rawXAccel = rawAccelFile.read()
accelScale =  accelScaleFile.read()
rawPressure = rawPressureFile.read()
pressureScale = pressureScaleFile.read()
tempOffset = tempOffsetFile.read()
rawTemp = rawTempFile.read()
tempScale = tempScaleFile.read()

xAccel = rawXAccel * accelScale
pressure = rawPressure * pressureScale * 10
temperature = tempOffset + (rawTemp * tempScale)
altitude = (1 - ((pressure/1013.25) ** 0.190284) * 145366.45
dataFile.write(xAccel + "," + pressure + "," + temperature + "," + altitude + "\n")

rawXAccelFile.close()
accelScaleFile.close()
rawPressureFile.close()
pressureScaleFile.close()
tempOffsetFile.close()
rawTempFile.close()
tempScaleFile.close()
dataFile.close()