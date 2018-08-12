import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x = "2">
            <id>10000</id>
            <name>chuck</name>
        </user>
        <user x = "3">
            <id>10001</id>
            <name>harsh</name>
        </user>
        <user x = "4">
            <id>10002</id>
            <name>jonas</name>
        </user>
    </users>
</stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('user count :' , len(lst))
for item in lst:
    print("name : " , item.find('name').text)
    print("email id : " ,item.find('id').text )
    print("attribute:" , item.find("x"))
