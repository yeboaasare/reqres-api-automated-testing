import pytest

'''
Fixtures are used when we want to run some code before every test method. 
So instead of repeating the same code in every test we define fixtures. 
Usually, fixtures are used to initialize database connections, pass the base , etc
A method is marked as a fixture by marking with @pytest.fixture

This fixture returns the API URL which would be used by every API test script.
'''
@pytest.fixture
def supply_url():
	url = 'https://reqres.in/api/'
	return {
		'url':url,
	}