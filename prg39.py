chars="abcdefghijklmnopqrstuvwxyz.!,? "
message='It was a bright cold day in April, and the clocks were striking thirteen.'


for char in chars:
    count=message.count(char)
    if count>1:
        print(char,count)
        
