#include<string>
#include<vector>
#include<iostream>
#include<fstream>
using namespace std;

vector<int> *parse_line(string line, vector<int> *line_vector){
    string number = "";
    
    for(int i = 0; i < line.length(); i++){
        if(line[i] == ' ' && number.length() > 0){
            line_vector->push_back(stoi(number));
            number = "";
        }
        if(line[i] >= 48 && line[i] <= 57){
            number += line[i];
        }
    }
    line_vector->push_back(stoi(number));
    return line_vector;
}

int parse_line_task_2(string line){
    string number = "";
    
    for(int i = 0; i < line.length(); i++){
        if(line[i] >= 48 && line[i] <= 57){
            number += line[i];
        }
    }

    return stoi(number);
}



int parse_input(string file, vector<int> *time_vector, vector<int> *length_vector){
    ifstream myfile;
    string line;

    myfile.open(file);
    if(myfile.is_open()){
        getline(myfile, line);
        parse_line(line, time_vector);
        getline(myfile, line);
        parse_line(line, length_vector);

        myfile.close();
        return 0;
    }else{
        cout << "Unable to open file";
        return -1;
    }
}


int calculate_number_of_wins(int index, vector<int> *time_vector, vector<int> *length_vector){
    int time = time_vector->at(index);
    int length_to_beat = length_vector->at(index);
    int wins = 0;

    for(auto i = 0; i < time+1; i++){
        int time_left = time-i;
        int speed = i;
        int length = i * time_left;

        if(length > length_to_beat){
            wins++;
        }
    }

    return wins;
}

int main(){
    vector<int> time_vector;
    vector<int> length_vector;
    
    parse_input("input.txt", &time_vector, &length_vector);
    int total = 1;
    for (auto i = 0; i < time_vector.size(); ++i)
        total *= calculate_number_of_wins(i, &time_vector, &length_vector);

    cout << total << endl;
    return(0);
    
    return 0;
}