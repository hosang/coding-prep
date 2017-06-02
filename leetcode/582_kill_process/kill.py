from collections import defaultdict

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        p_to_ch = defaultdict(list)
        for parent, child in zip(ppid, pid):
            p_to_ch[parent].append(child)
            
        killed_pids = [kill]
        for pid in killed_pids:
            killed_pids.extend(p_to_ch[pid])
        return killed_pids
        
