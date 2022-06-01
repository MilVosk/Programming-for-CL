def find_happiest(filename):
    dict_asia = {}
    dict_europe = {}
    dict_africa = {}
    dict_oceania = {}
    dict_latinAmerica = {}
    dict_northAmerica = {}
    dict_happiest = {}
    dict = {}
    asia = {}
    europe = {}
    africa = {}
    latinAmerica = {}
    oceania = {}
    northAmerica = {}
    with open(filename, "r") as file:
        for line in file:
            lines = line.split(',')
            no_newline = lines[3].strip('\n')
            dict[lines[2]] = {}
            dict[lines[2]][no_newline] = lines[1]
        for key, value in dict.items():
            if "Asia" in value or "asia" in value:
                dict_asia[key] = {}
                dict_asia[key] = value
                asia = dict_asia[max(dict_asia)]
            elif "Europe" in value or "europe" in value:
                dict_europe[key] = {}
                dict_europe[key] = value
                europe = dict_europe[max(dict_europe)]
            elif "Africa" in value or "africa" in value:
                dict_africa[key] = {}
                dict_africa[key] = value
                africa = dict_africa[max(dict_africa)]
            elif "Latin America and Caribbeans" in value:
                dict_latinAmerica[key] = {}
                dict_latinAmerica[key] = value
                latinAmerica = dict_latinAmerica[max(dict_latinAmerica)]
            elif "latin america and caribbeans" in value:
                dict_latinAmerica[key] = {}
                dict_latinAmerica[key] = value
                latinAmerica = dict_latinAmerica[max(dict_latinAmerica)]
            elif "Oceania" in value or "oceania" in value:
                dict_oceania[key] = {}
                dict_oceania[key] = value
                oceania = dict_oceania[max(dict_oceania)]
            elif "North America" in value or "north america" in value:
                dict_northAmerica[key] = {}
                dict_northAmerica[key] = value
                northAmerica = dict_northAmerica[max(dict_northAmerica)]
        for x in (asia, europe, africa, latinAmerica, oceania, northAmerica):
            dict_happiest.update(x)
        return dict_happiest
