

def time_it_out(fnc):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        rez = fnc(*args, **kwargs)
        stop_time = time.perf_counter()
        print(f'Whole operation took: {round(stop_time-start_time, 2)} secods.')
        return rez
    return wrapper




