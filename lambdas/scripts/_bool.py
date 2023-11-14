# Basics
IDENTITY = lambda boolean: boolean
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

# Logical operators
NOT = lambda boolean: boolean(FALSE)(TRUE)

OR = lambda x: lambda y: x(TRUE)(y)
NOR = lambda x: lambda y: NOT(x(TRUE)(y))

XOR = lambda x: lambda y: x(y(FALSE)(TRUE))(y(TRUE)(FALSE))
XNOR = lambda x: lambda y: NOT(XOR(x)(y))

AND = lambda x: lambda y: x(y)(FALSE)
NAND = lambda x: lambda y: NOT(x(y)(FALSE))

IMPLICATION = lambda x: lambda y: x(y(TRUE)(FALSE))(TRUE)
