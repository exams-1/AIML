from sympy import symbols,Or,Not,Implies,satisfiable
Rain = symbols('Rain')
harry_visited_hagrid = symbols('harry_visited_hagrid')
harry_visited_dumbledore = symbols('harry_visited_dumbledore')
sentence_1 = Implies(Not(Rain),harry_visited_hagrid)
sentence_2 = Or(harry_visited_hagrid,harry_visited_dumbledore) & Not(harry_visited_hagrid & harry_visited_dumbledore)
sentence_3 = harry_visited_dumbledore
knowledge_base = sentence_1 & sentence_2 & sentence_3
solution=satisfiable(knowledge_base,all_models=True)
for model in solution:
    if model[Rain]:
        print("Rained")
    else:
        print("Not rained")
