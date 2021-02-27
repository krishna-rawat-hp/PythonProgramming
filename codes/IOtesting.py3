import io,os,time

def normal_io():
	n = input().strip()
	print("end time normal_io:",time.perf_counter())
	print(n)

def fast_io():
	input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
	print("start time fast_io:",time.perf_counter())
	n = input().decode().strip()
	print("end time fast_io:",time.perf_counter())
	print(n)

if __name__ == "__main__":
	normal_io()
	fast_io()