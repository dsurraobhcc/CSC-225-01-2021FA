# raising an exception

# returns a syllable count
def check_haiku(poem):
    syllable_count = (5, 7, 5, 'Yes')

    # Check that a haiku can be no more than 50 characters long
    if len(poem) > 50:
        raise Exception('Haiku can be no more than 50 characters long')

    # do more processing

    return (syllable_count)

if __name__ == '__main__':
    poem = 'hello/there/worldworldworldworldworldworldworldworldworldworldworldworldworldworldworld'
    
    try:
        syllable_count = check_haiku(poem)
    except  Exception as e:
        print(e)