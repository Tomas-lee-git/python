def get_country_city(city, country, population = None):
    """接受城市、国家、人口（可选），返回一个相应信息"""
    if population:
        str = f"{city.title()}, {country.title()} - population {population}"
    else:
        str = f"{city}, {country}".title()
    return str