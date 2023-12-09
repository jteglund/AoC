#include<string>
#include<vector>
#include<iostream>
#include<fstream>
#include<tuple>
using namespace std;

bool is_digit(char c);

vector<int> *parse_line(string line, vector<int> *numbers);

vector<vector<int>> *parse_input(string file, vector<vector<int>> *all_readings);

bool check_all_zeros(vector<int> *vector);