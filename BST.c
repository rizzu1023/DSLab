/*tree is non linear data structure
tree is a graph
tree is collection of virtises & edges
in tree there are no cycle
tree have one root(Parent) & many childrens(Branches)
the node which have no children called leaf
binary tree have atmost two children
operation- insertion, deletion, searching, tradition
traversing in tree-  inorder(infix a+b)     preorder(prefix  +ab)      postorder(postfix ab+)
Inorder     LDR (left data right)
preorder    DLR (data left right)
postorder   LRD (left right data)
deletion    i) The node has no child
*           ii) The node has 1 child
*           iii) The node has 2 child
*           iv)  The node has
*/

#include<stdio.h>
#include<stdlib.h>

typedef struct bst{
	int data;
	struct bst *left,*right;
}node;

void insert(node **r,int num){
     node *temp,*ptr;
     temp=*r;
     ptr=(node*)malloc(sizeof(node));
     ptr->data=num;
     ptr->left=NULL;
     ptr->right=NULL;
     if(temp==NULL)
		  *r=ptr;
	  else{
		   if(num<temp->data){
			   if(temp->right==NULL)
					temp->right=ptr;
				else
					insert(&temp->right,num);
		   }
		   else{
				  if(temp->left==NULL)
					temp->left=ptr;
				  else
					insert(&temp->left,num);
		  }
	}
}


void traverse_inorder(node *r){
	if(r!=NULL){		
	traverse_inorder(r->left);
	printf("%d\t",r->data);
	traverse_inorder(r->right);
        }
}
 
int search_bst(node *r,int num){
     
    if(r==NULL)
		  return 0;
	  else{
		  if(r->data==num)
		  return 1;
		  else{
		   if(num>r->data)
		      return search_bst(r->right,num);
		      else
		        return search_bst(r->left,num);
}
}
}                                                                        

 void search_node(int **x,node *root,node **parent,node **xsucc,int num,int *f){                                      //x is number to be deleted
 
 
 }
 
 void delete(node **r,int num){
          node *temp,*parent,*xsucc,*x;
          int f=0;
          *parent=NULL;x=NULL;
          temp=*r;
          search_node(x,temp,&parent,&xsucc,num,&f);
			if(f==0){
				 printf("\nThe element %d is not fount",x);
				 return;
			 }
			 if(x->left==NULL && x->right==NULL)
			 {
			 }
			 else if(x->left!=NULL)
			 {
			 }
			 else if(x->right!=NULL)
			 {
			 }
			 else if(x->left!=NULL && x->right!=NULL)
			 {
			 }
			 
				 
}
int main(){
	  node *root=NULL;
	  insert(&root,20);
	  insert(&root,10);
	  insert(&root,35);
      insert(&root,2);	  
	  insert(&root,12);
	  traverse_inorder(root);
	  if(search_bst(root,10)==1)
	   printf("\nThe number is found");
	   else
	    printf("\nThe number is not found");
	  return 0;
}
