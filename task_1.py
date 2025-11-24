import math
import matplotlib.pyplot as plt

def f(x):
    return math.exp(math.sin(3*x)+ x*x)


def linspace(a,b,n):
    """Возвращает n точек на промежутке [a,b]"""
    
    if n==1:
        return[a]
    
    step = (b - a) / (n - 1)
    return [a + i * step for i in range(n)]


def lagrange_interpolate(x_eval_list, x_nodes, y_nodes):
    """
    x_eval_list - массив точек  
    x_nodes - узлы интерполяции (n+1 массив)  
    y_nodes - значения f(x) в узлах (n+1 массив)  
    Возвращает список значений Ln(x)
    """
    
    n = len(x_nodes)
    result = []
    
    for x in x_eval_list:
        total = 0.0
        for i in range(n):
            num = 1.0
            den = 1.0
            for j in range(n):
                if i != j:
                    num *= (x - x_nodes[j])
                    den *= (x_nodes[i] - x_nodes[j])
            
            if den == 0:
                li = 0.0
            else:
                li = num / den
            total += y_nodes[i] * li
        result.append(total)    
    return result


def abs_list(list):
    """Абсолютное значение"""
    return [abs(x) for x in list]


def max_list(list):
    """Максимальное значение"""
    return max(list)


def factorial(n):
    """Факториал"""
    if n < 0:
        raise ValueError("Нельзя вычислить факториал отр. числа")
    
    result = 1
    for i in range(2,n + 1):
        result *= i
    return result


def omega_at(x, x_nodes):
    prod = 1.0
    for xi in x_nodes:
        prod *= (x - xi)
    return prod


def omega_list(x_list, x_nodes):
    """Вычисление omega(x)"""
    return [omega_at(x, x_nodes) for x in x_list]


def main():
    a,b = 0.0, 1.0
    n_degree = 10
    n_nodes = n_degree + 1
    
    x_nodes = linspace(a, b, n_nodes)
    y_nodes = [f(x) for x in x_nodes]
    
    n_fine = 100
    x_fine = linspace(a, b, n_fine)
    f_true = [f(x) for x in x_fine]
    
    # Интерполянт
    f_interpolate = lagrange_interpolate(x_fine, x_nodes, y_nodes)
    
    # Практическая погрешность
    errors = [abs(f_true[i] - f_interpolate[i]) for i in range(len(x_fine))]
    eps_practical = max_list(errors)
    
    # Оценка omega(x)
    omega_vals = abs_list(omega_list(x_fine,x_nodes))
    max_omega = max(omega_vals)
    
    # Теоретическая погрешность
    M11 = 1e5
    factorial_11 = factorial(11)
    eps_theoretical = (M11 / factorial_11) * max_omega
    
    print(f"Практическая погрешность: {eps_practical}")
    print(f"Теоретическя погрешность: {eps_theoretical}")
    
    plt.figure(figsize=(12, 5))

    # График функции и интерполянта
    plt.subplot(1, 2, 1)
    plt.plot(x_fine, f_true, 'b-', label='f(x)')
    plt.plot(x_fine, f_interpolate, 'r--', label='L₁₀(x)')
    plt.plot(x_nodes, y_nodes, 'ko', label='Узлы')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Интерполяция (n=10, [0,1])')
    plt.legend()
    plt.grid(True)

    # График погрешности
    plt.subplot(1, 2, 2)
    plt.plot(x_fine, errors, 'm-')
    plt.yscale('log')
    plt.xlabel('x')
    plt.ylabel('|f(x) - L₁₀(x)|')
    plt.title('Погрешность (лог. шкала)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()
    
