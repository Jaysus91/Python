import temperature

def get_preheat_instructions(f: float) -> str:
    """Returns instructions for preheating the oven in deg F and deg C"""
    c = str(round(temperature.convert_to_celcius(f)))
    far= str(f)
    return 'Preheat oven to ' + far + ' degrees F (~'+ c +' degrees C).'

far = float(input('Enter the baking temp in deg F: '))
print(get_preheat_instructions(far))

