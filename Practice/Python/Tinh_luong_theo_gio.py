time_in = int(input("gio vao: "))
time_out = int(input("gio ra: "))
time_2 = 0 

time = time_out - time_in

if (8 <= time_in < time_out <= 24):
	print(f"ban da hat duoc {time} tieng")
	if 8 <= time_in <= time_out <= 17:
		time_2 = ((3*30) + ((time - 3) * (30 - ((30/100) * 30))))
		print(f"Tien cua ban la {(time_2 - (time_2 * (10/100)))}")
	elif time <= 3:
		print(f"tien cua ban la {time * 30}k")
	elif time > 3:
		print(f"Tien cua ban la {(3 * 30) + ((time - 3) * (30 - ((30/100) * 30)))}k")
else:
	print("Ban da nhap sai vui long nhap lai")
