
/*Description:Implementation of Binary Search Tree
*Learner:Mohammed Rizwan
 * Roll no:16CO39
 */
#include<stdio.h>
#include<stdlib.h>

typedef struct bst
{
	int data;
	struct bst *left,*right;
}node;

void insert(node **r,int num)
{
	node *temp,*ptr;
	temp=*r;
	if(temp==NULL)
	{	
		ptr=(node*)malloc(sizeof(node));
		ptr->data=num;
		ptr->left=NULL;
		ptr->right=NULL;
		*r=ptr;
	}
	else
	{
		if(num > temp->data)
		{
				insert(&temp->right,num);
		}
		else
		{
			insert(&temp->left,num);
		}
	}
}

void traverse_inorder(node *q)
{
	if(q!=NULL)
	{
		traverse_inorder(q->left);
		printf("%d\t",q->data);
		traverse_inorder(q->right);
	}
}

int search_bst(node *q,int num)
{
	if(q==NULL)
		return 0;
	else
	{
		if(q->data==num)
			return 1;
		else
		{
			if(num>q->data)
			{	
				return search_bst(q->right,num);
				return search_bst(q->left,num);
			}
		}
	}
}

void search_node(node **x,node *root,node **parent,int num,int *f)
{
	node *temp;
	temp=root;
	if(temp==NULL)
		return;
	while(temp!=NULL)
	{
		if(temp->data==num)
		{
		*f=1;
		*x=temp;
		return;
		}
	*parent=temp;
	if(num>temp->data)
		temp=temp->right;
	else
		temp=temp->left;
	}
}

void delete(node **r,int num)
{
	node *temp,*parent,*xsucc,*x;
	int f=0;
	parent=NULL;x=NULL;xsucc=NULL;
	temp=*r;
	search_node(&x,temp,&parent,num,&f);
		if(f==0){
		printf("\nTHE ELEMENT %d IS NOT FOUND");
		return;
	}
	//x has no child
	if(x->left==NULL && x->right==NULL)
	{
		if(x->data > parent->data)
			parent->right=NULL;
		else
			parent->left=NULL;
	}
	//x has left child
	else if(x->left!=NULL && x->right==NULL)
	{
		if(x->data > parent->data)
			parent->right=x->left;
		else
			parent->left=x->left;
	}
	//x hAS right child
	else if(x->right!=NULL && x->left==NULL)
	{
		if(x->data > parent->data)
			parent->right=x->right;
		else
			parent->left=x->right;
	}
	//x has both left and right child
	else if(x->left!=NULL && x->right!=NULL)
	{
		parent=x;
		xsucc=x->right;
		while(xsucc->left!=NULL)
		{
			parent=xsucc;
			xsucc=xsucc->left;
		}
		if(xsucc->data > parent->data)
			parent->right=NULL;
		else
		{
			parent->left=NULL;
			x->data=xsucc->data;
			x=xsucc;
		}
	}free(x);
}




int main()
{
int ch,d;
struct bstree *p,*root=NULL;
while(1)
{
printf("\n\n\t\t\tMENU\n1. Insert.\n2. Inroder. \n3. PreOrder.\n4. PostOrder.\n5. Search.\n6. Exit.");
printf("\n\tEnter your choice :: ");
scanf("%d",&ch);
switch(ch)
{
case 1:
printf("\nEnter data :: ");
scanf("%d",&d);
root=insert(root,d);
break;
case 2:
printf("\n\tInorder Traversal.");
inorder(root);
break;
case 3:
printf("\n\tPre Order Traversal.");
preorder(root);
break;
case 4:
printf("\n\tPost Order Traversal.");
postorder(root);
break;
case 5:
printf("\nEnter data :: ");
scanf("%d",&d);
p=search(root,d);
if(p==NULL)
printf("\nGiven Key does not exist..");
else
printf("\nGiven Key does exist..");
break;

case 6:
exit(0);
break;
}
}
}
