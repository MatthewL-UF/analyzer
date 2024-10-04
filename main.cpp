#include <iostream>

#include <string>
#include <vector>
#include <chrono>
#include <cmath>

inline long long systemTimeNanoseconds()
{
    return std::chrono::duration_cast<std::chrono::milliseconds>(
      std::chrono::time_point_cast<std::chrono::milliseconds>(
        std::chrono::system_clock::now()
      ).time_since_epoch()
    ).count();
}

inline std::vector<std::string>& getStringData()
{
    static std::vector<std::string> stringDataSet;

    if (stringDataSet.size() == 0)
    {
        char tempSet[6] = "     ";

        for (tempSet[0] = 'a'; tempSet[0] <= 'z'; tempSet[0]++)
            for (tempSet[1] = 'a'; tempSet[1] <= 'z'; tempSet[1]++)
                for (tempSet[2] = 'a'; tempSet[2] <= 'z'; tempSet[2]++)
                    for (tempSet[3] = 'a'; tempSet[3] <= 'z'; tempSet[3]++)
                        for (tempSet[4] = 'a'; tempSet[4] <= 'z'; tempSet[4]++)
                            stringDataSet.push_back(std::string(tempSet));
    }

    return stringDataSet;
}

int linear_search(std::vector<std::string> thing, std::string element) {
    for (int i=0; i < thing.size(); i++) {
        if (thing[i]==element)
        {
            return i;
        }

    }

    return -1;
}


int binary_search (std::vector<std::string> thing, std::string element) {
    int count=0;

    while (true){

        int middle = floor(thing.size()/2);

        std::string midway=thing[middle];

        if (midway==element){
            return count+middle;
        } else if (thing.size()==1) {
            return -1;
        }

        if (midway < element){
            thing.assign(thing.begin()+middle, thing.end());
            count += middle;

            //thing.begin()
        }
        else {
            thing.assign(thing.begin(), thing.begin()+middle);
        }
    }
}

    int main()
    {
        std::vector mainData=getStringData();

        std::cout<<linear_search(mainData, "mzzzz");

        std::cout<<binary_search(mainData, "mzzzz");

        return -1;
    }


//  std::chrono::system_clock::now()


/*int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}*/
