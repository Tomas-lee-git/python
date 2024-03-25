from city_functions import get_country_city

def test_country_city_uppercase():
    str = get_country_city("Santiago", "Chile")
    assert str == "Santiago, Chile"
    
def test_country_city_lowercase():
    str = get_country_city("santiago", "chile")
    assert str == "Santiago, Chile"
    
def test_country_city_population():
    str = get_country_city("santiago", "chile", population=500000)
    assert str == "Santiago, Chile - population 500000"