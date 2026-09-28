def char(text):
    d = {}

    for ch in text:
        d[ch] = d.get(ch, 0) + 1
        
    return d
    