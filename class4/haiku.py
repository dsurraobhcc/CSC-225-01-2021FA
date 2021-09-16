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
        raise Exception(f'Poem has more than three lines: {poem}') 

    # include Yes/No in the return value
    if syllable_counts == [5, 7, 5]:
        syllable_counts.append('Yes')
    else:
        syllable_counts.append('No')

    return tuple(syllable_counts)

if __name__ == '__main__':
    # read haikus from a file
    with open('haikus.txt') as f:
        for line in f:
            try:
                line = line.rstrip()
                print(check_haiku(line), line)
            except Exception as err:
                print(err)