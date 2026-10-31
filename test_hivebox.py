"""Test HiveBox Endpoints"""
import datetime as dt
import requests
from project import VERSION
from hivebox import print_version
from hivebox import print_temperature
def test_version():
    """Test /version Endpoint"""
    result = print_version()
    assert result == {"version":VERSION}

class MockResponse:# pylint: disable=too-few-public-methods
    """ Mock The Code """
    @staticmethod
    def json():
        """mock code"""
        return {'sensors':[{'title': 'Temperatur', 'unit': '°C', 'sensorType': 'BME280',
                 'icon': 'osem-thermometer', '_id': '5eba5fbad46fb8001b799789', 
                 'lastMeasurement': {'createdAt': str(dt.datetime.now(tz=dt.UTC)),
                                      'value': '12.15'}}]}
def test_temperature_mock(monkeypatch):
    """mock code"""
    def mock_get(*_args, **_kwargs):
        return MockResponse()
    monkeypatch.setattr(requests, "get", mock_get)
    result = print_temperature()
    assert "temperature" in result
    assert isinstance(result["temperature"],float)
