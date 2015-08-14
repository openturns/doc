// To compile:
// /usr/local/povray-3.7.0.rc3/bin/povray +L/usr/local/povray-3.7.0.rc3/share/povray-3.7/include/ +IUpButton.pov +H80 +W80 +Q9 +A0.1 +Am2 +UA
#include "colors.inc"
#include "metals.inc"
#include "glass.inc"
#include "textures.inc"

#declare Plastic=
  texture
{
  pigment {color 1.2*Wheat} finish {ambient 0.3 reflection {0.3 metallic}}
}

#declare T_Velour_Vert =
  texture
{
  pigment { Green }
  normal {
    bumps 0.5  // controls depth of bumps
    scale 0.25 // controls width of bumps
  }
}
global_settings {
  assumed_gamma 1
  ambient_light White // Ambient light is back!
}

camera {
  orthographic
  location <0,0,1000>
  right 2*x up 2*y direction -z
}

light_source { <-50,100,100>, White }

// Uncomment to highlight the button
light_source { <0,0,100>, White*0.6 }

// Round button
#declare b_round = sphere {
  <0,0,-1>,1
  // Squash the sphere in Z
  scale <1,1,0.2>
}

// Rounded square button
#declare b_rsquare = superellipsoid {
  // Adjust first parameter: 1=circle, 0=square
  <0.2,0.15>
  translate -z scale <1,1,0.2>
}

// Hollow round button
#declare b_hround = difference {
  sphere { <0,0,-0.1>,1 }
  sphere { <0,0,1>,1 scale 1.4 }
  scale <1,1,0.2>
}

// Right arrow
#declare c_rarrow = prism {
  // Object extends in Z range 0..1
  0, 1,
  6, <-1,-1>,<-0.3,-1>,<1,0>,<-0.3,1>,<-1,1>,<0.3,0>
  rotate 90*x
  scale <0.6,0.6,1>
}

// Button finish
#declare f_button = finish {
  ambient 0.1
  diffuse 0.3
  specular 0
  phong 0.6 phong_size 20
}

// Content finish
#declare f_content = finish {
  ambient 0.7
  diffuse 0.3
  specular 0
  phong 0
}

// Outer ring and cylinder,
// cylinder is needed to block light when button is pushed down
#declare o_ring = merge {
  difference {
    cylinder { <0,0,0>,<0,0,-20>,1 }
    cylinder { <0,0,1>,<0,0,-21>,0.8 }
  }
  torus { 0.9,0.1 rotate 90*x }
}

// Button and its contents
difference {
  object { b_round
    texture { Plastic }}
  object { c_rarrow translate <0.1,0,-0.1> rotate <0,0,90>
    texture { pigment { color Col_Glass_Ruby } finish { f_content } } }
  scale <0.8,0.8,1>
}

// Ring
object { o_ring
  texture { T_Velour_Vert }
  translate -0.2*z // Align with Z center of round button
}
