import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

# For all printing methods from Sympy
sym.init_printing()


def show_example_number(index):
    print("\n".join(("\n********", f"Example {index}", "********\n")))


# %%
#
# Ex 1 : dy/dt = -5 y(t) with y(0) = 1
# Plot solution from 0 to 20 with a step of 0.4
#
show_example_number(1)

# Variables
t = sym.symbols("t")
y = sym.Function("y")

# Initial conditions
ics = {y(0): 1}

# Build equation
left_hand = sym.Derivative(y(t), t)
right_hand = -5 * y(t)
eq = sym.Eq(left_hand, right_hand)
print("Diff equation :", sym.pretty(eq), sep="\n")

# Solve equation dsolve(eq, func)
sol = sym.dsolve(eq, y(t), ics=ics)
print("\nSolution :", sym.pretty(sol), sep="\n")

# Lambdify : Transform into function, from string to numpy function
fun_y = sym.lambdify(t, sol.rhs, modules=["numpy"])

a = 0
b = 20
h = 0.4
t = np.arange(a, b + h, h)
y = fun_y(t)

# Plot(y, t)
plt.plot(t, y, color="b")
plt.xlim(a, b)
plt.show()


# %%
#
# Ex 2 : f'(x) = x + (f(x) / 5) with f(0) = -3
#
show_example_number(2)

x = sym.var("x")
f = sym.Function("f")

# Equation, then solving
eq2 = sym.Eq(sym.Derivative(f(x), x), x + f(x) / 5)
ics = {f(0): -3}
sol2 = sym.dsolve(eq2, f(x), ics=ics).rhs
print("Solution :", sym.pretty(sym.simplify(sol2)), sep="\n")


# %%
#
# Ex 3 : f'(x) - f(x) = 0 with f(0) = A
#
show_example_number(3)

# Variables and initial condition
f_3 = sym.Function("f_3")
x_3 = sym.var("x_3")
A = sym.var("A")
ics = {f_3(0): A}

# Not using sym.Eq, simply using an expression, assumed to be equal to 0
sol3 = sym.dsolve(f_3(x_3).diff(x_3) - f_3(x_3), f_3(x_3), ics=ics)

print("Solution :", sym.pretty(sol3), sep="\n")
