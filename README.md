# CPU_Scheduling
## Description
A Python program that simulates four fundamental CPU scheduling algorithms used in operating systems. The simulator provides comparative analysis of different scheduling approaches with performance metrics.

## Features
- Interactive command-line interface
- Four scheduling algorithms implemented:
  - Non-preemptive SJF
  - Priority-based scheduling
  - Round Robin with configurable quantum
  - Basic FCFS scheduling
- Detailed execution timeline for processes
- Calculates key performance metrics:
  - Average turnaround time
  - Average waiting time
## Algorithms

### Shortest Job First (SJF)
- **Description**: Executes processes with shortest burst time first  
- **Type**: Non-preemptive implementation  
- **Advantage**: Optimal for minimizing waiting time  
- **Consideration**: Requires knowledge of burst times in advance  

### Priority Scheduling
- **Description**: Executes processes based on priority level  
- **Type**: Non-preemptive implementation  
- **Priority Scheme**: Higher number indicates higher priority  
- **Consideration**: May lead to starvation of lower priority processes  

### Round Robin (RR)
- **Description**: Uses time quantum for fair scheduling  
- **Type**: Preemptive implementation  
- **Key Feature**: Configurable time slice duration  
- **Advantage**: Prevents starvation of processes  

### First-Come First-Served (FCFS)
- **Description**: Executes processes in arrival order  
- **Type**: Simple non-preemptive scheduling  
- **Characteristic**: Serves as baseline for comparison  
- **Consideration**: May result in convoy effect  

## Input Format
For each algorithm, provide:

1. Number of processes (positive integer)
2. For each process:
   - Process ID (integer or string)
   - Burst time (positive integer)
   - Priority (required only for Priority Scheduling)
3. Additional parameters:
   - Time quantum (required only for Round Robin - positive integer)

Example input for Round Robin:
```plaintext
Number of processes: 3
Time quantum: 4
Process 1 burst time: 5
Process 2 burst time: 3
Process 3 burst time: 7
## Example

### Menu Selection
```plaintext
Scheduling Algorithms:
1. Shortest Job First (SJF)
2. Priority Scheduling
3. Round Robin (RR)
4. First-Come, First-Served (FCFS)
5. Exit

Enter your choice (1/2/3/4/5): 3
###Round Robin Simulation
plaintext
Enter the number of processes for Round Robin: 2
Enter the time slice: 4
Enter Burst Time for P1: 5
Enter Burst Time for P2: 3

Process P1 - Start: 0, End: 4
Process P1 - Start: 4, End: 5
Process P2 - Start: 5, End: 8

Average Turnaround Time: 6.5
Average Waiting Time: 3.5

Contributing
We welcome contributions to improve this project! Here's how you can help:

Fork the repository

Create a new feature branch:

bash
git checkout -b feature/your-feature-name
Commit your changes:

bash
git commit -m "Add your meaningful commit message"
Push to the branch:

bash
git push origin feature/your-feature-name
Open a pull request with a clear description of your improvements

## Installation
1. Ensure Python 3.6+ is installed
2. Clone the repository or download the script:
   ```bash
   git clone https://github.com/nisaiqbal000/CPU_Scheduling

Please ensure your code follows the existing style and includes appropriate documentation.
Free for educational and personal use. Commercial use requires permission.
