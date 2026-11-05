total_seconds = 59
hour=total_seconds//3600
minute=(total_seconds%3600)//60
seconds=total_seconds%60

print(total_seconds,"second = " ,hour,"h",minute,"min",seconds,"s")
print(f"{hour} h {minute} min {seconds} s")
