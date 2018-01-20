import xml.etree.ElementTree as ET

tree = ET.parse('../data/stations-facilities.xml')
root = tree.getroot()

for child in root.findall('stations/station'):
    for child2 in child.findall('openingHours'):
        child.remove(child2)

tree.write('../data/StationFacilitiesNOH.xml')


