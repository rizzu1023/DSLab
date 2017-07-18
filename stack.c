#include<stdio.h>
#include<stdlib.h>
#define MAX_SIZE 10
er
int stack[MAX_SIZE],top=-1;

int isFull(){
	//returns 1 if stack is full else returns -1
	return (top==MAX_SIZE-1)?1:-1;
} 

int isEmpty(){
//returns 1 if stack is empty else returns -1
    return (top==-1)?1:-1;
}

int peek(){
//return element at the top of stack
}

void push(int e){
//inserts an element into stack
	if(top<MAX_SIZE)
	{
        top=top+1;
        stack[top]=e;
        printf("element e is succesfully inserted");
		//increment the top
		//set top of stack equal e
		//msg element e successfully inserted
	}
	else{
        printf("stack is overflow");
		//msg stack overflow
	}
}

void pop(){
//deletes an element from top of stack
	int d;
	if(top>-1)
	{
        d=stack[top];
        top=top-1;
        printf("element d is successfully deleted");
		//d=top of stack
		//decrement the top
		//msg element d successfully deleted
	}
	else{
         printf("stack is underflow");
		//msg stack underflow
	}
}

int main(){
	int choice,e;
	do
	{
        printf("\n1.peek\n2.push.\n3.pop\n4.exit\n");
		//display menu 1.peek 2.push 3.pop 4.exit
		printf("enter your choice");
        scanf("%d",&choice);
		//take input in choice variable
		switch(choice){
			case 1:
				//call peek function
				break;
			case 2:
                push(e);
				//call push function
				break;
			case 3:
                pop(e);
				//call pop function
				break;
			case 4:
				//call exit(0) function or return 0
				break;
			default:
                printf("invalid choice");
				//invalid choice				
		}
	}while(1);
	return 0;
}
