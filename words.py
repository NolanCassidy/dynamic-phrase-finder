import sys

dict_from_file = set(line.strip() for line in open('diction10k.txt'))

def iterativeCheck(string,splitstring):
    if (len(string) == 0):
        print(splitstring)
        return True
    else:
        word = ""
        index = 0
        while (len(string) > index):
            word += string[index]
            if word in dict_from_file:
                if (iterativeCheck(string[index+1:], splitstring+word+" ")):
                    return True
                else:
                    index+=1
            else:
                index+=1
        return False

def memoizedCheck(string, splitstring, cache):
    if(len(string) == 0):
        print(splitstring)
        return True
    elif (string in cache):
        return False
    else:
        word = "";
        index = 0
        while (len(string) > index):
            word += string[index]
            if (word in dict_from_file):
                if (memoizedCheck(string[index+1:], splitstring+word+" ", cache)):
                    return True
                else:
                    index+=1
            else:
                cache.add(string)
                index+=1
        return False

def driver():
    for s in range(int(sys.stdin.readline().strip())):
        string = sys.stdin.readline().strip()
        print("phrase number: {}".format(s+1))
        print("{}\n".format(string))

        print("iteraive attempt:")
        iteraive = iterativeCheck(string,"")
        if(iteraive):
            print("YES, can be split\n")
        else:
            print("NO, cannot be split\n")

        print("memoized attempt:")
        cache = set()
        memoized=memoizedCheck(string,"",cache)
        if(memoized):
            print("YES, can be split\n")
        else:
            print("NO, cannot be split\n")


# call with Python 3
if __name__ == "__main__":                            #sets driver as __main__
    driver()
