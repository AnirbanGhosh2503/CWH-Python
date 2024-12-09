letter = ''' Dear <|Name|>,
             You are selected!
             <|Date|>'''
print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "14 September 2050"))