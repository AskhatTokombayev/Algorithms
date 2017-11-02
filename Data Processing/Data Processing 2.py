import json
from get_country_code import get_country_code
import pygal
from pygal.style import RotateStyle

#wm = pygal.maps.world.World()
#wm.title = 'North, Central and South America'
#wm.add('North America', ['ca', 'mx', 'us'])
#wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
#wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
#'gy', 'pe', 'py', 'sr', 'uy', 've'])
#wm.add('World',['fr', 'ge', 'sp', 'gr'])

#wm.render_to_file('americas.svg')

cc_population = {}
cc_pop1={}
cc_pop2={}
cc_pop3={}



filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

    pop_map = pygal.maps.world.World()
    pop_map.title = "2010"

    for pop_dict in pop_data:
        if pop_dict["Year"] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)

            if code:
                if population < 10**7:
                    cc_pop1[code] = population
                elif population <10**9:
                    cc_pop2[code] = population
                else:
                    cc_pop3[code] = population

            else:
                print("Error: " + country_name )

    pop_map.add('Population: 0-10m', cc_pop1)
    pop_map.add('Population: 10-1b', cc_pop2)
    pop_map.add('Population: 1b+', cc_pop3)

    wm_style = RotateStyle('#336699')
    wm = pygal.Worldmap(style=wm_style)

    pop_map.render_to_file('Population.svg')
