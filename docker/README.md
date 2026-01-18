## Build Strategy

This project uses **single-stage** build with precompiled binaries.

**Pros:**
- Fast builds
- Simple setup

**Cons:**
- Binaries depend on host machine
- Not ideal for CI/CD

For reproducible builds, consider multi-stage in the future.

## Build Environment

Binaries compiled on:
- **OS**: Debian 12 (Bookworm)
- **CPU**: Intel i5-12400 (Alder Lake)
- **Compiler**: GCC 12.2.0

### Compiler flags
```bash
cmake -B build \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_FLAGS="-O3 -march=native -mtune=native" \
  -DCMAKE_CXX_FLAGS="-O3 -march=native -mtune=native" \
  -DGGML_NATIVE=ON \
  -DGGML_AVX2=ON \
  -DGGML_FMA=ON \
  -DGGML_OPENMP=ON \
  -DBUILD_SHARED_LIBS=ON
```

**Note**: `-march=native` optimizes for the build machine. May not work on older CPUs without AVX2.

