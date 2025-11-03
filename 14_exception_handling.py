try: 
    result = 10 / 0
except Exception as e:
    print(f"Error: {e}")

try:
    sum(10, "abc")
except Exception as e :
    print(f"Error: {e}")



try:
    pass
except Exception as e:
    pass    
else:
    pass
finally:
    pass