

#include <iostream>
#include <stack>
#include <vector>
#include <fstream>
#include "Model.h"

using namespace std;

vector<vector<unsigned long long int> > pieceData;

void loadData(){
    pieceData.resize(12, vector<unsigned long long int>(0, 0));

    string line;
    ifstream myfile ("permutations.txt");
    if (myfile.is_open()){
        int currentPiece = 0;
        while ( getline (myfile,line) ){
            if(line.at(0) == '#'){
                line = line.erase(0,1);
            }
            int numLines = std::stoi(line, nullptr, 10);
            for(int i = 0; i < numLines; i++){
                getline (myfile,line);
                unsigned long long int piece = std::stoull(line, nullptr, 2);
                pieceData[currentPiece].push_back(piece);
            }
            currentPiece++;
        }
        myfile.close();
    }else{
         cout << "Unable to open file";
    }
}

void saveSolution(Model* solutionModel){
    ofstream myfile;
    myfile.open("solutions.txt",ios::app);
    for(int i = 0; i < 12; i++){
        myfile << solutionModel->piecesUsed[i]<<" ";
    }
    myfile<<"\n";
    myfile.close();
}

int main(){
    cout<<"Solve started..."<<endl;
    ofstream myfile;
    myfile.open ("solutions.txt",ios::trunc);
    myfile.close();

    loadData();

    stack<Model*> modelStack;
    Model *initialModel = new Model();
    Model *currentModel = NULL;
    Model *newModel = NULL;

    modelStack.push(initialModel);

    short int numPermutes = 0;
    short int modelStage = 0;
    short int oldModelStage = -1;

    while (!modelStack.empty()) {
        currentModel = modelStack.top();

        numPermutes = pieceData[currentModel->modelStage].size();
        modelStage = currentModel->modelStage;

        if(modelStack.size() < 193){
            cout<<modelStack.size()<<endl;
            cout<<currentModel->modelStage<<endl;
            oldModelStage = modelStage;
        }

        modelStack.pop();

        if(currentModel->isSolved()){
            cout<<"Found solution!"<<endl;
            saveSolution(currentModel);
        }else{
            for(short int i = 0; i < numPermutes; i++){
                if(currentModel->pieceFits(pieceData[modelStage][i])){
                    newModel = new Model(currentModel);
                    newModel->addPiece(pieceData[modelStage][i], i);
                    modelStack.push(newModel);
                }
            }
        }
    }
    cout<<"Finished!"<<endl;

}
