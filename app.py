import argparse
import multiprocessing
import math
import sys
import psutil


def burn(stop_flag):
    while not stop_flag.value:
        # Break up the workload into smaller chunks and check the stop_flag frequently
        for _ in range(1000):  # Smaller loop to allow frequent flag checking
            if stop_flag.value:
                break
            _ = math.factorial(1000000)  # Perform smaller units of work



def consume_cpu(percent):
    stop_flag = multiprocessing.Value('b', False)
    num_cores = multiprocessing.cpu_count()
    processes = []

    num_processes = int((percent / 100.0) * num_cores)  # Multiply by 2 for hyper-threading

    for _ in range(num_processes):
        process = multiprocessing.Process(target=burn, args=(stop_flag,))
        process.start()
        processes.append(process)

    input("Press ENTER to stop CPU consumption...\n")
    stop_flag.value = True
    # Join processes to clean up
    for process in processes:
        process.join()


def consume_memory(percent):
    total_memory = psutil.virtual_memory().available
    consume_bytes = int((percent / 100.0) * total_memory)
    block_size = 1024 * 1024 * 10  # 10MB block, increase block size for faster allocation
    data = []

    try:
        while len(data) * block_size < consume_bytes:
            data.append(b' ' * block_size)
        input("Memory utilization complete. Press Enter to release memory.")
    except MemoryError:
        print("Memory consumption stopped due to system limit.")
    finally:
        data = []  # Clear memory


def main():
    parser = argparse.ArgumentParser(description="Ramp up CPU or Memory utilization.")
    parser.add_argument("type", choices=["CPU", "memory"], help="Specify CPU or memory to consume")
    parser.add_argument("percent", type=int, help="Percentage of CPU or memory to consume (0-100)")
    args = parser.parse_args()

    if args.percent < 0 or args.percent > 100:
        print("Percent must be between 0 and 100.")
        return

    if args.type == "CPU":
        print(f"Consuming {args.percent}% CPU...")
        consume_cpu(args.percent)
    elif args.type == "memory":
        print(f"Consuming {args.percent}% memory...")
        consume_memory(args.percent)


if __name__ == '__main__':
    # Safely set start method if it's not already set
    try:
        if sys.platform == "win32":
            multiprocessing.set_start_method('spawn', force=True)
        else:
            multiprocessing.set_start_method('fork', force=True)
    except RuntimeError:
        pass  # Start method has already been set, continue execution
    main()
