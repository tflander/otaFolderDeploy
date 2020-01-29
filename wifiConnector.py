import time


class WiFiConnector:

    def __init__(self, network_station, ssid, password):
        self.network_station = network_station
        self.ssid = ssid
        self.password = password

    def connect(self):
        self.station.active(True)
        self.station.connect(self.ssid, self.password)
        while not self.station.isconnected():
            time.sleep_ms(200)

    def isconnected(self):
        return self.network_station.isconnected()
