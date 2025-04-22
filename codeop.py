def algebraic_simplification(expressions):
    simplified_exp=[]
    for expr in expressions:
        if "* 1" in expr:
            expr = expr.replace('* 1','')
        if "+ 0" in expr:
            expr = expr.replace('+ 0','')
        if "0 +" in expr:
            expr = expr.replace('0 +','')
        simplified_exp.append(expr)
    return simplified_exp

def common_subexpression_elimination(expression):
    sub_expr={}
    optimized_code =[]
    common_expression=[]
    
    for expr in expression:
        expr=expr.replace(" ","")
        if "=" in expr:
            var, rhs =expr.split("=",1)
            if rhs in sub_expr:
                optimized_code.append(f"{var}={sub_expr[rhs]}")  
            else:
                optimized_code.append(expr)
                sub_expr[rhs]=var
                
        else:
            optimized_code.append(expr)
    return(optimized_code)

def get_exp():
    exp=[]
    while True:
        i=input('->')
        if i=="" or i=="/n":
            break
        else:
            exp.append(i)
            
    return(exp) 

expressions=get_exp()
print("1 Algebric\n2 Common")
choice = input("Choose:")
if choice=="1":
    optimized_expressions=algebraic_simplification(expressions)
    print("\n Simplified code:")
    for line in optimized_expressions:
        print(line)
        
elif choice=="2":
    optimized_expressions=common_subexpression_elimination(expression)
    print("\n expression after elimination:")
    for line in expressions:
        print(line)
else:
    print("Invalid choice")