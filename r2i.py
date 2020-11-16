
class Solution:
	def romanToInt(self, s: str) -> int:

		sym=['M','D','C','L','X','V','I']

		d={'M':1000, 'D': 500, 'C': 100, 'L':50, 'X':10, 'V':5, 'I':1}

		sum = 0 
		i = 0 
		flag = True

		while flag:

			num = 0
			
			index = s.find(sym[i])

			if index != -1:
				num = d[sym[i]] - d[s[0]]*index
				sum += num

			s = s[index+1:]
			
			if s == '':
				flag = False

			elif s[0] != sym[i] and s.find(sym[i]) == -1:
				i += 1
    
		return(sum)
