#pragma once

#include <unsupported/Eigen/CXX11/Tensor>
#include <iostream>

using Tensor2 = Eigen::Tensor<double, 2>;
using TensorMap2 = Eigen::TensorMap <Eigen::Tensor<double, 2>>;

Tensor2 add_tensor_inner(const TensorMap2& a, const TensorMap2& b) {
  // Assuming these are the same dimensions
  std::cout << a.size() << std::endl;
  Eigen::Tensor<double, 2> result = a + b;
  return result;
}