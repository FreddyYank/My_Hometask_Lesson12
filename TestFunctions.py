import pytest
from Functions import House1, xet


if  House1.min() != 1:
    print("Error!")
else:
    print("Ok!")

if xet(10) == "Четное!":
    print("Ok!")
elif xet(12) != "Нечетное!":
    print("Ok!")
elif xet(13) == "Нечетное!":
    print("Ok!")
elif xet(13) != "Четное!":
    print("Ok")
elif xet(8) != "Четное":
    print("Ok")
elif xet(13) != "Нечетное":
    print("Ok")
else:
    print("Err")



