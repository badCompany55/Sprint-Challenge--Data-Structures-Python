class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
      if len(self.storage) == self.capacity:
          self.storage[self.current] = item
          if self.current < self.capacity - 1:
              self.current += 1
          else:
              self.current = 0
      else:
          self.storage.append(item)

  def get(self):
      return list(filter(lambda x: x is not None, self.storage))
