#
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use
# under the terms of the LICENSE.md file.
#
# For inquiries contact  george.drettakis@inria.fr
#

from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
import os

os.path.dirname(os.path.abspath(__file__))

setup(
    name="diff_gaussian_rasterization_stp",
    packages=["diff_gaussian_rasterization_stp"],
    install_requires=[
        "torch",
        "dacite",
    ],
    ext_modules=[
        CUDAExtension(
            name="diff_gaussian_rasterization_stp._C",
            sources=[
                "cuda_rasterizer/rasterizer_impl.cu",
                "cuda_rasterizer/forward.cu",
                "cuda_rasterizer/backward.cu",
                "rasterize_points.cu",
                "ext.cpp",
            ],
            include_dirs=[
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party"),
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm/"),
            ],
            extra_compile_args={
                "cxx": ["-O3"],
                "nvcc": ["-O3", "--use_fast_math", "-std=c++17"],
            },
        )
    ],
    cmdclass={"build_ext": BuildExtension},
)
