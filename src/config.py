from src.data.load import json_load
import pytz

FLAVOR_WHEEL = json_load("conf/flavour_wheel.json")
DRY_LEAF_ATTRS = json_load("conf/dry_appearance.json")
WET_LEAF_ATTRS = json_load("conf/wet_appearance.json")
TEXTURE = json_load("conf/texture.json")
TYPES = json_load("conf/tea_types.json")
PEKOE_GRADES = json_load("conf/pekoe_grades.json")
COUNTRY = list(pytz.country_names.values())
COUNTRY.insert(0, "N/A")
COLOR = ["Pale Yellow / Green", "Green", "Yellow", "Orange", "Red", "Brown"]
CLARITY = ["Clear", "Dark", "Murky"]
