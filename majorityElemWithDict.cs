public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int,int> dict=new Dictionary<int,int>();
        int n=nums.Count();
        int[] uniques=new int[n];
        int i=0;
        for (i=0;i<n;i++)
        {
            if(dict.ContainsKey(nums[i])){
                dict[nums[i]]++;
            }
            else
            {
                dict.Add(nums[i],1);
            }
        }
        foreach(KeyValuePair<int,int> entry in dict)
        {
            if(entry.Value>n/2)
            {
                return entry.Key;
            }
        }
        return 0;
    }
}
