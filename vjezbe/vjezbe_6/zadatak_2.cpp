#include <iostream>
#include <cmath>

void kruznica(float x, float y, float p, float q, float r){
    float R = r;
    float d = pow((x - p),2)+pow((y - q),2);
    float D = sqrt(d)-R;
    if (D < R){
         std::cout<<"Tocka se nalazi u kruznici."<<std::endl;
    }
    else
      if  (D == R){
        std::cout<<"Tocka je na kruznici."<<std::endl;
    }
    else
        if (D > R){
        std::cout<<"Tocka se nalazi izvan kruznice."<<std::endl;
        }

}

int main(){
    kruznica(1,2,3,4,2);
    return 0;

}