import xml.etree.ElementTree as ET


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

ET.register_namespace('elrad', "ELRAD")
ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")



tree = ET.parse('../data/StationFacilitiesNOH.xml')
treeStepFreeTube = ET.parse('../data/StepFreeTubeNNone.xml')

root = tree.getroot()
rootTreeStepFreeTube = treeStepFreeTube.getroot()

for child in root.findall('stations/station'):
    nameStation = child.find('name').text
    for child2 in rootTreeStepFreeTube.findall('{ELRAD}Station'):
        nameStationTreeStep = child2.find('{ELRAD}StationName').text
        #Matching with type transport tube
        if nameStationTreeStep == nameStation and child.attrib['type'] == 'tube':
            for child3 in child2:
                if child3.tag != '{ELRAD}StationName':
                    child.append(child3)


for childp in root.findall('stations/station/facilities'):
    for child2 in childp.findall('facility'):
        if child2.attrib['name'] == 'Toilets':
            childp.remove(child2)


indent(root)
tree.write('../data/Tflfacilities.xml', encoding="utf-8", xml_declaration=True)

