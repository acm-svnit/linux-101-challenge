import random
import string

def create_file(filename, size):
    chars = ''.join([random.choice(string.ascii_letters) for i in range(size)])  # 1

    with open(filename, 'w') as f:
        f.write(chars)
    pass



for i in range(100):
  if i < 10:
    create_file(f"file-0{i}.txt", 1024*8)
  else:
    create_file(f"file-{i}.txt", 1024*8)