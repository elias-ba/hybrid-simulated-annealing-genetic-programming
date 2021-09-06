from simulation import simulation

if __name__ == "__main__":

    results = simulation()

    sum_py_sur_rendements = sum(y/r for (_, y), _, r in results)
    message = f"La somme des Py/r est de: {sum_py_sur_rendements}"
    print("-"*len(message))
    print()
    print(message)
    print()
    print("-"*len(message))

    import matplotlib.pyplot as plt
    plt.plot(list(range(len(results))), [x for (x, _), _, _ in results], c='b')
    plt.plot(list(range(len(results))), [y for (_, y), _, _ in results], c='r')
    plt.plot(list(range(len(results))), [x + y for (x, y), _, _ in results], c='y')
    plt.plot(list(range(len(results))), [PD for (_, _), PD, _ in results], c='g')

    plt.show()