#include<GL/glut.h>

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);
    
     glBegin(GL_TRIANGLE_STRIP);
    
    glColor3f(0.0f,0.0f,0.0f);             
    glVertex2f(0.6f,0.1f);
    glVertex2f(0.2f,-0.4f);
    glVertex2f(-0.0f,-0.4f);   
    
    glColor3f(1.0f,1.0f,0.0f);             //Yellow
    glVertex2f(-0.9f,0.4f);
    glVertex2f(0.9f,0.4f);
    glVertex2f(0.0f,-0.4f);   
    
      glColor3f(1.0f,1.0f,0.0f);             //Yellow
    glVertex2f(-0.6f,0.1f);
    glVertex2f(-0.1f,0.6f);
    glVertex2f(-0.5f,0.3f);           
  
    glEnd();
    
    
     glBegin(GL_QUAD_STRIP);             //Blue
    
    glColor3f(0.0f,0.0f,1.0f);
    glVertex2f(0.9f,-0.9f);
    glVertex2f(0.5f,-0.9f);
    glVertex2f(0.7f,-0.2f);
    glVertex2f(0.5f,-0.3f);

    glColor3f(0.0f,1.0f,1.0f);    
     glVertex2f(-0.1f,0.5f);
    glVertex2f(-0.5f,-0.9f);
    glVertex2f(0.6f,0.4f);
    glVertex2f(-0.5f,-0.3f);
    
    glEnd();
    
    
   glFlush();
}
int main( int argc, char** argv)
{
    glutInit(&argc,argv);
    glutCreateWindow("Basic: Vertex, Primitive and Colour");
    glutInitWindowSize(320, 320);
    glutInitWindowPosition(50, 150);
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
