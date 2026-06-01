import time
import random


WALL_SOUND_DAMPENING = 43  

def test_volume(level):
    
    print(f"🎵 Testing volume: {level}... ", end="", flush=True)
    time.sleep(1.5)  
    
    if level <= WALL_SOUND_DAMPENING:
        print("Silence. Neighbor is chill.")
        return True  
    else:
        print("Neighbor is furious!")
        return False 

# --- BINARY SEARCH FOR MAX VOLUME ---
def find_max_safe_volume():
    low = 0
    high = 100
    optimal_volume = 0
    tests = 0
    
    print("APARTMENT TV CALIBRATION MODE\n")
    print("Goal: Find loudest setting before wall vibrations cause conflict.\n")
    
    while low <= high:
        tests += 1
        mid = (low + high) // 2
        
        if test_volume(mid):
            optimal_volume = mid   
            low = mid + 1
        else:
            high = mid - 1      
            
    print("\n" + "="*40)
    print(f"CALIBRATION COMPLETE in {tests} tests.")
    print(f"Optimal Volume Setting: {optimal_volume}")
    print(f"(Brute force would have taken {WALL_SOUND_DAMPENING+1} tests and many knocks)")

# Run the calibration
find_max_safe_volume()