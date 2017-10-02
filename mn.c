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
#include<string.h>


typedef struct student
{
  char name[100];
  char ID[10];
  struct student *next;
 }node;

void AddStudent(node *q)
{
   node *temp;
   temp=q;
   FILE *fp;                              //make a file pointer
   fp=fopen("student.txt","a");           //open file in append mode
   printf("\nEnter Name: ");
   scanf("\n\n%s",temp->name);
   fprintf(fp,"Name: %s\n",temp->name);
   printf("\nEnter ID: ");
   scanf("%s",temp->ID);
   fprintf(fp,"ID: %s\n",temp->ID);
   fclose(fp);
   printf("\n\tRECORD IS SUCCESFULY ADDED :)\n\n");
   temp->next=NULL;
}

void searchStudent(node *q)
{
  int c;
  char src[20];
  node *temp;
  temp=q;
printf("\n\nEnter student ID: ");
  scanf("%s",src);
while(temp!=NULL)
{
  c=strcmp(src,temp->ID);
  if(c==0)
{
  printf("\nName: %s",temp->name);
  printf("\n\nID: %s",temp->ID);
}
 else printf("\nNO RECORD FOUND");  
temp=temp->next;

}
}







void main()
{
  node *start,*temp;
  int c;
  FILE *fp;                              //make a file pointer
   fp=fopen("student.txt","a"); 
  printf("\t\t\t\t\t\tANJUMAN-I-ISLAM'S\n");
  printf("\t\t\t\t\tKALSEKAR TECHNICAL CAMPUS, NEW PANVEL\n");
  printf("----------------------------------------------------------------------------------------------\n");
  printf("----------------------------------------------------------------------------------------------\n");
  printf("Enter first student data\n");
  printf("Name: ");
  scanf("%s",start->name);
fprintf(fp,"Name: %s\n",start->name);
  printf("\nID: ");
  scanf("%s",start->ID);
fprintf(fp,"ID: %s\n",start->ID);
fclose(fp);
  temp=start;
  temp->next=NULL;
do{
  printf("\n\n1.Add Student\n\n2.searchStudent\n\n4.exit");
  printf("\n\n\tENTER YOUR CHOICE: "); 
  scanf("%d",&c);
  switch(c)
  {
    case 1: AddStudent(start);           //calling addstudent function
            break;
    case 2: searchStudent(start);              //search a student by unique ID
            break;
    case 4: exit(0);
            break;
    default: printf("invalid option");
}
}while(1);
return 0;
}

   
   
   


