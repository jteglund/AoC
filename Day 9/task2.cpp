#include "task1.h"
using namespace std;

int extrapolate_vector_backwards(vector<vector<int>> *sequences){
    for(int i = sequences->size()-2; i > -1; i--){
        int right = sequences->at(i).at(0);
        int below = sequences->at(i+1).at(0);
        sequences->at(i).insert(sequences->at(i).begin(), right-below);
    }

    return sequences->at(0).at(0);
}

int exrapolate_number_backwards(int right, int below){
    return right - below;
}

int predict_number_(vector<int> *readings){
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

    int below = extrapolate_vector_backwards(&sequence);
    int right = readings->at(0);

    return right - below;
}

int main(){
    vector<vector<int>> all_readings;

    parse_input("input.txt", &all_readings);
    
    int sum = 0;
    for(int i = 0; i < all_readings.size(); i++){
        sum += predict_number_(&all_readings.at(i));
    }

    cout << sum << endl;
}
