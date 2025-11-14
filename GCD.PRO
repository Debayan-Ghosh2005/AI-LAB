domains
        num = integer

predicates
        gcd(num, num, num)
        gcd3(num, num, num, num)

clauses
        gcd(X, 0, X).
        gcd(X, Y, G) :-
                R = X mod Y,
                gcd(Y, R, G).

        gcd3(A, B, C, G) :-
                gcd(A, B, G1),
                gcd(G1, C, G).
