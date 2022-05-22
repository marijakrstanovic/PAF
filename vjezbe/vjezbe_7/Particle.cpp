#include <iostream>
#include <math.h>
#include "Particle.h"

void Particle::move(){
    vy = vy + g * dt;
    x = x + vx * dt;
    y = y + vy * dt;
    t = t + dt;

}

double Particle::range(){
    while(y >= 0){
        move();
    }
    std::cout << x << std::endl;
    return x;
}

double Particle::time(){
    while(y >= 0){
        move();
    }
    std::cout << t << std::endl;
    return t;
}

Particle::Particle(double v, double theta, double x0, double y0)
{
    t = 0;

    v = v;
    theta = theta;
    x = x0; 
    y = y0;

    vy = sin(theta) * v;
    vx = cos(theta) * v;  
}
