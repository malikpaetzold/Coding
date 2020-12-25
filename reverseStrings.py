def string_reverser(our_string):
   """
   Reverse the input string

   Args:
      our_string(string): String to be reversed
   Returns:
      string: The reversed string
   """

   # TODO: Write your solution here
   out = ""
   l = len(our_string)
   for i in range(l):
      out += our_string[l-i-1]
   return out

print(string_reverser("test"))