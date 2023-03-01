dictonary = {
    "Father": 0,
    "God": 0,
    "Christ": 0,
    "Spirit": 0,
    "spirit": 0,
    "life": 0,
    "man": 0,
}

infile = open("book of John text.txt", "r")
script = infile.readlines()

for record in script:
    words = record.split(" ")

    for word in words:
        if word == "Father":
            dictonary[word] += 1
        elif word == "God":
            dictonary[word] += 1
        elif word == "Christ":
            dictonary[word] += 1
        elif word == "Spirit":
            dictonary[word] += 1
        elif word == "spirit":
            dictonary[word] += 1
        elif word == "life":
            dictonary[word] += 2
        elif word == "man":
            dictonary[word] += 1
        else:
            continue


for k, v in dictonary.items():
    print(k, ":", v)
