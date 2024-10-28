from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()

"""
Expected output: (you must have a function as close as possible to the original
version)
$> python tester.py
100%|[===============================================================>]| 333/333
100%| | 333/333 [00:01<00:00, 191.61it/s]

"""
