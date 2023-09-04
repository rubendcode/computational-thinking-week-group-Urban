from Xiao import Xiao, xiao_paragraphs
from Sebastian import Sebastian, sebastian_paragraphs
from ruben import Ruben, kelt_paragraphs
from sofia import Sofia, ruben_paragraphs
from Kelt import Kelt, sofia_paragraphs

def naming():
    members = [Xiao(), Sebastian(), Ruben(), Sofia(), Kelt()]
    members_str = "\n".join(members)
    return f"This is Team Urban.\nWe are:\n{members_str}"

print(naming())

def print_story():

    for act in range(3):
        print(xiao_paragraphs[act])
        print(sebastian_paragraphs[act])
        print(kelt_paragraphs[act])
        print(ruben_paragraphs[act])
        print(sofia_paragraphs[act])

if __name__ == "__main__":
    print_story()