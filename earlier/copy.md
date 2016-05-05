# yank, delete and paste

### use cases

1.   transposing characters: xp
2.   transposing lines: ddp

## yank && replace

### bg: yank && replace

### cf: dont work at all

### why:

1.   y && p write text to the unnamed register
2.   p paste context in the unamed register

### how:

_register_:

1.   unamed register: ""
2.   yank register: "0
3.   named register: "a-"z
4.   black hole regsiter: "_

_methods_:

1.   replace visual selection witg register: convinient 
2.   paste from register
