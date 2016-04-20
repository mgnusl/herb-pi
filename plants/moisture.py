#!/usr/bin/env python
""" Handles communication with MCP3008 connected to moisture sensors """
import spidev

spi = spidev.SpiDev()
try:
    spi.open(0, 1)
except Exception as e:
    print e


""" Moisture constants"""
LEVELS = {'LOW': 60, 'MODERATE': 75, 'HIGH': 90}


def read_adc(channel):
    """ Reads a 10bit value from ADC """
    if channel > 7 or channel < 0:
        raise ValueError('Channel does not exist')
    data = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((data[1] & 3) << 8) + data[2]


def get_moisture(channel, high, low):
    """ Gets calibrated moisture
    Params:ADC channel, sensor high value, sensor low value """
    if high == low:
        raise ValueError('Calibration error, maximum can not equal minimum')
    val = read_adc(channel)
    percentage = ((val - min(high, low)) * 100) / (abs(high - low))
    if low > high:
        percentage = 100 - percentage
    return percentage


def test():
    """ Returns calibrated moisture as percentage string """
    return str(get_moisture(0, 140, 1023)) + '%'
