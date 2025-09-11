import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def logger(func):
    def wrapper(*args, **kwargs):
        print("Args: ", args)
        print("Kwargs: ", kwargs)
        logging.info(f"Running function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def log(name, *args):
    print(f"{name} has started: {args}")