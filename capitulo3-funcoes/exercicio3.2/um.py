def do_twice(f, value):
  f(value)
  f(value)

def print_spam(value):
  print(value)

do_twice(print_spam, "master")

print("--------------")

def do_four(f, value):
  for i in range(4):
    f(value)
  
do_four(print_spam, "test")
