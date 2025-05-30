# Python Fundamentals

## Table Of Contents

# Fundamentals of Concurrency

## 1. Concurrency vs Parallelism

- **Concurrency** is all about managing multiple tasks at the same time, not necessarily simultaneously. Tasks may take turns, creating the illusion of **multitasking**.
- **Parallelism** is about running multiple tasks simultaneously, typically by leveraging multiple CPU cores.

## 2. Programs

- A **program** is simply a static file, like a Python script or an executable.
- A **program** sits on disk, and is passive until the operating system (OS) loads it into memory to run. Once this happens, the program becomes a **process**.

## 3. Processes

- A **process** is an independent instance of a running **program**.
- A **process** has its own memory space, resources, and execution state. **Processes** are isolated from each other, meaning one process cannot interfere with another unless explicitly designed to do so via mechanisms like **inter-process communication** (**IPC**).

- **Processes** can generally be categorised into **two types**:

  1. **I/O-bound processes**: Spend most of it’s time waiting for input/output operations to complete, such as file access, network communication, or user input. While waiting, the CPU sits idle.
  2. **CPU-bound processes**: Spend most of their time doing computations (e.g video encoding, numerical analysis). These tasks require a lot of CPU time.

- **Lifecycle of a process**:
  1. A **process** starts in a new state when created.
  2. It moves to the **ready state**, waiting for CPU time.
  3. If the process waits for an event like I/O, it enters the **waiting** state.
  4. Finally, it **terminates** after completing its task.

## 4. Threads

- A **thread** is the smallest unit of execution within a **process**.
- A **process** acts as a “container” for **threads**, and multiple threads can be created and destroyed over the process’s lifetime.
- Every process has at least one **thread** — the **main thread** — but it can also create additional threads.
- **Threads** share memory and resources within the same **process**, enabling efficient communication. However, this sharing can lead to **synchronisation** issues like race conditions or deadlocks if not managed carefully. Unlike **processes**, multiple **threads** in a single **process** are not isolated — one misbehaving thread can crash the entire process.

## 5. How does the OS manage threads and processes?

- The CPU can execute **only one task per core at a time**. To handle multiple tasks, the operating system uses **preemptive context switching**.
- During a context switch, the OS pauses the current task, saves its state and loads the state of the next task to be executed.
- This rapid switching creates the illusion of simultaneous execution on a single CPU core.
- For **processes**, context switching is more resource-intensive because the OS must save and load separate memory spaces. For threads, switching is faster because threads share the same memory within a process. However, frequent switching introduces overhead, which can slow down performance.
- True parallel execution of processes can only occur if there are **multiple CPU cores** available. Each core handles a separate process simultaneously.

# Python’s Concurrency Models

- Python provides three main approaches to handle multiple tasks simultaneously:
  1. multithreading
  2. multiprocessing, and
  3. asyncio
- Without **concurrency**, a program processes only one task at a time. During operations like file loading, network requests, or user input, it stays idle, wasting valuable CPU cycles. **Concurrency** solves this by enabling multiple tasks to run efficiently.

## 1. Multithreading

- **Multithreading** allows a **process** to execute **multiple threads** concurrently, with threads sharing the same memory and resources
- However, Python’s **Global Interpreter Lock** (**GIL**) limits multithreading’s effectiveness for CPU-bound tasks.

- What is **Python’s Global Interpreter Lock** (**GIL)**?:

  - The GIL is a lock that allows only one thread to hold control of the Python interpreter at any time, meaning only one thread can execute Python bytecode at once.
  - The GIL was introduced to simplify memory management in Python as many internal operations, such as object creation, are not thread safe by default. Without a GIL, multiple threads trying to access the shared resources will require complex locks or synchronisation mechanisms to prevent race conditions and data corruption.

- When is **GIL** a bottleneck?

  - For **single threaded programs**, the GIL is irrelevant as the thread has exclusive access to the Python interpreter.
  - For **multithreaded I/O-bound programs**, the GIL is less problematic as threads release the GIL when waiting for I/O operations.
  - For **multithreaded CPU-bound operations**, the GIL becomes a significant bottleneck. Multiple threads competing for the GIL must take turns executing Python bytecode.

- **Remarks**:

  - An interesting case worth noting is the use of `time.sleep`, which Python effectively treats as an I/O operation. The `time.sleep` function is not CPU-bound because it does not involve active computation or the execution of Python bytecode during the sleep period. Instead, the responsibility of tracking the elapsed time is delegated to the OS. During this time, the thread releases the GIL, allowing other threads to run and utilise the interpreter.

- **When should I use Multithreading**:
  - Best for fast I/O-bound tasks as the frequency of context switching is reduced and the Python interpreter sticks to a single thread for longer
  - Not ideal for CPU-bound tasks due to GIL.

## 2. Multiprocessing

- **Multiprocessing** enables a system to run multiple processes in parallel, each with its own memory, GIL and resources. Within each process, there may be one or more threads
- **Multiprocessing** bypasses the limitations of the **GIL**. This makes it suitable for CPU bound tasks that require heavy computation.
- However, **multiprocessing** is more resource intensive due to separate memory and process overheads.

- **When should I use Multiprocessing**:
  - Best for CPU-bound tasks which are computationally intensive.
  - When you need to bypass the GIL — Each process has it’s own Python interpreter, allowing for true parallelism.

## 3. Asyncio

- Unlike **threads** or **processes**, **asyncio** uses a single thread to handle multiple tasks.
- When writing asynchronous code with the **asyncio** library, you'll use the `async/await` keywords to manage tasks.

- Key concepts include:

  1. **Coroutines**: These are functions defined with `async def`. They are the core of **asyncio** and represent tasks that can be paused and resumed later.
  2. **Event loop**: It manages the execution of tasks.
  3. **Tasks**: Wrappers around coroutines. When you want a coroutine to actually start running, you turn it into a task — eg. using `asyncio.create_task()`
  4. **await** : Pauses execution of a **coroutine**, giving control back to the event loop.

- **How Asynio Works**:

  - **Asyncio** runs an event loop that schedules tasks. Tasks voluntarily “pause” themselves when waiting for something, like a network response or a file read. While the task is paused, the event loop switches to another task, ensuring no time is wasted waiting.
  - This makes **asyncio** ideal for scenarios involving many small tasks that spend a lot of time waiting, such as handling thousands of web requests or managing database queries. Since everything runs on a single thread, **asyncio** avoids the overhead and complexity of thread switching.

- **Key Difference Between Asyncio and Multithreading**:

  - **Multithreading** relies on the OS to switch between threads when one thread is waiting (**preemptive context switching**). When a thread is waiting, the OS switches to another thread automatically.
  - **Asyncio** uses a single thread and depends on tasks to “cooperate” by pausing when they need to wait (**cooperative multitasking**).

- **When should I use Asyncio**:
  - Ideal for slow I/O-bound tasks such as long network requests or database queries because it efficiently handles waiting, making it scalable.
  - Not suitable for CPU-bound tasks without offloading work to other processes.

# Resources and Further Reading

1. [Medium - Deep Dive into Multithreading, Multiprocessing, and Asyncio](https://towardsdatascience.com/deep-dive-into-multithreading-multiprocessing-and-asyncio-94fdbe0c91f0)
