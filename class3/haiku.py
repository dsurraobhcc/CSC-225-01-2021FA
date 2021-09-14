import re

def num_syllables(line):
    m = re.findall(r'[aeiouy]+', line)
    return len(m)

def check_haiku(poem):
    syllable_counts = []

    # number of lines should be three, line delimiter is /
    lines = poem.split('/')
    if len(lines) == 3:
        # loop through each line and count syllables
        for line in lines:
            syllable_counts.append(num_syllables(line))
    else:
        raise Exception('Poem has more than three lines') 

    # include Yes/No in the return value
    if syllable_counts == [5, 7, 5]:
        syllable_counts.append('Yes')
    else:
        syllable_counts.append('No')

    return tuple(syllable_counts)

if __name__ == '__main__':
    haiku1 = 'happy purple frog/eating bugs in the marshes/get indigestion/hello there'
    print(check_haiku(haiku1))
