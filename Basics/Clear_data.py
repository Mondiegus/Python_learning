def replace_all(text, dict):
    for i, j in dict.items():
        text = text.replace(i, j)
    return text

INPUT = list()
INPUT.append('ul.Mieszka II')
INPUT.append('UL. Zygmunta III WaZY')
INPUT.append('  bolesława chrobrego ')
INPUT.append('ul Jana III SobIESkiego')
INPUT.append('\tul. Jana trzeciego Sobieskiego')
INPUT.append('ulicaJana III Sobieskiego')
INPUT.append('UL. JA\tNA 3 SOBIES  KIEGO')
INPUT.append('ULICA JANA III SOBIESKIEGO  ')
INPUT.append('ULICA. JANA III SOBIeskieGO')
INPUT.append(' Jana 3 Sobieskiego  ')
INPUT.append('Jana III Sobi\teskiego ')


# text = 'ul.Mieszka II'
# print(text.upper())
functions = ['strip()', 'upper()', 'replace("UL","")', 'title()']
replace_dictionary = {'ULICA': '', 'UL': '', '.':'', '3':'III', 'TRZECIEGO':'III', "\t":'' , '   ':'', '  ':''}

for _datas in INPUT:
    _datas = _datas.strip()
    _datas = _datas.upper()
    _datas = replace_all(_datas, old_text)
    _datas = _datas.title()
    _datas = _datas.replace('Iii','III')
    _datas = _datas.replace('Ii','II')
    _datas = _datas.strip()
    print(_datas)
