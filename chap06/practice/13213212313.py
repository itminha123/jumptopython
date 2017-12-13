
text = input('?????') + '\n'

stack, result, cnt = [], '', 0

for w in text:
   if not stack:
       stack.append(w)
       cnt+=1
   elif w in stack:
       cnt+=1
   else:
       result+='{0}{1}'.format(stack[0], cnt)
       stack.pop()
       stack.append(w)
       cnt=1
print(result)