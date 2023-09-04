from Xiao import Xiao
from Sebastian import Sebastian
from ruben import Ruben

def naming():
    members = [Xiao(), Sebastian(), Ruben()]
    members_str = "\n".join(members)
    return f"This is Team Urban.\nWe are:\n{members_str}"

print(naming())