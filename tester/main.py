import requests
import time
import threading
import subprocess
import colorama
from colorama import Fore, Back, Style
from tqdm import tqdm

colorama.init(autoreset=True)

tests = [
  {
    "name": "Golang",
    "port": 8000
  },
  {
    "name": "JavaScript",
    "port": 8001
  },
  {
    "name": "Python",
    "port": 8002
  }
]

endpoints = [
  "jwt/generate/",
  "jwt/read/",
  "sql/insert/",
  "sql/select/"
]

host = "http://localhost"

num_requests = 50

results = {}

def request_cluster(url, num_requests, resp, index, use_tqdm=False):
  rf = tqdm(range(num_requests)) if use_tqdm else range(num_requests)

  resp[index] = []

  for _ in rf:
    st = time.time()
    try:
      r = requests.get(url)
      et = time.time()
      r.raise_for_status()
      resp[index].append(et - st)
    except Exception as e:
      print(Fore.RED + f"{url} returned non-200 HTTP code - quitting.\n{e}")
      exit()

for base in tests:
  print(f"Testing: {base['name']}")
  threads = []
  platform_results = {}

  for i, endpoint in enumerate(endpoints):
    if len(endpoints) - 1 == i:
      request_cluster(f"{host}:{base['port']}/{endpoint}", num_requests, platform_results, endpoint, use_tqdm=True)
    else:
      x = threading.Thread(target=request_cluster, args=(f"{host}:{base['port']}/{endpoint}", num_requests, platform_results, endpoint))
      x.start()
      threads.append(x)
  
  print("Waiting for other threads to finish", end="")
  if True in [t.is_alive() for t in threads]:
    while True in [t.is_alive() for t in threads]:
      time.sleep(0.25)
      print(".", end="")

  print("\nWaiting for one second", end="")

  for _ in range(4):  # I think the rate at which things were occuring was messing with things
    print(".", end="")
    time.sleep(0.25)

  results[base["name"]] = platform_results

  print("\n")

print("--- RESULTS ---")

for platform in results:
  print(Style.BRIGHT + Back.WHITE + Fore.BLUE + platform)
  overall_total = 0
  for endpoint in results[platform]:
    print(f" {endpoint}: ", end="")
    
    endpoint_total = 0
    for time in results[platform][endpoint]:
      endpoint_total += time
      overall_total += time
    endpoint_total /= num_requests
    
    print(f"{endpoint_total} seconds per request")
  
  overall_total /= len(endpoints) * num_requests

  print(Fore.GREEN + f"Average time per request: {overall_total} seconds")

  print()
