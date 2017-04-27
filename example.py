import attentive

stopper = attentive.set_signal_handler()

with persistence_service, collect_j1939_task, collect_rs232_task:
    while not stopper.is_set():
        stopper.wait(1)