def basiccal(string):
  string = "(" + string + ")" 
  stack = []
  queue = ""
  for item in string:
    if item == "(" or item == "+" or item == "-":
      if queue != "":
        stack.append(int(queue)) 
        queue = ""
      stack.append(item) 
    elif item == " ":
      continue
    elif item == ")":
      if queue != "":
        stack.append(int(queue)) 
        queue = ""
      last = stack.pop()
      second_last = stack.pop()
      temp = 0
      while second_last != "(":
        if second_last == "+":
          temp = temp + last
        elif second_last == "-":
          temp = temp - last
        last = stack.pop()
        second_last = stack.pop()
      stack.append(temp+last) 
    else:
      queue = queue+item 
  return stack[0]
