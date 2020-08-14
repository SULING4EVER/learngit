while True:
    task=input('Enter the materiel contains the QQ No. ~   ')
    import re
    find=re.compile(r'[^0-7]+\s\w+')
    print(find.findall(task))

