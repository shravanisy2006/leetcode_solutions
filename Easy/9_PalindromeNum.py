class Solution(object):
  
    def isPalindrome(self, x):
      
        self.x = x
        num = x
        rev = 0
      
        while x > 0 :
            rev = rev * 10 + x % 10
            x = x // 10
          
        if num == rev:
            return True
          
        else:
            return False

