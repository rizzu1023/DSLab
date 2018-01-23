#include<stdio.h>
#include<conio.h>
#include<graphics.h>

int main()
{
  int gd=0,gm;

initgraph(&gd,&gm,"");

   line(200,442,398,442);    // bottom line
   line(188,40,188,430);     //left line
   line(412,40,412,430);     //right line
   line(200,28,400,28);      //top line


   arc(400, 430,270,360,12);   //bottom right corner
   arc(200,430,180,270,12);   //bottom left corner
   arc(200,40,90,180,12);   //top left corner
   arc(400,40,0,90,12);   //top right corner


   circle(299,420,16);          //home button
   circle(299,420,17);
   rectangle(193,75,407,398);       //screen



   line(273,52,313,52);
   line(273,55,313,55);
   arc(273,53.5,90,270,2);
   arc(313,53.5,270,90,2);

   circle(250,53.5,5);         //front camera
   circle(250,53.5,5.5);
   circle(293,40,3);           //sensor

   rectangle(185,73,188,80);
   rectangle(185,100,188,130);     //volume button
   rectangle(185,135,188,165);
   rectangle(412,110,415,140);



 getch();
 return 0;
 }
