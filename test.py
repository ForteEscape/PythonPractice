from queue import Queue
num = int(input())
card = Queue()

for i in range(1, num + 1):
    card.put(i)

while card.qsize() > 1:
    card.get()
    card.put(card.get())
print(card.get())
