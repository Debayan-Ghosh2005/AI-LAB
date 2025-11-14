predicates
    parent(symbol, symbol).
    granddaughter(symbol, symbol).
    brother(symbol, symbol).
    aunt(symbol, symbol).
    male(symbol).
    female(symbol).
clauses
    parent(raju, rai).
    parent(raju, rana).
    parent(radha, rai).
    parent(radha, rana).
    parent(adhir, romi).
    parent(rai, romi).
    parent(rana, ranadhir).
    parent(rana, rabi).
    parent(ruma, ranadhire).
    parent(rabi, ratul).
    parent(rekha, ratul).

    male(raju).
    male(adhir).
    male(rana).
    male(ranadhir).
    male(rabi).

    female(radha).
    female(rai).
    female(ruma).
    female(romi).
    female(rekha).

    granddaughter(X, Y) :- female(X), parent(Y, Z), parent(Z, X).

    brother(X, Y) :- male(X), parent(Z, X), parent(Z, Y), X<> Y.

    aunt(P, R) :- parent(X, P), parent(Y, P), parent(X, Q), parent(Y, Q), parent(Q, R), female(P), male(X), female(Y), male(Q).
