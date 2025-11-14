predicates
        teacher(Symbol)
        imaginative(Symbol)
        not_imaginative(Symbol)
        good_students(Symbol)
        artist(Symbol)

clauses
        artist(john).
        good_students(mary).

        teacher(X) :- good_students(X).
        not_imaginative(X) :- good_students(X).
        imaginative(X) :- artist(X).
