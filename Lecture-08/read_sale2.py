with open("sales.txt","r") as sale_file:
  for line in sale_file:
      amount = float(line)
      print(format(amount,".2f"))