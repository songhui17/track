maxims for programmers

Be specific:
Using the mose specific form possible, e.g. when VS if

Use abstraction

Be concise

Use the provided tools

Don't be obscure

Be consistent


Special Forms

defintions: defun defstruct defvar defconstant defmacro labels

conditional: and case cond if or unless when

variable: let let* pop push seft incf decf

iteration: do do* dolist dotimes loop

other: delcare function progn quote return trace untrace


functions && macros:

(defun function-name (paramter...) "optional documentation" body...)
(defmacro macro-name (paramter...) "optional documentation" body...)

variables

(defvar variable-name initial-value "optional documentation")
(defparameter variable-name value "optional documentation")
(defconstant variable-name value "optional documentaion")

redef of constant cause error

structure

(defstruct structure-name "optional documentation" slot...)

(defstruct name
 first
 (middle nil)
 last)

(make-name :first 'hui :last 'song)
(name-first b)
(name-middle b)
(name-last b)
(setf (name-middle b) 'ex)
b => #S(NAME :FIRST HUI :MIDDLE EX :LAST SONG)

conditionals

(cond (test result...)
      (test result...)
      ...)

last cond-clause: (t result)

(case x      =>    (cond ((eql x 1) 10) ((eql x 2) 1))
 (1 10)
 (2 20))

(ecase x     =>    (cond (...) (t (error "no valid case")))
 (1 10)
 (2 20))

(typecase x           => (cond ((typep x 'number) (abs x)) ((typep x 'list) (length x)))
 (number (abs x))
 (list (length x))


(let ((variable value)...)
 body..)

(let ((x 40)
      (y (+1 1 1)))
 (+x x y)) => 42


((lambda (variable...)
    body...)
 value...)


((lambda (x y)
  (+ x y))
  0 ;x
  (+ 1 1) ;y
)

(let* ((x 6)
       (y (* x x)))
 (+ x y)) => 42

((lambda (x)
 (+ x ((lambda (x2) (* x2 x2)) x)))
 6)

Same to use x instead of x2
