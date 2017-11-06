__author__ = 'Me and myself'

import multiprocessing as mp
import time


def the_job(args):
    """The job for multiprocessing.

    Prints some stuff secured by a lock and 
    finally puts the input into a queue.

    """
    idx = args[0]
    lock = args[1]
    queue = args[2]

    lock.acquire()
    print 'I'
    print 'was '
    print 'here '
    print '!!!!'
    print '1111'
    print 'einhundertelfzigelf\n'
    who = ' By run %d \n' % idx
    print who
    lock.release()

    queue.put(idx)


def read_queue(queue):
    """Turns a qeue into a normal python list."""
    results = []
    while not queue.empty():
        result = queue.get()
        results.append(result)
    return results


def make_iterator(args, lock, queue):
    """Makes an iterator over args and passes the lock an queue to each element."""
    return ((arg, lock, queue) for arg in args)


def start_scenario(scenario_number=1):
    """Starts one of four multiprocessing scenarios.

    :param scenario_number: Index of scenario, 1 to 4

    """
    args = range(10)
    ncores = 3
    if scenario_number == 1:
        result = scenario_1_pool_no_manager(the_job, args, ncores)

    elif scenario_number == 2:
        result = scenario_2_pool_manager(the_job, args, ncores)

    elif scenario_number == 3:
        result = scenario_3_single_processes_no_manager(the_job, args, ncores)

    elif scenario_number == 4:
        result = scenario_4_single_processes_manager(the_job, args, ncores)

    if result != args:
        print 'Scenario %d fails: %s != %s' % (scenario_number, args, result)
    else:
        print 'Scenario %d successful!' % scenario_number


def scenario_1_pool_no_manager(jobfunc, args, ncores):
    """Runs a pool of processes WITHOUT a Manager for the lock and queue.

    FAILS!

    """
    mypool = mp.Pool(ncores)
    lock = mp.Lock()
    queue = mp.Queue()

    iterator = make_iterator(args, lock, queue)

    mypool.map(jobfunc, iterator)

    mypool.close()
    mypool.join()

    return read_queue(queue)


def scenario_2_pool_manager(jobfunc, args, ncores):
    """Runs a pool of processes WITH a Manager for the lock and queue.

    SUCCESSFUL!

    """
    mypool = mp.Pool(ncores)
    lock = mp.Manager().Lock()
    queue = mp.Manager().Queue()

    iterator = make_iterator(args, lock, queue)
    mypool.map(jobfunc, iterator)
    mypool.close()
    mypool.join()

    return read_queue(queue)


def scenario_3_single_processes_no_manager(jobfunc, args, ncores):
    """Runs an individual process for every task WITHOUT a Manager,

    SUCCESSFUL!

    """
    lock = mp.Lock()
    queue = mp.Queue()

    # iterator = make_iterator(args, lock, queue)
    iterator = ((arg, lock, queue) for arg in args)

    do_job_single_processes(jobfunc, iterator, ncores)

    return read_queue(queue)


def scenario_4_single_processes_manager(jobfunc, args, ncores):
    """Runs an individual process for every task WITH a Manager,

    SUCCESSFUL!

    """
    lock = mp.Manager().Lock()
    queue = mp.Manager().Queue()

    iterator = make_iterator(args, lock, queue)

    do_job_single_processes(jobfunc, iterator, ncores)

    return read_queue(queue)


def do_job_single_processes(jobfunc, iterator, ncores):
    """Runs a job function by starting individual processes for every task.

    At most `ncores` processes operate at the same time

    :param jobfunc: Job to do

    :param iterator:

        Iterator over different parameter settings,
        contains a lock and a queue

    :param ncores:

        Number of processes operating at the same time

    """
    keep_running = True
    process_dict = {}  # Dict containing all subprocees

    while len(process_dict)>0 or keep_running:

        terminated_procs_pids = []
        # First check if some processes did finish their job
        for pid, proc in process_dict.iteritems():

            # Remember the terminated processes
            if not proc.is_alive():
                terminated_procs_pids.append(pid)

        # And delete these from the process dict
        for terminated_proc in terminated_procs_pids:
            process_dict.pop(terminated_proc)

        # If we have less active processes than ncores and there is still
        # a job to do, add another process
        if len(process_dict) < ncores and keep_running:
            try:
                # task = iterator.next()
                task = next(iterator)
                proc = mp.Process(target=jobfunc,
                                  args=(task,))
                proc.start()
                process_dict[proc.pid] = proc
            except StopIteration:
                # All tasks have been started
                keep_running = False

        time.sleep(0.1)


def main():
    """Runs 1 out of 4 different multiprocessing scenarios"""
    start_scenario(3)


if __name__ == '__main__':
    main()
