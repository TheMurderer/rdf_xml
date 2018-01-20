from rdflib import Graph, URIRef, BNode, Literal, Namespace
import xml.etree.ElementTree as ET

g = Graph()

tfl = Namespace('http://tfl.gov.uk/tfl#') # same namespace as ns1 above

g.namespace_manager.bind('tfl', tfl, replace=True)

stationsFacilities = URIRef("https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml?app_id=3a0c4a01&app_key=ea95c6674605181c5dde64c7bb5d883c")
stepFreeTube = URIRef("https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml")

tree = ET.parse('../data/Tflfacilities.xml')
root = tree.getroot()

has = {}

has['hasName'] = URIRef('http://tfl.gov.uk/tfl#name')
has['hasContactsDetails'] = URIRef('http://tfl.gov.uk/tfl#ContactDetails')
has['hasContactsDetailsAddress'] = URIRef('http://tfl.gov.uk/tfl#ContactDetailsAddress')
has['hasContactsDetailsPhone'] = URIRef('http://tfl.gov.uk/tfl#ContactDetailsPhone')
has['hasServingLine'] = URIRef('http://tfl.gov.uk/tfl#servingLine')
has['hasFacility'] = URIRef('http://tfl.gov.uk/tfl#facility')
has['hasFacilities'] = URIRef('http://tfl.gov.uk/tfl#facilities')
has['hasEntrance'] = URIRef('http://tfl.gov.uk/tfl#entrance')
has['hasEntrances'] = URIRef('http://tfl.gov.uk/tfl#entrances')
has['hasEntranceToBookingHall'] = URIRef('http://tfl.gov.uk/tfl#entranceToBookingHall')
has['hasBookintHallToPlatform'] = URIRef('http://tfl.gov.uk/tfl#BookintHallToPlatform')
has['hasPath'] = URIRef('http://tfl.gov.uk/tfl#path')
has['hasHeading'] = URIRef('http://tfl.gov.uk/tfl#heading')
has['hasPathDescription'] = URIRef('http://tfl.gov.uk/tfl#pathDescription')
has['hasPlatformToTrain'] = URIRef('http://tfl.gov.uk/tfl#platformToTrain')
has['hasTrainName'] = URIRef('http://tfl.gov.uk/tfl#trainName')
has['hasPlatformToTrainSteps'] = URIRef('http://tfl.gov.uk/tfl#platformToTrainSteps')
has['hasPointName'] = URIRef('http://tfl.gov.uk/tfl#pointName')
has['hasPlacemark'] = URIRef('http://tfl.gov.uk/tfl#Placemark')
has['hasDescription'] = URIRef('http://tfl.gov.uk/tfl#Description')
has['hasPoint'] = URIRef('http://tfl.gov.uk/tfl#Point')
has['hasCoordinates'] = URIRef('http://tfl.gov.uk/tfl#Coordinates')
has['hasStyleUrl'] = URIRef('http://tfl.gov.uk/tfl#styleUrl')
has['hasPublicToilet'] = URIRef('http://tfl.gov.uk/tfl#PublicToilet')
has['hasLocation'] = URIRef('http://tfl.gov.uk/tfl#Location')
has['hasPaymentRequired'] = URIRef('http://tfl.gov.uk/tfl#PaymentRequired')
has['hasAccessibility'] = URIRef('http://tfl.gov.uk/tfl#Accessibility')
has['hasAdditionalAccessibilityInformation'] = URIRef('http://tfl.gov.uk/tfl#AdditionalAccessibilityInformation')
has['hasBlueBadgeCarParkSpaces'] = URIRef('http://tfl.gov.uk/tfl#BlueBadgeCarParkSpaces')
has['hasTaxiRanksOutsideStation'] = URIRef('http://tfl.gov.uk/tfl#TaxiRanksOutsideStation')
has['hasLift'] = URIRef('http://tfl.gov.uk/tfl#Lift')
has['hasAccessViaLift'] = URIRef('http://tfl.gov.uk/tfl#AccessViaLift')
has['hasLimitedCapacityLift'] = URIRef('http://tfl.gov.uk/tfl#LimitedCapacityLift')
has['hasToilets'] = URIRef('http://tfl.gov.uk/tfl#Toilets')
has['hasAccessibleToilet'] = URIRef('http://tfl.gov.uk/tfl#AccessibleToilet')
has['hasAccessibleToiletNote'] = URIRef('http://tfl.gov.uk/tfl#AccessibleToiletNote')
has['hasSpecificEntrance'] = URIRef('http://tfl.gov.uk/tfl#SpecificEntrance')
has['hasSpecificEntranceRequired'] = URIRef('http://tfl.gov.uk/tfl#SpecificEntranceRequired')
has['hasSpecificEntranceInstructions'] = URIRef('http://tfl.gov.uk/tfl#SpecificEntranceInstructions')
has['hasAccessibilityType'] = URIRef('http://tfl.gov.uk/tfl#AccessibilityType')
has['hasAirportInterchange'] = URIRef('http://tfl.gov.uk/tfl#AirportInterchange')
has['hasPierInterchange'] = URIRef('http://tfl.gov.uk/tfl#PierInterchange')
has['hasMainBusInterchange'] = URIRef('http://tfl.gov.uk/tfl#MainBusInterchange')
has['hasEmiratesAirLineInterchange'] = URIRef('http://tfl.gov.uk/tfl#EmiratesAirLineInterchange')
has['hasTramlinkInterchange'] = URIRef('http://tfl.gov.uk/tfl#TramlinkInterchange')
has['hasNationalRailInterchange'] = URIRef('http://tfl.gov.uk/tfl#NationalRailInterchange')
has['hasAccessibleInterchanges'] = URIRef('http://tfl.gov.uk/tfl#AccessibleInterchanges')
has['hasLineName'] = URIRef('http://tfl.gov.uk/tfl#LineName')
has['hasPlatform'] = URIRef('http://tfl.gov.uk/tfl#Platform')
has['hasDirectionTowards'] = URIRef('http://tfl.gov.uk/tfl#DirectionTowards')
has['hasStepMin'] = URIRef('http://tfl.gov.uk/tfl#StepMin')
has['hasStepMax'] = URIRef('http://tfl.gov.uk/tfl#StepMax')
has['hasGapMin'] = URIRef('http://tfl.gov.uk/tfl#GapMin')
has['hasGapMax'] = URIRef('http://tfl.gov.uk/tfl#GapMax')
has['hasLevelAccessByManualRamp'] = URIRef('http://tfl.gov.uk/tfl#LevelAccessByManualRamp')
has['hasLocationOfLevelAccess'] = URIRef('http://tfl.gov.uk/tfl#LocationOfLevelAccess')
has['hasLine'] = URIRef('http://tfl.gov.uk/tfl#line')
has['hasLines'] = URIRef('http://tfl.gov.uk/tfl#lines')
has['hasNaptan'] = URIRef('http://tfl.gov.uk/tfl#naptan')
has['hasDescription'] = URIRef('http://tfl.gov.uk/tfl#Description')
has['hasNaptanId'] = URIRef('http://tfl.gov.uk/tfl#NaptanID')
has['hasId'] = URIRef('http://tfl.gov.uk/tfl#id')
has['hasType'] = URIRef('http://tfl.gov.uk/tfl#type')
has['hasTicketHalls'] = URIRef('http://tfl.gov.uk/tfl#TicketHalls')
has['hasLifts'] = URIRef('http://tfl.gov.uk/tfl#Lifts')
has['hasEscalators'] = URIRef('http://tfl.gov.uk/tfl#Escalators')
has['hasGates'] = URIRef('http://tfl.gov.uk/tfl#Gates')
has['hasPhotoBooths'] = URIRef('http://tfl.gov.uk/tfl#PhotoBooths')
has['hasCashMachines'] = URIRef('http://tfl.gov.uk/tfl#CashMachines')
has['hasPayphones'] = URIRef('http://tfl.gov.uk/tfl#Payphones')
has['hasCarPark'] = URIRef('http://tfl.gov.uk/tfl#CarPark')
has['hasVendingMachines'] = URIRef('http://tfl.gov.uk/tfl#VendingMachines')
has['hasHelpPoints'] = URIRef('http://tfl.gov.uk/tfl#HelpPoints')
has['hasBridge'] = URIRef('http://tfl.gov.uk/tfl#Bridge')
has['hasWaitingRoom'] = URIRef('http://tfl.gov.uk/tfl#WaitingRoom')
has['hasOtherFacilities'] = URIRef('http://tfl.gov.uk/tfl#OtherFacilities')
has['hasStation'] = URIRef('http://tfl.gov.uk/tfl#Station')
has['hasZones'] = URIRef('http://tfl.gov.uk/tfl#Zones')
has['hasZone'] = URIRef('http://tfl.gov.uk/tfl#Zone')
has['hasNaptans'] = URIRef('http://tfl.gov.uk/tfl#Naftans')
has['hasDirection'] = URIRef('http://tfl.gov.uk/tfl#Direction')

