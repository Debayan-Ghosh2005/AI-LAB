predicates
	fruit(Symbol)
	cooked(Symbol)
	tasty(Symbol)

clauses
	fruit(apple).
	fruit(mango).
	cooked(apple).

	tasty(X) :- fruit(X), not(cooked(X)).
