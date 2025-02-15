apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    linux-headers \
    python3-dev \
    cmake \
    ninja \
    make \    # Added make
    git \     # Added git for some Python packages that might need it
    libressl-dev \  # Added SSL dev files
    libffi-dev     # Added libffi for some Python dependencies
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt