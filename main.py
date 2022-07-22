import sys



special_characters = "\"!@#$%^&*()-+?_=,<>/."

def generate(s):


    s=s.replace('https://','')
    output=""

    for c in s:
        if c=='.':
            output+='%2e'
            continue
        if special_characters.count(c)<=0:
            output+="%{:02x}".format(ord(c))
            continue
        output+=c
    return 'https://'+output

if __name__ == "__main__":
    s=""
    if len(sys.argv)<=1:
        print("usage: myprogram.py <url>")

    else:
        s=sys.argv[1]
        print(generate(s))



