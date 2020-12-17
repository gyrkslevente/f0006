egyik = int(input('kérek egy számot: '))
masik = int(input('egy másikat: '))
if egyik > masik:
    ki = 'Az ' + str(egyik) + ' a nagyobb.'
elif egyik == masik:
    ki = 'Egyenlőek.'
else:
    ki = 'A ' + str(masik) + ' a nagyobb.'
print(ki)