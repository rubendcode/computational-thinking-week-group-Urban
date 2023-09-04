from Xiao import Xiao

def naming():
    members = [Xiao()]
    members_str = ",\n".join(members)
    return f"This is Team Urban.\nWe are:\n{members_str},\n"

print(naming())