Predicates
	like(Symbol, Symbol).
	programmer(Symbol).
	web(Symbol).
	dbs(Symbol).
Clauses
	like(akhilesh, math).
	like(awirobson, math).
	like(akhilesh, algo).
	like(awirobson, algo).
	like(awirobson, java).
	like(manab, java).
	like(manab, english).
	like(akhilesh, english).
	like(manab, sql).
	like(manab, js).
	like(manab, html).
	like(akhilesh, sql).

	programmer(X) :-
    			like(X, math),
    			like(X, c),
    			like(X, algo),
    			like(X, java).

	web(X) :-
    		like(X, dancing),
    		like(X, java),
    		like(X, html),
    		like(X, js),
    		like(X, sql),
    		like(X, english).

	dbs(X) :-
    		like(X, math),
    		like(X, sql),
    		like(X, algo),
    		like(X, english).
