# EN3160 Assignment 02 – Fitting and Alignment

All assignment work belongs in `EN3160_Assignment_02.ipynb`. The notebook currently contains only setup checks and section placeholders; implement Task 1 manually when ready.

## Windows / Python 3.11 setup

Run these commands from `Assignment2` in PowerShell:

```powershell
# Create the environment only if .venv does not already exist.
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --prefix .venv --name en3160-assignment02 --display-name "EN3160 Assignment 02 (Python 3.11)"
.\.venv\Scripts\python.exe -m jupyterlab EN3160_Assignment_02.ipynb
```

Select **EN3160 Assignment 02 (Python 3.11)** as the kernel. Registration is local to `.venv`; repeat the registration command if the repository moves. In PyCharm, select `Assignment2\.venv\Scripts\python.exe` as the existing project interpreter and use it for the notebook. Run the initial setup cell before starting Task 1. Activation is optional because the commands use the environment's interpreter explicitly.

`requirements.txt` pins the eight direct dependencies to installed versions. Their required transitive dependencies are installed by pip. It intentionally excludes unrelated packages.

## Inputs

The supplied files are already located in `images/`:

- `AAAA1.jpg`
- `ADAD1.jpg`
- `AECC1.jpg` — Task 4 reference PCB
- `AECC2.jpg`
- `AECC3.jpg`
- `AECC4.jpg`
- `flag.png`
- `the_berry_farms_sunflower_field.jpeg`
- `wadham.jpg`

The initial notebook cell checks file existence, Pillow integrity, OpenCV decoding, and image dimensions. Task 3 still requires choosing a couple of image pairs; no pair selection or results have been supplied by this setup.

## Assignment constraints

- Task 1: use scale-normalized LoG and scale-space extrema detection; do not use `cv2.HoughCircles()`.
- Task 2: implement line and circle RANSAC manually; do not use a library RANSAC estimator.
- Task 3: demonstrate homography-based perspective warping and blending with a couple of image pairs of your own choice.
- Task 4: use SIFT, BFMatcher, RANSAC homography, alignment, and difference comparisons against `AECC1.jpg`.
- Keep the final report to **four pages or fewer**; each extra page incurs a two-mark penalty. No final report has been created.

The parent Git repository manages this directory. The local `.gitignore` excludes environments, IDE files, and caches while retaining the notebook and input images.
