import multiprocessing

class Runner:
    def run_parallel():
        PROCESSES = 4
        with multiprocessing.Pool(PROCESSES) as pool:
            params = [(1, ), (2, ), (3, ), (4, )]
            results = [pool.apply_async(double, p) for p in params]

            for r in results:
                print('\t', r.get())
