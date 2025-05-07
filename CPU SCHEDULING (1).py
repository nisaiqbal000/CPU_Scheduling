class SJF:
    def processData(self):
        no_of_processes = int(input("Enter the number of processes for SJF: "))
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))
            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
            temporary.extend([process_id, burst_time])
            process_data.append(temporary)
        process_data.sort(key=lambda x: x[1])  # Sort by burst time
        self.schedulingProcess(process_data)

    def schedulingProcess(self, process_data):
        start_time = [0] * len(process_data)
        exit_time = [0] * len(process_data)
        total_turnaround_time = 0
        total_waiting_time = 0

        for i in range(len(process_data)):
            if i == 0:
                start_time[i] = 0
            else:
                start_time[i] = exit_time[i - 1]
            exit_time[i] = start_time[i] + process_data[i][1]
            turnaround_time = exit_time[i] - process_data[i][0]
            waiting_time = turnaround_time - process_data[i][1]

            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time

            print(f"Process {process_data[i][0]} - Start Time: {start_time[i]}, End Time: {exit_time[i]}")

        average_turnaround_time = total_turnaround_time / len(process_data)
        average_waiting_time = total_waiting_time / len(process_data)

        print(f"Average Turnaround Time: {average_turnaround_time}")
        print(f"Average Waiting Time: {average_waiting_time}")


class PriorityScheduling:
    def processData(self):
        no_of_processes = int(input("Enter the number of processes for Priority Scheduling: "))
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))
            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
            priority = int(input(f"Enter Priority for Process {process_id}: "))
            temporary.extend([process_id, burst_time, priority])
            process_data.append(temporary)
        process_data.sort(key=lambda x: x[2], reverse=True)  # Sort by priority (higher priority first)
        self.schedulingProcess(process_data)

    def schedulingProcess(self, process_data):
        start_time = [0] * len(process_data)
        exit_time = [0] * len(process_data)
        total_turnaround_time = 0
        total_waiting_time = 0

        for i in range(len(process_data)):
            if i == 0:
                start_time[i] = 0
            else:
                start_time[i] = exit_time[i - 1]
            exit_time[i] = start_time[i] + process_data[i][1]
            turnaround_time = exit_time[i] - process_data[i][0]
            waiting_time = turnaround_time - process_data[i][1]

            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time

            print(f"Process {process_data[i][0]} - Start Time: {start_time[i]}, End Time: {exit_time[i]}")

        average_turnaround_time = total_turnaround_time / len(process_data)
        average_waiting_time = total_waiting_time / len(process_data)

        print(f"Average Turnaround Time: {average_turnaround_time}")
        print(f"Average Waiting Time: {average_waiting_time}")


class RoundRobin:
    def processData(self):
        no_of_processes = int(input("Enter the number of processes for Round Robin: "))
        time_slice = int(input("Enter the time slice: "))
        process_data = []
        for i in range(no_of_processes):
            process_id = f"P{i + 1}"
            burst_time = int(input(f"Enter Burst Time for {process_id}: "))
            process_data.append([process_id, burst_time])

        self.schedulingProcess(process_data, time_slice)

    def schedulingProcess(self, process_data, time_slice):
        remaining_time = [process[1] for process in process_data]
        total_turnaround_time = 0
        total_waiting_time = 0
        current_time = 0

        while True:
            all_processes_done = True
            for i in range(len(process_data)):
                if remaining_time[i] > 0:
                    all_processes_done = False
                    if remaining_time[i] > time_slice:
                        current_time += time_slice
                        remaining_time[i] -= time_slice
                    else:
                        current_time += remaining_time[i]
                        total_turnaround_time += current_time
                        remaining_time[i] = 0

            if all_processes_done:
                break

        total_turnaround_time = total_turnaround_time / len(process_data)
        total_waiting_time = total_turnaround_time - sum(process[1] for process in process_data)

        print(f"Average Turnaround Time: {total_turnaround_time}")
        print(f"Average Waiting Time: {total_waiting_time}")


class FCFS:
    def processData(self):
        no_of_processes = int(input("Enter the number of processes for FCFS: "))
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))
            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
            temporary.extend([process_id, burst_time])
            process_data.append(temporary)
        self.schedulingProcess(process_data)

    def schedulingProcess(self, process_data):
        start_time = [0] * len(process_data)
        exit_time = [0] * len(process_data)
        total_turnaround_time = 0
        total_waiting_time = 0

        for i in range(len(process_data)):
            if i == 0:
                start_time[i] = 0
            else:
                start_time[i] = exit_time[i - 1]
            exit_time[i] = start_time[i] + process_data[i][1]
            turnaround_time = exit_time[i] - process_data[i][0]
            waiting_time = turnaround_time - process_data[i][1]

            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time

            print(f"Process {process_data[i][0]} - Start Time: {start_time[i]}, End Time: {exit_time[i]}")

        average_turnaround_time = total_turnaround_time / len(process_data)
        average_waiting_time = total_waiting_time / len(process_data)

        print(f"Average Turnaround Time: {average_turnaround_time}")
        print(f"Average Waiting Time: {average_waiting_time}")


class Scheduler:
    def main(self):
        while True:
            print("Scheduling Algorithms:")
            print("1. Shortest Job First (SJF)")
            print("2. Priority Scheduling")
            print("3. Round Robin (RR)")
            print("4. First-Come, First-Served (FCFS)")
            print("5. Exit")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == '1':
                sjf = SJF()
                sjf.processData()
            elif choice == '2':
                priority = PriorityScheduling()
                priority.processData()
            elif choice == '3':
                rr = RoundRobin()
                rr.processData()
            elif choice == '4':
                fcfs = FCFS()
                fcfs.processData()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.main()
