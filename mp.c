//Student Management System
//unique ID
//Name
//Address
//class
//Add student
//search student
//Modify student record
//exit
//phone number
//mail address
//department
//CGPA


#include<stdio.h>
#include<stdlib.h>


struct student
{
  char name[100];
  char ID[10];
  int CGPA;
  long MN;
  char MA[50];
  char DE[20];
  char class[20];
 };

void AddStudent()
{
   struct student s;
   FILE *fp;                              //make a file pointer
   fp=fopen("student.txt","a");           //open file in append mode
   printf("\nEnter Name: ");
   scanf("%s",s.name);
   fprintf(fp,"Name: %s\n",s.name);
   printf("\nEnter ID: ");
   scanf("%s",s.ID);
   fprintf(fp,"ID: %s\n",s.ID);
   fclose(fp);
   printf("\nThe record is succesfully added\n\n");
}








void main()
{
  int c;
  printf("\t\t\t\t\t\tANJUMAN-I-ISLAM'S\n");
  printf("\t\t\t\t\tKALSEKAR TECHNICAL CAMPUS, NEW PANVEL\n");
  printf("----------------------------------------------------------------------------------------------\n");
  printf("----------------------------------------------------------------------------------------------\n");
  do{
  printf("\n1.Add Student\n4.exit");
  printf("\nENTER YOUR CHOICE: "); 
  scanf("%d",&c);
  switch(c)
  {
    case 1: AddStudent();            //calling addstudent function
            break;
    case 4: exit(0);
            break;
    default: printf("invalid option");
}
}while(1);
return 0;
}

   
   
   


