class Pet:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"{self.name}さんこんにちわ"


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        name = sys.argv[1]
        pet = Pet(name)
        print(pet.greet())
    else:
        print("名前を引数で指定してください")
