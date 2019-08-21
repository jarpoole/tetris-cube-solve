
#include<iostream>
#include <inttypes.h>
#include "Model.h"

using namespace std;

Model::Model(){
    volumeUsed = 0;
    modelStage = 0;
    for(short int i = 0; i < 12; i++){
        piecesUsed[i] = -1;
    }
}

Model::Model(Model *other){
    volumeUsed = other->volumeUsed;
    for(short int i = 0; i < 12; i++){
        piecesUsed[i] = other->piecesUsed[i];
    }
    modelStage = other->modelStage;
}

Model::~Model(){

}

bool Model::pieceFits(unsigned long long int piece){
    return (piece & volumeUsed) == 0;
}

void Model::addPiece(unsigned long long int piece, short int pieceNum){
    volumeUsed = volumeUsed | piece;
    piecesUsed[modelStage] = pieceNum;
    modelStage++;
}

bool Model::isSolved(){
    if (modelStage == 12){
        if(volumeUsed == 0xFFFFFFFFFFFFFFFF){
            return true;
        }
    }
    return false;
}
