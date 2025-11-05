#!/usr/bin/env python3
# Split paired images/masks into 80% train, 10% test, 10% val.
# Input layout (BASE_DIR):
#   images/
#   masks/
# Output (created inside BASE_DIR):
#   train_images/, train_masks/, test_images/, test_masks/, val_images/, val_masks/

from pathlib import Path
import shutil
import random

# Set this to your base directory path
BASE_DIR = Path("dataset")  # <-- change this

IMAGE_DIR = BASE_DIR / "images"
MASK_DIR = BASE_DIR / "masks"

OUT_DIRS = {
    "train_images": BASE_DIR / "train_images",
    "train_masks":  BASE_DIR / "train_masks",
    "test_images":  BASE_DIR / "test_images",
    "test_masks":   BASE_DIR / "test_masks",
    "val_images":   BASE_DIR / "val_images",
    "val_masks":    BASE_DIR / "val_masks",
}

ALLOWED_EXTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".gif"}


def collect_files(folder: Path):
    return {p.stem: p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in ALLOWED_EXTS}


def ensure_clean_dirs():
    for d in OUT_DIRS.values():
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)


def split_indices(n: int, train_ratio=0.8, test_ratio=0.1):
    n_train = int(n * train_ratio)
    n_test = int(n * test_ratio)
    n_val = n - n_train - n_test
    return n_train, n_test, n_val


def copy_pair(stem: str, img_map: dict, msk_map: dict, split: str):
    shutil.copy2(img_map[stem], OUT_DIRS[f"{split}_images"] / img_map[stem].name)
    shutil.copy2(msk_map[stem], OUT_DIRS[f"{split}_masks"] / msk_map[stem].name)


def main():
    if not IMAGE_DIR.is_dir() or not MASK_DIR.is_dir():
        raise SystemExit("Missing 'images' or 'masks' subdirectory in BASE_DIR")

    images = collect_files(IMAGE_DIR)
    masks = collect_files(MASK_DIR)

    paired_stems = sorted(set(images).intersection(masks))
    if not paired_stems:
        raise SystemExit("No paired image/mask filenames found (matching stems)")

    random.seed(42)
    random.shuffle(paired_stems)

    n = len(paired_stems)
    n_train, n_test, n_val = split_indices(n, 0.8, 0.1)

    train_stems = paired_stems[:n_train]
    test_stems  = paired_stems[n_train:n_train + n_test]
    val_stems   = paired_stems[n_train + n_test:]

    ensure_clean_dirs()

    for s in train_stems:
        copy_pair(s, images, masks, "train")
    for s in test_stems:
        copy_pair(s, images, masks, "test")
    for s in val_stems:
        copy_pair(s, images, masks, "val")

    print(f"Total pairs: {n}")
    print(f"train: {len(train_stems)}  test: {len(test_stems)}  val: {len(val_stems)}")
    print("Done")


if __name__ == "__main__":
    main()
