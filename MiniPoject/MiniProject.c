/*Description:Student information System
*Learner:Mohammed Rizwan 16co39
         Mohammed Atay madina 16co36
         Mohammed Husain 16co37
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>


typedef struct student
{
  char name[30];
  char ID[10];
  char gender[10];
  char mail[40];
  char cl[10];
  char department[10];
  char mobile[13];
  struct student *next;
 }node;


void display(node *s)
{
  node *ptr;
	ptr=s;
	printf("\n");
	while(ptr!=NULL)
	{
        printf("\n%s",ptr->ID);
		printf("\t%s",ptr->name);
        printf("\t%s",ptr->gender);
        printf("\t%s",ptr->mail);
        printf("\t%s",ptr->mobile);
        printf("\t%s",ptr->department);
        printf("\t%s",ptr->cl);
		ptr=ptr->next;
	}
}


int displayall(node *s)
{

    FILE *fp;
    node *temp;
    char ch;
    {

        fp=fopen("Student.txt","r");
        ch=fgetc(fp);
        if(ch==EOF)
        {
            printf("\nNO RECORD FOUND");
            return 0;
        }
        printf("\n\nRECORDS AVAILABLE\n");
        while(ch!=EOF)
        {

            printf("%c",ch);
            ch=fgetc(fp);
            }
            fclose(fp);
        }
return 1;
        }


void AddStudent(node **s)
{
   node *temp,*ptr;
   ptr=(node*)malloc(sizeof(node));
   if(ptr==NULL)
   printf("Not enough memory");
   FILE *fp;
   fp=fopen("Student.txt","a");
   printf("\n\nEnter ID: ");
   scanf("%s",ptr->ID);
 fprintf(fp,"ID: %s\n",ptr->ID);
   printf("\nEnter Name: ");
   scanf("%s",ptr->name);
 fprintf(fp,"Name: %s\n",ptr->name);
   printf("\nEnter Gender: ");
   scanf("%s",ptr->gender);
 fprintf(fp,"Gender: %s\n",ptr->gender);
   printf("\nEnter Email Address: ");
   scanf("%s",ptr->mail);
 fprintf(fp,"Email: %s\n",ptr->mail);
   printf("\nEnter Mobile Number: ");
   scanf("%s",ptr->mobile);
 fprintf(fp,"Mobile Number: %s\n",ptr->mobile);
   printf("\nEnter Department: ");
   scanf("%s",ptr->department);
 fprintf(fp,"Department: %s\n",ptr->department);
   printf("\nEnter Class: ");
   scanf("\n\n%s",ptr->cl);
 fprintf(fp,"Class: %s\n",ptr->cl);
 fprintf(fp,"\n");
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
  int c,n=0;
  char src[10];
  node *temp;
  temp=s;
printf("\n\nEnter student ID: ");
  scanf("%s",src);
while(temp!=NULL)
{
  c=strcmp(src,temp->ID);
  if(c==0)
{
  n=1;
  printf("\nID: %s",temp->ID);
  printf("\nName: %s",temp->name);
  printf("\nGender: %s",temp->gender);
  printf("\nEmail Address: %s",temp->mail);
  printf("\nMobile Number: %s",temp->mobile);
  printf("\nDepartment: %s",temp->department);
  printf("\nCLass: %s",temp->cl);

}
 temp=temp->next;
}
  if(n==0)
  printf("\nNO RECORD FOUND");
}

void extra(node *h)
{
    FILE *fp3;
    node *amp;
    amp=h;
    fp3=fopen("Student.txt","w");
    while(amp!=NULL)
    {
        fprintf(fp3,"\nID: %s\n",amp->ID);
        fprintf(fp3,"Name: %s\n",amp->name);
        fprintf(fp3,"Gender: %s\n",amp->gender);
        fprintf(fp3,"Email: %s\n",amp->mail);
        fprintf(fp3,"Mobile Number: %s\n",amp->mobile);
        fprintf(fp3,"Department: %s\n",amp->department);
        fprintf(fp3,"Class: %s\n",amp->cl);
        fprintf(fp3,"\n");
        amp=amp->next;
    }
    fclose(fp3);
    printf("\n\tRECORD IS SUCCESFULY DELETED  :)");

}

void delStudent(node **s)
{
	int n=0,c;
     char src[10];
	node *prev,*temp,*cmp;
	temp=*s;
	cmp=*s;
     printf("\n\nEnter Student ID: ");
     scanf("%s",src);

	while(temp!=NULL)
	{
		  c=strcmp(temp->ID,src);
            if(c==0)
		{
			n=1;
			if(temp==*s)
				*s=temp->next;
			else
				prev->next=temp->next;
			free(temp);
			break;
		}
		else
		{
			prev=temp;
			temp=temp->next;
		}
	}

	if(n==0)
		printf("\nNO RECORD FOUND\n");
    display(*s);

    FILE *fp1;
    char ch;
    fp1 = fopen("Student.txt", "r");
    ch = getc(fp1);
    while (ch != EOF){
    ch = getc(fp1);
 }

    rewind(fp1);



        fclose(fp1);
        remove("Student.txt");
        extra(cmp);

}






int main()
{
  node *start;
  int c;
  printf("\t\t\t\t\tANJUMAN-I-ISLAM'S\n");
  printf("\t\t\t\tKALSEKAR TECHNICAL CAMPUS, NEW PANVEL\n");
 start=NULL;
do{
  printf("\n====================================================================================");
  printf("\n\n1.Add Student\n\n2.Search Student\n\n3.Delete Student\n\n4.Display All Records\n\n5.exit");
  printf("\n====================================================================================");
  printf("\n\n\tENTER YOUR CHOICE: ");
  scanf("%d",&c);
  switch(c)
  {
    case 1: AddStudent(&start);
            break;
    case 2: searchStudent(start);
            break;
    case 3: delStudent(&start);
            break;
    case 4: displayall(start);
            break;
    case 5: exit(0);
            break;
    default: printf("invalid option");
}
}while(1);
return 0;
}



