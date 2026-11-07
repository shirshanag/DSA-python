nums = [2,1,2,2,2]
n=len(nums)
freq_map={}
for i in nums:
    freq_map[i]=0
    # if nums[i] in freq_map:
    #     freq_map[nums[i]]+=1
for i in range(0,n):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
for k,v in freq_map.items():
    if v>1:
        print(k)

