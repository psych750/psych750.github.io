# TODO


[ ] https://bookdown.org/yihui/rmarkdown-cookbook/working-directory.html  and use of here; opening Rmd vs. Proj
[ ] Useful R patterns:
    [ ] %in% and negation (e.g., choosing which columns NOT to select)
    [ ] summarize_if
    [ ] if_else/case_when
    [ ] coalesce - the thing that gives you the non-na value of a set of columns
    [ ] here
    [ ] rowwse and across
    [ ] sjmisc:: rec, dicho, recode_to, split_var (what's group_var?)
    [ ] grepl string matching --> regexps

[o] CHallenge exercise: max(set(a),key=a.count) to find mode. Have students explain why it works. 

[ ] Add recursive fibonacci to function notebook?
    - efficient one line- fib = lambda n,a=0,b=1: a if n<=0 else fib(n-1,b,a+b)
    - fib = lambda n,x=(0,1):[x := (x[1], sum(x)) for i in range(n+1)][-1][0]

