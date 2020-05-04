import textwrap

def wrap(string, max_width):
  res=''
  for i in range(0,len(string),max_width):
    res+=string[i:max_width+i]+'\n'
  return res   

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
