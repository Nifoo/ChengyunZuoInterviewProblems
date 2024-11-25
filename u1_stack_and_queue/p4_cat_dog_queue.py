from collections import deque
from datetime import datetime, tzinfo, timezone


class Pet:
    def __init__(self, type):
        self.type = type


class Dog(Pet):
    def __init__(self):
        super("Dog")


class Cat(Pet):
    def __init__(self):
        super("Cat")


# 1. add() to cat or dog into a queue
# 2. poll_all() to poll all the entities from the queue
# 3. poll_dog() to poll only dogs
# 4. poll_cat() to poll only cats
# 5. is_empty() to check if no entities
# 6. is_dog_empty() to check if no dogs
# 7. is_cat_empty() to check if no cats

class PetWithTime:
    def __init__(self, pt):
        self.pet = pt

    def with_timestamp(self):
        self.timestamp = datetime.now()
        return self


class CatDogQueue:
    def __init__(self):
        self.cat_que = deque()
        self.dog_que = deque()

    def add(self, pt: Pet):
        if pt.type == "Dog":
            self.dog_que.append(PetWithTime(pt).with_timestamp())
        else:
            self.cat_que.append(PetWithTime(pt).with_timestamp())

    def poll_all(self):
        if len(self.cat_que) == 0 and len(self.dog_que) == 0:
            return None
        if len(self.cat_que) == 0:
            return self.dog_que.popleft().pt
        elif len(self.dog_cat) == 0:
            return self.cat_que.popleft().pt

        if self.cat_que[0].timestamp < self.dog_que[0].timestamp:
            return self.cat_que.popleft().pt
        else:
            return self.dog_que.popleft().pt

    def poll_dog(self):
        if len(self.dog_que) == 0:
            return None
        return self.dog_que.popleft()

    def poll_cat(self):
        if len(self.cat_que) == 0:
            return None
        return self.cat_que.popleft()

    def is_empty(self):
        return len(self.cat_que) == 0 and len(self.dog_que) == 0

    def is_dog_empty(self):
        return len(self.dog_que) == 0

    def is_cat_empty(self):
        return len(self.cat_que) == 0

    timezone
