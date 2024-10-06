import time


def get_data() -> tuple:
    string_data_set = ["."] * (26**5)
    temp_set = [".", ".", ".", ".", "."]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = 0
    for i in range(len(alphabet)):
        temp_set[4] = alphabet[i]
        for j in range(len(alphabet)):
            temp_set[3] = alphabet[j]
            for k in range(len(alphabet)):
                temp_set[2] = alphabet[k]
                for l in range(len(alphabet)):
                    temp_set[1] = alphabet[l]
                    for m in range(len(alphabet)):
                        temp_set[0] = alphabet[m]
                        string_data_set[index] = (temp_set[0] + temp_set[1] + temp_set[2] + temp_set[3] + temp_set[4])
                        index += 1
    string_data_set.sort()
    string_data_tuple = tuple(string_data_set)
    return string_data_tuple




def linear_search(container: tuple, element: str) -> int:
    for i in range(len(container)):
        if container[i] == element:
            return i
    return -1


def binary_search(newContainer: tuple, element: str) -> int:

    #Code is slow. might have to rework to do the linear search inhouse.

    #newContainer=container #this might be the culprit
    count = 0

    while True:

        middle=len(newContainer)//2

        #midway=linear_search(newContainer[:middle], element)

        midway=newContainer[middle]


        if midway==element:
            return count+middle
        elif len(newContainer)==1:
            return -1


        if midway<element:
            newContainer=newContainer[middle:]
            count+=middle

        else:
            newContainer=newContainer[:middle]




def time_measurer(func_choice, input_data, searcher):
    start_time = time.time()
    location = func_choice(input_data, searcher)
    end_time = time.time()
    print(end_time - start_time)
    return end_time - start_time



def main():
    string_data = get_data()
    knowledge=[]
    print("not_here Linear search")
    knowledge.append(time_measurer(linear_search, string_data, "not_here"))
    print("Index: "+ str(knowledge[len(knowledge)-1]))
    newContainer = string_data

    print("not_here Binary search")
    knowledge.append(time_measurer(binary_search, newContainer, "not_here"))
    print("Index: "+ str(knowledge[len(knowledge)-1]))

    print("mzzzz Linear search")
    knowledge.append(time_measurer(linear_search, string_data, "mzzzz"))
    newContainer = string_data
    print("Index: " + str(knowledge[len(knowledge) - 1]))

    print("mzzzz Binary search")
    knowledge.append(time_measurer(binary_search, newContainer, "mzzzz"))
    print("Index: " + str(knowledge[len(knowledge) - 1]))

    print("aaaaa Linear search")
    knowledge.append(time_measurer(linear_search, string_data, "aaaaa"))
    print("Index: " + str(knowledge[len(knowledge) - 1]))
    newContainer = string_data

    print("aaaaa Binary search")
    knowledge.append(time_measurer(binary_search, newContainer, "aaaaa"))
    print("Index: " + str(knowledge[len(knowledge) - 1]))

    """
    #For testing purposes:
    
    while True:
        print("1) not_here linear")
        print("2) not_here binary")
        print("3) mzzzz linear")
        print("4) mzzzz binary")
        print("5) aaaaa linear")
        print("6) aaaaa binary")

        try:
            choice=knowledge[int(input())-1]
        except ValueError:
            continue
        print(choice)
    """



if __name__ == '__main__':
    main()
