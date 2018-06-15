#!/user/bin/python
print("python")

movies = ["the one", "the two", "the three"]
print(movies[1])
print("length == " + str(len(movies)))


movies.append(["the four", "the five"])
for m in movies:
    if isinstance(m, list):
        print(m)


def print_m(mov):
    for m in mov:
        if isinstance(m, list):
            print_m(m)
        else:
            print(m)


print_m(movies)
