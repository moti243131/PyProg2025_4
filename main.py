"""Лабораторная работа 4: сравнение рекурсивной и итеративной реализации факториала.
"""

import timeit
from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt


def fact_recursive(n: int) -> int:
    """Вычисляет факториал рекурсивным способом.

    Args:
        n: Неотрицательное целое число.

    Returns:
        Значение n! (n факториал).

    Raises:
        ValueError: Если n < 0.
    """
    if n < 0:
        raise ValueError("Факториал определён только для n >= 0")
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)


def fact_iterative(n: int) -> int:
    """Вычисляет факториал итеративным способом (через цикл).

    Args:
        n: Неотрицательное целое число.

    Returns:
        Значение n! (n факториал).

    Raises:
        ValueError: Если n < 0.
    """
    if n < 0:
        raise ValueError("Факториал определён только для n >= 0")
    result: int = 1
    for i in range(1, n + 1):
        result *= i
    return result


def run_benchmark(
    func: Callable[[int], int],
    n: int,
    repeat: int = 5,
    number: int = 1000,
) -> float:
    """Замеряет среднее время выполнения функции для заданного n.

    Args:
        func: Функция факториала (fact_recursive или fact_iterative).
        n: Аргумент для функции.
        repeat: Количество серий прогонов.
        number: Количество вызовов в одной серии.

    Returns:
        Минимальное время из серии (в секундах).
    """
    times = timeit.repeat(lambda: func(n), repeat=repeat, number=number)
    return min(times)


def run_clean_benchmark(n: int = 50) -> None:
    """Проводит чистый бенчмарк одного вызова для заданного числа.

    Args:
        n: Число для тестирования (по умолчанию 50).
    """
    t_rec = timeit.timeit(lambda: fact_recursive(n), number=1)
    t_iter = timeit.timeit(lambda: fact_iterative(n), number=1)
    print(f"Чистый бенчмарк (один вызов для n={n}):")
    print(f"  Рекурсивный:  {t_rec:.2e} с")
    print(f"  Итеративный: {t_iter:.2e} с")


def main() -> None:
    """Основная функция: бенчмарк и визуализация."""
    # Один фиксированный список чисел для всех прогонов
    test_data: list[int] = list(range(10, 151, 10))

    times_recursive: list[float] = []
    times_iterative: list[float] = []

    for n in test_data:
        times_recursive.append(
            run_benchmark(fact_recursive, n, repeat=5, number=1000)
        )
        times_iterative.append(
            run_benchmark(fact_iterative, n, repeat=5, number=1000)
        )

    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.plot(test_data, times_recursive, "o-", label="Рекурсивный")
    plt.plot(test_data, times_iterative, "s-", label="Итеративный")
    plt.xlabel("n (размер входного числа)")
    plt.ylabel("Время вычислений (с)")
    plt.title("Сравнение рекурсивной и итеративной реализации факториала")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    save_path = Path(__file__).parent / "benchmark_factorial.png"
    plt.savefig(save_path, dpi=150)
    plt.show()

    # Чистый бенчмарк одного вызова
    run_clean_benchmark(n=50)


if __name__ == "__main__":
    main()
