#include "task1.h"

using namespace std;

bool is_digit(char c){
    return((c >= 48 && c <= 57) || c == '-');
}

vector<int> *parse_line(string line, vector<int> *numbers){
    string number = "";
    
    for(int i = 0; i < line.length(); i++){
        if(is_digit(line[i])){
            number += line[i];
        }else if(number.length() > 0){
            numbers->push_back(stoi(number));
            number = "";
        }
    }
    if(number.length() > 0){
        numbers->push_back(stoi(number));
        number = "";
    }
    return numbers;
}

vector<vector<int>> *parse_input(string file, vector<vector<int>> *all_readings){
    ifstream myfile;
    string line;
    
    myfile.open(file);
    if(myfile.is_open()){
        while(getline(myfile, line)){
            vector<int> vector;
            parse_line(line, &vector);
            all_readings->push_back(vector);
        }

        myfile.close();
        return all_readings;
    }else{
        cout << "Unable to open file";
        return all_readings;
    }
}

bool check_all_zeros(vector<int> *vector){
    for(int i; i < vector->size(); i++){
        if(vector->at(i) != 0){
            return false;
        }
    }
    return true;
}

int extrapolate_vector(vector<vector<int>> *sequences){
    for(int i = sequences->size()-2; i > -1; i--){
        int left = sequences->at(i).at(sequences->at(i).size()-1);
        int below = sequences->at(i+1).at(sequences->at(i+1).size()-1);
        sequences->at(i).push_back(left+below);
    }

    return sequences->at(0).at(sequences->at(0).size()-1);
}

int exrapolate_number(int left, int below){
    return left + below;
}

int predict_number(vector<int> *readings){
    vector<vector<int>> sequence;
    bool all_zeros = false;
    vector<int> vec;
    
    for(int i = 0; i < readings->size()-1; i++){
        vec.push_back(readings->at(i+1) - readings->at(i));
    }
    
    sequence.push_back(vec);
    all_zeros = check_all_zeros(&sequence.at(sequence.size()-1));
    
    while(!all_zeros){
        vector<int> vec;
        
        for(int i = 0; i < sequence.at(sequence.size()-1).size()-1; i++){
            vec.push_back(sequence.at(sequence.size()-1).at(i+1) - sequence.at(sequence.size()-1).at(i));
        }
        
        sequence.push_back(vec);
        all_zeros = check_all_zeros(&sequence.at(sequence.size()-1));
    }

    int below = extrapolate_vector(&sequence);
    int left = readings->at(readings->size()-1);

    return left + below;
}

/*
int main(){
    vector<vector<int>> all_readings;

    parse_input("input.txt", &all_readings);
    
    int sum = 0;
    for(int i = 0; i < all_readings.size(); i++){
        sum += predict_number(&all_readings.at(i));
    }

    cout << sum << endl;
}
*/
