// Day 1 AOC - C++ solution

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

    part1();
    part2();

    return 0;
}

void part1() {
      const std::string filename = "day1.txt";

    std::ifstream file(filename);

    if (!file.is_open()) {
        std::cerr << "Error: Could not open the file" << std::endl;
    }

    std::vector<float> list1;
    std::vector<float> list2;
    std::vector<float> differences_list;
    std::string line;
    int result = 0;

    while (std::getline(file, line)) {
        float num1, num2;

        if(sscanf(line.c_str(), "%f\t%f", &num1, &num2) == 2) {
            list1.push_back(num1);
            list2.push_back(num2);
        }
    }

    file.close();

    // ensure lists are of the same size
    if (list1.size() != list2.size()) {
        std::cerr << "Error: Lists are of different sizes";
    }

    // sort the lists
    std::sort(list1.begin(), list1.end());
    std::sort(list2.begin(), list2.end());

    // loop and subtract the values to find the differences
    for (size_t i = 0; i < list1.size(); i++) {
        if(list1[i] > list2[i]) {
            differences_list.push_back(list1[i] - list2[i]);
        } else {
            differences_list.push_back(list2[i] - list1[i]);
        }
   
    }

    std::cout << "Sorted list 1: ";
    for (int num : list1) {
        std::cout << num << " ";
    }

    std:cout << "\n";

    std::cout << "Sorted list 2: ";
    for (int num : list2) {
        std::cout << num << " ";
    }

    for(int number : differences_list) {
        result += number;
    }

    std::cout << result << std::endl;
}

void part2() {
    const std::string filename = "day1.txt";

    std::ifstream file(filename);

    if (!file.is_open()) {
        std::cerr << "Error: Could not open the file" << std::endl;
    }

    std::vector<float> list1;
    std::vector<float> list2;
    std::vector<float> frequencies;
    std::string line;
    int sum = 0;

    while (std::getline(file, line)) {
        float num1, num2;

        if(sscanf(line.c_str(), "%f\t%f", &num1, &num2) == 2) {
            list1.push_back(num1);
            list2.push_back(num2);
        }
    }

    file.close();

    if (list1.size() != list2.size()) {
        std::cerr << "Error: Lists are of different sizes";
    }

    for (size_t i = 0; i < list1.size(); i++) {

        int frequency = std::count(list2.begin(), list2.end(), list1[i]);
        int result = list1[i] * frequency;
        sum += result;
    }

    std::cout << sum << std::endl;
}