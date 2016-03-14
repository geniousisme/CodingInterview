class Solution(object):
    def arrange_cooling_tasks(self, tasks, range): # cannot sort
        task_pos_dict = {}
        task_ptr = 0
        while task_ptr < len(tasks):
            if task_pos_dict.get(tasks[task_ptr]) is None or                   \
               task_ptr - task_pos_dict.get(tasks[task_ptr]) >= range + 1:
                task_pos_dict[tasks[task_ptr]] = task_ptr
                task_ptr += 1
            else:
                diff = range + 1 - task_ptr + task_pos_dict.get(tasks[task_ptr])
                task_pos_dict[tasks[task_ptr]] = task_ptr + diff
                tasks = tasks[:task_ptr] + '*' * diff + tasks[task_ptr:]
                task_ptr += diff + 1
        return tasks, task_ptr # tasks is the final result, taks_ptr is the length

    # follow up 1: what happen if range is very small?
    # if range is small, then we can maintain a k-size hash to solve it.

    # follow up 2: what is the order of the input can change? use the frequency to sort.
    # arrange the elements with most frequency

if __name__ == "__main__":
    s = Solution()
    print s.arrange_cooling_tasks("AABCB", 2)
    print s.arrange_cooling_tasks("ABABA", 2)
    print s.arrange_cooling_tasks("A", 2)
    print s.arrange_cooling_tasks("ACACA", 2)



