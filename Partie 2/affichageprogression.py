from tqdm import tqdm

def display_progress(total_attempts, attempt):
    with tqdm(total=total_attempts, desc="Brute Force Progress") as pbar:
        pbar.update(attempt)
