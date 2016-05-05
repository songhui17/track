# Macro


## what: macros allow us to record a sequence of change and then play them back.


## how: q{0-9a-zA-Z"}

e.g

_buffer_: 

foo = "foo:" + foo + "\n";
bar = "bar:" + bar + "\n";
foobar = "foobar:" + foobar + "\n";

_reg a_:

"a   byeA = "^[pa:" + ^[pa + "\n";^[

## note: when recoring a macro, ensure that every command is repeatable.

e.g

private bool _a;
public bool A{
    get{ return _a;}
    set{ _a = value;}
}
private int _bin;
public int Bin{
    get{ return _bin;}
    set{ _bin = value;}
}
private float _config;
public float Config{
    get{ return _config;}
    set{ _config = value;}
}


## execute macro in parallel: :normal @a

e.g

1) One
2) Two
// break up the monotony
3) Three
4) Four
