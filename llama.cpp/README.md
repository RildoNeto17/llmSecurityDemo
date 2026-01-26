# Binaries

This folder contains precompiled binaries for Docker.

## Structure
```
llama.cpp/
├── build/
│   ├── bin/      # llama-server, owasp-llm-tool
│   └── lib/      # shared libraries (.so)
└── models/       # qwen2.5-0.5b-instruct-q4_0.gguf
```

## Source Code

https://github.com/FrancescoPaoloL/llama.cpp/tree/feature/owasp-llm-tool/examples/owasp-llm-tool

## Build from source
```bash
git clone https://github.com/FrancescoPaoloL/llama.cpp.git
cd llama.cpp
git checkout feature/owasp-llm-tool

cmake -B build \
  -DCMAKE_BUILD_TYPE=Release \
  -DGGML_NATIVE=ON \
  -DGGML_AVX2=ON \
  -DGGML_FMA=ON \
  -DGGML_OPENMP=ON \
  -DBUILD_SHARED_LIBS=ON

cmake --build build -j$(nproc) --target owasp-llm-tool
cmake --build build -j$(nproc) --target llama-server
```

## Model
```bash
wget https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_0.gguf -P models/
```

## Note

Binaries are platform-specific. For Azure deployment, see [infra/azure/README.md](../infra/azure/README.md).


