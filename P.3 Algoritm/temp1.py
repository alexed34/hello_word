from datetime import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        with open('func_time_logs.txt', 'a+') as file:
            file.write(f"Время выполнения {func.__name__} {end - start}\n")

        return res

    return wrapper

