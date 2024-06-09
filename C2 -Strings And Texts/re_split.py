import re

string1 = "books::authors,:,harrypotter::jkrowling,:,nikkilauda::laudashab,:,berserk::kentaromuira "

string2 = ""


# splitlist  = re.split(r"\s+,:,\s"  , string1)
# joinedlist = "_".join(splitlist)


splitlist  = re.split(r"(:,)"  , string1)
print(splitlist)