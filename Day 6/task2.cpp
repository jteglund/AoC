#include<string>
#include<vector>
#include<iostream>
#include<fstream>
#include<tuple>
using namespace std;


long parse_line(string line){
    string number = "";
    
    for(int i = 0; i < line.length(); i++){
        if(line[i] >= 48 && line[i] <= 57){
            number += line[i];
        }
    }

    return stol(number);
}



std::tuple<long, long> parse_input(string file){
    ifstream myfile;
    string line;

    myfile.open(file);
    if(myfile.is_open()){
        getline(myfile, line);
        long time = parse_line(line);
        getline(myfile, line);
        long length = parse_line(line);

        myfile.close();
        return {time, length};
    }else{
        cout << "Unable to open file";
        return {-1, -1};
    }
}


int calculate_number_of_wins(long time, long length_to_beat){
    int wins = 0;
    
    for(long i = 0; i < time+1; i++){
        long time_left = time-i;
        long speed = i;
        long length = i * time_left;
        
        if(length > length_to_beat){
            wins++;
        }
    }

    return wins;
}

int main(){
    auto [time, length] = parse_input("input.txt");
    int total;
    total = calculate_number_of_wins(time, length);
    
    return 0;
}