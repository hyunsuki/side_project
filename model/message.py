from enum import Enum

class Place(Enum):pass

class Action(Enum):pass

class Result(Enum):pass

def main():
    print(Place(0).value + Action(0) + Result(0))

if __name__ == '__main__':
    main() 
