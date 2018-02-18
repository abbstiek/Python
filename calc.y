//  Abygail Stiekman  //
// COP4020 02/25/2017 // 
//		 aes15d		  //
%{
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  
  FILE *outfile;
  int yyline = 1; 
  int yycolumn = 1;
  char string_table[20000];
  extern int yyleng;
  extern char* yytext;
  
  //used from trans.y example//
  void print_header(void);
  void print_end(void);
  void yyerror(const char *str);
  int yywrap(void);
  void print_exp(const char *s);
  void error(const char * str);

  struct symbolTable{
	char name[10];
	int init;
	int decl;
	int value;
  };
  
  struct symbolTable table[20];
  
%}

%union {
  int sv;
  struct 
  {
	int v;
    char s[1000];
  } attr;
}

%token		VARnumber
%token		DIVnumber
%token		SEMInumber
%token		LPARENnumber
%token		MINUSnumber
%token		TIMESnumber
%token		COMMAnumber
%token		RPARENnumber
%token		PLUSnumber
%token		EQnumber
%token		EOFnumber
%token		<sv> ICONSTnumber                     
%token		PRINTnumber
%token		PROGRAMnumber
%token		ISnumber
%token		BEGINnumber
%token		ENDnumber
%token		<sv> IDnumber
%type <attr> factor
%type <attr> exp
%type <attr> term 
%type <attr> statement
%type <attr> id_list
%type <attr> statement_list
%type <attr> declaration



%% 

Program:	PROGRAMnumber IDnumber ISnumber compound
			{}
			;

compound:	BEGINnumber 
				{
					print_header();
				} 
			statement_list
			ENDnumber 
				{
					print_end();
				}
			;

statement:	IDnumber EQnumber exp 
				{
					int x = 0;	
					for(; x < 20; x++)
					{
						if((table[x].decl == 1) && (!strcmp(table[x].name, string_table + $1)))
						{
							table[x].value = $3.v;
							table[x].init = 1;
							break;
						}
					}
					if(x == 20)
					{
						error("Referencing an undeclared variable on line");
						return 0;
					}
					
					sprintf($$.s, "%s = %s;", table[x].name, $3.s);
				}			

			| PRINTnumber exp
			{
				print_exp($2.s);
				printf("%d\n", $2.v);
			}									
			| declaration
			{
				sprintf($$.s, "%s;", $1.s);
			}
			;
			
statement_list:	statement 
			{
				fprintf(outfile, "%s\n", $1.s);
			}
			| statement_list SEMInumber statement
			{
				fprintf(outfile, "%s\n", $3.s);	
			}
			;
			
declaration:	VARnumber id_list
			{
				sprintf($$.s, "int %s", $2.s); 	
			}
			;

id_list:	IDnumber 
			{
				$$.v = $1;
				
				int x = 0;
				for(; x < 20; x++)
				{
					if(!strcmp(table[x].name, string_table + $$.v))
					{
						error("Duplicate declaration on line");
						return 0;
					}
				}
				for(x = 0; x < 20; x++)
				{
					if(table[x].decl != 1)
					{
						strcpy(table[x].name, string_table + $$.v);
						table[x].decl = 1;
						break;
					}
				}
				sprintf($$.s, "%s", table[x].name);	
			}
			| id_list COMMAnumber IDnumber
			{
				$$.v = $3;
				
				int x = 0;
				for(; x < 20; x++)
				{
					if (!strcmp(table[x].name, string_table + $$.v))
					{
						error("Duplicate declaration on line");
					}
				}
				for(x = 0; x < 20; x++)
				{				
					if (table[x].decl == 0)
					{
						strcpy(table[x].name, string_table + $$.v);
						table[x].decl = 1;
						break;
					}
				}
				sprintf($$.s, "%s, %s", $1.s, table[x].name);
			};
			
exp:		exp PLUSnumber term
			{
				$$.v = $1.v + $3.v;
				sprintf($$.s, "%s + %s", $1.s, $3.s);
			}
			| exp MINUSnumber term
			{
				$$.v = $1.v - $3.v;
				sprintf($$.s, "%s - %s", $1.s, $3.s);
			}
			| MINUSnumber term	
			{
				$$.v = (-1) * $2.v;
				sprintf($$.s, "-%s", $2.s);				
			}			
			| term
			{
				$$.v = $1.v;
				sprintf($$.s, "%s", $1.s);
			};
			
term:		term TIMESnumber factor
			{
				$$.v = $1.v * $3.v;
				sprintf($$.s, "%s * %s", $1.s, $3.s);
			}
			| term DIVnumber factor
			{	
				if ($3.v == 0)
				{
					error("Dividing by zero on line");
					return 0;
				}
				else
				{
					$$.v = $1.v / $3.v;
					sprintf($$.s, "%s / %s", $1.s, $3.s);
				}	
			}
			| factor
			{
				$$.v = $1.v;
				sprintf($$.s, "%s", $1.s);
			}
			;

factor:		IDnumber 
			{
				$$.v = $1;
				
				int x = 0;
				for(; x < 20; x++)
				{			
					if ((table[x].decl == 1) && (!strcmp(table[x].name, string_table + $1)))
					{
						if(table[x].init == 0)
						{
							error("Referencing an uninitialized variable on line");
							return 0;
						}
						else
						{
							$$.v = table[x].value;
							break;
						}
					}
				}
				if(x == 20)
				{
					error("Referencing an undeclared variable on line");
					return 0;
				}
				
				sprintf($$.s, "%s", table[x].name);
			}
			| ICONSTnumber 
			{
				$$.v = $1;
				sprintf($$.s, "%d", $1);
			}
			| LPARENnumber exp RPARENnumber 
			{
				$$.v = $2.v;
				sprintf($$.s, "(%s)", $2.s);
			}
			;

%%

int main()
{
	if (!yyparse())
	{
		//printf("accept\n");
		return 0;
	}
	else 
	{
		//printf("reject\n");
		return 1;
	}
}    

int yywrap()
	{return 1;}
	
void print_exp(const char *s)
{fprintf(outfile, "cout << %s << endl;", s);}
void print_header()
{
	if ((outfile = fopen("mya.cpp", "w")) == NULL) {
		printf("Can't open file mya.cpp.\n");
		exit(0);
	}
	fprintf(outfile, "#include <iostream>\n");
	fprintf(outfile, "#include <stdio.h>\n");
	fprintf(outfile, "using namespace std;\n");
	fprintf(outfile, "\nint main()\n");
	fprintf(outfile, "{\n");
}

void print_end()
{
	fprintf(outfile, "}\n");
	fclose(outfile);
}
void error(const char * str)
{
	printf("%s %d.\n", str, yyline);
}
void yyerror(const char *str)
{    
	printf("line %d: %s\n", yyline , str);
}