from operator import itemgetter


def parser():
    fin = open("result.txt", "r")
    fout = open("log.txt", "w+")

    for line in fin:
        parts = line.split(" ")
        # print parts
        st = parts[-2] + " " + "INV " + parts[1]
        if parts[0] == "INSERT":
            st += " " + "W "
        else:
            st += " " + "R "
        st += parts[3] + ":" + parts[4]
        if parts[0] == "INSERT":
            st += " " + parts[-3]
        str2 = st

        st = parts[-1][:-1] + " " + "RES " + parts[1]
        if parts[0] == "INSERT":
            st += " " + "W "
        else:
            st += " " + "R "
        st += parts[3] + ":" + parts[4]
        if parts[0] == "READ":
            st += " " + parts[-3]
        fout.write(str2 + "\n")
        fout.write(st + "\n")
    fout.close()

def sorter():
    fin = open("log.txt", "r")

    strs = []

    for line in fin:
        st = line.split(" ")
        strs.append(st)

    fin.close()
    sorted(strs, key=itemgetter(0))
    fout = open("log.txt", "w")
    for i in range(0, len(strs)):
        fout.write(" ".join(strs[i]))

    fout.close()
