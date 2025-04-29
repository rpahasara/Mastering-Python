# 🍎 Python Setup for macOS

## ✅ Step 1: Download Python

1. Visit the official site: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click “Download Python 3.13.3” (latest version) for macOS.
3. Open the `.pkg` installer and follow the instructions.

> 🔥 Important: This installs Python as `python3`, not `python`.

---

## ✅ Step 2: Verify Installation

Open Terminal and run:

```bash
python3 --version
```

## ✅ Step 3: Install pip (if not already)

Python from python.org usually includes pip. Check with:

```bash
pip3 --version
```

If it’s missing, reinstall Python or manually install with:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

You're ready to start coding! 🎉
