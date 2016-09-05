#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main( int argc, char *argv[]){
       FILE *pf,*ps,*pc;
       char c;
       ps=fopen(argv[1],"r");
       pc=fopen("testo.txt","w");
       fscanf(ps,"%c",&c);
       while(!feof(ps)){
                        if(c=='<'){
                                   do{
                                   fscanf(ps,"%c",&c);
                                   }while(c!='>');
                        }
                        else{
                             fprintf(pc,"%c",c);}
                        fscanf(ps,"%c",&c);
       }
       fclose(pc);
       fclose(ps);
       pf=fopen("tag.txt","r");
       fscanf(pf,"%c",&c);
       while(!feof(pf)){
                        if(c=='>'){
                                 printf("%c\n",c);}
                        else{
                             printf("%c",c);}
                        fscanf(pf,"%c",&c);
       }  
       system("pause");       
	   return 0;
}
