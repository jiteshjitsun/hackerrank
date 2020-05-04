n=input().split()
for i in range(int(n[0])//2):
  print((((int(n[1]))//2-i*3-1)*'-').ljust(1)+i*'.|.'+'.|.'+i*'.|.'+(((int(n[1]))//2-i*3-1)*'-').rjust(1))
print((((int(n[1]))//2-3)*'-').ljust(1)+'WELCOME'+(((int(n[1]))//2-3)*'-').rjust(1))
for i in range(int(n[0])//2-1,-1,-1):
  print((((int(n[1]))//2-i*3-1)*'-').ljust(1)+i*'.|.'+'.|.'+i*'.|.'+(((int(n[1]))//2-i*3-1)*'-').rjust(1))
