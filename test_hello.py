from hello import Pet


def test_pet_greet():
    pet = Pet("たろう")
    assert pet.greet() == "たろうさんこんにちわ"