stations = BNode()


for child in root.findall('stations/station'):

    name = child.find('name')

    address = child.find('contactDetails/address')
    phone = child.find('contactDetails/phone')
    servingLine = child.find('servingLines/servingLine')
    station = BNode()
    g.add((stations, has['hasStation'],station))
    g.add((station, has['hasId'], Literal(child.attrib['id'])))
    g.add((station, has['hasType'], Literal(child.attrib['type'])))
    g.add((station, has['hasName'], Literal(name.text)))

    contactDetails = BNode()
    g.add((station, has['hasContactsDetails'], contactDetails))
    g.add((contactDetails,has['hasContactsDetailsAddress'], Literal(address.text) ))
    g.add((contactDetails, has['hasContactsDetailsPhone'], Literal(phone.text)))
    for servingLineXMLNode in child.findall('servingLines'):
        g.add((station,has['hasServingLine'], Literal(servingLineXMLNode.text)))

    facilities = BNode()
    g.add((station, has['hasFacilities'], facilities))
    for facilityXMLNode in child.findall('facilities/facility'):
        facility = BNode()
        g.add((facilities, has['hasFacility'], facility))
        if facilityXMLNode.attrib['name'] == 'Tickets Halls':
            g.add((facility, has['hasTicketHalls'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Lifts':
            g.add((facility, has['hasLift'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Escalators':
            g.add((facility, has['hasEscalators'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Gates':
            g.add((facility, has['hasGates'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Photo Booths':
            g.add((facility, has['hasPhotoBooths'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Cash Machines':
            g.add((facility, has['hasCashMachines'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Payphones':
            g.add((facility, has['hasPayphones'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Car park':
            g.add((facility, has['hasCarPark'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Vending Machines':
            g.add((facility, has['hasVendingMachines'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Help Points':
            g.add((facility, has['hasHelpPoints'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Bridge':
            g.add((facility, has['hasBridge'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Waiting Room':
            g.add((facility, has['hasWaitingRoom'], Literal(facilityXMLNode.text)))
        elif facilityXMLNode.attrib['name'] == 'Other Facilities':
            g.add((facility, has['hasOtherFacilities'], Literal(facilityXMLNode.text)))

    zonesXMLnode = child.find('zones')

    if zonesXMLnode is not None:
        zones = BNode()
        g.add((station,has['hasZones'],zones))
        for zoneXMLNode in zonesXMLnode.findall('zone'):
            g.add((zones, has['hasZone'], Literal(zoneXMLNode.text)))


    if child.findall('entrances') is not None:
        entrances = BNode()
        g.add((station, has['hasEntrances'], entrances))

        for entranceXMLNode in child.findall('entrances/entrance'):
            entranceToBookingHall = entranceXMLNode.find('entranceToBookingHall')
            entrance = BNode()
            g.add((entrances, has['hasEntrance'], entrance ))
            g.add((entrance, has['hasName'], Literal(child.find('name').text)))
            g.add((entrance,has['hasEntranceToBookingHall'],  Literal(entranceToBookingHall.text)))

            if entranceXMLNode.findall('bookingHallToPlatform') :
                for bookingHallToPlatformXMLNode in entranceXMLNode.findall('bookingHallToPlatform'):
                    bookingHallToPlatform = BNode()
                    g.add((entrance, has['hasBookintHallToPlatform'], bookingHallToPlatform))
                    for pathXMLNode in bookingHallToPlatformXMLNode.findall('path'):
                        heading = pathXMLNode.find('heading')
                        pathDescription = pathXMLNode.find('pathDescription')
                        pathBookingHallToPlatform = BNode()
                        g.add((bookingHallToPlatform, has['hasPath'], pathBookingHallToPlatform))
                        g.add((pathBookingHallToPlatform,has['hasHeading'],  Literal(heading.text)))
                        g.add((pathBookingHallToPlatform, has['hasPathDescription'], Literal(pathDescription.text)))
                    if bookingHallToPlatformXMLNode.find('pointName') is not None:
                        for pointNameXMLNode in bookingHallToPlatformXMLNode.findall('pointName'):
                            if pointNameXMLNode is not None and pointNameXMLNode.text != '' :
                                g.add((bookingHallToPlatform,has['hasPointName'],Literal(pointNameXMLNode.text) ))
                    if bookingHallToPlatformXMLNode.find('pathDescription') is not None:
                        for pathDescriptionXMLNode in bookingHallToPlatformXMLNode.findall('pathDescription'):
                            g.add((bookingHallToPlatform,has['hasPathDescription'],Literal(pathDescriptionXMLNode.text) ))

            if entranceXMLNode.findall('platformToTrain') is not None:
                for  platformToTrainXMLNode in entranceXMLNode.findall('platformToTrain'):
                    platformToTrain = BNode()

                    trainName = platformToTrainXMLNode.find('trainName')
                    platformToTrainSteps = platformToTrainXMLNode.find('platformToTrainSteps')
                    g.add((entrance,has['hasPlatformToTrain'],platformToTrain ))
                    g.add((platformToTrain, has['hasTrainName'], Literal(trainName.text)))
                    g.add((platformToTrain, has['hasPlatformToTrainSteps'], Literal(platformToTrainSteps.text)))

    for placemarkXMLNode in child.findall('Placemark'):
        placemark = BNode()
        g.add((station, has['hasPlacemark'], placemark ))
        g.add((placemark, has['hasName'],  Literal(placemarkXMLNode.find('name').text) ))
        g.add((placemark, has['hasDescription'], Literal(placemarkXMLNode.find('description').text)))
        point = BNode()
        g.add((placemark, has['hasPoint'], point))
        g.add((point, has['hasCoordinates'] , Literal(placemarkXMLNode.find('Point/coordinates').text) ))
        g.add((placemark,  has['hasStyleUrl'], Literal(placemarkXMLNode.find('styleUrl').text) ))

    for publicToiletXMLNode in child.findall('{ELRAD}PublicToilet'):
        location = publicToiletXMLNode.find('{ELRAD}Location')
        publicToilet = BNode()
        g.add((station, has['hasPublicToilet'], publicToilet))
        if location is not None and location.text:
            g.add((publicToilet, has['hasLocation'], Literal(location.text)))
        paymentRequired = publicToiletXMLNode.find('{ELRAD}PaymentRequired')
        g.add((publicToilet, has['hasPaymentRequired'], Literal(paymentRequired.text)))

    for accessibilityXMLNode in child.findall('{ELRAD}Accessibility'):

        additionalAccessibilityInformation = accessibilityXMLNode.find('{ELRAD}AdditionalAccessibilityInformation')
        blueBadge = accessibilityXMLNode.find('{ELRAD}BlueBadgeCarParkSpaces')
        taxiRanksOutsideStation = accessibilityXMLNode.find('{ELRAD}TaxiRanksOutsideStation')
        accessViaLift = accessibilityXMLNode.find('{ELRAD}Lifts/{ELRAD}AccessViaLift')
        limitedCapacityLift = accessibilityXMLNode.find('{ELRAD}Lifts/{ELRAD}LimitedCapacityLift')
        accesibleToilets = accessibilityXMLNode.find('{ELRAD}Toilets/{ELRAD}AccessibleToilet')
        accesibleToiletsNote = accessibilityXMLNode.find('{ELRAD}Toilets/{ELRAD}AccessibleToiletNote')
        specificEntranceRequired = accessibilityXMLNode.find('{ELRAD}SpecificEntrance/{ELRAD}SpecificEntranceRequired')
        specificEntranceInstructions = accessibilityXMLNode.find('{ELRAD}SpecificEntrance/{ELRAD}SpecificEntranceInstructions')
        accessibilityType = accessibilityXMLNode.find('{ELRAD}AccessibilityType')

        accessibility = BNode()
        g.add((station, has['hasAccessibility'], accessibility))
        if additionalAccessibilityInformation is not None and additionalAccessibilityInformation.text != '':
            g.add((accessibility, has['hasAdditionalAccessibilityInformation'], Literal(additionalAccessibilityInformation.text)))
        if blueBadge is not None and blueBadge.text != '':
            g.add((accessibility, has['hasBlueBadgeCarParkSpaces'],Literal(blueBadge.text)))
        if taxiRanksOutsideStation is not None and taxiRanksOutsideStation.text != '':
            g.add((accessibility, has['hasTaxiRanksOutsideStation'],Literal(taxiRanksOutsideStation.text)  ))
        if accessViaLift is not None and accessViaLift.text != '':
            lift = BNode()
            g.add((accessibility, has['hasLift'], lift))
            g.add((lift, has['hasAccessViaLift'],Literal(accessViaLift.text) ))
            g.add((lift, has['hasLimitedCapacityLift'], Literal(limitedCapacityLift.text)))
        if accesibleToilets is not None and accesibleToilets.text != '':
            toilets = BNode()
            g.add ((accessibility, has['hasToilets'], toilets ))
            g.add((toilets, has['hasAccessibleToilet'], Literal(accesibleToilets.text) ))
            if accesibleToiletsNote.text != '':
                g.add((toilets, has['hasAccessibleToiletNote'], Literal(accesibleToilets.text)))
        specificEntrance = BNode()
        g.add((accessibility, has['hasSpecificEntrance'], specificEntrance))
        g.add((specificEntrance, has['hasSpecificEntranceRequired'], Literal(specificEntranceRequired.text)))
        if specificEntranceInstructions is not None and specificEntranceInstructions.text != '':
            g.add((specificEntrance, has['hasSpecificEntranceInstructions'], Literal(specificEntranceInstructions.text)))
        if accessibilityType is not None:
            g.add((accessibility, has['hasAccessibilityType'], Literal(accessibilityType.text)))

    for accessibleInterchangesXMLNode in child.findall('{ELRAD}AccessibleInterchanges'):
        airportInterchange = accessibleInterchangesXMLNode.find('{ELRAD}AirportInterchange')
        pierInterchange = accessibleInterchangesXMLNode.find('{ELRAD}PierInterchange')
        mainBusInterchange = accessibleInterchangesXMLNode.find('{ELRAD}MainBusInterchange')
        emiratesAirLineInterchange = accessibleInterchangesXMLNode.find('{ELRAD}EmiratesAirLineInterchange')
        tramlinkInterchange = accessibleInterchangesXMLNode.find('{ELRAD}TramlinkInterchange')
        nationalRailInterchange = accessibleInterchangesXMLNode.find('{ELRAD}NationalRailInterchange')

        accessibleInterchanges = BNode()
        g.add((station, has['hasAccessibleInterchanges'], accessibleInterchanges))
        g.add((accessibleInterchanges, has['hasAirportInterchange'], Literal(airportInterchange.text)))
        g.add((accessibleInterchanges, has['hasPierInterchange'], Literal(pierInterchange.text)))
        g.add((accessibleInterchanges, has['hasMainBusInterchange'], Literal(mainBusInterchange.text) ))
        g.add((accessibleInterchanges, has['hasEmiratesAirLineInterchange'], Literal(emiratesAirLineInterchange.text)))
        g.add((accessibleInterchanges, has['hasTramlinkInterchange'], Literal(tramlinkInterchange.text)))
        g.add((accessibleInterchanges, has['hasNationalRailInterchange'], Literal(nationalRailInterchange.text)))

    if child.findall('{ELRAD}Lines') is not None:
        lines = BNode()
        g.add((station, has['hasLines'], lines ))
        for lineXMLNode in child.findall('{ELRAD}Lines/{ELRAD}Line'):
            linename = lineXMLNode.find('{ELRAD}LineName')
            platform = lineXMLNode.find('{ELRAD}Platform')
            direction = lineXMLNode.find('{ELRAD}Direction')
            directionTowards = lineXMLNode.find('{ELRAD}DirectionTowards')
            stepMin = lineXMLNode.find('{ELRAD}StepMin')
            stepMax = lineXMLNode.find('{ELRAD}StepMax')
            gapMin = lineXMLNode.find('{ELRAD}GapMin')
            gapMax = lineXMLNode.find('{ELRAD}GapMax')
            levelAccessByManualRamp = lineXMLNode.find('{ELRAD}LevelAccessByManualRamp')
            locationOfLevelAccess = lineXMLNode.find('{ELRAD}LocationOfLevelAccess')

            line = BNode()
            g.add((lines, has['hasLine'], line))
            g.add((line, has['hasLineName'], Literal(linename.text)))
            g.add((line, has['hasPlatform'], Literal(platform.text)))
            g.add((line, has['hasDirection'], Literal(direction.text)))
            g.add((line, has['hasDirectionTowards'], Literal(directionTowards.text)))
            g.add((line, has['hasStepMin'], Literal(stepMin.text)))
            g.add((line, has['hasStepMax'], Literal(stepMax.text)))
            g.add((line, has['hasGapMin'], Literal(gapMin.text)))
            g.add((line, has['hasGapMax'], Literal(gapMax.text)))
            if levelAccessByManualRamp is not None and levelAccessByManualRamp.text != '':
                g.add((line, has['hasLevelAccessByManualRamp'], Literal(levelAccessByManualRamp.text)))
            if locationOfLevelAccess is not None and locationOfLevelAccess.text != '':
                g.add((line, has['hasLocationOfLevelAccess'], Literal(locationOfLevelAccess.text)))

    if child.findall('{ELRAD}Naptans') is not None:
        naptans = BNode()
        g.add((station, has['hasNaptans'], naptans ))
        for naptanXMLNode in child.findall('{ELRAD}Naptans/{ELRAD}Naptan'):
            description = naptanXMLNode.find('{ELRAD}Description')
            naptanId = naptanXMLNode.find('{ELRAD}NaptanID')
            naptan = BNode()
            g.add((naptans, has['hasNaptan'], naptan))
            g.add((naptan,  has['hasDescription'], Literal(description.text)))
            g.add((naptan,  has['hasNaptanId'], Literal(naptanId.text)))



g.serialize(destination="../data/TflfacilitiesRDF.xml", format="xml")

