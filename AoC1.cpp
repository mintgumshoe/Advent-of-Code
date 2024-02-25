#include <unordered_map>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

unordered_map<string, char> numberMap = {
    {"one", '1'},
    {"two", '2'},
    {"three", '3'},
    {"four", '4'},
    {"five", '5'},
    {"six", '6'},
    {"seven", '7'},
    {"eight", '8'},
    {"nine", '9'}
};

char findFirstNumber(string input) {
    for (int i = 0; i < input.length(); ++i) {
        if (isdigit(input[i])) {
            return input[i];
        }
        // Maps a string to the respective digit, used for part two
        string substring = "";
        for (int j = i; j < input.length(); ++j) {
            substring += input[j];
            if (numberMap.find(substring) != numberMap.end()) {
                return numberMap[substring];
            }
        }
        
    }
    return '0'; // indicates no number found
}

char findLastNumber(string input) {
  for (int i = input.length() - 1; i >= 0; --i) {
        if (isdigit(input[i])) {
            return input[i];
        }
        
        string substring = "";
        for (int j = i; j >= 0; --j) {
            substring = input[j] + substring;
            if (numberMap.find(substring) != numberMap.end()) {
                return numberMap[substring];
            }
        }
        
    }
    return '0'; // indicates no number found
}

string sumNums(char firstNum, char lastNum) { 
  string first(1, firstNum);
  string last(1, lastNum);
  return first + last; 
}

int main() {
  // Open a file for reading
  ifstream inputFile("testcode.txt");

  // Read the file line by line
  string line;
  int bigSum = 0;
  while (getline(inputFile, line)) {
    bigSum += stoi(sumNums(findFirstNumber(line), findLastNumber(line)));
  }

  cout << "Sum: " << bigSum << endl; // Expect ANSWER! :D 
  // Part 1: 54632
  // Part 2: 54019
  
  // Close the file
  inputFile.close();

}
