from test_lib import *
def round_down_to_nearest_15(value):
    return (value // 15) * 15

def uuren(minuten):
    if minuten >= 60:
        hours = minuten // 60
        minutes = minuten % 60
       
        rounded_minutes = round_down_to_nearest_15(minutes)
        return f'{hours:02}:{rounded_minutes:02}'
    else:
       
        rounded_minutes = round_down_to_nearest_15(minuten)
        return f'00:{rounded_minutes:02}'


expected = '08:15'
antwoord = uuren(498)
test('test1: ',expected,antwoord)

expected = '10:00'
antwoord = uuren(611)
test('test1: ',expected,antwoord)

expected = '20:45'
antwoord = uuren(1249)
test('test1: ',expected,antwoord)

expected = '00:30'
antwoord = uuren(39)
test('test1: ',expected,antwoord)
report()