import pytest

class Test_create_fixture():

    @pytest.fixture(params=[0,1])
    def my_fixture(self, request):
        "Call incident creation api."

        # POST request to API using params value in request data, get data from API      
        my_data = {'abc': 123, 'severity': 0, 'req_param': request.param}

        return my_data

    def test_incident_severity(self, my_fixture):
        assert my_fixture.get('severity') == my_fixture.get('req_param')