import xml.etree.ElementTree as ET

def totalorder2Dict(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    #hitta alla element med tagen 'Totalorder'
    orders = root.findall("*/Totalorder")

    #lista med dictionaries
    orderDicts = [{}] 
    for order in orders:
        
        #  skapar en Dictionary med ID
        orderDict = {'TotalorderID': order.find('TotalorderID').text}
        # Lägger de andra elementen till dictionarin
        orderDict['TotalorderNamn'] = order.find('TotalorderNamn').text
        orderDict['TotalorderProjekt'] = order.find('TotalorderProjekt').text
        orderDict['Aktiv'] = order.find('Aktiv').text
        
        #TotalDate och TotalorderKom finns inte i alla ordrar
        if order.find('TotalDate') != None:
            orderDict['TotalDate'] = order.find('TotalDate').text
        else:
            print("TotalDate kunde inte hittas i order med id: ", orderDict['TotalorderID'])

        if order.find('TotalorderKom') != None:
            orderDict['TotalorderKom'] = order.find('TotalorderKom').text
            
        #append order till listan
        orderDicts.append(orderDict)
    return orderDicts
