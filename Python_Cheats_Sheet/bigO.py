import time
"""The big O """

def greet_user():
  for i in range(0,11):
    time.sleep(1)
    print(i)
  return "Hello, world!"




if __name__ == "__main__":
  start = time.time()
  print(f"Runtime started at: {start:.2f}")
  time.sleep(1)

  print(greet_user())
  time.sleep(1)
  end = time.time()
  print(f"Runtime ended at: {end:.2f}")
  time.sleep(1)
  print(f"Total time = {(end - start):.2f}")
  print(format(22.22222, ".2f"))



