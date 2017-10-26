#include<stdio.h>
#include<stdlib.h>
#include<string.h>


typedef struct student
{
  char name[30];
  char ID[10];
  struct student *next;
 }node;


void display(node *s)
{
  node *ptr;
	ptr=s;
	printf("\n");
	while(ptr!=NULL)
	{
		printf("\n%s",ptr->name);
          printf(" %s",ptr->ID);
		ptr=ptr->next;
	}
}


void AddStudent(node **s)
{
   node *temp,*ptr;
   ptr=(node*)malloc(sizeof(node));
   if(ptr==NULL)
   printf("Not enough memory");
   FILE *fp;                              //make a file pointer
 fp=fopen("student.txt","a");           //open file in append mode
   printf("\nEnter Name: ");
   scanf("\n\n%s",ptr->name);
 fprintf(fp,"Name: %s\n",ptr->name);
   printf("\nEnter ID: ");
   scanf("%s",ptr->ID);
 fprintf(fp,"ID: %s\n",ptr->ID); 
  ptr->next=NULL;
   
    temp=*s;
	if(temp==NULL)
		*s=ptr;
	else
	{
		while(temp->next!=NULL)
			temp=temp->next;
		temp->next=ptr;
	}
 fclose(fp);
   printf("\n\tRECORD IS SUCCESFULY ADDED :)\n\n");
   display(*s);
}


void searchStudent(node *s)
{
  int c,n=1;
  char src[20];
  node *temp;
  temp=s;
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

}}



int main()
{
  node *start,*temp;
  int c;
  printf("\t\t\t\t\t\tANJUMAN-I-ISLAM'S\n");
  printf("\t\t\t\t\tKALSEKAR TECHNICAL CAMPUS, NEW PANVEL\n");
  printf("----------------------------------------------------------------------------------------------\n");
  printf("----------------------------------------------------------------------------------------------\n");
start=NULL;
do{
  printf("\n\n1.Add Student\n\n2.Search Student\n\n3.exit");
  printf("\n\n\tENTER YOUR CHOICE: "); 
  scanf("%d",&c);
  switch(c)
  {
    case 1: AddStudent(&start);            //calling addstudent function
            break;
    case 2: searchStudent(start);
            break;
    case 3: exit(0);
            break;
    default: printf("invalid option");
}
}while(1);
return 0;
}

   
 

