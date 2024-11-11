from test_lib import test, report
NITRATE_PERC = 75
CHARCOAL_PERC = 15
SULFUR_PERC = 10
 

nitrate = 613.7
charcoal = 117.1	
sulfur = 66.7	
 
def powdermix(NITRATE_PERC, CHARCOAL_PERC, SULFUR_PERC, nitrate, charcoal, sulfur):
  
    p1 = nitrate / NITRATE_PERC
    c1 = CHARCOAL_PERC * p1
    s1 = SULFUR_PERC * p1

    p2 = charcoal / CHARCOAL_PERC
    n2 = NITRATE_PERC * p2
    s2 = SULFUR_PERC * p2

    p3 = sulfur / SULFUR_PERC
    n3 = NITRATE_PERC * p3
    c3 = CHARCOAL_PERC * p3

  
    if charcoal >= c1 and sulfur >= s1:
        return round(nitrate, 2), round(c1, 2), round(s1, 2)
    elif nitrate >= n2 and sulfur >= s2:
        return round(n2, 2), round(charcoal, 2), round(s2, 2)
    else:
        return round(n3, 2), round(c3, 2), round(sulfur, 2)

mix = powdermix(NITRATE_PERC, CHARCOAL_PERC, SULFUR_PERC, nitrate, charcoal, sulfur)
expected = (500.25, 100.05, 66.7)
test('example test: ', expected, mix)
report()