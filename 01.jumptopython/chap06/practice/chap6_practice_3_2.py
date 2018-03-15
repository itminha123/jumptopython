
morse = {'.-'  :'A' ,'-...':'B','-.-.':'C','-..' :'D',
         '.'   :'E' ,'..-.':'F','--.' :'G','....':'H',
         '..'  :'I' ,'.---':'J','-.-' :'K','.-..':'L',
         '--'  :'M' ,'-.'  :'N','---' :'O','.--.':'P',
         '--.-':'Q' ,'.-.' :'R','...' :'S','-'   :'T',
         '..-' :'U' ,'...-':'V','.--' :'W','-..-':'X',
         '-.--':'Y' ,'--..':'Z','':' '}

while True:
    text  = input('Enter Morse code.')
    mos   = ''
    for i in text.split(' ') :
        if i in morse:
            mos += morse[i]
    # if text == '' :
    #     mos += ' '
    print(mos)
    # print(mos)


