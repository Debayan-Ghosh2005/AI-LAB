predicates
    has_fever(symbol).
    has_rash(symbol).
    has_cough(symbol).
    has_conjunctivitis(symbol).
    has_runnynose(symbol).
    has_chill(symbol).
    has_headache(symbol).
    has_sorethroat(symbol).
    has_bodyache(symbol).

    measles(symbol).
    flu(symbol).
    chicken_pox(symbol).

clauses
    % Patient symptoms
    has_fever(bob).
    has_fever(joe).
    has_fever(jhon).
    has_fever(jill).

    has_rash(bob).
    has_rash(jhon).

    has_cough(joe).
    has_cough(jhon).
    has_cough(jill).

    has_conjunctivitis(joe).
    has_conjunctivitis(jhon).
    has_conjunctivitis(jill).

    has_runnynose(joe).
    has_runnynose(jhon).
    has_runnynose(jill).

    has_chill(bob).
    has_chill(joe).
    has_chill(jill).

    has_headache(joe).
    has_headache(jill).

    has_sorethroat(joe).
    has_sorethroat(jill).

    has_bodyache(bob).

    % ----------------------------------------------------
    % Disease Rules (exactly as your handwritten logic)
    % ----------------------------------------------------

    measles(X) :-
        has_fever(X),
        has_cough(X),
        has_conjunctivitis(X),
        has_runnynose(X),
        has_rash(X),
        write("Suffering from measles").

    chicken_pox(X) :-
        has_fever(X),
        has_rash(X),
        has_bodyache(X),
        has_chill(X),
        write("Suffering from chicken pox").

    flu(X) :-
        has_fever(X),
        has_headache(X),
        has_conjunctivitis(X),
        has_chill(X),
        has_sorethroat(X),
        write("Suffering from flu").
