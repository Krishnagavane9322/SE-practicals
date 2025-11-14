class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id  # Unique ID for each job
        self.deadline = deadline  # Deadline for the job (maximum time slot)
        self.profit = profit  # Profit if the job is completed

def job_sequencing(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Find the maximum deadline to determine the number of time slots needed
    max_deadline = max(job.deadline for job in jobs)
    
    # Array to keep track of free time slots (None means slot is free)
    time_slots = [None] * max_deadline
    
    # Track the total profit and scheduled jobs
    total_profit = 0
    scheduled_jobs = []
    
    # Go through each job in the sorted list
    for job in jobs:
        # Try to schedule the job in the latest available slot before its deadline
        for slot in range(job.deadline - 1, -1, -1):
            if time_slots[slot] is None:  # If slot is free
                time_slots[slot] = job.job_id  # Assign the job to this slot
                scheduled_jobs.append(job.job_id)  # Add to the scheduled jobs list
                total_profit += job.profit  # Add the job's profit
                break  # Exit the loop once the job is scheduled
    
    return scheduled_jobs, total_profit

# Example usage
jobs = [
    Job('A', 2, 100),
    Job('B', 1, 19),
    Job('C', 2, 27),
    Job('D', 1, 25),
    Job('E', 3, 15)
]

sequence, profit = job_sequencing(jobs)
print("Scheduled Jobs:", sequence)
print("Total Profit:", profit)
