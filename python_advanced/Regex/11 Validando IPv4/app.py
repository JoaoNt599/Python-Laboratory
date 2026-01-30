import re


# 0.0.0.0 255.255.255.255


ip_reg_exp = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5] |             # 250-255
            2[0-4][0-9] |       # 200-249
            1[0-9]{2} |         # 100-199
            [1-9][0-9] |         # 10-99
            [0-9]               # 0-9
        )
        \.?
    ){4}
    \b
    $
''', flags=re.X)            # X = VERBOSE

     
for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))