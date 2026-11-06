def convert(total_second):
 hours = total_second//3600
 minutes = (total_second%3600)//60
 seconds = total_second%60
 print(f" {total_second} second = {hours}h - {minutes}m - {seconds}s")

#(a) and (b)
convert(9875)
#(c)
convert(3600)
convert(59)
convert(86399)