#include<iostream>
#include<fstream>
#include<string>
#include<array>
using namespace std;



int is_real_number(string line){
    string numbers[] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    for(int i = 1; i < 10; i++){
        for(int j = 0; j < numbers[i].length(); j++){
            if(numbers[i][j] != line[j]){
                break;
            }
            if(numbers[i].length()-1 == j){
                return i;
            }
        }
    }
    return -1;
}

int decode_line(string line){
    string digits = "";
    for(int i = 0; i < line.length(); i++){
        if ((int) line[i] >= 48 && (int) line[i] <= 57){
            digits = digits + line[i];
        } else {
            string tmp = line;
            tmp = tmp.erase(0, i);
            int is_number = is_real_number(tmp);
            if(is_number != -1){
                digits = digits + to_string(is_number);
            }
        }
    }
    
    string result = "00";
    result[0] = digits[0];
    result[1] = digits[digits.length()-1];
    return stoi(result);
}

int main(){
    ifstream myfile;
    string line;
    int total = 0;
    myfile.open("input.txt");
    if(myfile.is_open()){
        while(getline(myfile, line)){
            total = total + decode_line(line);
        }
        cout << total << endl;
        myfile.close();
    }else{
        cout << "Unable to open file";
    }
    return(0);
}