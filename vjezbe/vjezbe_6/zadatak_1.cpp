#include <iostream>


void jednadba_pravca(float x1,float x2, float y1, float y2){
    if (x1!=x2){
      float k;
      k = (x2-x1/y2-y1);
      float l;
      l = (y1-k*x1);
      std::cout<<"Jednadzba pravca je y="<<k<<"x+"<<l<<"." <<std::endl;
    }
    else{
      float k;
      k = (x2-x1/y1-y2);
      float l;
      l = (y1-k*x1);
      std :: cout <<"Jednadzba pravca je y="<<k<<"x+"<<l<<"."<<std::endl;
    }
    
    }

int main(){
    jednadba_pravca(1,2,1,2);
    return 0;

}