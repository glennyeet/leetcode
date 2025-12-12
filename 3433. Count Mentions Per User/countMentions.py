from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # Simulation: O(e * log(e) * n) time, O(e + n) space

        n = numberOfUsers
        type_priority = {"OFFLINE": 0, "MESSAGE": 1}
        sorted_events = sorted(events, key=lambda e: (int(e[1]), type_priority[e[0]]))
        mentions = [0] * n
        online_at = [0] * n
        for type, timestamp, mentions_string in sorted_events:
            timestamp = int(timestamp)
            if type == "MESSAGE":
                if mentions_string == "ALL":
                    for i in range(n):
                        mentions[i] += 1
                elif mentions_string == "HERE":
                    for i in range(n):
                        if timestamp >= online_at[i]:
                            mentions[i] += 1
                else:
                    for user_id in mentions_string.split(" "):
                        user_id = int(user_id[2:])
                        mentions[user_id] += 1
            elif type == "OFFLINE":
                user_id = int(mentions_string)
                online_at[user_id] = timestamp + 60
        return mentions
