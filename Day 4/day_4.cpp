#include<iostream>
#include<fstream>
#include<string>
#include<array>
using namespace std;

void parse_card(string card, int *winning_numbers, int *your_numbers){
    int first_index = -1;
    for(int i = 0; i < card.length(); i++){
        if(card[i] == ':'){
            first_index = i+2;
            break;
        }
    }

    bool win_num = true;
    int index = 0;
    string number = "";

    for(int i = first_index; i < card.length(); i++){
        if(card[i] == '|'){
            win_num = false;
            index = 0;
            i++;
            //Mer saker !!II!J
        }else if(card[i] == ' '){
            if(number.length() != 0){
                //Spara nummer
                if(win_num){
                    winning_numbers[index] = stoi(number);
                } else{
                    your_numbers[index] = stoi(number);
                }
                //Reset number
                number = "";
                index++;
            }
        }else if(card[i] >= 48 && card[i] <= 57){
            number += card[i];
        }
    }
    your_numbers[index] = stoi(number);
}

int calculate_winnings(int *winning_numbers, int *your_numbers){
    int WINNING_NUMBERS = 10;
    int YOUR_NUMBERS = 25;
    int number_of_wins = 0;

    for(int i = 0; i < YOUR_NUMBERS; i++){
        for(int j = 0; j < WINNING_NUMBERS; j++){
            if(your_numbers[i] == winning_numbers[j] && number_of_wins == 0){
                number_of_wins = 1;
            }else if(your_numbers[i] == winning_numbers[j]){
                number_of_wins = number_of_wins * 2;
            }
        }
    }
    return number_of_wins;
}

void update_multiplier(int *multiplier, int n_wins, int start_index){
    int multiplier_length = 215;
    for(int i = 0; i < n_wins; i++){
        if(i+start_index < multiplier_length){
            multiplier[i+start_index] = multiplier[i+start_index] +1; 
        }
    }
}

int n_matching_numbers(int *winning_numbers, int *your_numbers){
    int WINNING_NUMBERS = 10;
    int YOUR_NUMBERS = 25;
    int number_of_wins = 0;

    for(int i = 0; i < YOUR_NUMBERS; i++){
        for(int j = 0; j < WINNING_NUMBERS; j++){
            if(your_numbers[i] == winning_numbers[j]){
                number_of_wins++;
            }
        }
    }
    return number_of_wins;
}

int main(){
    int *winning_numbers = (int *)calloc(10, sizeof(int)); // 5, 10
    int *your_numbers = (int *)calloc(25, sizeof(int)); //8, 25
    int *multiplier = (int *)calloc(215, sizeof(int));

    ifstream myfile;
    string line;
    int total = 0;
    int index = 0;
    myfile.open("input.txt");
    if(myfile.is_open()){
        while(getline(myfile, line)){
            parse_card(line, winning_numbers, your_numbers);
            for(int i = 0; i < multiplier[index]+1; i++){
                int n_matches = n_matching_numbers(winning_numbers, your_numbers);
                update_multiplier(multiplier, n_matches, index+1);
            }
            index++;
        }
        for(int i = 0; i < 215; i++){
            total += (multiplier[i]+1);
        }
        cout << total << endl;
        myfile.close();
    }else{
        cout << "Unable to open file";
    }
    free(multiplier);
    free(winning_numbers);
    free(your_numbers);
    return(0);
}