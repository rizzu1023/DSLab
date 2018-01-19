#include<stdio.h>
#include<graphics.h>

int main()
{
  int gd=DETECT,gm;

initgraph(&gd,&gm,NULL);

   line(200,412,398,412);    // bottom line
   arc(400, 400, 0, 100, 12); //bottom right corner
   arc(200,400,90,190,12);   //bottom left corner
   line(188,70,188,400);     //left line
   line(412,70,412,400);     //right line
   arc(200,70,180,280,12);
   line(200,58,400,58);
   arc(400,70,270,370,12);
  
   
   
 getch();
 return 0;
}
