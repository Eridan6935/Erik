import math
import random
import matplotlib.pyplot as plt
import cmath

print("=" * 60)
print("УРОВЕНЬ 1: Конвертация между формами без модуля cmath")
print("=" * 60)


def to_polar(a, b):
    """
    Перевод из алгебраической формы (a, b) в полярную (r, phi).
    math.atan2(b, a) автоматически учитывает правильную четверть.
    """
    r = math.sqrt(a ** 2 + b ** 2)
    phi = math.atan2(b, a)
    return r, phi


def to_algebraic(r, phi):
    """
    Перевод из полярной формы (r, phi) в алгебраическую (a, b).
    """
    a = r * math.cos(phi)
    b = r * math.sin(phi)
    return a, b


# Проверка функции на тесте из методички
a_test, b_test = 3, -4
r_test, phi_test = to_polar(a_test, b_test)
a2_test, b2_test = to_algebraic(r_test, phi_test)
print(f"Тест (3, -4) -> Polar -> Alg: ({a2_test:.4f}, {b2_test:.4f})")

# Сверка с cmath на 5 случайных числах
print("\nСверка to_polar / to_algebraic c cmath:")
for i in range(5):
    a_rand = random.uniform(-10, 10)
    b_rand = random.uniform(-10, 10)

    # Наши функции
    r_custom, phi_custom = to_polar(a_rand, b_rand)

    # Стандартный cmath
    r_cmath, phi_cmath = cmath.polar(complex(a_rand, b_rand))

    print(f"№{i + 1}: Свои: (r={r_custom:.4f}, phi={phi_custom:.4f}) | "
          f"cmath: (r={r_cmath:.4f}, phi={phi_cmath:.4f})")

print("\n" + "=" * 60)
print("УРОВЕНЬ 2: Возведение в степень по формуле Муавра")
print("=" * 60)


def power_demoivre(a, b, n):
    """
    Возведение числа a + bi в степень n по формуле Муавра.
    Запрещено использовать cmath и оператор ** для комплексных чисел.
    """
    # 1. Переводим в полярные координаты
    r, phi = to_polar(a, b)

    # 2. Применяем формулу Муавра: r^n и угол n * phi
    r_n = r ** n
    phi_n = n * phi

    # 3. Переводим обратно в алгебраическую форму
    a_res, b_res = to_algebraic(r_n, phi_n)
    return a_res, b_res


# Проверка на 5 случайных значениях
for i in range(5):
    a_rnd = random.uniform(-5, 5)
    b_rnd = random.uniform(-5, 5)
    n_rnd = random.randint(1, 8)

    got = power_demoivre(a_rnd, b_rnd, n_rnd)
    expected_complex = complex(a_rnd, b_rnd) ** n_rnd
    expected = (expected_complex.real, expected_complex.imag)

    print(f"Тест {i + 1} (n={n_rnd}):")
    print(f"  Муавр:   ({got[0]:.4f}, {got[1]:.4f})")
    print(f"  Python **: ({expected[0]:.4f}, {expected[1]:.4f})")

print("\n" + "=" * 60)
print("УРОВЕНЬ 2: Отрисовка поворота 2D-объекта (корабля)")
print("=" * 60)

# Исправленные вершины корабля из задания для корректной замкнутой фигуры
ship = [(0, 1), (-0.6, -1), (0, -0.5), (0.6, -1)]


def rotate_shape(points, angle_deg):
    """
    Поворачивает список точек на угол angle_deg с помощью комплексных чисел.
    """
    rot = cmath.rect(1, math.radians(angle_deg))
    rotated_points = []
    for x, y in points:
        z = complex(x, y) * rot
        rotated_points.append((z.real, z.imag))
    return rotated_points


rotated_ship = rotate_shape(ship, 40)


def draw_shape(pts, color, label):
    # Замыкаем контур (соединяем последнюю точку с первой)
    closed_pts = pts + [pts[0]]
    xs, ys = zip(*closed_pts)
    plt.plot(xs, ys, color=color, marker='o', label=label)


plt.figure(figsize=(6, 6))
draw_shape(ship, 'gray', 'До поворота')
draw_shape(rotated_ship, 'purple', 'После поворота на 40°')
plt.gca().set_aspect('equal')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.title("Поворот 2D-объекта через комплексные числа")
plt.savefig("ship_rotation.png", dpi=120)
print("График корабля сохранен в файл 'ship_rotation.png'.")
plt.close()

print("\n" + "=" * 60)
print("BOSS-УРОВЕНЬ: Спирограф / Розетка")
print("=" * 60)


def spirograph(turns=8, points_per_turn=200, growth=0.02):
    """
    Генерация спирального узора с использованием формулы Муавра.
    """
    xs, ys = [], []
    total_points = turns * points_per_turn
    delta_phi = (2 * math.pi) / points_per_turn

    # Начальный модуль
    r0 = 1.0

    for k in range(total_points):
        # Рост радиуса и накопление угла
        r_k = r0 * ((1 + growth) ** k)
        phi_k = k * delta_phi

        # Формула Муавра для поворота и масштабирования
        x = r_k * math.cos(phi_k)
        y = r_k * math.sin(phi_k)

        xs.append(x)
        ys.append(y)

    return xs, ys


xs_spiro, ys_spiro = spirograph(turns=10, points_per_turn=150, growth=0.01)

plt.figure(figsize=(6, 6))
plt.plot(xs_spiro, ys_spiro, linewidth=0.8, color='indigo')
plt.axis('off')
plt.gca().set_aspect('equal')
plt.title("Спирограф (Формула Муавра)", fontsize=10)
plt.savefig("spirograph.png", dpi=150)
print("График спирографа сохранен в файл 'spirograph.png'.")
plt.close()

print("\nВсе задания выполнены успешно!")
print("\nВсе задания выполнены успешно!")
