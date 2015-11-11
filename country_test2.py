# import lxml library
from lxml import etree as ElementTree
# genereer data voor input later
file = open("country_data.xml")
data = file.read()
tree = ElementTree.fromstring(data)
rank = tree.xpath('.//rank')[0]


def finding_parent(input):
    # maak een lege lijst
    output = []
    # zolang de input een parent heeft, get parent
    while input != None:
        input = input.getparent()
        # voeg steeds een element toe aan de lijst 'output' tot en met de root (bij root, parent=None)
        if input != None:
            output.append(input)
    print(output)


finding_parent(rank)






