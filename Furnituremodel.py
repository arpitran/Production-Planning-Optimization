from gurobipy import *

def solve(Products,steps,a,b,g,h,l,u,s,c):

    #Create a model
    m = Model("Production of furniture items")
    #make decision variables
    x={}
    for i in Products:
        x[i]=m.addVar(vtype=GRB.CONTINUOUS, name='x_%s' %i)

    
        m.update()
        
    # objective function
    m.setObjective(quicksum((s[i]-c[i])*x[i] for i in Products), GRB.MAXIMIZE)

    # ADD Constraints
    for j in steps:
        m.addConstr(quicksum(a[i,j]*x[i] for i in Products)<=b[j])
    for j in steps:
        m.addConstr(quicksum(g[i,j]*x[i] for i in Products)<=h[j])
    for i in Products:
        m.addConstr(x[i]<=u[i])
    for i in Products:
        m.addConstr(x[i]>=l[i])
    
    m.optimize()
    print("maximum profit: %g" %m.objVal)

    for i in products:
        print("Units of %s=%g" %(i,x[i].x))

                    
