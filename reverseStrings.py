def string_reverser(our_string):
   """
   Reverse the input string

   Args:
      our_string(string): String to be reversed
   Returns:
      string: The reversed string
   """

   # TODO: Write your solution here
   i = len(our_string) - 1
   out = ""
   while i >= 0:
      out += our_string[i]
      i -= 1
   return out

print(string_reverser("test"))