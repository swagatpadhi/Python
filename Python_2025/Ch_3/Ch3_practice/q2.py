letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "4th Jan, 2025"))