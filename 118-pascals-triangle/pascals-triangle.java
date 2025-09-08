class Solution {
    private List<Integer> findRows(int n){
        List<Integer> row = new ArrayList<>();
        int ans = 1;
        row.add(1);
        for(int i=1;i<n;i++){
            ans = ans*(n-i);
            ans/=i;
            row.add(ans);
        }
        return row;
    }
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans  = new ArrayList<>();
        for(int i=0;i<numRows;i++){
            ans.add(findRows(i+1));
        }
        return ans;
    }
}