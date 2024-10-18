# async comprehension

### sources : 
https://peps.python.org/pep-0530/
https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/
https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3

### notes

yield x ==> instead of storing everything in the memory , one element is stored at the time 
    // unless you store the generator as a list "l = list(gen())


-- returns a generator object that can be iterated over, function only runs when generator is being iterated

example :

    def fn():
        yield 1
        yield 2
        yield "loay"
        yield "abassi"

    generator = fn()
    for i in generator : 
        print(i)
        
        //will print each yielded value each time
    possible to use (next(gen())) // will start from scratch each call 
    create object first "gen = gen()" then loop through it 

when annotating a generator it should be "->Generator[type]