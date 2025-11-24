import math


def f(x):
    return math.exp(math.sin(3*x)+ x*x)


def nearest_nodes(x, x_grid):
    """Возвращает j, x_grid[j-1], x_grid[j], x_grid[j+1] - узлы близжайшие к x"""
    n = len(x_grid)
    j = min(range(n), key=lambda i: abs(x_grid[i] - x))
    
    if j == 0:
        j = 1
    elif j == n - 1:
        j = n-2
        
    return j, x_grid[j-1], x_grid[j], x_grid[j+1]


def gauss_interpolation(x0, x_grid, epsilon = 1e-6):
    """
    Вычисляет f(x0)  
    Подбирает шаг h до достижения точноси епсилон  
    """
    h = 0.1
    max_iterations = 20
    
    for iter in range(max_iterations):
        a,b = 0.0, 1.0
        n = int((b-a) / h) + 1
        x_grid = [a + i * h for i in range(n)]
        
        # Близжайщие узлы к x0
        j, x_prev, x_curr, x_next = nearest_nodes(x0,x_grid)

        # Значения функции
        y_prev = f(x_prev)
        y_curr = f(x_curr)
        y_next = f(x_next)
        
        # Конечные разности
        y1_half = y_next - y_curr
        y2_j = y_prev - 2*y_curr + y_next
        
        t = (x0 - x_curr) / h
        
        approx = y_curr + y1_half * t + y2_j * t * (t-1) / 2.0
        
        true_val = f(x0)
        error = abs(true_val - approx)
        
        # Оценка теоретической погрешности
        M3 = 100.0
        reminder_bound = M3 * (h**3) * abs(t * (t*t - 1)) / 6.0
        
        if error < epsilon:
            print(f"Точность: {epsilon}, при h = {h}")
            return approx, error, h, reminder_bound
        
        h /= 2.0
        
        if h < 1e-8:
            break
        

if __name__ == "__main__":
    x0 = 0.3
    epsilon = 1e-4
    
    result, err, final_h, reminder_bound = gauss_interpolation(x0, None, epsilon)
    print(f"Результат при x0 = {x0}: {result}")
    print(f"Практическая погрешность: {err}")
    print(f"Теоретическая погрешность погрешность: {reminder_bound}")
