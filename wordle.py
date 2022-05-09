import random
words = [i.strip() for i in open("five.txt","r").readlines()]
word = random.choice(words)
guess = "      "

n = 0
while n != 6:
  guess = input(":")
  if not guess in words or len(guess) != 5:
    print("Invalid word!")
    n -= 1
  else:
    w = word
    out = ""
    c = {}
    for i in range(5):
      if guess[i] == word[i]: w = w[:i] + "+" + w[i+1:]
      c[word[i]] = word.count(word[i])
    for i in range(5):
      if w[i] == "+": out += word[i]
      elif guess[i] in w and c[guess[i]] > 0:
        out += "."
        c[guess[i]] -= 1
      else: out += "_"
    for i in out: print(i,end=' ')
    print()
  print()
  if guess == word:
    print(f"Congrats! ({n+1}/6)")
    exit(0)
  n += 1

print(f"Answer:{word}")
