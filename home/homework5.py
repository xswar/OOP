import re

a = '7(616)230-24-32 7(713)808-98-79 ' \
    '992(891)584-10-04 992(34)787-35-87 ' \
    '9(673)605-18-53 996(010)206-44-19 ' \
    '96(96)553-02-13 996(7339)828-94-80 ' \
    '96(971)806-77-23 996(63)863-50-64'
b = re.sub('996', '+7', a)
print(b)
