#include <math.h>
#include <Particle.h>
#define _USE_MATH_DEFINES

void Particle::move(float dt){
    vy = vy - 9.81*dt;
    x = x + vx * dt;
    y = y + vy * dt;
};

void Particle::return_to_start(){
    vx = v0*cos(theta);
    vy = v0*sin(theta);
    x = x0;
    y = y0;
};

Particle::Particle(float a, float b, float c, float d){
    v0 = a;
    theta = (b/180)*M_PI;
    x0 = c;
    y0 = d;
    vx = v0*cos(theta);
    vy = v0*sin(theta);
    x = x0;
    y = y0;
};

float Particle::range(float dt){
    while(y > 0){
        move(dt);
    }
    return x - x0;
};

float Particle::time(float dt){
    float t = 0;
    while(y > 0){
        move(dt);
        t = t + dt;
    }
    return t;
}