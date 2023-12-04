#include<iostream>
#include<fstream>
#include<string>
#include<array>
using namespace std;
#define RGB ['r', 'g', 'b']

//Räkna antal sets
int count_sets(string game_data){
    int counter = 1;
    for(int i = 0; i < game_data.length(); i++){
        if(game_data[i] == ';'){
            counter++;
        }
    }
    return counter;
}

int parse_id(string game_data){
    string parse_id = "";
    bool end_of_id = false;
    int id_counter = 5;
    while(!end_of_id){
        if(game_data[id_counter] >= 48 && game_data[id_counter] <= 57){
            parse_id += game_data[id_counter];
        }else{
            end_of_id = true;
        }
        id_counter++;
    }
    return stoi(parse_id);
}

string parse_number(string game_data, int start_index){
    string parsed_number = "";
    bool end_of_number = false;
    int index_counter = start_index;
    while(!end_of_number){
        if(game_data[index_counter] >= 48 && game_data[index_counter] <= 57){
            parsed_number += game_data[index_counter];
        }else{
            end_of_number = true;
        }
        index_counter++;
    }
    return parsed_number; 
}

//Vi behöver id, nr of sets, sets(RGB...RGB)
//Returns a pointer to an array. [id, nr_sets, R, G, B...*nr_sets]
int *parse_game_data(string game_data){
    char rgb[3] = {'r', 'g', 'b'};
    int rgb_length[3] = {3, 5, 4};

    int nr_sets = count_sets(game_data);
    int *parsed_data = (int *) calloc(2+(nr_sets * 3), sizeof(int));


    parsed_data[0] = parse_id(game_data);
    parsed_data[1] = nr_sets;
    
    int first_index = 8;
    if(parsed_data[0] >= 10 && parsed_data[0] < 100){
        first_index++;
    }else if(parsed_data[0] == 100){
        first_index = first_index + 2;
    }

    int set = 0;
    for(int j = first_index; j < game_data.length(); j++){
        if(game_data[j] == ';'){
            set++;
            j += 2;
        }else if(game_data[j] == ','){
            j += 2;
        }
        string number = parse_number(game_data, j);

        j = j+number.length()+1;
        for(int i = 0; i < 3; i++){
            if(game_data[j] == rgb[i]){
                // Spara värdet i array
                parsed_data[2+(set*3)+i] = stoi(number);
                // Hoppa till nästa komma
                j += rgb_length[i]-1;
                break;
            }
        }
    }
    return parsed_data;
}

//Returns id if game possible. -1 of not
int determine_game_possible(string game_data){
    int bag[3] = {12, 13, 14};

    int *parsed_game = parse_game_data(game_data);
    bool game_possible = true;
    for(int i = 0; i < parsed_game[1]; i++){
        for(int j = 0; j < 3; j++){
            if(parsed_game[(i*3)+j+2] > bag[j]){
                game_possible = false;
                return -1;
            }
        }
    }
    return parsed_game[0];
}

int determine_fewest_possible_cubes(string game_data){
    int bag[3] = {0, 0, 0};
    int *parsed_game = parse_game_data(game_data);

    for(int i = 0; i < parsed_game[1]; i++){
        for(int j = 0; j < 3; j++){
            if(parsed_game[(i*3)+j+2] > bag[j]){
                bag[j] = parsed_game[(i*3)+j+2]; 
            }
        }
    }
    return bag[0]*bag[1]*bag[2];
}

int main(){
    ifstream myfile;
    string line;
    int total = 0;
    int count = 0;
    myfile.open("input.txt");
    if(myfile.is_open()){
        while(getline(myfile, line)){
            total += determine_fewest_possible_cubes(line);
        }
        cout << total << endl;
        myfile.close();
    }else{
        cout << "Unable to open file";
    }

    return(0);
    
}