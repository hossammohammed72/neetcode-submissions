class TimeMap:

    def __init__(self):
        self.hashmap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key][timestamp] = value
        else:
             self.hashmap[key] = {timestamp:value}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        timestamps = list(self.hashmap[key].keys())
        nearest_timestamp = self.search_timestamps(0,len(timestamps),timestamp,timestamps)
       # print(nearest_timestamp,self.hashmap,key)
        if nearest_timestamp == -1:
            return ""
        return self.hashmap[key][nearest_timestamp]
        
    def search_timestamps(self,start,end,target,arr):
        if start>=end:
            if arr[end-1] < target:
                return arr[end-1]
            return -1
        mid = int((start+end)/2)
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            return self.search_timestamps(start,mid,target,arr)
        else:
            return self.search_timestamps(mid+1,end,target,arr)
            