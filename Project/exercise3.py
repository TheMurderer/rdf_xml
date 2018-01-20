import xml.etree.ElementTree as ET

ET.register_namespace('', "ELRAD")
ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
tree = ET.parse('../data/step-free-tube-guide.xml')
root = tree.getroot()

for child in root.findall('{ELRAD}Station'):
    for child2 in child.findall('{ELRAD}Accessibility'):
        for child3 in child2.findall('{ELRAD}AccessibilityType'):
            if child3.text == 'None':
                child2.remove(child3)

tree.write('../data/StepFreeTubeNNone.xml')


