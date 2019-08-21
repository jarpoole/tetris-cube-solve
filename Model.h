
#ifndef MODEL_H
#define MODEL_H

class Model{
    public:
        Model();
        ~Model();

        Model(Model *other); //Copy Constructor

        bool pieceFits(unsigned long long int);
        void addPiece(unsigned long long int, short int);
        bool isSolved();

        unsigned long long int volumeUsed;
        short int piecesUsed[12];
        short int modelStage;

    private:

};

#endif
