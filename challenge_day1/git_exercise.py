from Xiao import Xiao
from Sebastian import Sebastian
from ruben import Ruben
from sofia import Sofia

def naming():
    members = [Xiao(), Sebastian(), Ruben(), Sofia()]
    members_str = "\n".join(members)
    return f"This is Team Urban.\nWe are:\n{members_str}"

print(naming())