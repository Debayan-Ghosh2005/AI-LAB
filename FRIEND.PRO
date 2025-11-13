PREDICATES
	male(symbol)
	female(symbol)
	friend(symbol,symbol)
	ffriend(symbol,symbol)
clauses
	male(aritra).
	male(sangram).
	
	female(sonali).
	female(banalikha). 
	female(kajal).
	
	friend(sangram, aritra).
	friend(sangram, kajal).
	friend(aritra, sonali).
	friend(sonali, banalikha).
	friend(banalikha, sonali).
	friend(banalikha, sangram).
	friend(kajal,aritra).
	ffriend(X, Y) :- friend(X, Y),female(X).
	
	