class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> map_tasks;
        for (const auto& task : tasks) {
            map_tasks[task]++;
        }

        priority_queue<pair<int, char>> maxHeap;
        for (const auto& [task, freq] : map_tasks) {
            maxHeap.push({freq, task});
        }

        deque<pair<int, char>> queueTimeout;

        unsigned time = 0;

        while (!maxHeap.empty() || !queueTimeout.empty()) {
            char currTask;
            if (maxHeap.empty()) {
                // remove from front of queue
                auto [newTime, newTask] = queueTimeout.front();
                queueTimeout.pop_front();
                time = newTime;
                currTask = newTask;
            } else {
                // remove from front of queue if time reached
                while (queueTimeout[0].first <= time) {
                    auto newTask = queueTimeout[0].second;
                    queueTimeout.pop_front();
                    maxHeap.push({map_tasks[newTask], newTask});
                }

                auto [freq, task] = maxHeap.top();
                maxHeap.pop();
                currTask = task;
            }

            map_tasks[currTask]--;
            time += 1;

            if (map_tasks[currTask] > 0) {
                queueTimeout.push_back({time + n, currTask});
            }

        }
        return time;
    }
};
