from ._bool import NOT, TRUE, XNOR, XOR
from ._natural import ADD, DIFF, LTE, MUL
from ._pair import CAR, CDR, CONS

# signed numbers
SIGN = lambda n: CONS(TRUE)(n)
NEG = lambda p: CONS(NOT(CAR(p)))(CDR(p))
ISPOS = lambda p: CAR(p)
ISNEG = lambda p: NOT(CAR(p))
UNSIGN = lambda p: CDR(p)
SADD = lambda a: lambda b: (
    XNOR(CAR(a))(CAR(b))(CONS(CAR(a))(ADD(CDR(a))(CDR(b))))(  # same sign
        CONS(XOR(CAR(a))(LTE(CDR(a))(CDR(b))))(  # opposite sign  # calculate sign
            DIFF(CDR(a))(CDR(b))
        )  # calculate value
    )
)
SSUB = lambda a: lambda b: SADD(a)(CONS(NOT(CAR(b)))(CDR(b)))
SMUL = lambda a: lambda b: CONS(XNOR(CAR(a))(CAR(b)))(MUL(CDR(a))(CDR(b)))
