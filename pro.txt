batsman(sachin).
batsman(saurav).
batsman(yuvraj).
bowler(nehra).
bowler(bumrah).
wicketkeeper(dhoni).
wicketkeeper(dravid).
cricketer(X):-batsman(X).
cricketer(Y):-bowler(Y).
cricketer(Z):-wicketkeeper(Z).


Testing in Prolog :press ; for next output
?- batsman(X).